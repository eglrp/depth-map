import subprocess, os

import datetime

from tqdm import tqdm

print(subprocess.check_output(['cmake','.']))
print(subprocess.check_output(['make']))

timestamp = str(datetime.datetime.now()).replace(" ", "_")

# Get the video input
video_source = '/Users/rohuntripathi/Course_3D_Reconstruction/datasets/Split_Museum_1_second_segments'
videos_to_process = sorted(os.listdir(video_source))[:30]

video_result = '/Users/rohuntripathi/Course_3D_Reconstruction/datasets/Split_Museum_1_second_segments_DfUSMC_result'

# Usage: DfUSMC <data_name> <video_extension> <video_path> <result_path>
executable_path = '/Users/rohuntripathi/Course_3D_Reconstruction/DfUSMC/DfUSMC'
for one_video in tqdm(videos_to_process):
	name, ext = one_video.split(".")
	print("executing", "_".join([executable_path, name, ext, video_source, video_result]))
	returned_object = subprocess.check_output([executable_path, name, ext, video_source, video_result])
	open(os.path.join(video_result, name + "_" + timestamp + ".log"), "w").write(str(returned_object))

