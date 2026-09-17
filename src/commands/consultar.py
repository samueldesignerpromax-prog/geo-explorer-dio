from src.services.trilha_service import buscar_trilha


def consultar_trilha(trilha_id: str):
    trilha = buscar_trilha(trilha_id)
    if not trilha:
        print(f"❌ Trilha '{trilha_id}' não encontrada.")
        return

    print(f"\n📚 {trilha.nome} ({trilha.nivel})")
    print(f"⏱️  Carga horária: {trilha.horas}h")
    print(f"📝 {trilha.descricao}\n")
    print("Módulos:")
    for i, m in enumerate(trilha.modulos, 1):
        print(f"  {i}. {m.titulo} - {m.horas}h")
    print()
