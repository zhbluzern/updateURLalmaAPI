import json
import urllib.request
from lxml import etree
import re
import pandas as pd

#Namespaces
ns = {'xmlns' : 'http://www.loc.gov/zing/srw/', 
  'mets' : 'http://www.loc.gov/METS/', 'xlink': 'http://www.w3.org/1999/xlink'}  

filename = "SoSaGraphics_ARK_MMSIDs_20230310.json"
# Opening JSON file and return JSON object as a dictionary
f = open(filename)
id_url_list = json.load(f)

resultSet = []
for id in id_url_list:
    #METS-Datei von ZentralGut einlesen
    zentralGutUrl = f"https://zentralgut.ch/sourcefile?id={id['mmsID']}"
    resultDet = {}
    #Initial Request        
    root = etree.parse(urllib.request.urlopen(zentralGutUrl))
    #Initial xpath to parse the DEFAULT-FileGroup
    fileUrl = root.xpath(".//mets:fileGrp[@USE='DEFAULT']/mets:file/mets:FLocat/@xlink:href",namespaces=ns)
    
    #Wenn vorhanden, dann Thumbnail-Pfad umschreiben auf 150px Breite
    try:
      fileUrl = re.sub("\/800\/0\/", "/150/0/", fileUrl[0])
      print(fileUrl)
    except IndexError:
       fileUrl = "error"
       print(f"error on: {id['mmsID']}")

    #ResultDict schreiben
    resultDet["mmsId"] = str(id['mmsID']) #stringify mmsId da als integer im Json vorliegt.
    resultDet["001"] = id['networkID']
    resultDet["thumbnailUrl"] = fileUrl
    resultSet.append(resultDet)
    #break

#Export ResultSet to XLS
df = pd.DataFrame(resultSet)
df.to_excel('SoSaGraphiken_NZID_ThumbnailURL.xlsx')