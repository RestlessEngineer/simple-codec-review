#!/usr/bin/env python3

import numpy as np
import cv2 

def get_video_metric(video_file_name: str, out_video_file: str, width: int, height: int) -> tuple[list[int], list[int]]:
    """get statistic from video file and save video with fragments. This function return count of contours and summarised radius.

    Args:
        video_file_name (str): name video file 
        out_video_file (str): output video file
        width (int): frame width 
        height (int): frame height

    Returns:
        tuple:  array of contours and radius count
    """

    cnt_contours = [] 
    cnt_radius = []
    
    out_file = None
    if(out_video_file):
        out_file = cv2.VideoWriter(out_video_file, cv2.VideoWriter_fourcc(*'DIVX'), 6, (width, height))
    
    cap = cv2.VideoCapture(video_file_name)
    if not cap.isOpened():
        print("Error: Could not open video file.")
        exit()

    print("get_video_state: read data from " + video_file_name)
    
    while True:
        ret, frame_enc = cap.read()
        
        # Check if we have reached the end of the video
        if not ret:
            break

        gray_real = cv2.cvtColor(frame_enc, cv2.COLOR_RGB2GRAY)
        bin_real = cv2.threshold(gray_real, 130, 255, cv2.THRESH_BINARY)[1]
        contours, _ = cv2.findContours(bin_real, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        cnt_contours.append(len(contours))

        contours_zero = np.zeros(frame_enc.shape)
        sum_radius = 0
        for contour in contours:
            ((x, y), radius) = cv2.minEnclosingCircle(contour)
            sum_radius = sum_radius + radius

            if(out_video_file):
                cv2.drawContours(contours_zero, contours, -1, (0,0,255), 1)
                cv2.circle(contours_zero, (int(x),int(y)), int(radius), (0,255,0), 2)
        
        cnt_radius.append(sum_radius)
        
        if(out_video_file):
            out_file.write(contours_zero.astype('uint8'))

    return cnt_contours, cnt_radius


import argparse

parser = argparse.ArgumentParser(description="Example script with command-line arguments")
parser.add_argument("--video_file", type=str, help="video file path")
parser.add_argument("--output_file", type=str, default=None, help="output video file path")
parser.add_argument("--data_file", type=str, default=None, help="file to save countours count and summarised radiuses")

args = parser.parse_args()

video_path = args.video_file 
output_video_file = args.output_file 
data_output = args.data_file 

counters, raduises = get_video_metric(video_path, output_video_file, 1920, 1080)

if(data_output):
    with open(data_output, "w") as f:
        f.write(' '.join(map(str,counters)))
        f.write("\n")
        f.write(' '.join(map(str,raduises)))

