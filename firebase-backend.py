import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("./hfg-project-fe558-firebase-adminsdk-6m0wo-b22b5aa40a.json")
firebase_admin.initialize_app(cred)


