# 🖼️ Image Encryption and Decryption Tool | Aatheka Abdul Kadar

This project is a simple Python-based tool that encrypts and decrypts images using a **pixel value shifting technique**. It leverages the **Python Imaging Library (Pillow)** to read, manipulate, and save images.

---

## 🔐 Features

- Encrypts an image by shifting each pixel's RGB values using a **secret key**.
- Decrypts the encrypted image using the same key.
- Supports any image format compatible with **Pillow** (e.g., JPG, PNG).
- Simple command-line interface for user interaction.

---

## ⚙️ How It Works

1. The tool reads an image pixel by pixel.
2. For each pixel `(r, g, b)`, it adds the secret key to each channel during **encryption**:
(r + key) % 256, (g + key) % 256, (b + key) % 256

3. During **decryption**, it subtracts the key:
(r - key) % 256, (g - key) % 256, (b - key) % 256

4. The `% 256` ensures that pixel values stay within the valid range `[0, 255]`.

---

## 📦 Requirements

- Python 3.x
- [Pillow](https://pypi.org/project/Pillow/) library

Install Pillow with:

```bash
pip install pillow
```

---

## ▶️ Usage

1. Save the script as image_cipher.py

2. Run it from the terminal:

```bash
python image_cipher.py
```

3. Choose whether to Encrypt (e) or Decrypt (d).

4. Enter:

-Input image path (e.g., photo.jpg)

-Output image path (e.g., photo_encrypted.png)

-Secret key (an integer)


---

## ⚠️ Notes

- The same key used for encryption must be used for decryption.

- Using the wrong key will result in a distorted image.

- Only works with RGB images. If using grayscale or images with alpha channel, slight modifications may be needed.
