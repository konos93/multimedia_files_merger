# mp3_merger
merge multiple mp3 using python and ffmpeg

Why i build that ?
because for an audio book with 20 parts of 20 mb with 1 hour each one audacity to load , merge and export needs 40 min for my old laptop with this stuff here needs 1 min 
ffmpeg is cool

How to Use

   Upon running the script, a GUI window will appear for file selection.
    Select one or more audio files that you want to concatenate. You can select files of any format.
    Click the "Open" button to confirm your selection.
    The script will concatenate the selected audio files into a single MP3 file named output.mp3.
    Once the concatenation is completed, the script will display a message indicating that the process is finished.
    The selected_files.txt file, which was temporarily created to list the selected files for FFmpeg, will be deleted automatically.

Notes
    If you encounter any issues, ensure that FFmpeg is correctly installed and available in your system's PATH. or have in the same folder with the merger.py ffmpeg for windows
    use bulkrename utility or any similar program to keep the names of the files in a pecific potition for the copined file
