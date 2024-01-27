import os
import tkinter as tk
from tkinter import filedialog
import subprocess
from concurrent.futures import ThreadPoolExecutor

def get_file_duration(file_path):
    # Run FFprobe to get the duration of the file
    command = ['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'default=noprint_wrappers=1:nokey=1', file_path]
    result = subprocess.run(command, capture_output=True, text=True)

    # Parse the duration from the FFprobe output and convert to HH:MM:SS
    duration_seconds = float(result.stdout.strip())
    hours = int(duration_seconds // 3600)
    minutes = int((duration_seconds % 3600) // 60)
    seconds = int(duration_seconds % 60)

    duration_str = '{:02}:{:02}:{:02}'.format(hours, minutes, seconds)
    return duration_str

def concatenate_files(file_paths, output_file):
    # Save absolute file paths and durations to selected_files.txt
    with open('selected_files.txt', 'w', encoding='utf-8') as file:
        cumulative_duration_seconds = 0

        for i, file_path in enumerate(file_paths):
            duration = get_file_duration(file_path)

            cumulative_duration_seconds += float(duration.split(":")[0]) * 3600 + float(duration.split(":")[1]) * 60 + float(duration.split(":")[2])

            cumulative_hours = int(cumulative_duration_seconds // 3600)
            cumulative_minutes = int((cumulative_duration_seconds % 3600) // 60)
            cumulative_seconds = int(cumulative_duration_seconds % 60)

            cumulative_duration_str = '{:02}:{:02}:{:02}'.format(cumulative_hours, cumulative_minutes, cumulative_seconds)

            file.write(f'file \'{os.path.abspath(file_path)}\' duration {duration} cumulative_duration {cumulative_duration_str}\n')

    print('Selected file paths and durations (with cumulative durations) have been saved to selected_files.txt')

    # Define the FFmpeg command as a list of arguments
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
'''    
        # Delete the selected_files.txt file
    try:
        os.remove('selected_files.txt')
    except OSError as e:
        print(f"Error deleting selected_files.txt: {e}")
   
    print("Concatenation completed. Output file:", output_file)
'''    
def main():
    # Create a GUI window for file selection
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Prompt the user to select one or more files
    file_paths = filedialog.askopenfilenames(title="Select files", filetypes=[("All Files", "*.*")])

    # Check if the user selected any files or canceled
    if not file_paths:
        print("No files selected. Exiting.")
    else:
        # Specify the output file name
        output_file = f'output{os.path.splitext(file_paths[0])[1]}'

        # Use ThreadPoolExecutor for concurrent processing
        with ThreadPoolExecutor() as executor:
            executor.submit(concatenate_files, file_paths, output_file)

if __name__ == "__main__":
    main()
