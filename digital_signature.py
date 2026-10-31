from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
from cryptography.hazmat.primitives import serialization

# 1. Generate a private key
private_key = Ed25519PrivateKey.generate()

# 2. Generate the corresponding public key
public_key = private_key.public_key()

# 3. Create a message
message = b"Send 1 BTC to Swati"

# 4. Sign the message using private key
signature = private_key.sign(message)

# 5. Verify the signature using public key
try:
    public_key.verify(signature, message)
    print("Signature is VALID!")
except Exception:
    print("Signature is INVALID!")

# 6. Display public key
public_bytes = public_key.public_bytes(
    encoding=serialization.Encoding.Raw,
    format=serialization.PublicFormat.Raw
)

print("Public Key:", public_bytes.hex())

# 7. Display signature
print("Digital Signature:", signature.hex())

# 8. Try modifying the message
modified_message = b"Send 10 BTC to Swati"

try:
    public_key.verify(signature, modified_message)
    print("Modified message is VALID!")
except Exception:
    print("Modified message is INVALID!")
