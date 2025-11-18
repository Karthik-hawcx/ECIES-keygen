# Key Generation (X25519 + Ed25519)

This folder contains a minimal requirements.txt to generate Hawcx (IDP) and Customer (SP) key pairs using the script at the repo root: `Key-gen.py`.

## Prerequisites
- Python 3.10+

## Setup
```bash
# From the repo root
python3 -m venv .venv
source .venv/bin/activate   # On macOS/Linux
# .venv\\Scripts\\activate    # On Windows PowerShell

pip install -r requirements.txt
```

## Generate keys
```bash
python3 Key-gen.py
```

You will see two blocks of output:
- Hawcx Side Keys: use in the auth service (IDP priv keys + SP pub keys)
- Customer Side Keys: use on the customer side (SP priv keys + IDP pub keys)

All values are PEM-formatted keys with BEGIN/END markers. To store in Kubernetes secrets, you can use these PEM blocks directly or Base64-encode them as needed by your configuration.

## Sample Output

```
### Hawcx Side Keys ###

IDP_ED25519_PRIVATE_KEY_PEM:
-----BEGIN PRIVATE KEY-----
MC4CAQAwBQYDK2VwBCIEIGj6UMel4v96Np4xSIO9bnI/hWS/yJj1cCyiQjiX1sa9
-----END PRIVATE KEY-----

IDP_X25519_PRIVATE_KEY_PEM:
-----BEGIN PRIVATE KEY-----
MC4CAQAwBQYDK2VuBCIEIHhbuUOEmuWP4skuX2OUHcvQoiRAkzysItCSzAJZI3lg
-----END PRIVATE KEY-----

SP_ED25519_PUBLIC_KEY_PEM:
-----BEGIN PUBLIC KEY-----
MCowBQYDK2VwAyEAF/8SqWHvy6yYWfcFWFxHaZxTjw7uR/fUXFLzfPSafVk=
-----END PUBLIC KEY-----

SP_X25519_PUBLIC_KEY_PEM:
-----BEGIN PUBLIC KEY-----
MCowBQYDK2VuAyEAwfWhFstumhNnQ99c3fIpYrZ+cmI4JIP1DdUD6CIqxD4=
-----END PUBLIC KEY-----

### Customer Side Keys ###

SP_X25519_PRIVATE_KEY_PEM:
-----BEGIN PRIVATE KEY-----
MC4CAQAwBQYDK2VuBCIEILJkfH5LZFdUaWanHmKoA+bBceVfLW64lgeoSHgdlnclg
-----END PRIVATE KEY-----

IDP_X25519_PUBLIC_KEY_PEM:
-----BEGIN PUBLIC KEY-----
MCowBQYDK2VuAyEAq1ELvIWuTIP/8grbhqejBItPInLu+Eg8Qt3gNjTjUkw=
-----END PUBLIC KEY-----

IDP_ED25519_PUBLIC_KEY_PEM:
-----BEGIN PUBLIC KEY-----
MCowBQYDK2VwAyEAixnIsF/HzbYb15YnG9thtBzCezYxNCwld4XxGtvH7LU=
-----END PUBLIC KEY-----

SP_ED25519_PRIVATE_KEY_PEM:
-----BEGIN PRIVATE KEY-----
MC4CAQAwBQYDK2VwBCIEIB4Q/9Kao1n2UhVFTmyEXmyOPlcwElkEszTBbnr+QdKQ
-----END PRIVATE KEY-----
```

## Notes
- X25519 keys are used for ECIES (encryption/decryption).
- Ed25519 keys are used for signing/verification.
- Never commit real production keys to source control.

