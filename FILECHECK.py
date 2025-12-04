import hashlib

print("=== File Integrity Checker ===")

filename = input("Enter the file name: ")

def sha256_of_file(path):
    sha = hashlib.sha256()
    try:
        with open(path, "rb") as f:
            while chunk := f.read(4096):
                sha.update(chunk)
        return sha.hexdigest()
    except FileNotFoundError:
        print("File not found.")
        return None

file_hash = sha256_of_file(filename)

if file_hash:
    print("\nSHA-256 hash of the file:")
    print(file_hash)

    expected = input("\nEnter expected hash (or press Enter to skip): ")

    if expected:
        if expected.lower() == file_hash.lower():
            print("✔ The file matches the expected hash.")
        else:
            print("✘ WARNING: Hash does not match.")
