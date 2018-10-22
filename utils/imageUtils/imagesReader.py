def imageToByteImage(imageFilePath):
    with open(imageFilePath, 'rb') as image_file:
        image = image_file.read()
    return image