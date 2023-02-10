import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("./hfg-project-fe558-firebase-adminsdk-6m0wo-b22b5aa40a.json")
firebase_admin.initialize_app(cred)
db = firestore.client() # connecting to firestore

def get_volunteers():
    users_ref = db.collection(u'volunteers')
    docs = users_ref.stream()
    result = []
    for doc in docs:
        result.append(doc.to_dict())
    return result

def match_volunteers(volunteers, location, focus):
    result = volunteers # not deep copy
    result = filter(lambda x: x['focus'] == focus && x['location'] == location)
    return result
