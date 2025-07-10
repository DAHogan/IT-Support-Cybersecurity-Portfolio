###### This script will scan a specific directory for files containing sensitive information (e.g., credit card numbers or social security numbers).

### Script Functionality:
  # The script will:
  # 1.  Take a directory path as input.
  # 2.  Scan all files in the directory for sensitive information.
  # 3.  Output the file names and paths of files containing sensitive information.

###  Sample Code:
import os
import re

def scan_directory(directory_path):
    # Define regular expressions for sensitive information
    cc_regex = r"\b\d{13,16}\b"  # Credit card numbers
    ssn_regex = r"\b\d{3}-\d{2}-\d{4}\b"  # Social security numbers

    # Scan files in the directory
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                with open(file_path, "r") as f:
                    file_content = f.read()
                    if re.search(cc_regex, file_content) or re.search(ssn_regex, file_content):
                        print(f"Sensitive information found in file: {file_path}")
            except Exception as e:
                print(f"Error scanning file: {file_path} - {str(e)}")

# Get directory path from user input
directory_path = input("Enter directory path: ")
scan_directory(directory_path)
