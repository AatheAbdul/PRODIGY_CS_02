from PIL import Image

def encrypt_image(input_path, output_path, key):
    image = Image.open(input_path)
    pixels = image.load()

    for i in range(image.size[0]):       # width
        for j in range(image.size[1]):   # height
            r, g, b = pixels[i, j]
            # Encrypt each channel with key (mod 256 to keep valid range)
            pixels[i, j] = (
                (r + key) % 256,
                (g + key) % 256,
                (b + key) % 256
            )

    image.save(output_path)
    print("Image encrypted and saved as:", output_path)

def decrypt_image(input_path, output_path, key):
    image = Image.open(input_path)
    pixels = image.load()

    for i in range(image.size[0]):
        for j in range(image.size[1]):
            r, g, b = pixels[i, j]
            # Decrypt each channel by reversing the encryption
            pixels[i, j] = (
                (r - key) % 256,
                (g - key) % 256,
                (b - key) % 256
            )

    image.save(output_path)
    print("Image decrypted and saved as:", output_path)

def main():
    print("Simple Image Encryption Tool")
    choice = input("Encrypt or Decrypt (e/d): ").lower()
    if choice not in ['e', 'd']:
        print("Invalid choice.")
        return

    input_path = input("Enter input image path (e.g., image.jpg): ")
    output_path = input("Enter output image path: ")
    try:
        key = int(input("Enter secret key (integer): "))
    except ValueError:
        print("Key must be an integer.")
        return

    if choice == 'e':
        encrypt_image(input_path, output_path, key)
    else:
        decrypt_image(input_path, output_path, key)

if __name__ == "__main__":
    main()
