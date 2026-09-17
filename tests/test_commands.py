from src.commands.listar import listar_trilhas
from src.commands.consultar import consultar_trilha
from src.commands.certificado import emitir_certificado
from src.services.trilha_service import carregar_trilhas, buscar_trilha
from src.services.certificado_service import gerar_codigo_certificado


def test_carregar_trilhas():
    trilhas = carregar_trilhas()
    assert len(trilhas) >= 4


def test_buscar_trilha_existente():
    t = buscar_trilha("python")
    assert t is not None
    assert t.nome == "Python para Dados"


def test_buscar_trilha_inexistente():
    assert buscar_trilha("nao-existe") is None


def test_listar_trilhas(capsys):
    listar_trilhas()
    out = capsys.readouterr().out
    assert "Python para Dados" in out


def test_consultar_trilha(capsys):
    consultar_trilha("ia")
    out = capsys.readouterr().out
    assert "Inteligência Artificial" in out


def test_certificado_codigo_unico():
    c1 = gerar_codigo_certificado("Ana", "python")
    c2 = gerar_codigo_certificado("Ana", "python")
    assert c1 != c2  # timestamp muda
    assert len(c1) == 12


def test_emitir_certificado(capsys):
    emitir_certificado("Carlos", "cloud")
    out = capsys.readouterr().out
    assert "Carlos" in out
    assert "Cloud com IBM" in out
