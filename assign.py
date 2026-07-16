from pydantic import BaseModel
from passlib.context import CryptContext

class SignupRequest(BaseModel):
    password: str

# CryptoContext Objects

bcrypt_context = CryptContext(schemes=["bcrypt"])
argon2_context = CryptContext(schemes=["argon2"])

TEST_PASSWORDS = [
    "Sunshine@2024", "P@ssword-" + "X" * 70
]

# hash password function

def hash_password(password: str):
    password_bytes = password.encode("utf-8")
    if len(password_bytes) < 72:
        print(f"{password[:20]}--- Hashed using Bcrypt")
        return bcrypt_context.hash(password)
    else: 
        print(f"{password[:20]}--- Hashed using argon2")
        return argon2_context.hash(password)
    
for pwd in TEST_PASSWORDS:
    request = SignupRequest(password=pwd)
    hashed_password = hash_password(request.password)
    print("Hash:", hashed_password)
    print("-" * 60)


# The signup endpoint must always use HTTPS because it encrypts passwords while they travel between the client and the server. Using plain HTTP would allow attackers to intercept sensitive information, leading to credentials theft and authorized access.
    