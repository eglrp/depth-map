from PIL import Image
import os
import glob


def to_jpg(path, target_folder):
    os.makedirs(os.path.join(path, target_folder), exist_ok=True)

    for file_path in glob.glob(os.path.join(path + "*.bmp")):

        _, one_file = os.path.split(file_path)

        target_path = os.path.join(path, target_folder, one_file.split(".")[0] + ".jpg")
        image = Image.open(file_path)
        image.resize((1280, 720), Image.BILINEAR).save(target_path, "JPEG")

if __name__ == '__main__':
    path = '/Users/rohuntripathi/Course_3D_Reconstruction/DfUSMC/Dataset/Notre-Dame-result/'
    target_folder = "processed_jpg"

    to_jpg(path, target_folder)
