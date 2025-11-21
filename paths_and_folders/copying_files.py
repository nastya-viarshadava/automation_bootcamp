from pathlib import Path
import shutil

scr = Path.home() / 'PycharmProjects' / 'plaintext-files' / 'dad_jokes.txt'
dest = Path.home() / 'documents' / 'python_automation' / 'copying_stuff'
dest_file_path = dest / 'dad_jokes.txt'

if not(scr.exists()):
    print('The source file does not exist.')
elif dest_file_path.exists():
    print('The file already exists in the destination folder.')
else:
    shutil.copy(scr, dest)
