import os
import shutil
LABELS_LOCATION = '/path/to/parts_lfw_funneled_gt_images'
INPUT_LOCATION = '/path/to/lfw_funneled'

def main():
    # Perform some tidy up on the LFW parts labelled dataset
    # to make it easier to read in when training model
    CreateLabelDirectories(LABELS_LOCATION)
    RemoveUnlabelled(INPUT_LOCATION,LABELS_LOCATION)

def CreateLabelDirectories(labelDirectoryLocation):
    # Create a directory for each person and place all the mask labels for
    # that person in their directory
    filenames = os.listdir(labelDirectoryLocation)
    for filename in filenames:
        if '._' not in filename and os.path.isfile(os.path.join(labelDirectoryLocation, filename)):
            if os.path.isdir(os.path.join(labelDirectoryLocation, filename[:-9])):
                os.rename(labelDirectoryLocation + '/'+ filename, os.path.join(labelDirectoryLocation + '/' + filename[:-9] , filename))
            else:
                os.mkdir(os.path.join(labelDirectoryLocation, filename[:-9]))
                os.rename(labelDirectoryLocation + '/'+ filename, os.path.join(labelDirectoryLocation + '/' + filename[:-9] , filename))


def RemoveUnlabelled(inputDirectoryLocation,labelDirectoryLocation):
    # Remove the examples from the lfw dataset that don't
    # have masks for image segmentation labelling
    labelDirectory = os.listdir(labelDirectoryLocation)
    allDirectory = os.listdir(inputDirectoryLocation)
    nonLabelledImages = set(allDirectory) - set(labelDirectory)
    for image in nonLabelledImages:
        if os.path.isdir(inputDirectoryLocation + '/' + image):
            print('removing {} directory'.format(image))
            shutil.rmtree(inputDirectoryLocation + '/' + image)


if __name__ == "__main__":
    main()
