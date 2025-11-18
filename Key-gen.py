from cryptography.hazmat.primitives.asymmetric import x25519, ed25519
from cryptography.hazmat.primitives import serialization

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
print("IDP_ED25519_PRIVATE_KEY_PEM:")
print(priv_pem(set1_ed_priv).decode("utf-8"))
print("IDP_X25519_PRIVATE_KEY_PEM:")
print(priv_pem(set1_x_priv).decode("utf-8"))
print("SP_ED25519_PUBLIC_KEY_PEM:")
print(pub_pem(set2_ed_pub).decode("utf-8"))
print("SP_X25519_PUBLIC_KEY_PEM:")
print(pub_pem(set2_x_pub).decode("utf-8"))
print()

# ---------------------------------------------------------------------
# 🟩 Customer side configuration (sends its priv + Hawcx’s pub)
# ---------------------------------------------------------------------
print("### Customer Side Keys ###\n")
print("SP_X25519_PRIVATE_KEY_PEM:")
print(priv_pem(set2_x_priv).decode("utf-8"))
print("IDP_X25519_PUBLIC_KEY_PEM:")
print(pub_pem(set1_x_pub).decode("utf-8"))
print("IDP_ED25519_PUBLIC_KEY_PEM:")
print(pub_pem(set1_ed_pub).decode("utf-8"))
print("SP_ED25519_PRIVATE_KEY_PEM:")
print(priv_pem(set2_ed_priv).decode("utf-8"))


