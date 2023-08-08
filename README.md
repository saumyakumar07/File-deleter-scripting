# File Deleter Project

The **File Deleter** project is a Python script that allows you to automatically delete specific files of your choice, such as `.psd` files, from a designated drive. This can be useful for cleaning up clutter or removing unwanted files in a specific location without having to manually search and delete them.

Please note that this project involves deleting files permanently, so use it with caution and make sure to double-check the files you intend to delete.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
- [Usage](#usage)
- [Configuration](#configuration)
- [License](#license)

## Getting Started

### Prerequisites

To use this project, you'll need:

- Python 3.x installed on your system.

 ### Usage
 Open the file_deleter.py script in a text editor or IDE of your choice.

Modify the DRIVE_PATH variable to specify the drive path where you want to delete files. For example:
DRIVE_PATH = 'C:/Users/YourUsername/Documents'
TARGET_EXTENSIONS = ['.psd', '.txt']
python file_deleter.py

### Configuration

You can further customize the script behavior by modifying the following variables in file_deleter.py:

DRIVE_PATH: The path of the drive where files will be deleted from.
TARGET_EXTENSIONS: List of file extensions to be targeted for deletion.
CONFIRM_DELETION: If True, the script will prompt for confirmation before deleting each file.

### License

This project is licensed under the MIT License, which means you're free to modify and distribute the code as long as you include the original license in your distribution. However, please note that this project comes with no warranties or guarantees. Use it at your own risk




   
