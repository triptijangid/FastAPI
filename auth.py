from fastapi import HTTPException, status, Depends
from passlib.context import CryptContext
from fastapi.security import HTTPBasic, HTTPBasicCredentials

bcrypt_library = CryptContext(schemes=["bcrypt"])
security_app = HTTPBasic()
fake_user_db = {}

def sign_up(username: str, name: str, email: str, password: str):
    # TODO: Check if username already exists in fake_user_db; raise HTTP 400 if so
    if username in fake_user_db:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User is already exists. Please try different username.") 
    # TODO: Hash the password using bcrypt_library.hash()
    
    hashed_password = bcrypt_library.hash(password)
    # TODO: Store the user record (with hashed password, not raw password) in fake_user_db
    fake_user_db[username] = {
        "username": username,
        "name": name,
        "email": email,
        "password": hashed_password
    }

    return {"message": "User registered successfully."}

def authenticate_user(
    user_details: HTTPBasicCredentials = Depends(security_app)
):
    # TODO: Extract the username from user_details
    username = user_details.username
    password = user_details.password

    user = fake_user_db.get(username)
    # TODO: Check if username exists in fake_user_db; raise HTTP 401 if not found
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found. Please sign up first.")
    # TODO: Call bcrypt_library.verify(raw_password, stored_hash) to check the password
    if not bcrypt_library.verify(password, user["password"]):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invald Credentials.")
    # TODO: Return the username on success; raise HTTP 401 on failure
    return username
try:
    sign_up("alice_dev", "Alice Dev", "alice@example.com", "SecurePass99")
    print("Step 1: Success")
    print("Stored Password:", fake_user_db["alice_dev"]["password"])
except HTTPException as e:
    print(f"Step 1: {e.status_code} - {e.detail}")

try:
    sign_up(
        "alice_dev",
        "Alice Again",
        "alice2@example.com",
        "AnotherPass"
    )
except HTTPException as e:
    print(f"Step 2: {e.status_code} - {e.detail}")

try:
    credentials = HTTPBasicCredentials(username="alice_dev", password="SecurePass99")
    result = authenticate_user(credentials)
    print("Step 3:", result)
except HTTPException as e:
    print(f"Step 3: {e.status_code} - {e.detail}")

try:
    credentials = HTTPBasicCredentials(
        username="alice_dev",
        password="WrongPass"
    )
    result = authenticate_user(credentials)
    print("Step 4:", result)
except HTTPException as e:
    print(f"Step 4: {e.status_code} - {e.detail}")

try:
    credentials = HTTPBasicCredentials(
        username="bob_dev",
        password="AnyPass"
    )
    result = authenticate_user(credentials)
    print("Step 5:", result)
except HTTPException as e:
    print(f"Step 5: {e.status_code} - {e.detail}")