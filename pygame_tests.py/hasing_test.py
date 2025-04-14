import hashlib
import os

def hash_password(password):
    # Generate a random salt
    salt = os.urandom(16)

    # Hash the password with the salt
    hashed_password = hashlib.sha256(salt + password.encode()).hexdigest()
    return salt.hex() + ':' + hashed_password

def verify_password(stored_password, provided_password):
    salt, hashed_password = stored_password.split(':')
    return hashed_password == hashlib.sha256(bytes.fromhex(salt) + provided_password.encode()).hexdigest()

# Example usage
password_to_hash = "mysecretpassword"
stored_password = hash_password(password_to_hash)
print("Stored password:", stored_password)

# Verification
password_to_verify = "mysecretpassword"
if verify_password(stored_password, password_to_verify):
    print("Password verified successfully.")
else:
    print("Password verification failed.")

password_to_verify = "wrongpassword"
if verify_password(stored_password, password_to_verify):
    print("Password verified successfully.")
else:
    print("Password verification failed.")