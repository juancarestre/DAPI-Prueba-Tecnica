from PIL import Image

def getImageMeta(imageFilePath):
    try:
        imagename=imageFilePath.split('/')[-1].split('.')[0]
    except:
        try:
            imagename=imageFilePath.split('\\')[-1].split('.')[0]
        except:
            imagename=imageFilePath.split('.')[0]

    im = Image.open(imageFilePath)
    width, height = im.size
    return {'imagename':imagename,'width':width,'height':height}