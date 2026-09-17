from src.services.trilha_service import buscar_trilha
from src.services.certificado_service import gerar_codigo_certificado


def emitir_certificado(nome: str, trilha_id: str):
    trilha = buscar_trilha(trilha_id)
    if not trilha:
        print(f"❌ Trilha '{trilha_id}' não encontrada.")
        return

    codigo = gerar_codigo_certificado(nome, trilha_id)

    print("\n" + "=" * 50)
    print("🎓 CERTIFICADO GEO-EXPLORER")
    print("=" * 50)
    print(f"Aluno:  {nome}")
    print(f"Trilha: {trilha.nome}")
    print(f"Carga:  {trilha.horas}h")
    print(f"Código: {codigo}")
    print("=" * 50 + "\n")
