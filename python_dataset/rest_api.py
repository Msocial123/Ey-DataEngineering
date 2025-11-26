import requests

# REST API (Representational State Transfer)
# send HTTP request to an external API servers and receive response back (JSON)
# python provides a simple powerfull HTTP library i.e request consuming REST APIs (pip install requests)

# create -> POST() send new data to the api
# read --> GET() get data from API
# update --> PUT/PATCH update existing data
# Delete -->DELETE remove the data from API
#defining the API end point
# url="https://jsonplaceholder.typicode.com/users"
# #make a get request
# response = requests.get(url)
#
# #check the status
#
# if response.status_code == 200:
#     users=response.json() # in the form of json response
#     print(response.status_code)
#     for user in users[:3]:
#         print(f"ID:{user['id']},Name:{user['name']},Email:{user['email']}")
# else:
#         print("failed to connect ",response.status_code)

# POst

# url="https://jsonplaceholder.typicode.com/users"
# new_post={
#     "title":"Data Posting",
#     "body":"sending this to check working or not",
#     "userId":1
# }
#
# response = requests.post(url,json=new_post)
# print("status code:",response.status_code)
# print("response of JSON",response.json())

