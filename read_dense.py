import numpy as np
import pylab as plt
import os


def read_array(path):
    with open(path, "rb") as fid:
        width, height, channels = np.genfromtxt(fid, delimiter="&", max_rows=1,
                                                usecols=(0, 1, 2), dtype=int)
        fid.seek(0)
        num_delimiter = 0
        byte = fid.read(1)
        while True:
            if byte == b"&":
                num_delimiter += 1
                if num_delimiter >= 3:
                    break
            byte = fid.read(1)
        array = np.fromfile(fid, np.float32)
    array = array.reshape((width, height, channels), order="F")
    return np.transpose(array, (1, 0, 2)).squeeze()


def main():

    depth_map_dir = '/Users/rohuntripathi/Course_3D_Reconstruction/datasets/Split_Panther_3_second_segment_periodic_first_30_frames/depth_map_bin_for_key_frames'
    required_output_dir = '/Users/rohuntripathi/Course_3D_Reconstruction/datasets/Split_Panther_3_second_segment_periodic_first_30_frames/depth_map_graymap'

    for one_file in os.listdir(depth_map_dir):

        depth_map = read_array(os.path.join(depth_map_dir, one_file))    
        name = one_file.split(".")[0]
        min_depth, max_depth = np.percentile(depth_map, [5, 95])
        depth_map[depth_map < min_depth] = min_depth
        depth_map[depth_map > max_depth] = max_depth
        
        plt.imsave(os.path.join(required_output_dir, name + '.png'), depth_map, format="png", cmap='gray_r')

        # plt.imshow(depth_map, cmap='gray_r')
        # plt.axis('off')
        # plt.savefig(os.path.join(required_output_dir, name + '.png'), bbox_inches='tight', dpi=800)


if __name__ == "__main__":
    main()
