import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://faceattendancerealtime-8637c-default-rtdb.firebaseio.com/"
})

ref=db.reference('Students')

data={
    "1201201":
    {
        "name":"Jeff Bezos",
        "major":"Computer Science",
        "starting_year":2021,
        "total_attendance":6,
        "standing":"G",
        "year":4,
        "last_attendance_time":"2024-05-26 00:54:34"
    },
    "1201202":
    {
        "name":"Elon Musk",
        "major":"Artificial Intelligence",
        "starting_year":2022,
        "total_attendance":12,
        "standing":"E",
        "year":3,
        "last_attendance_time":"2024-05-26 00:54:34"
    },
    "1201203":
    {
        "name":"Narendra Modi",
        "major":"Political Science",
        "starting_year":2023,
        "total_attendance":6,
        "standing":"O",
        "year":2,
        "last_attendance_time":"2024-05-26 00:54:34"
    }
}

for key,value in data.items():
    ref.child(key).set(value)





