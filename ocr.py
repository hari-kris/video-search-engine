from PIL import Image
import pytesseract
import os
import string


def pre_processing(text):
    """
    Perform various pre processing on the input text
    :param text:
    :return:
    """
    text = remove_punctuations(text)
    text = removing_numbers(text)
    text = remove_special_characters(text)
    text = remove_empty_lines(text)
    return text


# function to remove the punctuation in given text
def remove_punctuations(text):
    """
    Remove punctuation present in the text
    :param text: input text
    :return: cleaned text
    """
    for punctuation in string.punctuation:
        text = str(text)
        text = text.replace(punctuation, '')
    return text


def removing_numbers(text):
    """
    Removing number in the text
    :param text: input text
    :return: cleaned text
    """
    return text.replace('\d+', '')


def remove_special_characters(text):
    """
    Removing special character in the text
    :param text: input text
    :return: cleaned text
    """
    return text.replace('[^A-Za-z0-9]+', ' ')


def remove_empty_lines(text):
    """
    Removing empty line in the text
    :param text: input text
    :return: cleaned text
    """
    lines = text.split("\n")
    non_empty_lines = [line for line in lines if line.strip() != ""]

    string_without_empty_lines = ""
    for line in non_empty_lines:
          string_without_empty_lines += line + "\n"
    return string_without_empty_lines


def store_file(output_path, file_name, content):
    """
    Store the text file for laster processing
    :param output_path: output path where the file to be stored
    :param file_name: file name to created
    :param content: cleaned file content
    :return: None
    """
    file_obj = open(output_path+file_name,'w')
    file_obj.write(content)
    file_obj.close()


if __name__ == '__main__':
    input_path = "/data/BITS/SEM-3/ASSIGNMENT-2/FRAMES/"
    frames = os.listdir(input_path)
    output_path = "/data/BITS/SEM-3/ASSIGNMENT-2/TEXT/"
    for frame in frames:
        output = pytesseract.image_to_string(Image.open(input_path + frame))
        output = pre_processing(output)
        if output.strip() != "":
            store_file(output_path, frame.replace(".jpg", ".txt"), output)