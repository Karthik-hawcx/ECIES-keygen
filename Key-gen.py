import base64
from cryptography.hazmat.primitives.asymmetric import x25519, ed25519
from cryptography.hazmat.primitives import serialization

def pem_base64(pem_bytes):
    """Convert PEM bytes to Base64 (compact single-line string)."""
    return base64.b64encode(pem_bytes).decode("utf-8")

def priv_pem(key):
    return key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption(),
    )

def pub_pem(key):
    return key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo,
    )

# --- Generate Set 1 (Hawcx/IDP keys) ---
set1_x_priv = x25519.X25519PrivateKey.generate()
set1_x_pub = set1_x_priv.public_key()

set1_ed_priv = ed25519.Ed25519PrivateKey.generate()
set1_ed_pub = set1_ed_priv.public_key()

# --- Generate Set 2 (Customer/SP keys) ---
set2_x_priv = x25519.X25519PrivateKey.generate()
set2_x_pub = set2_x_priv.public_key()

set2_ed_priv = ed25519.Ed25519PrivateKey.generate()
set2_ed_pub = set2_ed_priv.public_key()

# ---------------------------------------------------------------------
# 🟦 Hawcx side configuration (sends its priv + customer's pub)
# ---------------------------------------------------------------------
print("### Hawcx Side Keys ###\n")
print(f"IDP_ED25519_PRIVATE_KEY_PEM: {pem_base64(priv_pem(set1_ed_priv))}")
print(f"IDP_X25519_PRIVATE_KEY_PEM: {pem_base64(priv_pem(set1_x_priv))}")
print(f"SP_ED25519_PUBLIC_KEY_PEM: {pem_base64(pub_pem(set2_ed_pub))}")
print(f"SP_X25519_PUBLIC_KEY_PEM: {pem_base64(pub_pem(set2_x_pub))}\n")

# ---------------------------------------------------------------------
# 🟩 Customer side configuration (sends its priv + Hawcx’s pub)
# ---------------------------------------------------------------------
print("### Customer Side Keys ###\n")
print(f"SP_X25519_PRIVATE_KEY_PEM: {pem_base64(priv_pem(set2_x_priv))}")
print(f"IDP_X25519_PUBLIC_KEY_PEM: {pem_base64(pub_pem(set1_x_pub))}")
print(f"IDP_ED25519_PUBLIC_KEY_PEM: {pem_base64(pub_pem(set1_ed_pub))}")
print(f"SP_ED25519_PRIVATE_KEY_PEM: {pem_base64(priv_pem(set2_ed_priv))}")


