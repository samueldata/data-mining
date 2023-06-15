import time

start = time.time()  # Stores the start time of execution

input_file_name = "value_processed_no_blank.txt"
output_file_name = "path_label.txt"

with open(input_file_name, "r") as input_file, open(output_file_name, "w") as output_file:
    for line in input_file:
        line = line.rstrip("\n")  # Removes the trailing newline, if any
        last_backslash_index = line.rfind("\\")  # Finds the index of the last backslash
        if last_backslash_index != -1:  # Checks if the line contains at least one backslash
            string_after_backslash = line[last_backslash_index + 1:]  # Extracts the string after the last backslash
            output_file.write(string_after_backslash + "\n")  # Writes the string to the output file

end = time.time()  # Stores the end time of execution
execution_time = end - start  # Calculates the total execution time

print("Execution time:", execution_time, "seconds")
