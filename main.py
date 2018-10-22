from amazonRekConector.amazonRek import RekognitionAWSClient
from utils.csvUtil import csvUtils
from utils.filePathsUtil import filesInFolder
from utils.imageUtils.imagesReader import imageToByteImage
from utils.imageUtils.imageMeta import getImageMeta

from textWragglers.responseWraggler import responseToJSON
from textWragglers.responseWraggler import responseToCSV

def main(imageFolder):
        temp=[]
        imagesFilePaths=filesInFolder(imageFolder).getPaths()
        byteImages=[imageToByteImage(image) for image in imagesFilePaths]
        imagesMeta=[getImageMeta(image) for image in imagesFilePaths]

        accessKeys=csvUtils.CSVToDict('resources/accessKeysCreds/accessKeys.csv',',')
        rekognition=RekognitionAWSClient(accessKeys['Access key ID'][0],accessKeys['Secret access key'][0],accessKeys['Region'][0])
        
        for index in range(len(imagesMeta)): 
            response=rekognition.detect_text(byteImages[index])
            responseToJSON(response,imagesMeta[index],'results/')
            temp=responseToCSV(response,'results/',temp)


if __name__=="__main__":
    main()
