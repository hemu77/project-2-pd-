import os#to get a new directory ,etc...
import re #regexlib-search for specific episodes and transcribe em
import requests 
from bs4 import BeautifulSoup as bs
rss_feed_url="https://lexfridman.com/feed/podcast/"
page=requests.get(rss_feed_url)
#check whether the contents are loaded correctly print(page.content)
soup=bs(page.content, 'xml')
#we can see all the items i webpg in readable way print(soup)
podcast_items=soup.find_all('item')
#index need to be 0,else,we didnt get the required result,use .text to get text
#print(podcast_items[0].find('description')).text---
#from the above text,i found out that links are in enclosure tag
#---------------------------------------------------------
#mp3_url=podcast_items[0].find('enclosure')['url']
#to download the mp3 file..
#mp3_file=requests.get(mp3_url)
#with open('myfile.mp3','wb') as f:
    #f.write(mp3_file.content)
#succesful,this is to download a single podcast.
#for multiple podcasts------------------------------------
os.mkdir('./downloads/')#create a directory
#count=0#intialize and limit the count for downloading
#for podcast in podcast_items:
    #if count==10:
        #break
    #title=podcast.find('title').text
     #print(title)-here,we get titles of all the podcast episodes in the URL
    #mp3_url=podcast.find('enclosure')['url']
     #print(mp3_url)-links of all the episodes
    #mp3_file=requests.get(mp3_url)
    #with open(f'./downloads/{title}.mp3','wb') as f:#stored with its title name
        #f.write(mp3_file.content)

    #count +=1
#succesfully downloaded 10 episodes---------------------------------------------------
#building smart search capabilities-we only download the required podcast
count=0
for podcast in podcast_items:
    if count==5:
        break
    title=podcast.find('title').text
    description=podcast.find('description').text
    #print(title)-here,we get titles of all the podcast episodes in the URL
    mp3_url=podcast.find('enclosure')['url']
    if re.search(r'robot',description,re.I):
        mp3_file=requests.get(mp3_url)
        with open(f'./downloads/{title}.mp3 ','wb') as f:#stored with its title name
            f.write(mp3_file.content)
    count+=1
#succesfully downloaded the specific podcasts(with filter)-----------------------------------------
#transcribe podcasts(API->assemblyAi)-----------------------------------------------------------------------------------
       






