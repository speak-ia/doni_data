import pyrebase
# import firebase_admin
# from firebase_admin import credentials, firestore

config = {
        "apiKey": "AIzaSyDaA4vxzVEhDoPMkPk_GgyaeoJivXXEbgs",
        "authDomain": "project-data-3518e.firebaseapp.com",
        "projectId": "project-data-3518e",
        "storageBucket": "project-data-3518e.appspot.com",
        "messagingSenderId": "1017548587806",
        "appId": "1:1017548587806:web:e79417855a39fe547fff0f",
        "databaseURL": ""
    }

firebase = pyrebase.initialize_app(config)

auth = firebase.auth()
# # Initialize the Firebase app with credentials
# cred = credentials.Certificate("C:/Users/Phoenix/PycharmProjects/donidata/service/project-data-3518e-firebase-adminsdk-o70gi-89b6484885.json")
# firebase_admin.initialize_app(cred)
#
# # Create a Firestore client
# db = firestore.client()