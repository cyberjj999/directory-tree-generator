# Directory Tree Generator

This Python script generates a visual representation of a directory tree structure, similar to the Linux `tree` command. It supports various customization options such as including or excluding files, ignoring specific folders, limiting the depth of the tree, and adding placeholder comments for each file or directory in the output.

## Features

- Display a visual representation of a directory tree structure
- Include or exclude files from the output
- Ignore specific folders
- Limit the depth of the tree
- Add placeholder comments for each file or directory in the output

## Requirements

- Python 3.6 or higher

## Usage

1. Clone or download the repository to your local machine.
2. Open the terminal or command prompt and navigate to the directory containing the `main.py` script.
3. Run the script by executing `python main.py`.
4. Customize the script by modifying the variables in the `if __name__ == "__main__":` block at the end of the script:

```python
if __name__ == "__main__":
    folder_path = 'path/to/your/folder'
    level_deep = 2
    include_files = False
    folders_to_ignore = ['node_modules']
    include_comments_placeholder = False

    tree(folder_path, level_deep, include_files,
         folders_to_ignore=folders_to_ignore, include_comments_placeholder=include_comments_placeholder)
```

- `folder_path`: The path to the folder you want to visualize.
- `level_deep`: The depth of the tree structure to display.
- `include_files`: Set to `True` to include files in the output, `False` to display only directories.
- `folders_to_ignore`: A list of folder names to ignore in the output.
- `include_comments_placeholder`: Set to `True` to include placeholder comments for each file or directory in the output.

## Example Output

```
// example comment
react-game-marketplace-webapp
│   // example comment
├── public
│   // example comment
├── src
│   // example comment
│   └── assets
│   // example comment
└── youtube-video-notes
```

This output shows a visual representation of a directory tree structure, with placeholder comments for each file and directory, and with the same indentation.