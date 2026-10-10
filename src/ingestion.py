from pathlib import Path
import chromadb
from chromadb.utils import embedding_functions 

RACINE = Path(__file__).parent.parent
DATA_DIR = RACINE / "data"
DB_DIR = RACINE / "chroma_db" 

def decouper_fiche(chemin):
    lignes = chemin.read_text( encoding="utf-8").splitlines()
    titre = lignes[0].lstrip("# ").strip() if lignes else chemin.stem 
    morceaux, section, contenu = [], "Introduction", [] 

    for ligne in lignes[1:]:
        if ligne startswith("##"):
            if "\n" .join(contenu) .strip():
                morceaux.append((section, "\n".join(contenu).strip()))

            section, contenu = ligne[3:].strip(), []
        else :
            contenu.append(ligne)

 if "\n".join(contenu).strip():
        morceaux.append((section, "\n".join(contenu).strip()))
    return titre, morceaux


def main():
    embed = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name="paraphrase-multilingual-MiniLM-L12-v2"
    )
    client = chromadb.PersistentClient(path=str(DB_DIR))

    # On repart de zéro à chaque lancement
    try:
        client.delete_collection("fiches")
    except Exception:
        pass
    collection = client.create_collection("fiches", embedding_function=embed)

    ids, textes, metas = [], [], []
    for chemin in sorted(DATA_DIR.glob("*.md")):
        titre, morceaux = decouper_fiche(chemin)
        for i, (section, contenu) in enumerate(morceaux):
            ids.append(f"{chemin.stem}-{i}")
            textes.append(f"{titre}\n{section}\n{contenu}")
            metas.append({"fiche": chemin.name, "section": section})

    collection.add(ids=ids, documents=textes, metadatas=metas)
    print(f"{len(ids)} morceaux indexés depuis {DATA_DIR}")


if __name__ == "__main__":
    main()

    