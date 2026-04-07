import hashlib

def generate_key(master_password):
    hash_object = hashlib.sha256(master_password.encode())
    return hash_object.hexdigest()
