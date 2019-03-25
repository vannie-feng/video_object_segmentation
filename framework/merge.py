#!/usr/bin/python2.7

from sys import exit
import cv2
import glob
import os


# DIR_NAME = 'Full-Resolution/cat-girl'; SIZE = (4096, 2160)
# DIR_NAME = 'Full-Resolution/car-shadow'; SIZE = (1920, 1080)
#DIR_NAME = 'Full-Resolution/giant-slalom'; SIZE = (3840, 2160)
DIR_NAME='Fusion/car-shadow';SIZE=(3840,2160)

def imgs2video(imgs_dir, save_name):

    fps = 24
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video_writer = cv2.VideoWriter(save_name, fourcc, fps, SIZE)
    # no glob, need number-index increasing
    imgs = glob.glob(os.path.join(imgs_dir, '*.png'))

    for i in range(len(imgs)):

        imgname = os.path.join(imgs_dir, '{:05d}.png'.format(i))
        print imgname
        frame = cv2.imread(imgname)
        video_writer.write(frame)

    video_writer.release()


if __name__ == '__main__':

    imgs2video(DIR_NAME, 'a.mp4')


    exit(0)
