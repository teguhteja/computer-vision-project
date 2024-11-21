import sys
import os

def create_markdown_files(input_file):
    """
    Reads a text file and creates separate markdown files for each line.
    
    Args:
        input_file (str): Path to the input text file.
    """
    if not os.path.exists(input_file):
        print(f"Error: File '{input_file}' not found.")
        return

    try:
        with open(input_file, 'r', encoding='utf-8') as infile:
            lines = infile.readlines()
            for idx, line in enumerate(lines, start=1):
                line_content = line.strip()
                if line_content:  # Skip empty lines
                    file_name = f"{idx}.{line}.md"
                    with open(file_name, 'w', encoding='utf-8') as outfile:
                        outfile.write(f"# {line_content}\n")
                    print(f"Created: {file_name}")
    except Exception as e:
        print(f"Error while processing the file: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <input_text_file>")
    else:
        input_file = sys.argv[1]
        create_markdown_files(input_file)
