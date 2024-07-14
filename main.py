from PIL import Image
import numpy as np

def encode_message(image_path, message, output_path):
    image = Image.open(image_path)
    image = image.convert("RGB")
    np_image = np.array(image)

    #binary conversion
    binary_message = ''.join([format(ord(char), '08b') for char in message])
    # Add a delimiter to mark the end of the message
    binary_message += '1111111111111110'  

    message_index = 0
    for row in np_image:
        for pixel in row:
            for color_index in range(3):
                if message_index < len(binary_message):
                    # Modify the least significant bit of each color value
                    pixel[color_index] = int(bin(pixel[color_index])[2:-1] + binary_message[message_index], 2)
                    message_index += 1

    # Save the image
    encoded_image = Image.fromarray(np_image)
    encoded_image.save(output_path)
    print(f"Message encoded in {output_path}")

def decode_message(image_path):
    # Load the image
    image = Image.open(image_path)
    image = image.convert("RGB")
    np_image = np.array(image)

    binary_message = ''
    for row in np_image:
        for pixel in row:
            for color_index in range(3):  
                # Extract the least significant bit (LSB) of each color value
                binary_message += bin(pixel[color_index])[-1]

    # Split binary message by 8-bit chunks and convert to characters
    message = ''
    for i in range(0, len(binary_message), 8):
        byte = binary_message[i:i+8]
        if byte == '1111111111111110':  # Check for the delimiter
            break
        if len(byte) == 8:
            message += chr(int(byte, 2))

    return message

def main():
 
 a = int(input("1. Encode\n2. Decode\n"))
 if(a==1):
  input_image_path = input("Enter the path to the input image: ")
  secret_message = input("Enter the message to be encoded: ")
  encode_message(input_image_path, secret_message, output_image_path)
  output_image_path = input("Enter the path to output image: ")

 if(a==2):
  output_image_path = input("Enter the path to output image: ")
  decoded_message = decode_message(output_image_path)
  print(f"Decoded message: {decoded_message}")

if __name__ == '__main__' :
   main()