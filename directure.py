import os
import sys

def print_directory_structure(path, indent_level=0, ignore_list=None, write_mode=False, output_file=None):
    # Get a list of all items (files and directories) in the given path
    items = os.listdir(path)

    if ignore_list is None:
        ignore_list = []

    for item in items:
        if item in ignore_list:
            continue  # Skip items that are in the ignore list

        # Get the absolute path of the item
        item_path = os.path.join(path, item)

        # Prepare the formatted line for the directory structure
        line = ' ' * indent_level + '|-- ' + item

        # Print the item to the console
        print(line)

        # If write_mode is enabled, write the line to the output file
        if write_mode and output_file:
            output_file.write(line + "\n")

            # If it's a file, also write its content to the output file
            if os.path.isfile(item_path):
                output_file.write("\n" + "-" * 40 + "\n")
                output_file.write(f"Content of {item}:\n\n")
                try:
                    with open(item_path, 'r') as file:
                        output_file.write(file.read())
                except Exception as e:
                    output_file.write(f"Error reading file {item}: {e}")
                output_file.write("\n" + "-" * 40 + "\n\n")

        # If the item is a directory, recursively call this function
        if os.path.isdir(item_path):
            print_directory_structure(item_path, indent_level + 4, ignore_list, write_mode, output_file)

# Function to write both directory structure and file contents to a file
def write_structure_and_contents(directory_path, ignore_list, output_filename):
    with open(output_filename, 'w') as f:
        # Write the directory structure and contents of files
        f.write("Directory Structure and File Contents:\n\n")
        print_directory_structure(directory_path, ignore_list=ignore_list, write_mode=True, output_file=f)

# Get the list of command-line arguments
args = sys.argv[1:]

# Check if -w flag is present for writing output to a file
write_mode = '-w' in args

# If -w is present, remove it from args and get the filename to write
if write_mode:
    args.remove('-w')
    output_filename = "directory_structure_and_contents.txt"

# The remaining args are files and directories to ignore
ignore_list = args

# Specify the path of the directory you want to analyze
directory_path = '/Users/atharvatonape/Desktop/Project'

# If write_mode is enabled, write the structure and contents to the output file
if write_mode:
    write_structure_and_contents(directory_path, ignore_list, output_filename)
    print(f"\nDirectory structure and contents written to {output_filename}")
else:
    # Just print the directory structure if -w flag is not provided
    print_directory_structure(directory_path, ignore_list=ignore_list)
