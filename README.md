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

All values are Base64-encoded PEM blocks. To store in Kubernetes secrets, you can use the PEM (multi-line with BEGIN/END) or keep these Base64 strings as needed by your configuration.

## Notes
- X25519 keys are used for ECIES (encryption/decryption).
- Ed25519 keys are used for signing/verification.
- Never commit real production keys to source control.

