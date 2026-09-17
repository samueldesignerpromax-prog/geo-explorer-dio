import random

from src.services.trilha_service import buscar_trilha

PERGUNTAS = {
    "iniciante": [
        "O que é uma variável?",
        "Explique o que é um loop.",
        "Para que serve uma função?",
    ],
    "intermediario": [
        "Explique o conceito de overfitting.",
        "O que é uma API REST?",
        "Como funciona um algoritmo de clustering?",
    ],
    "avancado": [
        "Explique o teorema CAP.",
        "Como funciona um pipeline de CI/CD?",
        "O que é idempotência em APIs?",
    ],
}


def gerar_desafio(trilha_id: str):
    trilha = buscar_trilha(trilha_id)
    if not trilha:
        print(f"❌ Trilha '{trilha_id}' não encontrada.")
        return

    banco = PERGUNTAS.get(trilha.nivel, PERGUNTAS["iniciante"])
    pergunta = random.choice(banco)

    print(f"\n🎯 Desafio da trilha: {trilha.nome}")
    print(f"Nível: {trilha.nivel}")
    print(f"\n➡️  {pergunta}\n")
