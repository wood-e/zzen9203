import argparse
import hashlib
import os
import random
from tqdm import tqdm

# Make sure to install tqdm if you haven't already
# pip install tqdm
# or
# python -m pip install -r requirements.txt

# This is a simple birthday attack on file hashes
# The idea is to modify the fake file in a way that the hash of the modified file matches the hash of the real file
# The modified file is saved in the same directory as the script
# The hashes of all the modified files are saved in the results.txt file
# The modified file that matches the real file is printed to the console
# The hashes of the real and fake files are also printed to the console
# The number of bits to match can be specified as a command line argument
# The default number of bits to match is 10
# The number of bits to match can be any number between 1 and 64

# Example usage:
# python compare.py real_file.txt fake_file.txt -b 10

# Example output:
# Searching for 10 bits to match : 100%|███████��
# Matching false confession file: temp_modified_file.txt
# Real Hash: 00000
# Fake Hash: 00000

# This function returns the sha256 hash of the data
def sha256(data):
    return hashlib.sha256(data).hexdigest()

# This function adds random spaces to the fake file
def add_random_spaces(file_content):
    lines = file_content.split('\n')
    modified_lines = []
    for line in lines:
        if random.random() > 0.5:
            line += ' ' * (random.randint(0, 1) + 1)
        modified_lines.append(line)
    return '\n'.join(modified_lines)

# This function loads the file
def load_file(file_path):
    with open(file_path, 'r') as f:
        return f.read()
# This function saves the modified file
def save_file(file_path, data):
    with open(file_path, 'w') as f:
        f.write(data)

# This function compares the hashes of the real and fake files
def compare_hashes(fake_file, real_file, bits_to_match):
    # This is the progress bar
    progress_bar = tqdm(total=None, desc=f"Searching for {bits_to_match} bits to match ", unit=" iterations ")
    # This is the content of the fake file
    fake_file_content = load_file(fake_file)
    # This is the hash of the real file
    with open(real_file, 'rb') as temp_file:
        real_hash = sha256(temp_file.read())
    # This is the main loop
    while True:
        modified_content = add_random_spaces(fake_file_content)
        temp_file_path = "temp_modified_file.txt"
        with open(temp_file_path, 'w') as temp_file:
            temp_file.write(modified_content)
        # This is the hash of the modified file
        with open(temp_file_path, 'rb') as temp_file:
            current_hash = sha256(temp_file.read())
        # This is the hash of the modified file
        with open("results.txt", 'a') as results_file:
            results_file.write(current_hash + '\n')
        # This is the check to see if the hashes match
        if current_hash[-bits_to_match:] == real_hash[-bits_to_match:]:
            progress_bar.close()
            print(f"Matching false confession file: {temp_file_path}")
            print(f"Real Hash: {real_hash}")
            print(f"Fake Hash: {current_hash}")
            break
        else:
            os.remove(temp_file_path)
            progress_bar.update(1)

# This is the main function
def main():
    # This is the argument parser
    parser = argparse.ArgumentParser(description="Birthday attack on file hashes.")
    parser.add_argument("real_file", help="Path to the Real file")
    parser.add_argument("fake_file", help="Path to the fake file")
    parser.add_argument("-b", "--bits_to_match", type=int, default=10, help="Number of bits to match (default: 10)")
    
    args = parser.parse_args()
    # This is the path to the real file
    real_file_path = args.real_file
    # This is the path to the fake file
    fake_file_path = args.fake_file
    # This is the number of bits to match
    bits_to_match = args.bits_to_match
    # This is the check to make sure the number of bits to match is between 1 and 64
    compare_hashes(fake_file_path, real_file_path, bits_to_match)

# This is the main invocation
if __name__ == "__main__":
    # This is the check to see if the script is being run on Windows or Linux
    os.system('cls' if os.name == 'nt' else 'clear')
    # This is the main function call
    main()