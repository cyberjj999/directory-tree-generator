import os


def list_files(folder_path, level_deep, folders_to_ignore, include_files, level=0):
    if level >= level_deep:
        return

    items = os.listdir(folder_path)
    last_item = items[-1] if items else None

    for item in items:
        item_path = os.path.join(folder_path, item)

        if os.path.isdir(item_path):
            if item not in folders_to_ignore:
                tree_prefix = "│   " * \
                    (level - 1) + ("└───" if item ==
                                   last_item else "├───") if level > 0 else ""
                print(f"{tree_prefix}{item}")
                list_files(item_path, level_deep, folders_to_ignore,
                           include_files, level + 1)

        elif include_files:
            tree_prefix = "│   " * \
                (level - 1) + ("└───" if item ==
                               last_item else "├───") if level > 0 else ""
            print(f"{tree_prefix}{item}")


def main():
    folder_path = 'C://Users/JJ/Desktop/Personal Learning/Javascript Project/React Tutorial/react-game-marketplace-webapp'
    # Replace with your desired level deep
    level_deep = 3
    # Replace with folder names to ignore
    folders_to_ignore = ["node_modules"]
    include_files = True  # Set to False if you don't want to include files

    if os.path.isdir(folder_path):
        list_files(folder_path, level_deep, folders_to_ignore, include_files)
    else:
        print(f"Error: {folder_path} is not a valid directory path")


if __name__ == "__main__":
    main()
