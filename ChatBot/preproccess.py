import re

def preprocess_script(input_file_path, output_file_path):
    # Read the content of the script file
    with open(input_file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    # Initialize variables
    processed_lines = []
    current_character = None
    dialogue_buffer = []

    # Process each line
    for line in lines:
        line = line.strip()  # Remove leading/trailing whitespace

        # Detect if the line is a character name in all caps
        if re.match(r'^[A-Z\s]+$', line) and not any(c.islower() for c in line):
            # If there's a current character, save their accumulated dialogue
            if current_character:
                processed_lines.append(f'{current_character}: {" ".join(dialogue_buffer)}')
                dialogue_buffer = []
            current_character = line
        else:
            # Collect dialogue lines
            if current_character:
                dialogue_buffer.append(line)

    # Save the last character's dialogue if applicable
    if current_character and dialogue_buffer:
        processed_lines.append(f'{current_character}: {" ".join(dialogue_buffer)}')

    # Write the processed script to a new file
    with open(output_file_path, "w", encoding="utf-8") as file:
        file.write('\n'.join(processed_lines))

    print(f"Processed script saved to {output_file_path}")

# Path to the input file and output file
input_file_path = "Step_Brothers_Script.txt"
output_file_path = "Processed_Step_Brothers_Script.txt"

# Preprocess the script
preprocess_script(input_file_path, output_file_path)
