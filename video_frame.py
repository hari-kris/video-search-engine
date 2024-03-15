import cv2
import pandas as pd
import numpy as np
import os


# Function to extract frames
def video_to_frames(filename, path):
    # Path to video file
    vidObj = cv2.VideoCapture(path)

    # Used as counter variable
    count = 0

    # checks whether frames were extracted
    success = 1

    while success:

        # vidObj object calls read
        # function extract frames
        success, image = vidObj.read()
        if count % 60 == 0:
            # Saves the frames with frame-count
            cv2.imwrite("FRAMES/%s_Frame_%d.jpg" % (filename, count), image)

        count += 1


if __name__ == '__main__':
    input_path = "/data/BITS/SEM-3/ASSIGNMENT-2/VIDEO/"
    files = os.listdir(input_path)
    # Calling the function
    for file_name in files:
        video_to_frames(file_name, input_path + file_name)