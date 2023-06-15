import re

# List of provided lines
lines = [
    "\\DIR01\\groups\\dependency01",
    "\\DIR01\\groups\\dependency02",
    # ... remaining lines
    "\\DIR99\\groups\\dependency99"
]

# Regular expression to find content between parentheses
pattern = r"\s?\(.*?\)"

# Iterate over the lines and remove content between parentheses
formatted_lines = []
for line in lines:
    formatted_line = re.sub(pattern, "", line)
    formatted_lines.append(formatted_line)

# Print the formatted lines
for line in formatted_lines:
    print(line)
