import json
from tabulate import tabulate

with open('followers.json') as file:
    followers_json = json.load(file)

with open('following.json') as file:
    following_json = json.load(file)

following_list = []
for following in following_json["relationships_following"]:
    following_list.append(following["string_list_data"][0]["value"])

followers_list = []
for follower in followers_json:
    followers_list.append(follower["string_list_data"][0]["value"])

not_following_back = []
mutual_followers = []
for user in following_list:
    if user not in followers_list:
        not_following_back.append(user)
    else:
        mutual_followers.append(user)

print("Users not following back:")
for user in not_following_back:
    print(user)

print("\nMutual followers:")
for user in mutual_followers:
    print(user)
