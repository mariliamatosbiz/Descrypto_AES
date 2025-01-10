from itertools import product
import string
from Crypto.Cipher import AES
from binascii import unhexlify

def is_ascii_readable(text):
    """Verifica se o texto é legível em ASCII."""
    try:
        text.decode('ascii')
        return True
    except UnicodeDecodeError:
        return False

def decrypt_aes_ecb(ciphertext, key):
    """Descriptografa o texto cifrado usando AES no modo ECB."""
    cipher = AES.new(key.encode('utf-8'), AES.MODE_ECB)
    return cipher.decrypt(ciphertext)

def brute_force_aes(ciphertext, key_prefix, unknown_length):
    """Realiza força bruta para descobrir a chave AES."""
    charset = string.ascii_letters + string.digits
    for combination in product(charset, repeat=unknown_length):
        key = key_prefix + ''.join(combination)
        try:
            decrypted = decrypt_aes_ecb(ciphertext, key)
            if is_ascii_readable(decrypted):
                return key, decrypted
        except ValueError:
            continue
    return None, None

def main():
    # Arquivos de entrada
    weak_file = "arquivo-weak-7.in-full.hex"
    # strong_file = "arquivo-strong-7.in-full.hex"

    # Lendo os arquivos de entrada
    with open(weak_file, 'r') as f:
        weak_ciphertext = unhexlify(f.read().strip())

    # with open(strong_file, 'r') as f:
    #     strong_ciphertext = unhexlify(f.read().strip())

    # Configurações para a chave fraca
    weak_prefix = "SecurityAES"
    weak_unknown_length = 5

    # Quebrando a chave fraca
    print("Quebrando a chave fraca...")
    weak_key, weak_decrypted = brute_force_aes(weak_ciphertext, weak_prefix, weak_unknown_length)
    if weak_key:
        print(f"Chave fraca encontrada: {weak_key}")
        print(f"Texto decifrado: {weak_decrypted.decode('ascii')}")
    else:
        print("Falha ao quebrar a chave fraca.")

    # # Configurações para a chave forte
    # strong_prefix = "Security00"
    # strong_unknown_length = 6

    # # Quebrando a chave forte
    # print("Quebrando a chave forte...")
    # strong_key, strong_decrypted = brute_force_aes(strong_ciphertext, strong_prefix, strong_unknown_length)
    # if strong_key:
    #     print(f"Chave forte encontrada: {strong_key}")
    #     print(f"Texto decifrado: {strong_decrypted.decode('ascii')}")
    # else:
    #     print("Falha ao quebrar a chave forte.")

if __name__ == "__main__":
    main()
