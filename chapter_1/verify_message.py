import json
from typing import Union

from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPrivateKey, RSAPublicKey
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
import hashlib
from sympy import mod_inverse
from block import Block

# Configuration
GENERATE_PRIVATE_KEY = False
DERIVE_PUBLIC_KEY_FROM_PRIVATE_KEY = False
PRIVATE_KEY_FILE = "nelsonkey.pem"
PUBLIC_KEY_FILE = "nelsonkey.pub"
MESSAGE = b"Nelson likes cat"

def get_private_key():
    # We either generate the primary key or load it
    if GENERATE_PRIVATE_KEY:
        return rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend
        )
    else:
        with open(PRIVATE_KEY_FILE, 'rb') as private_key_file:
            return serialization.load_pem_private_key(
                private_key_file.read(),
                password=None,
                backend=default_backend()
            )

def get_public_key(private_key):
    if DERIVE_PUBLIC_KEY_FROM_PRIVATE_KEY:
        return private_key.public_key()
    else:
        with open(PUBLIC_KEY_FILE, 'rb') as public_key_file:
            return serialization.load_pem_public_key(
                public_key_file.read(),
                backend=default_backend()
            )


def get_signature(private_key):
    return private_key.sign(
        data=MESSAGE,
        padding=padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        algorithm=hashes.SHA256()
    )



def verify_message(message_signature, public_key):
    print(f'Message signature: {message_signature}')
    public_key.verify(
        message_signature,
        MESSAGE,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )

def test_rsa():
    """
    Primary variables -> Encryptin -> Decryptin
    """
    # 3 Primary data
    first_prime_number = 11
    second_prime_number = 17
    public_exponent = 7

    # 3 Complementary variables
    private_exponent = mod_inverse(public_exponent, (first_prime_number - 1) * (second_prime_number - 1))
    modulus = first_prime_number * second_prime_number
    plaintext_value = ord('A')

    # RSA Encryption
    encrypted_message = (plaintext_value ** public_exponent) % modulus
    print(f'Encrypted message: {encrypted_message}')  # Output: 142

    # RSA Decryption
    decrypted_message_value = (encrypted_message ** private_exponent) % modulus
    print(f'Decrypted message: {chr(decrypted_message_value)}')  # Output: A


def sign_and_verify():
    # Private - Public - Signature - Verify
    private_key: RSAPrivateKey = get_private_key()
    public_key: RSAPublicKey = get_public_key(private_key)
    signature = get_signature(private_key)
    verify_message(signature, public_key)

def find_string_that_makes_hash_start_with_zero(leading_zeros_count, obj):
    # Make JSON and encode
    obj_string = json.dumps(obj.__dict__).encode('utf-8')
    print(obj_string)
    for number in range(10_000_000):
        combined_string_hash = hashlib.sha256(obj_string + str(number).encode('utf-8')).hexdigest()
        if combined_string_hash[0:leading_zeros_count] == '0' * leading_zeros_count:
            print(f'Found string that makes object hash start with zero: {number}')
            print(f'Final hash: {combined_string_hash}')
            return combined_string_hash

def main():
    sign_and_verify()
    test_rsa()
    find_string_that_makes_hash_start_with_zero(5, Block())

main()