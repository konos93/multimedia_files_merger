import os
import tkinter as tk
from tkinter import filedialog
import subprocess

# Create a GUI window for file selection
root = tk.Tk()
root.withdraw()  # Hide the main window

# Prompt the user to select one or more files
file_paths = filedialog.askopenfilenames(title="Select files", filetypes=[("All Files", "*.*")])

# Check if the user selected any files or canceled
if not file_paths:
    print("No files selected. Exiting.")
else:
    # Save absolute file paths to selected_files.txt
    with open('selected_files.txt', 'w') as file:
        for file_path in file_paths:
            file.write(f'file \'{os.path.abspath(file_path)}\'\n')

    print('Selected file paths have been saved to selected_files.txt')

    # Define the FFmpeg command as a list of arguments
    ffmpeg_command = [
        'ffmpeg',
        '-f', 'concat',
        '-safe', '0',
        '-i', 'selected_files.txt',
        '-c', 'copy',
        'output.mp3'
    ]

    # Check if the file exists before running the FFmpeg command
    if not os.path.exists('selected_files.txt'):
        print("Error: selected_files.txt does not exist.")
    else:
        # Execute the FFmpeg command
        subprocess.run(ffmpeg_command)

 
 # Delete the selected_files.txt file
    try:
        os.remove('selected_files.txt')
       # print("selected_files.txt deleted.")
    except OSError as e:
        print(f"Error deleting selected_files.txt: {e}")

print("Concatenation completed.")
