import os, io
from google.cloud import vision
from google.cloud.vision import types

def find_brand_from_image():
    FILE_NAME="new_image.jpg"
    os.environ['GOOGLE_APPLICATION_CREDENTIALS']=r'ServiceAccountToken.json'
    client=vision.ImageAnnotatorClient()
    #print(client)
    #FILE_NAME='adidas1.jpg'
    request = {
        'source': {'image_uri': 'https://firebasestorage.googleapis.com/v0/b/uoft-hacks-51954.appspot.com/o/adidas-Trefoil-White-%26-Black-T-Shirt-_289236-front-US.jpg?alt=media&token=cb61c33e-78d9-481c-85f5-f0e0e8a19975&fbclid=IwAR1qnWbElK5Rsu2whKmpv1dys14ELhuu5BQzDNErC3FscvfK7d8iBZ8-xjA'},
    }
    
    logos_on_image=client.logo_detection(request)
    text_on_image=client.text_detection(request)
    web_on_image=client.web_detection(request)
    
    print(logos_on_image,text_on_image,web_on_image)
    texts=logos_on_image.logo_annotations
    texts2=text_on_image.text_annotations

    wordDict={}
    # print(dir(client))
    for text in texts:
        print(text.description,text.score)
        if(str(text.description.upper()) in wordDict):
            wordDict[str(text.description.upper())]=max(float(wordDict[text.description.upper()]),text.score)
        else:
            wordDict[str(text.description.upper())]=text.score



    for text in texts2:
        print(text.description,text.score)
        if(str(text.description.upper()) in wordDict):
            wordDict[str(text.description.upper())]=max(float(wordDict[text.description.upper()]),text.score)
        else:
            wordDict[str(text.description.upper())]=text.score

    print("word dict",wordDict)
    try:
        brand=max(wordDict,key=wordDict.get)
    except:
        print('error')
        return "error"
    print(brand)
    return brand

    #search logos, web for adidas

if __name__=="__main__":
    brand=find_brand_from_image()
