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

## Sample Output

```
### Hawcx Side Keys ###

IDP_ED25519_PRIVATE_KEY_PEM: LS0tLS1CRUdJTiBQUklWQVRFIEtFWS0tLS0tCk1DNENBUUF3QlFZREsyVndCQ0lFSU9LdHViSmF2WHZrWG05SHptL2xqTyt1dnA1M0xNWHpIRjQ3SzlzZlFHSFoKLS0tLS1FTkQgUFJJVkFURSBLRVktLS0tLQo=
IDP_X25519_PRIVATE_KEY_PEM: LS0tLS1CRUdJTiBQUklWQVRFIEtFWS0tLS0tCk1DNENBUUF3QlFZREsyVnVCQ0lFSURnT2oyekFtNFZmRHROOXhPZlNkQm1NZEFxMWs1OC85Wm9TMFEvVGNOOUEKLS0tLS1FTkQgUFJJVkFURSBLRVktLS0tLQo=
SP_ED25519_PUBLIC_KEY_PEM: LS0tLS1CRUdJTiBQVUJMSUMgS0VZLS0tLS0KTUNvd0JRWURLMlZ3QXlFQUxObjB4cDV3TVdtQ1ZQZTBqMnRzM09sdGZLWisxWm5oc0Vmc21SYS9YVWc9Ci0tLS0tRU5EIFBVQkxJQyBLRVktLS0tLQo=
SP_X25519_PUBLIC_KEY_PEM: LS0tLS1CRUdJTiBQVUJMSUMgS0VZLS0tLS0KTUNvd0JRWURLMlZ1QXlFQXE1UzNSQ1ZucU56TXNNb21kS2RubEJQb2FjdmxJTGhKc1M4bXRyRTUzeE09Ci0tLS0tRU5EIFBVQkxJQyBLRVktLS0tLQo=

### Customer Side Keys ###

SP_X25519_PRIVATE_KEY_PEM: LS0tLS1CRUdJTiBQUklWQVRFIEtFWS0tLS0tCk1DNENBUUF3QlFZREsyVnVCQ0lFSU9qSWZuNUxaRmRVYVduSEttb0ErYkJjZVZmTFc2NGxnZW9TSGdkbG5jbGcKLS0tLS1FTkQgUFJJVkFURSBLRVktLS0tLQo=
IDP_X25519_PUBLIC_KEY_PEM: LS0tLS1CRUdJTiBQVUJMSUMgS0VZLS0tLS0KTUNvd0JRWURLMlZ1QXlFQXExRUx2SVd1VElQLzhncmJocWVqQkl0UEluTGxVK2c4UXQzZ05qVGpVa3c9Ci0tLS0tRU5EIFBVQkxJQyBLRVktLS0tLQo=
IDP_ED25519_PUBLIC_KEY_PEM: LS0tLS1CRUdJTiBQVUJMSUMgS0VZLS0tLS0KTUNvd0JRWURLMlZ3QXlFQWl4bklzRi9IQnpZYjE1WW5HOXRodEJ6Q2V6WXhOQ3dsZDRYeEd0dkg3TFU9Ci0tLS0tRU5EIFBVQkxJQyBLRVktLS0tLQo=
SP_ED25519_PRIVATE_KEY_PEM: LS0tLS1CRUdJTiBQUklWQVRFIEtFWS0tLS0tCk1DNENBUUF3QlFZREsyVndCQ0lFSUI0US85S2FvMW4yVWhWRlRteUVYbXlPUGxjd0Vsa0VzelRCYm5yK1FkS1EKLS0tLS1FTkQgUFJJVkFURSBLRVktLS0tLQo=
```

## Notes
- X25519 keys are used for ECIES (encryption/decryption).
- Ed25519 keys are used for signing/verification.
- Never commit real production keys to source control.

