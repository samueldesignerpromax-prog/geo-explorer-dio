from src.services.trilha_service import carregar_trilhas


def listar_trilhas():
    trilhas = carregar_trilhas()
    print("\n🌍 Trilhas disponíveis:\n")
    for t in trilhas:
        print(f"  [{t.id}] {t.nome} ({t.nivel}) - {t.horas}h")
    print()
