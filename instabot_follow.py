"""This is an example of
Instagram bots (Real acoounts created by me)
that follow accounts.
"""

import pyrebase
from instapy import InstaPy
from instapy import smart_run


#Lior Keren Instabots from Firebase configuration
config = {
  "apiKey": "AIzaSyAS2GJAxLbHhuuHEj5kj8mfdEzDvRVONd4",
  "authDomain": "instagramunandaut.firebaseapp.com",
  "databaseURL": "https://instagramunandaut-default-rtdb.firebaseio.com",
  "storageBucket": "instagramunandaut.appspot.com"
}

#List of users 
lst = []

# number of elements as n
n = int(input("Enter number of users to interact : "))
 
# iterating till the range
for i in range(0, n):
    input_var = input("Enter user to follow: ")
    #insert user from input to list
    lst.append(input_var)

firebase = pyrebase.initialize_app(config)
db = firebase.database()
all_users = db.child("instausers").get()

for user in all_users.each():
    if user.val() is not None:
      #for each user name and passw login to instagram and follow
      print(user.val().get('pas'))
      print(user.val().get('username'))
      # get an InstaPy session!
      # set headless_browser=True to run InstaPy in the background
      session  = InstaPy(username = user.val().get('username'),
                  password = user.val().get('pas'),
                  headless_browser=False)
      session.set_skip_users(skip_private = False)
      with smart_run(session):
          """ Activity flow """
          # general settings
          session.set_relationship_bounds(enabled=True,
                                          delimit_by_numbers=True,
                                          max_followers=8500,
                                          min_followers=45,
                                          min_following=77)

          #follow users by name
          session.follow_by_list(followlist = lst, times=1, sleep_delay=600, interact=False)
          session.set_do_follow(enabled=True, percentage=10, times=2)
          
          print("Done")