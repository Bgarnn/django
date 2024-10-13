from local_lib.path import Path

def path_test():
    folder = Path('test_folder')
    file = folder / 'test_file.txt'
    if not folder.exists():
        folder.mkdir()
    with file.open(mode='w') as f:
        f.write('This is a test using the path module.')
    with file.open(mode='r') as f:
        print("File content:", f.read())

if __name__ == "__main__":
    path_test()
