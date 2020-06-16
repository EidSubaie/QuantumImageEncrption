from tools import encrypt, decrypt
from utils import generate_key
from PIL import Image


def demo():
    FILENAME = "random.png"
    
    with open(FILENAME) as f:
        image = Image.open(f, "r")
    
    key = generate_key()
    quantum_encrypted_image = encrypt(image, key)
    decrypted_image = decrypt(quantum_encrypted_image, key)
    decrypted_image.save('decrypted.png')

if __name__ == "__main__":
    demo()
