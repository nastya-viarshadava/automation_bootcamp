from pathlib import Path

# p = r'C:\Users\aviar\PycharmProjects\paths_and_folders'
# p = r'C:/Users/aviar/PycharmProjects/paths_and_folders'

p = input("Please enter the target folder")

path = Path(p)

if path.exists():
    print("I exist!")