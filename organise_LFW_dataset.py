import os
import shutil
FOLDER= "/the/folder/location/of/downloadedfiles/"
LABELS_LOCATION = FOLDER +'/parts_lfw_funneled_gt_images/'
INPUT_LOCATION =  FOLDER +'/lfw_funneled/'


# Files needed from the LFW parts labelled page(http://vis-www.cs.umass.edu/lfw/part_labels/)
# ground truth images which unzips to parts_lfw_funneled_gt_images (http://vis-www.cs.umass.edu/lfw/lfw-funneled.tgz)
# funneled images which unzips to lfw_funneled (http://vis-www.cs.umass.edu/lfw/part_labels/parts_lfw_funneled_gt_images.tgz)
# test/train/validation txt files(http://vis-www.cs.umass.edu/lfw/part_labels/parts_test.txt,
# http://vis-www.cs.umass.edu/lfw/part_labels/parts_train.txt, http://vis-www.cs.umass.edu/lfw/part_labels/parts_validation.txt)
# NOTE: rename the .txt files before running so that its just test.txt for example
def main():
    # Organise the input images and their masks into test train
    # and validation folders
    CreateDirectories(INPUT_LOCATION,LABELS_LOCATION)


def getTestTrainSplits():
    # Returns a dictionary of each example name as the key and the value
    # being whether that example is in the test, training or
    # validation set (As per LFW example splits)
    splits= {}
    for split in ["train", "validation", "test"]:
        file = open(FOLDER + split + ".txt")
        lines = file.readlines()
        for line in lines:
            # Format the line to conform with naming conventions
            line = line.split()
            if len(line[1])<4:
                # Adding 0's to the front of image numbers so that
                # all images have the same numbering format
                line[1] = ("0"*(4-len(line[1]))) + line[1]
            line = '_'.join(line)
            splits[line] = split

    return splits


def CreateDirectories(inputDirectoryLocation, labelDirectoryLocation):
    # Create images/(test,train,validation) and masks/(test,train,validation)
    # folders and populate them
    for i in ["images","masks"]:
        os.mkdir(os.path.join(FOLDER, i))
        for k in ["test","train","validation"]:
            os.mkdir(os.path.join(FOLDER, i, k))

    splits =  getTestTrainSplits()
    for example in splits:

        if os.path.isfile(os.path.join(inputDirectoryLocation, example[:-5], example + ".jpg")) and os.path.isfile(os.path.join(labelDirectoryLocation,  example + ".ppm")):
            shutil.copy(os.path.join(inputDirectoryLocation, example[:-5], example + ".jpg"),os.path.join(FOLDER ,"images",splits[example]))
            shutil.copy(os.path.join(labelDirectoryLocation,  example + ".ppm"),os.path.join(FOLDER, "masks",splits[example]))



if __name__ == "__main__":
    main()
