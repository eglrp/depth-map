import glob
import numpy as np
import pandas as pd
import os

source_directory = "/Users/rohuntripathi/Course_3D_Reconstruction/datasets/" \
                   "Split_Museum_1_second_segments_DfUSMC_result_longer_convergence/"

files = glob.glob(os.path.join(source_directory, "*.log"))
files = sorted(files)

columns = ["inlier", "convergence", "focal length", "k1", "k2", "confidence threshold", "circles?"]
extracted = np.zeros((len(files), len(columns)))


for index, one_file in enumerate(files):
    print(one_file)

    lines = open(one_file).readlines()
    if len(lines) == 1:
        lines = lines[0].split("\\n")

    for line in lines:
        if "num inlier: " in line:
            extracted[index, 0] = float(line.lstrip("num inlier: ").split("/")[0])

        if "Ceres Solver Report" in line:
            if "NO_CONVERGENCE" in line:
                extracted[index, 1] = 0
            elif "CONVERGENCE" in line:
                extracted[index, 1] = 1
            else:
                raise Exception("Did not fine convergence in report - " + line)

        if "focal length: " in line:
            extracted[index, 2] = float(line.lstrip("focal length: ").rstrip("\n"))

        if "radial distortion: " in line:
            extracted[index, 3] = float(line.lstrip("radial distortion: ").split()[0].rstrip("\n"))
            extracted[index, 4] = float(line.lstrip("radial distortion: ").split()[1].rstrip("\n"))

        # confidence threshold: 0.989317
        if "confidence threshold: " in line:
            extracted[index, 5] = float(line.lstrip("confidence threshold: ").split()[0].rstrip("\n"))


pd.DataFrame(extracted, columns=columns).to_csv('museum_camera_instrinsics.csv')