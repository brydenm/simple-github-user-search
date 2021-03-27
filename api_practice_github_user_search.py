#import the necessary libraries
import requests
import json
import datetime

print('.......................')
print('..Github user search...')
print('.......................\n\n')

username = input("Enter username to search GITHUB: ")
searchurl = 'https://api.github.com/users/' + username

#instantiate a get request
response = requests.get(searchurl)

#print the status code showing if API call was successful (200) or not (usually 400-500?)
print("Response status code: {} \n".format(response.status_code))
if response.status_code == 200:
    print('Search success! \n Displaying github user details:')
    print(response.json())
else:
    print('Search not successful :(')
