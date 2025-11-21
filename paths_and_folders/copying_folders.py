from pathlib import Path
import shutil

scr = Path.home() / 'documents' / 'python_automation' / 'fun_w_folders'
dest = Path.home() / 'documents' / 'python_automation' / 'copying_stuff' / 'fun_w_folders'

shutil.copytree(scr, dest, dirs_exist_ok=True)
