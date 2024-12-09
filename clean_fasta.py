import os
import re

# Function to extract text within parentheses from the first line of a FASTA file
def modify_fasta_header(fasta_file):
    try:
        with open(fasta_file, "r") as file:
            lines = file.readlines()
        
        if lines:
            # Extract text within parentheses from the first line using regex
            header = lines[0]
            match = re.search(r'\((.*?)\)', header)  # Extract text inside parentheses
            if match:
                # Replace the first line with the content inside the parentheses
                lines[0] = f"{match.group(1)}\n"
            
            # Write the modified content back to the file
            with open(fasta_file, "w") as file:
                file.writelines(lines)
            print(f"Header modified for {fasta_file}")
        else:
            print(f"No content in file: {fasta_file}")
    except Exception as e:
        print(f"Error processing {fasta_file}: {e}")

# Directory containing the FASTA files
fasta_directory = './fasta_files'  # Replace with the path to your directory containing FASTA files

# List all FASTA files in the directory
fasta_files = [f for f in os.listdir(fasta_directory) if f.endswith('.fasta')]

# Process each FASTA file
for fasta_file in fasta_files:
    fasta_file_path = os.path.join(fasta_directory, fasta_file)
    modify_fasta_header(fasta_file_path)

print("Finished modifying all FASTA files.")
