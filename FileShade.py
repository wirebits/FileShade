# FileShade
# A tool which transfer files in password protected text.
# Author - WireBits

import base64
import argparse

def encode_xor(key, filepath):
    with open(filepath, 'rb') as file:
        data = file.read()
    encoded_data = bytes([b ^ ord(key[i % len(key)]) for i, b in enumerate(data)])
    return encoded_data

def decode_xor(key, encoded_data):
    decoded_data = bytes([b ^ ord(key[i % len(key)]) for i, b in enumerate(encoded_data)])
    return decoded_data

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="FileShade")
    parser.add_argument("-e", "--encode", action="store_true", help="Encode the input file")
    parser.add_argument("-d", "--decode", action="store_true", help="Decode the input file")
    parser.add_argument("-p", "--password", required=True, help="Password to protect/decrypt the file")
    parser.add_argument("-i", "--input", required=True, help="Input file to encode/decode")

    args = parser.parse_args()

    if args.encode:
        encoded_data = encode_xor(args.password, args.input)
        output_filename = args.input + ".txt"
        with open(output_filename, "wb") as file:
            file.write(base64.urlsafe_b64encode(encoded_data))
        print(f"File has been encoded and saved as {output_filename}!")
    elif args.decode:
        if not args.input.endswith('.txt'):
            print("Error: Input file must be a .txt file.")
            exit(1)
        input_filename = args.input[:-4]
        with open(args.input, "rb") as file:
            encoded_data = base64.urlsafe_b64decode(file.read())
        decoded_data = decode_xor(args.password, encoded_data)
        with open(input_filename, "wb") as file:
            file.write(decoded_data)
        print(f"File has been decoded and saved as {input_filename}!")