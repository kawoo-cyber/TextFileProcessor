# file_processor.py

# Step 1: Create and write to input.txt
with open("input.txt", "w") as file:
    file.write("This is the first line.\n")
    file.write("Python makes file handling easy.\n")
    file.write("We are writing a simple script.\n")
    file.write("This script reads and processes text files.\n")
    file.write("Finally, it writes the results to a new file.\n")

# Step 2: Read the contents of input.txt
with open("input.txt", "r") as file:
    content = file.read()

# Step 3: Process the content
word_count = len(content.split())  # Count the number of words
uppercase_content = content.upper()  # Convert text to uppercase

# Step 4: Write the processed text and word count to output.txt
with open("output.txt", "w") as file:
    file.write(uppercase_content)
    file.write(f"\n\nWord Count: {word_count}")

# Step 5: Print success message
print("Processing complete! Check output.txt for results.")
