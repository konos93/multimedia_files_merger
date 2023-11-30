# multimedia_files_merger
merge multiple multimedia_files using python and ffmpeg , the multimedia_files should be the same file

Why i build that ?
because for an audio book or video with 20 parts of 20 mb with 1 hour each one audacity to load , merge and export needs 40 min for my old laptop with this stuff here needs 1 min 
ffmpeg is cool


How to Use

2 options 
1 install python and all the depedencies this script needs 
2 have on the same folder ffmpeg.exe and merger.exe .u cannot have ffmpeg.exe on the same folder if u install it in your system here are some instructions https://www.youtube.com/watch?v=r1AtmY-RMyQ
merger exe is merger.py with [pyinstaller  
](https://pypi.org/project/auto-py-to-exe/)
 Upon running the script, a GUI window will appear for file selection.
    Select one or more audio files that you want to concatenate. You can select files of any format.
    Click the "Open" button to confirm your selection.
    The script will concatenate the selected audio files into a single MP3 file named output.mp3.
    Once the concatenation is completed, the script will display a message indicating that the process is finished.
    The selected_files.txt file, which was temporarily created to list the selected files for FFmpeg, will be deleted automatically.

Notes

   If you encounter any issues, ensure that FFmpeg is correctly installed and available in your system's PATH. or have in the same folder with the merger.py ffmpeg for windows
    use bulkrename utility or any similar program to keep the names of the files in a specific position for the combined file

   use only english characters  in pathfiles due to ffpeg cant read others. like 
C:\Users\konos93\Downloads\Music\newfolder

