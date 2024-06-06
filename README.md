
# Garderobe File Organizer

Garderobe is a simple Python script designed to help you organize files in your Desktop, Downloads, or current directory. The script scans the chosen folder, categorizes files by their extensions, and moves them to a structured directory within your `~/Documents/Garderobe` folder.

## Features

- Automatically categorizes and moves files based on their extensions.
- Avoids overwriting existing files by appending a counter to duplicate filenames.
- User-friendly menu for selecting which directory to tidy up.

## Prerequisites

- Python 3.x
- `shutil`, `os`, `sys`, `termios`, `tty`, and `collections` modules (all are part of the Python Standard Library)

## Installation

1. Clone this repository or download the script file.

   ```bash
   git clone https://github.com/JCPetrelli/tidy_garderobe.git
   ```

2. Navigate to the directory containing the script.

   ```bash
   cd garderobe
   ```

## Usage

1. Run the script.

   ```bash
   python3 garderobe.py
   ```

2. Follow the on-screen menu to choose an option:
   - Press `1` to tidy your Desktop.
   - Press `2` to tidy your Downloads.
   - Press `3` to tidy your current directory.

## How It Works

### Main Functions

- **scan_and_move_files(source_folder)**:
  - Scans the provided folder for files.
  - Categorizes files by their extensions.
  - Moves files to `~/Documents/Garderobe/<EXTENSION>` folder, creating the folder if it does not exist.

- **getch()**:
  - Captures a single character input from the user without requiring the Enter key to be pressed.

- **display_menu()**:
  - Displays a menu for the user to choose which directory to tidy.

### Main Flow

- Displays the menu to the user.
- Captures the user's choice.
- Calls `scan_and_move_files` with the appropriate folder based on the user's choice.

## Example

If you choose to tidy your Desktop, all files on your Desktop will be moved to corresponding folders in `~/Documents/Garderobe`. For instance, all `.txt` files will be moved to `~/Documents/Garderobe/TXT`.

## Using Terminal Aliases
To quickly trigger the Garderobe script, you can set up terminal aliases. This allows you to run the script with a simple command like tidy_desktop, tidy_downloads, or tidy_current.

Open your terminal and edit your shell configuration file (e.g., ~/.bashrc for Bash or ~/.zshrc for Zsh):

bash
Copy code
nano ~/.bashrc
# or
nano ~/.zshrc
Add the following aliases to the file:

bash
Copy code
alias tidy_desktop='python3 /path/to/garderobe.py 1'
alias tidy_downloads='python3 /path/to/garderobe.py 2'
alias tidy_current='python3 /path/to/garderobe.py 3'
Make sure to replace /path/to/garderobe.py with the actual path to your garderobe.py script.

Save the file and reload your shell configuration:

```bash
source ~/.bashrc
# or
source ~/.zshrc
```

Now, you can use the aliases to quickly run the script:

```bash
tidy_desktop    # To tidy your Desktop
tidy_downloads  # To tidy your Downloads
tidy_current    # To tidy your current directory
```

## Contributing

If you have suggestions for improvements or find any bugs, please open an issue or submit a pull request.

---

Feel free to customize the sections as per your needs. Happy organizing!
