import argparse
import hashlib
import os
import random
from tqdm import tqdm

# Make sure to install tqdm if you haven't already
# pip install tqdm

def sha256(data):
    return hashlib.sha256(data).hexdigest()

def add_random_spaces(file_content):
    lines = file_content.split('\n')
    modified_lines = []
    for line in lines:
        if random.random() > 0.5:
            line += ' ' * (random.randint(0, 1) + 1)
        modified_lines.append(line)
    return '\n'.join(modified_lines)

def load_file(file_path):
    with open(file_path, 'r') as f:
        return f.read()

def save_file(file_path, data):
    with open(file_path, 'w') as f:
        f.write(data)

def compare_hashes(fake_file, real_file, bits_to_match):
    progress_bar = tqdm(total=None, desc=f"Searching for {bits_to_match} bits to match ", unit=" iterations ")
    fake_file_content = load_file(fake_file)
    
    with open(real_file, 'rb') as temp_file:
        real_hash = sha256(temp_file.read())

    while True:
        modified_content = add_random_spaces(fake_file_content)
        temp_file_path = "temp_modified_file.txt"
        with open(temp_file_path, 'w') as temp_file:
            temp_file.write(modified_content)

        with open(temp_file_path, 'rb') as temp_file:
            current_hash = sha256(temp_file.read())

        with open("results.txt", 'a') as results_file:
            results_file.write(current_hash + '\n')

        if current_hash[-bits_to_match:] == real_hash[-bits_to_match:]:
            progress_bar.close()
            print(f"Matching false confession file: {temp_file_path}")
            print(f"Real Hash: {real_hash}")
            print(f"Fake Hash: {current_hash}")
            break
        else:
            os.remove(temp_file_path)
            progress_bar.update(1)

def main():
    parser = argparse.ArgumentParser(description="Birthday attack on file hashes.")
    parser.add_argument("real_file", help="Path to the Real file")
    parser.add_argument("fake_file", help="Path to the fake file")
    parser.add_argument("-b", "--bits_to_match", type=int, default=10, help="Number of bits to match (default: 10)")

    args = parser.parse_args()

    real_file_path = args.real_file
    fake_file_path = args.fake_file
    bits_to_match = args.bits_to_match
    
    compare_hashes(fake_file_path, real_file_path, bits_to_match)

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    main()