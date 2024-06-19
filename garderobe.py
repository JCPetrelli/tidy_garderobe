import os
import shutil
import sys
import termios
import tty
from collections import defaultdict
import argparse

# Function to scan and move files
def scan_and_move_files(source_folder):
    if not os.path.exists(source_folder):
        print(f"The folder {source_folder} does not exist.")
        return

    file_mappings = defaultdict(list)

    # Create mappings of extensions to file paths
    for file in os.listdir(source_folder):
        file_path = os.path.join(source_folder, file)
        if os.path.isfile(file_path):
            file_extension = os.path.splitext(file)[1].lower()
            if file_extension:
                file_mappings[file_extension].append(file_path)

    for ext, files in file_mappings.items():
        destination_folder = os.path.join(os.path.expanduser('~/Documents/Garderobe'), ext[1:].upper())
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)

        for file_path in files:
            file_name = os.path.basename(file_path)
            dest_path = os.path.join(destination_folder, file_name)
            base, extension = os.path.splitext(file_name)
            counter = 1
            # Avoid overwriting files
            while os.path.exists(dest_path):
                dest_path = os.path.join(destination_folder, f"{base}_{counter}{extension}")
                counter += 1
            shutil.move(file_path, dest_path)
            print(f"Moved {file_path} to {dest_path}")

# Function to get single character input without pressing Enter
def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

# Display the menu
def display_menu():
    print("Choose an option:")
    print("1: Tidy my Desktop")
    print("2: Tidy my Downloads")
    print("3: Tidy my current directory")
    print("Press the corresponding number key to choose an option.")

def main():
    parser = argparse.ArgumentParser(description="Tidy specific directories.")
    parser.add_argument('choice', nargs='?', help="Choice of directory to tidy: 1 for Desktop, 2 for Downloads, 3 for current directory.")
    args = parser.parse_args()

    if args.choice:
        choice = args.choice
    else:
        display_menu()
        choice = getch()

    if choice == '1':
        desktop_folder = os.path.join(os.path.expanduser('~'), 'Desktop')
        scan_and_move_files(desktop_folder)
    elif choice == '2':
        downloads_folder = os.path.join(os.path.expanduser('~'), 'Downloads')
        scan_and_move_files(downloads_folder)
    elif choice == '3':
        current_folder = os.getcwd()
        scan_and_move_files(current_folder)
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
