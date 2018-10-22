import json
import re
import sys
sys.path.append("..")
from utils.csvUtil.csvUtils import DictToCSV

def wordDictGen(word,x,y,confidence):
	wordDict={
		'word':word,
		'position': {
			'x':x,
			'y':y
		},
		'confidence':confidence
	}
	return wordDict

def responseToJSON(response,imageMetaData,saveOutPut):
	words=[]
	for index,word in enumerate(response['TextDetections']):

		uniqueword=wordDictGen(word['DetectedText'],
		int(word['Geometry']['Polygon'][2]['X']*imageMetaData['width']),
		int(word['Geometry']['Polygon'][2]['Y']*imageMetaData['height']),
		float("{0:.2f}".format(word['Confidence']/100)))

		words.append(uniqueword)

	fullresponseDict={'words':words}

	with open('{}/{}.json'.format(saveOutPut,imageMetaData['imagename']), 'w') as fp:
		json.dump(fullresponseDict, fp)

def responseToCSV(response,saveOutPut,temp):
	words = [word['DetectedText'] for word in response['TextDetections']]
	posibleDate=[word.replace('.',' ').replace('/',' ').replace(',',' ') for word in words if ('199' in word or '20' in word or '/' in word) and not '$' in word]
	
	posibleInvoiceNumber=['{} {}'.format(word,words[index+1]) for index,word in enumerate(words) if ('invoice' in word.lower() or 'invoice #' in word.lower() or 'invoice number' in word.lower()) and '$' not in word.lower() ]
	numberxx = [re.findall(r'\b\d+\b', stringWithNumbers) for stringWithNumbers in posibleInvoiceNumber]
	posibleInvoiceNumber = [number[0] for number in numberxx if len(number)]

	posibleTotalAmount=['{}'.format(word) for index,word in enumerate(words) if 'amount' in word.lower() and ('$' in word or 'E' in word) or '.' in word and ('$' in word or 'E' in word)]

	return DictToCSV(saveOutPut+'invouceResults.csv',{'Date':posibleDate,'Invoice Number':posibleInvoiceNumber,'Total Amount':posibleTotalAmount},',',temp)



	# dateRegex=r''+'(Jan(uary)?|Feb(ruary)?|Mar(ch)?|Apr(il)?|May|Jun(e)?|Jul(y)?|Aug(ust)?|Sep(tember)?|Oct(ober)?|Nov(ember)?|Dec(ember)?)\s+\d{1,2}\s+\d{4}'
	# dateRegex=r''+'^\d\d\d\d/(0?[1-9]|1[0-2])/(0?[1-9]|[12][0-9]|3[01]) (00|[0-9]|1[0-9]|2[0-3]):([0-9]|[0-5][0-9]):([0-9]|[0-5][0-9])$'
	# try:
	# 	x= [re.search(dateRegex,date) for date in posibleDate]
	# 	xdate=[xs.group() for xs in x if not xs==None]
	# except:
	# 	pass
	# print (xdate)

	# print(posibleInvoiceNumber)
	# numberxx = [re.findall(r'\b\d+\b', stringWithNumbers) for stringWithNumbers in posibleInvoiceNumber]
	# numberxx = [number[0] for number in numberxx if len(number)]
	# print(numberxx)

	# print(posibleTotalAmount)
	# numberxx = [re.findall(r'\b\d+\b', stringWithNumbers)[0] for stringWithNumbers in posibleTotalAmount]
	# print(numberxx)