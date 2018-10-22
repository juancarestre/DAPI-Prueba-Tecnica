import csv

def CSVToDict(filePath,delimiter):
    with open(filePath, 'r') as csvfile:
        resultDict={}
        spamreader = csv.reader(csvfile, delimiter=delimiter, quotechar='|')
        for index,row in enumerate(spamreader):
            if index>0:
                for keyIndex,key in enumerate(list(resultDict.keys())):
                    resultDict[key].append(row[keyIndex])            
            else:
                for element in row:
                    resultDict[element]=[]
        return resultDict
        
def DictToCSV(fileName,Dict,delimiter,temp):
    
    with open(fileName,'w',newline='') as f:
        w = csv.writer(f)
        w.writerow(Dict.keys())
        valuesList=list(Dict.values())
        valuesToAdd=[]
        valueToAdd=[]

        for value in valuesList:
            valuesToAdd.append([])

        for index,value in enumerate(valuesList):
            for valuein in enumerate(value):
                valuesToAdd[index].append(valuein[1])
        
        temp.append(valuesToAdd)
        for values in temp:
            values = [str(value).replace('[','').replace(']','').replace("'","").replace(',',' ') for value in [valuesx for valuesx in values]]
            w.writerow(values)
        
    return temp


