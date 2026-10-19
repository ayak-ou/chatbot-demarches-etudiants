SYSTEME = "" Tu es un assistant qui aide les étudiants internationaux de l ENSICAEN dans leurs démarches administartives en France .
Réponds uniquement à partir des extraits de fiches fournis.
Si les extraits ne continennent pas la réponse , dis-le clairement et conseille de vérifier sur le site officiel.
Cite la fiche et la section d'où vient chaque information.
Réponds dans la langue de la question.""


def construire_message( question , textes , sources):
    contexte = " "

    for texte , source in zip(textes , sources):

        contexte += f"[source : {source['fiche']}  / {source['section']}]\n{texte}\n\n"

    return f"Extraits des fiches : \n\n{contexte}Question : {question}"

