import os
import moviepy.editor as mp


def extract_audio_file(file_path, output_path):
    my_clip = mp.VideoFileClip(file_path)
    my_clip.audio.write_audiofile(output_path+".mp3")


if __name__ == '__main__':
    input_path = "/data/BITS/SEM-3/ASSIGNMENT-2/VIDEO/"
    output_path = "/data/BITS/SEM-3/ASSIGNMENT-2/AUDIO/"
    files = os.listdir(input_path)
    # Calling the function
    for file_name in files:
        extract_audio_file(input_path + file_name, output_path + file_name.replace(".mp4",""))