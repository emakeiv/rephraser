import jwt
import uuid
from pathlib import Path
from datetime import datetime, timedelta
from cryptography.x509 import load_pem_x509_certificate
from cryptography.hazmat.primitives import serialization


def encode_token():
    now = datetime.utcnow()
    payload = {
        "iss": "https://auth.coffeemesh.io/",
        "sub": str(uuid.uuid4()),
        "aud": "http://127.0.0.1:8000/",
        "iat": now.timestamp(),
        "exp": (now + timedelta(hours=24)).timestamp(),
        "scope": "openid",
    }

    private_key_text = (
        (Path(__file__).parent / "keys/private_key.pem").read_text().encode("utf-8")
    )
    private_key = serialization.load_pem_private_key(private_key_text, password=None)
    return jwt.encode(payload=payload, key=private_key, algorithm="RS256")


def decode_token(access_token):
    public_key_text = (
        (Path(__file__).parent / "keys/public_key.pem").read_text().encode("utf-8")
    )
    public_key = load_pem_x509_certificate(public_key_text).public_key()
    return jwt.decode(
        access_token,
        key=public_key,
        algorithms=jwt.get_unverified_header(access_token)["alg"],
        audience="http://127.0.0.1:8000/",
    )
