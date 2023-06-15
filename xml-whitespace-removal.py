import os
import chardet

# Define the path to the original XML file
original_file_path = 'input-file.xml'

# Define the path to the updated XML file
updated_file_path = 'output-file.xml'

# Detect the encoding of the original file
with open(original_file_path, 'rb') as original_file:
    result = chardet.detect(original_file.read())
    encoding = result['encoding']

# Open the original file for reading and the updated file for writing, using the detected encoding
with open(original_file_path, 'r', encoding=encoding) as original_file, open(updated_file_path, 'w', encoding='utf-8') as updated_file:
    # Iterate over each line in the original file
    for line in original_file:
        # Remove trailing whitespace from the line
        updated_line = line.rstrip()
        
        # Write the updated line to the updated file
        updated_file.write(updated_line + os.linesep)

# Print a success message indicating the process is completed
print('Whitespace removed successfully!')
