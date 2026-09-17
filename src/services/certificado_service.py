import hashlib
from datetime import datetime


def gerar_codigo_certificado(nome: str, trilha_id: str) -> str:
    timestamp = datetime.now().isoformat()
    base = f"{nome}|{trilha_id}|{timestamp}"
    return hashlib.sha256(base.encode("utf-8")).hexdigest()[:12].upper()
