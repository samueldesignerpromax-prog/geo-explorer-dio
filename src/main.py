import argparse

from src.commands.listar import listar_trilhas
from src.commands.consultar import consultar_trilha
from src.commands.desafio import gerar_desafio
from src.commands.certificado import emitir_certificado


def main():
    parser = argparse.ArgumentParser(
        prog="geo-explorer",
        description="🌍 Explore trilhas de aprendizagem de forma interativa.",
    )
    sub = parser.add_subparsers(dest="comando")

    sub.add_parser("listar", help="Lista todas as trilhas disponíveis")

    p_cons = sub.add_parser("consultar", help="Mostra detalhes de uma trilha")
    p_cons.add_argument("id", help="ID da trilha (ex: python)")

    p_des = sub.add_parser("desafio", help="Gera um desafio para a trilha")
    p_des.add_argument("id", help="ID da trilha")

    p_cert = sub.add_parser("certificado", help="Emite um certificado")
    p_cert.add_argument("nome", help="Nome do aluno")
    p_cert.add_argument("--trilha", required=True, help="ID da trilha")

    args = parser.parse_args()

    if args.comando == "listar":
        listar_trilhas()
    elif args.comando == "consultar":
        consultar_trilha(args.id)
    elif args.comando == "desafio":
        gerar_desafio(args.id)
    elif args.comando == "certificado":
        emitir_certificado(args.nome, args.trilha)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
