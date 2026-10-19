import anthropic 
from config import ANTHROPIC_API_KEY , MODELE_LLM , NB_MORCEAUX 
from prompts import SYSTEME , construire_message
from retriever import rechercher 

client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

def repondre(question):

    textes , sources = rechercher(question , NB_MORCEAUX)

    message = construire_message(question , textes , sources)

    reponse = client.messages.create(

        model=MODELE_LLM,

        max_tokens=1000,

        system=SYSTEME,

        messages=[{"role" : "user" , "content" : message}],
    )

    return reponse.content[0].text

