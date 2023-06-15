import codecs
import time

start = time.time()  # Stores the start time of execution


def process_line(line):
    if line.count("\\") >= 5:
        fifth_backslash_index = -1
        for _ in range(5):
            fifth_backslash_index = line.index("\\", fifth_backslash_index + 1)
        line = line[:fifth_backslash_index + 1]
    line = line.rstrip("\\")  # Removes the trailing backslash from the line
    return line

input_file_name = "value.txt"
output_file_name = "value_processed.txt"

with codecs.open(input_file_name, "r", encoding="utf-8") as input_file, open(output_file_name, "w") as output_file:
    for line in input_file:
        if line.count("\\") < 5:
            output_file.write(line)
        else:
            processed_line = process_line(line)
            output_file.write(processed_line + "\n")

end = time.time()  # Stores the end time of execution
execution_time = end - start  # Calculates the total execution time

print("Execution time:", execution_time, "seconds")
