# Birthday Attack
This task is directly related to the Birthday Attack task where we needed to modify the last few digits of a file to prove that we can modify and hack a file to imitate the Birthday Attack.

## Dependencies
##Installation

1. Clone the repository to your local machine:
```bash
   git clone https://github.com/wood-e/zzen9203.git
```
2. Setup a virtual environment:
```bash
   python3 -m venv venv
```
3. Activate the virtual environment:
```bash
   source venv/bin/activate
```
4. Install the required dependencies:
```bash
    pip install -r requirements.txt
```
5. Run the script:
```bash
   python compare.py real_file.txt fake_file.txt -b 10
```

##Usage
This is an extremely simple tool that takes two files, a real one and a fake one and compares the hashes of the files. 
The tool will then modify the fake file until it's hash matches the provided number of bits of the hash that needs to be modified.

The Birthday Attack script supports the following command-line arguments:

--file: The path to the input file. This should be a plain text file containing the data to be hashed.
--hash: The hashing algorithm to use. Supported options include md5, sha1, and sha256.
--output: The path to the output file. This will be a text file containing the modified data.

The tool takes 3 arguments:
- real_file: The path to the real file. This is the text file containing the data of the real file
- fake_file: The path to the fake file. This is the file that you want to be modified to match the real_file
- -b: The number of bits that you want to match. This is the number of bits that you want to match in the hash of the real_file and the fake_file