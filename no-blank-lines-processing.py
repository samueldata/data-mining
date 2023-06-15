import time

start = time.time()  # Stores the start time of execution

input_file_name = "value_processed.txt"
output_file_name = "value_processed_no_blank.txt"

with open(input_file_name, "r") as input_file, open(output_file_name, "w") as output_file:
    for line in input_file:
        if line.strip():  # Checks if the line is not blank
            output_file.write(line)

end = time.time()  # Stores the end time of execution
execution_time = end - start  # Calculates the total execution time

print("Execution time:", execution_time, "seconds")
