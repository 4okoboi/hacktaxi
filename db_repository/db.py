import pyrebase

firebaseConfig = {'apiKey': "AIzaSyCWSPbFxEGKCnQNjMY_8HhgbjmqDTluQ0o",
                  'authDomain': "hack-8645c.firebaseapp.com",
                  'databaseURL': "https://hack-8645c-default-rtdb.asia-southeast1.firebasedatabase.app",
                  'projectId': "hack-8645c",
                  'storageBucket': "hack-8645c.appspot.com",
                  'messagingSenderId': "463099006706",
                  'appId': "1:463099006706:web:36c5ad0612c2976adaca6b"}

firebase = pyrebase.initialize_app(firebaseConfig)

database = firebase.database()
db_auth = firebase.auth()
# storage = firebase.storage()
# for i in database.child('Users').child('WAHG1aibNpWfXMyCztAjPVbO7qn2').get().each():
#     print(i.val())

