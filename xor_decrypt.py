import base64

# Step 1: Caesar Cipher brute-force
ciphertext = "mznxpz"
alphabet = 'abcdefghijklmnopqrstuvwxyz'

for shift in range(26):
    decrypted = ''.join(alphabet[(alphabet.index(c) - shift) % 26] for c in ciphertext)
    if decrypted == "rescue":
        print(f"Shift {shift}: {decrypted}")

# Step 2: The passphrase (anagram of 'rescue')
passphrase = "SECURE"

# Step 3: XOR decryption
b64_cipher = "Jw0KBlIMAEUXHRdFKyoxVRENEgkPEBwCFkQ="
data = base64.b64decode(b64_cipher)

# Repeat the key to match data length
key = (passphrase * (len(data) // len(passphrase) + 1)).encode()[:len(data)]

# XOR decryption
plaintext_bytes = bytes([b ^ k for b, k in zip(data, key)])
plaintext = plaintext_bytes.decode(errors='ignore')

print("\nDecrypted message:")
print(plaintext)