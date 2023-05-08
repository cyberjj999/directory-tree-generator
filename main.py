# Source:
# - https://chat.openai.com/c/25eac37b-d623-4a5e-a35a-f86ad9f43f07
# - https://stackoverflow.com/questions/9727673/list-directory-tree-structure-in-python
from pathlib import Path
from itertools import islice

space = '    '
branch = '│   '
tee = '├── '
last = '└── '


def tree(dir_path: Path, level: int = -1, include_files: bool = False,
         length_limit: int = 1000, folders_to_ignore: list = None, include_comments_placeholder: bool = False):
    """Given a directory Path object print a visual tree structure"""
    if folders_to_ignore is None:
        folders_to_ignore = []

    dir_path = Path(dir_path)  # accept string coerceable to Path
    files = 0
    directories = 0

    def inner(dir_path: Path, prefix: str = '', level=-1):
        nonlocal files, directories
        if not level:
            return  # 0, stop iterating
        if not include_files:
            contents = [d for d in dir_path.iterdir() if d.is_dir()
                        and d.name not in folders_to_ignore]
        else:
            contents = [p for p in dir_path.iterdir(
            ) if p.name not in folders_to_ignore]
        pointers = [tee] * (len(contents) - 1) + [last]
        for pointer, path in zip(pointers, contents):
            if path.is_dir():
                if include_comments_placeholder:
                    yield prefix + branch.strip() + '   // example comment'
                yield prefix + pointer + path.name
                directories += 1
                extension = branch if pointer == tee else space
                yield from inner(path, prefix=prefix+extension, level=level-1)
            elif include_files:
                if include_comments_placeholder:
                    yield prefix + branch.strip() + '   // example comment'
                yield prefix + pointer + path.name
                files += 1

    if include_comments_placeholder:
        print('// example comment')
    print(dir_path.name)
    iterator = inner(dir_path, level=level)
    for line in islice(iterator, length_limit):
        print(line)
    if next(iterator, None):
        print(f'... length_limit, {length_limit}, reached, counted:')
    print(f'\n{directories} directories' +
          (f', {files} files' if files else ''))


if __name__ == "__main__":
    folder_path = 'C://Users/JJ/Desktop/Personal Learning/Javascript Project/React Tutorial/react-game-marketplace-webapp'
    level_deep = 2
    include_files = False
    folders_to_ignore = ['node_modules']
    include_comments_placeholder = False

    tree(folder_path, level_deep, include_files,
         folders_to_ignore=folders_to_ignore, include_comments_placeholder=include_comments_placeholder)
