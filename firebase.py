from firebase.firebase import FirebaseApplication

import time

url = "https://ht-lifestyle.firebaseio.com/Food-Store.json"

name = "Food Club"
latitude = 1.332947
longitude = 103.7074744
Address = "Ngee Ann Polytechnic, 535 Clementi Rd, Singapore 599489"

firebase = FirebaseApplication(url, None)
result = firebase.patch("/Food-Store/Food Club/",{"name":name,"latitude":latitude,"longitude":longitude, "address":Address})
print(result)
    
  
