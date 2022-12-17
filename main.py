import cv2
import numpy as np
import os
import argparse
from loguru import logger

def parse_args():
    '''Parse input arguments'''
    parser = argparse.ArgumentParser(
        description="Crop image generator")

    parser.add_argument("--input",
                        default='input/image',
                        help="Location of input directory to be cropped.")

    parser.add_argument("--output",
                        default='output',
                        help="Location of output directory to save cropped images.")

    parser.add_argument("-t", "--type",
                        default='classes',
                        type=str,
                        help="Types of the cropped image.")

    args = parser.parse_args()
    return args


def main():
    args = parse_args()        

    dir = args.input
    out_dir = args.output
    logger.info('Input is located in '+ dir)

    objs = [i for i in args.type.split(',')]
    print(objs)

    logger.info(f'This program is to generate {args.type} images.')
            
    for obj in objs:
        os.makedirs(os.path.join(out_dir, obj))
        logger.info(f'new directory of {obj} is generated.')

    logger.info('Cropped images will be saved under '+out_dir)

    # global image, oriImage

    for file in os.listdir(dir):

        cv2.namedWindow("image",  cv2.WINDOW_NORMAL)

        fullpath = os.path.join(dir, file)

        logger.info(f"{file} is being checked.")

        image = cv2.imread(fullpath)
        oriImage = image.copy()

        key = cv2.waitKey(1) & 0xFF
        while True:
            i = image.copy()
            cv2.imshow("image", i)

            key = cv2.waitKey(1) & 0xFF
            if key == ord('a'): # Quit croping in the current image

                loc2Save = os.path.join(out_dir, objs[0], os.path.basename(file))
                cv2.imwrite(loc2Save, oriImage)
                logger.info(f'This is {objs[0]}. Saved it.')
                break

            if key == ord('s'): # Quit croping in the current image

                loc2Save = os.path.join(out_dir, objs[1], os.path.basename(file))
                cv2.imwrite(loc2Save, oriImage)
                logger.info(f'This is {objs[1]}. Saved it.')
                break

            if key == ord('q'):
                logger.info(f'Not relevant. Do not save it.')
                break

    # close all open windows
    cv2.destroyAllWindows()

if __name__ == "__main__":

    main()
