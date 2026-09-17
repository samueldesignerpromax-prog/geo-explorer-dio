import json
import os

from src.models import Trilha

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "trilhas.json")


def carregar_trilhas() -> list[Trilha]:
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
    return [Trilha.from_dict(t) for t in data["trilhas"]]


def buscar_trilha(trilha_id: str) -> Trilha | None:
    for t in carregar_trilhas():
        if t.id == trilha_id:
            return t
    return None
