import os

def count_lines_in_folder(folder, extensions=(".py",)):
    total_lines = 0
    for root, _, files in os.walk(folder):
        for file in files:
            if file.endswith(extensions):
                with open(os.path.join(root, file), 'r', encoding='utf-8', errors='ignore') as f:
                    total_lines += sum(1 for _ in f)
    return total_lines

folder_path = "land"
print(count_lines_in_folder(folder_path))  # or the path to your project folder