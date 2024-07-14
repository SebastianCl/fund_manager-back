import secrets
import hashlib


class Utils:

    def generar_numero_unico() -> str:
        numero_aleatorio = secrets.randbelow(1000)
        id_unico = hashlib.sha256(secrets.token_bytes(32)).hexdigest()
        numero_unico = f"{numero_aleatorio}{id_unico[:10]}"
        return numero_unico
