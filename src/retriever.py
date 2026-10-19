from pathlib import Path 
import chromadb 
from chromadb.utils import embedding_functions


RACINE = Path(__file__).parent.parent

DB_DIR = RACINE / "chroma_db"

def rechercher (question , n=3):
    embed = embedding_functions.SentenceTransformerEmbeddingFuction(
        model_name ="paraphrase-multilingual-MiniLM-L12-v2"
    )

    client = chromadb.PersistentClient(path = str(DB_DIR))
    collection = client.get_collection("fiches" , embedding_function = embed)
    resultats = collection.query(quesry_texts=[question] , n_results=n)
    return resultats["documents"][0] , resultats["metadatas"][0]

if __name__ == "__main__":

    question = input("Ta question : ")

    textes , sources = rechercher(question)
    for texte , source in zip(textes , sources ):

        print(f"---{source['fiche']} / {source['section']}---")
        print(texte)
        print()
        


