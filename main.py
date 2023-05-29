import pandas as pd
import os
import re
import tensorflow as tf
from keras import layers
from sklearn.model_selection import train_test_split

IMGheight = 192
IMGWidth = 192

# Extract the irradiance level from the filename
def extract_irradiance(filename):
    pattern = r"_I_(.*?)\.jpg"
    match = re.search(pattern, filename)
    if match:
        return float(match.group(1))
    return None

def extract_loss(filename):
    pattern = r"_L_(.*?)_I_"
    match = re.search(pattern, filename)
    if match:
        return float(match.group(1))
    return None

def extract_time(filename):
    pattern = r"_(\w+)_(\w+)_(\d+)_(\d+)__(\d+)__(\d+)_(\d+)"
    match = re.search(pattern, filename)
    if match:
        day = (match.group(1))
        month = (match.group(2))
        date = int(match.group(3))
        hour = int(match.group(4))
        minute = int(match.group(5))
        second = int(match.group(6))
        return day, month, date, hour, minute, second
    return None

def prepare_dataset():
    # Load the images and extract the irradiance levels
    image_dir = 'Solar_Panel_Soiling_Image_dataset/PanelImages'
    image_filenames = os.listdir(image_dir)
    images = []
    irradiances = []
    times = []
    count = 0
    for filename in image_filenames:
        count += 1
        if count == 100:
            break
        image_path = os.path.join(image_dir, filename)
        # Load the image and convert it to array format
        image = tf.keras.preprocessing.image.load_img(image_path, target_size=(IMGheight, IMGWidth))
        image = tf.keras.preprocessing.image.img_to_array(image)
        images.append(image)
        # Extract the irradiance level from the filename and store it
        irradiance = extract_irradiance(filename)
        loss = extract_loss(filename)
        time = extract_time(filename)
        if irradiance is not None:
            irradiances.append(irradiance)
            times.append(time)

    # Convert the lists to NumPy arrays
    images = tf.stack(images)
    irradiances = tf.constant(irradiances)
    times = tf.constant(times)

    return images, irradiances, times


def main():
    return
    

if __name__ == '__main__':
    main()