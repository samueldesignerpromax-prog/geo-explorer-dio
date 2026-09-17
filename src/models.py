from dataclasses import dataclass
from typing import List


@dataclass
class Modulo:
    titulo: str
    horas: int


@dataclass
class Trilha:
    id: str
    nome: str
    nivel: str
    horas: int
    descricao: str
    modulos: List[Modulo]

    @classmethod
    def from_dict(cls, data: dict) -> "Trilha":
        modulos = [Modulo(**m) for m in data.get("modulos", [])]
        return cls(
            id=data["id"],
            nome=data["nome"],
            nivel=data["nivel"],
            horas=data["horas"],
            descricao=data.get("descricao", ""),
            modulos=modulos,
        )
