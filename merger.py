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
    # Check if all selected files have the same extension
    extensions = {os.path.splitext(file_path)[1] for file_path in file_paths}
    if len(extensions) > 1:
        print("Warning: Selected files have different extensions. Please choose files with the same extension for concatenation.")
    else:
        # Save absolute file paths to selected_files.txt
        with open('selected_files.txt', 'w' , encoding='utf-8') as file:
            for file_path in file_paths:
                file.write(f'file \'{os.path.abspath(file_path)}\'\n')

        print('Selected file paths have been saved to selected_files.txt')

        # Extract the file extension from the first file in the list
        _, file_extension = os.path.splitext(file_paths[0])

        # Define the FFmpeg command as a list of arguments
        output_file = f'output{file_extension}'
        ffmpeg_command = [
            'ffmpeg',
            '-f', 'concat',
            '-safe', '0',
            '-i', 'selected_files.txt',
            '-c', 'copy',
            output_file
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

print("Concatenation completed. Output file:", output_file)
