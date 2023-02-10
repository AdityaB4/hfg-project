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
    result = filter(lambda x: x['focus'] == focus and x['location'] == location)
    return result

def add_volunteer(tele_id, name, age, location, focus):
    doc_ref = db.collection(u'volunteers').document(u'tele_id')
    doc_ref.set({
        u'name': name,
        u'tele_id': tele_id,
        u'age': age,
        u'location': location,
        u'focus':focus
    })

 
def add_user(tele_id, name, age, location, focus):
    doc_ref = db.collection(u'users').document(u'tele_id')
    doc_ref.set({
        u'name': name,
        u'tele_id': tele_id,
        u'age': age,
        u'location': location,
        u'focus':focus
    })
   
 
def update_user(tele_id, name= None, age= None, location= None, focus= None):
    doc_ref = db.collection(u'users').document(u'tele_id')
    doc = doc_ref.get().to_dict()
    doc_ref.set({
        u'name': name or doc['name'],
        u'tele_id': tele_id,
        u'age': age or doc['age'],
        u'location': location or doc['location'],
        u'focus':focus or doc['focus']
    }, merge=True)
   
 
def update_volunteer(tele_id, name= None, age= None, location= None, focus= None):
    doc_ref = db.collection(u'volunteeers').document(u'tele_id')
    doc = doc_ref.get().to_dict()
    doc_ref.set({
        u'name': name or doc['name'],
        u'tele_id': tele_id,
        u'age': age or doc['age'],
        u'location': location or doc['location'],
        u'focus':focus or doc['focus']
    }, merge=True)
   
