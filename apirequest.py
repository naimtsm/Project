import requests
import pandas as pd

#Using GET Request
baseurl = 'https://rickandmortyapi.com/api/'
endpoint = 'character'

def main_request(baseurl, endpoint, x):
    req =  requests.get(baseurl + endpoint + f'?page={x}')
    return req.json()

def get_pages(response):
    return response['info']['pages']

# Character information
def parse_json(response):

    charlist = []  # Create empty list
    for item in response['results']:  # making a loop that want to access 'result' key  

        # save name & number of episode inside a dictionary 'char'
        char = { 'ID' : item['id'], 
                'Name' : item['name'],
                 'No_episode': len(item['episode']),
                 'Status' : item['status'],
                 'Species' : item['species']

                }

        #add dictionary into list 'charlist'
        charlist.append(char)


        # get name & number of episode the character have           
        #print(item['episode'])     
        #print(item['name'], len(item['episode']))   
    return charlist

        
# name = (data['results'][0]['name'])
# episodes = (data['results'][0]['episode'])
      


#NOTES ~ Response [200] consider as good response


mainlist = [] #add new list
data = main_request(baseurl, endpoint, 2)
# print(get_pages(data))

#start from 1, make sure no data st art with 0, +1 use to adjust the number
for x in range(1,get_pages(data)+1):
    print(x)
    mainlist.extend(parse_json(main_request(baseurl, endpoint, x)))
print(len(mainlist))



#Export to CSV file---------------
df= pd.DataFrame(mainlist)

#Test the head and tail of the dataset
#print(df.head(), df.tail())
df.to_csv('Character_list.csv', index = False) #index= False, to eliminate the index


