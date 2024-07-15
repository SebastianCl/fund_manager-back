import secrets
import hashlib


class Utils:

    def generate_unique_number() -> str:
        random_number = secrets.randbelow(1000)
        unique_id = hashlib.sha256(secrets.token_bytes(32)).hexdigest()
        unique_number = f"{random_number}{unique_id[:10]}"
        return unique_number
