from bs4 import BeautifulSoup
from urllib.request import urlopen

import requests

URL_list=[]
Temp_list=[]

def Process(URL):
    print ( "Reading %s..." %(URL) )
    counter = 0
    
    html_page = urlopen(URL)
    soup = BeautifulSoup(html_page)
    
    for link in soup.findAll('a'):
        if type( link.get('href') ) == str :
            URL_list.append(link.get('href'))
            counter=counter+1
        
    print ("Found %d URLs on this page" %(counter) )
    return counter


def Scrap_Text(url):
    html = urlopen(url).read()
    soup = BeautifulSoup(html)
    file = open("Data.txt", "a")
    for script in soup(["script","style"]):
        script.extract()
    text = soup.get_text()


    lines = (line.strip() for line in text.splitlines())

    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))

    text = '\n'.join(chunk for chunk in chunks if chunk)
    file.write(text)
    file.close()
    print(text)

    

URL = input("Seed input >> :")
URL_list.append(URL)



for item in URL_list:
    if URL_list[URL_list.index(item)][0:4]=="http" or URL_list[URL_list.index(item)][0:4]=="www.":
            Process(item)
            Scrap_Text(item)
            
        
print(URL_list)
print ("size of list now is : %d" %(len(URL_list)) )

