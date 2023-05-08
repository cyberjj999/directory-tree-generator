import os


# def list_files(start_path, level_deep, folders_to_ignore, level=0):
#     if level >= level_deep:
#         return

#     for item in os.listdir(start_path):
#         item_path = os.path.join(start_path, item)

#         print(item)
#         if os.path.isdir(item_path):
#             if item not in folders_to_ignore:
#                 tree_prefix = "│   " * level if level > 0 else ""
#                 print(f"{tree_prefix}├───{item}")
#                 list_files(item_path, level_deep, level + 1)

#         else:
#             tree_prefix = "│   " * level if level > 0 else ""
#             print(f"{tree_prefix}└───{item}")


def better_tree_command(folder_path, desired_level):
    current_level = 0

    # Walk through the directory
    for root, dirs, files in os.walk(folder_path):
        # Increment the directory level
        current_level += 1

        # if we're currently 3 levels deep, but desired level is 2 (i.e. current_level > desired_level), then we don't need to do anything
        if current_level > desired_level:
            break

        # for file in files:
        #     # Join the root path and file name
        #     file_path = os.path.join(root, file)
        #     print(file_path)  # Print the file path


def generate_tree_prefix(level):
    return "│    "


def main():
    # filepath = input("Enter the directory path: ")
    # level_deep = int(input("Enter the level deep: "))
    folder_path = 'C://Users/JJ/Desktop/Personal Learning/Javascript Project/React Tutorial/react-game-marketplace-webapp'
    folders_to_ignore = ['node_modules']
    level_deep = 2

    if os.path.isdir(folder_path):
        list_files(folder_path, level_deep, folders_to_ignore)
    else:
        print(f"Error: {folder_path} is not a valid folder path")


if __name__ == "__main__":
    main()
