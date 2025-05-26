import logging
import argparse

from base import RespiratoryMonitor


if __name__ == "__main__":
    logging.basicConfig(format="%(asctime)s :: %(message)s", level=logging.INFO)
    
    parser = argparse.ArgumentParser()
    parset.add_argument('-d', '--data_path', type=ascii, default='.')
    
    args = parser.parse_args()
    
    data_path = args.data_path # path to the folder with video content

    rm = RespiratoryMonitor(capture_target=data_path+"small_cat.mp4", save_calibration_image=True, motion_extraction_method="flow")