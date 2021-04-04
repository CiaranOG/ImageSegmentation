import os
import shutil
import cv2
import tensorflow as tf
from keras.preprocessing.image import save_img
import numpy as np
FOLDER= "/home/ciaran/Workspace/faceRecognition/ImageSegmentation/masks1"


def main():
    # Organise the input images and their masks into test train
    # and validation folders
    convert_masks()


def convert_masks():

    for directory in ["train", "validation", "test"]:
        for file in os.listdir(FOLDER + "/" + directory):
            newName = file[:-4] + ".png"
            mask = cv2.imread(os.path.join(FOLDER,directory,file))
            mask = maskToPixelLabels(mask)
            print("mask:",mask.shape)
            #mask = tf.keras.preprocessing.image.array_to_img(mask)
            os.remove(os.path.join(FOLDER,directory,file))
            cv2.imwrite(os.path.join(FOLDER,directory,newName), mask)





def maskToPixelLabels(imageMask):
    matrix = []
    for row in imageMask:
        matrixRow = []
        for pixel in range(len(row)):
            new  = [k for k, element in enumerate(row[pixel]) if element!=0]
            matrixRow += [new]
        matrix +=[matrixRow]
    matrix = np.array(matrix)
    return matrix



if __name__ == "__main__":
    main()
