
# Project Structure Explorer

**Motivation**  
I created this tool after struggling to explain project structures and errors to ChatGPT. It was difficult to clearly communicate my project's directory structure and file contents. With this tool, you can easily generate a visual representation of your project's directory structure, including file contents if desired, which can then be shared or used to debug with AI models like ChatGPT.

## Features
- **Visualize Directory Structure**: Print the entire directory structure of your project.
- **Include File Contents**: Optionally append the contents of specific files or directories to the output for detailed exploration.
- **Ignore List**: Specify files and folders to ignore while exploring the structure.
- **Full Explore List**: Define directories for detailed exploration and file content output.
- **Write Output to File**: Generate an output file containing the directory structure and selected file contents.

## Example Directory Structure

Here’s a sample output showing a typical directory structure:

```
|-- src
    |-- app.py
    |-- utils.py
|-- tests
    |-- test_app.py
|-- README.md
|-- .gitignore
|-- venv (ignored)
|-- __pycache__ (ignored)
```

## Usage

### 1. Print the Directory Structure:
To print your directory structure, navigate to your project directory and run:

```
python explorer.py
```

This will print the directory structure, ignoring default directories like `venv`, `__pycache__`, and `.git`.

### 2. Write Directory Structure and File Contents to an Output File:
To generate a file (`structure.txt`) with the directory structure and the contents of specific files, use:

```
python explorer.py -w
```

### 3. Specify Directories for Detailed Exploration:
To explore specific directories and include their contents, use the `--explore` option:

```
python explorer.py --explore src,tests
```

This will include the contents of the files inside the `src` and `tests` directories in the output.

### 4. Custom Ignore List:
If you want to add more files or directories to ignore, simply pass them as arguments:

```
python explorer.py venv .cache
```

This command will ignore the `venv` and `.cache` directories while printing the structure or writing to the output file.

## How It Works

- **`print_directory_structure(path, ignore_list, full_explore_list)`**: Recursively prints the directory structure, ignoring any directories or files on the ignore list and optionally fully exploring directories on the explore list.
  
- **`write_file_contents(path, ignore_list, full_explore_list)`**: Appends the contents of files in explored directories to the output.

- **`write_structure_and_contents(directory_path, ignore_list, output_filename, full_explore_list)`**: Combines the directory structure and file content writing functionalities into a single output file.

---

You can use this tool to generate a clean, structured output of your project that you can share or use for troubleshooting with AI tools.
