from PIL import Image
import numpy as np


def encrypt_decrypt_image(image_path, key, output_path):

    # Open image
    img = Image.open(image_path).convert("RGB")

    # Convert image to NumPy array
    img_array = np.array(img, dtype=np.uint8)

    # Resize key to match image shape
    key_array = np.resize(np.array(key, dtype=np.uint8), img_array.shape)

    # XOR operation
    result_array = np.bitwise_xor(img_array, key_array)

    # Convert array back to image
    result_img = Image.fromarray(result_array)

    # Save image
    result_img.save(output_path)

    print(f"Saved: {output_path}")


# Encryption key
key = [123, 45, 67]

# Encrypt image
encrypt_decrypt_image(
    "jaguar.png",
    key,
    "encrypted_image.png"
)

# Decrypt image
encrypt_decrypt_image(
    "encrypted_image.png",
    key,
    "decrypted_image.png"
)

print("Encryption and Decryption Completed Successfully.")