import os 
from pathlib import Path 
from dotenv import load_dotenv

RACINE = Path(__file__).parent.parent

load_dotenv(RACINE / ".env")

ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")


MODELE_LLM = "claude-haiku-5-5"

NB_MORCEAUX = 3
