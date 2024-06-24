import requests
import os
import datetime


# With Requests we have multiple options
# Get, Post, Put, Delete
# We've used requests.get() to get data from a URL
# We can also use requests.post() to send data to a URL
# We're going to POSTing data to Pixela to track our habit

# $ curl -X POST https://pixe.la/v1/users -d '{"token":"thisissecret", "username":"a-know", "agreeTermsOfService":"yes", "notMinor":"yes"}'# {"message":"Success.","isSuccess":true}

with open("user_param.txt","r") as file:
    for line in file:
        if line.strip():  # ignore empty lines
            key, value = line.strip().split('=', 1)
            os.environ[key] = value

token = os.environ.get('token')
username = os.environ.get('username')
agreeTermsOfService = os.environ.get('agreeTermsOfService')
notMinor = os.environ.get('notMinor')

## Create User Account
pixela_endpoint = "https://pixe.la/v1/users"
user_params = {"token": token,
               "username": username,
               "agreeTermsOfService": agreeTermsOfService,
               "notMinor": notMinor}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)


## Create a Graph
graph_endpoint = f"{pixela_endpoint}/{username}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Reading Graph",
    "unit": "pages",
    "type": "int",
    "color": "ajisai"
}

headers = {"X-USER-TOKEN": token}

# graph_response = requests.post(url=graph_endpoint,
#               json=graph_config,
#               headers=headers)
#
# print(graph_response.text)

# We can see it at https://pixe.la/v1/users/pattycakes/graphs/graph1.html

## Post a Pixel
# We can now post a pixel to our graph

pixel_creation_endpoint = f"{pixela_endpoint}/{username}/graphs/graph1"
today = datetime.datetime.now().strftime("%Y%m%d")

post_pixel_response = requests.post(url=pixel_creation_endpoint,
                                    json={"date": today, "quantity": "1"},
                                    headers=headers)
print(post_pixel_response.text)

# We can see it at https://pixe.la/v1/users/pattycakes/graphs/graph1.html

## HTTP REQUESTS FOR PUT AND DELETE
# PUT will change existing data
# DELETE will remove data

# Update a Pixel
# We can update a pixel by sending a PUT request
# put_pixel_endpoint = f"{pixela_endpoint}/{username}/graphs/graph1/{today}"
# put_pixel_params = {"quantity": "2"}
#
# put_pixel_response = requests.put(url=put_pixel_endpoint,
#                                   json=put_pixel_params,
#                                   headers=headers)
# print(put_pixel_response.text)

# Delete a Pixel
# We can delete a pixel by sending a DELETE request
# delete_pixel_endpoint = f"{pixela_endpoint}/{username}/graphs/graph1/{today}"
# delete_pixel_response = requests.delete(url=delete_pixel_endpoint, headers=headers)
# print(delete_pixel_response.text)

