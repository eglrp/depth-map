i=1
for avi in Split_Museum_1_second_segments/*.MTS; do
    name=`echo $avi | cut -f1 -d'.'`
    output_folder="Split_Museum_1_second_segment_all_first_frames/"
    jpg_ext='.jpg'
    echo "$i": extracting the first frame of the video "$avi" into "$output_folder$name$jpg_ext"
    ffmpeg -loglevel panic -i $avi -vframes 1 -f image2 "$output_folder$name$jpg_ext"
    i=$((i+1))
 done