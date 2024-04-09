import os
import hashlib

def hash_file(file_path):
    # Generate the hash of a file
    hasher = hashlib.sha256()
    with open(file_path, 'rb') as f:
        while True:
            data = f.read(65536)  # Read in 64kb chunks
            if not data:
                break
            hasher.update(data)
    return hasher.hexdigest()

def search_hash(hash_to_find):
    # Define the root directory to start searching from
    root_dir = "C:\\"  # Update this with the root directory you want to start searching from

    # Initialize a flag to track if the hash is found
    hash_found = False

    # Loop through all files in the directory
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            file_path = os.path.join(root, file)
            # Compute the hash of the file
            file_hash = hash_file(file_path)
            # Compare the hash with the user input
            if file_hash == hash_to_find:
                hash_found = True
                break  # Exit the loop if the hash is found

    # Check if the hash is found or not and return the result
    if hash_found:
        return "found"
    else:
        return "not found"

# Get user input for the hash to search for
hash_input = input("Enter the hash to search for: ")

# Search for the hash
result = search_hash(hash_input)

# Print the result
print(result)
