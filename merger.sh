#!/bin/bash

cd ~/audio_record/aomehting/mp3 || { echo "❌ Directory not found"; exit 1; }

> filelist.txt  # Clear or create

declare -a files=(recording_*.mp3)
total_seconds=0

for file in "${files[@]}"; do
    if [[ -f "$file" ]]; then
        # Get duration in seconds using ffprobe
        duration=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$file")
        duration=${duration%%.*}  # Truncate to whole seconds

        # Convert to HH:MM:SS
        h=$((duration / 3600))
        m=$(( (duration % 3600) / 60 ))
        s=$((duration % 60))
        duration_str=$(printf "%02d:%02d:%02d" $h $m $s)

        # Previous cumulative time (before adding current)
        cum_h=$((total_seconds / 3600))
        cum_m=$(( (total_seconds % 3600) / 60 ))
        cum_s=$((total_seconds % 60))
        cum_str=$(printf "%02d:%02d:%02d" $cum_h $cum_m $cum_s)

        # Add current file's duration to cumulative
        total_seconds=$((total_seconds + duration))

        # New cumulative (after this file)
        new_cum_h=$((total_seconds / 3600))
        new_cum_m=$(( (total_seconds % 3600) / 60 ))
        new_cum_s=$((total_seconds % 60))
        new_cum_str=$(printf "%02d:%02d:%02d" $new_cum_h $new_cum_m $new_cum_s)

        # Write line with metadata as comment (ffmpeg ignores comments)
        echo "file '$file'" >> filelist.txt
        echo "# duration: $duration_str, starts at $cum_str, ends at $new_cum_str" >> filelist.txt
    fi
done

echo "✅ Created filelist.txt with durations and timeline."

# Run ffmpeg to merge
echo "🎬 Merging files into output.mp3..."
ffmpeg -f concat -safe 0 -i filelist.txt -c copy output.mp3

if [ $? -eq 0 ]; then
    echo "✅ Merge completed: output.mp3"
    echo "📊 Total duration: $(printf "%02d:%02d:%02d" $((total_seconds / 3600)) $(((total_seconds % 3600) / 60)) $((total_seconds % 60)))"
else
    echo "❌ FFmpeg error during merge."
fi
