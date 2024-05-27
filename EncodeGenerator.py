import cv2
import face_recognition
import pickle
import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app (cred, { 
    'databaseURL':"https://faceattendancerealtime-8637c-default-rtdb.firebaseio.com/",

    'storageBucket':"faceattendancerealtime-8637c.appspot.com"
})

# encode faces 

# Importing the students images
folderPath='Images'
PathList=os.listdir(folderPath)
print(PathList)
imgList=[]
# extract the id's as well
studentIds=[]
for path in PathList:
    imgList.append(cv2.imread(os.path.join(folderPath,path)))
    studentIds.append(os.path.splitext(path)[0])

    '''print(path)
    # get id's
    print(os.path.splitext(path)[0])'''

    fileName=f'{folderPath}/{path}'
    bucket=storage.bucket()
    blob=bucket.blob(fileName)
    blob.upload_from_filename(fileName)

# print(len(imgList))

print(studentIds)

def findEncodings(imageList):
    encodeList=[]
    for img in imageList:
        # bgr to rgb
        img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode=face_recognition.face_encodings(img)[0]
        encodeList.append(encode)

    return encodeList

print("Encoding Started....")
encodeListKnown=findEncodings(imgList)
encodeListKnownWithIds=[encodeListKnown,studentIds]
# print(encodeListKnown)
print("Encoding Complete")

file=open("EncodeFile.p",'wb')
pickle.dump(encodeListKnownWithIds,file)
file.close()
print("File Saved")


