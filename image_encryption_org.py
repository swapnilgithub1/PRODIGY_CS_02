
from PIL import Image
import numpy as np
def encrypt_image(image_path, output_path, key):
     # Open the image
     image = Image.open(image_path)
     # Convert the image to a NumPy array
     image_array = np.array(image)
     # Apply the encryption key (simple XOR operation and swapping)
     np.random.seed(key)
     random_indices = np.random.permutation(image_array.size)
     flat_array = image_array.flatten()
     encrypted_array = flat_array[random_indices]
     # Reshape and convert back to image
     encrypted_array = encrypted_array.reshape(image_array.shape)
     encrypted_image = Image.fromarray(encrypted_array)
      # Save the encrypted image
     encrypted_image.save(output_path)
     print(f"Image encrypted and saved to {output_path}")
 
     
def decrypt_image(encrypted_path, output_path, key):
     # Open the encrypted image
     encrypted_image = Image.open(encrypted_path)
     # Convert the encrypted image to a NumPy array
     encrypted_array = np.array(encrypted_image)
     # Reverse the encryption key
     np.random.seed(key)
     random_indices = np.random.permutation(encrypted_array.size)
     decrypted_array = np.zeros_like(encrypted_array.flatten())
     decrypted_array[random_indices] = encrypted_array.flatten()
     # Reshape and convert back to image
     decrypted_array = decrypted_array.reshape(encrypted_array.shape)
     decrypted_image = Image.fromarray(decrypted_array)
     # Save the decrypted image
     decrypted_image.save(output_path)
     print(f"Image decrypted and saved to {output_path}")

if __name__ == "__main__":
    # Example usage
    key = 1234  # Encryption key (must be the same for encryption and decryption)

    # Encrypt the image
    encrypt_image("z1.png", "encrypted_image.png", key)

    # Decrypt the image
    decrypt_image("encrypted_image.png", "decrypted_image.png", key)

 
     
