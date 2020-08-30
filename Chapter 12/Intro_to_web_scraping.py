"""
# Web scraping is the term for using a program to download and process content from the web.
# This Chapter covers: webbrowsers, requests, bs4, selenium
# I will try to use Wikipedia.org and Google.maps for testing

# webbrowsers / the webbrowser module:
    # will only open() a tab to an URL
    # Method: open a tab with your Standard browser by passing the URL to the webbrowser.open() function
        # Example: Open goole Map at a certain adress
        #          https://www.google.com
        #                                /maps/place
        #                                           /[an adress in the right format]
"""

import webbrowser
#webbrowser.open("https://www.google.com/maps/place/Schönbrunn")
#webbrowser.open("https://en.wikipedia.org/wiki/Schönbrunn_Palace")





# request module
# to download files 
import requests

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
print (type(res))
if res.status_code == requests.codes.ok:
    print (res)
    print ("Status Code for 'ok' is 200, similar to 404, which is 'not found'. Ever.")
    print (res.raise_for_status)
no_res = requests.get("https://automatetheboringstuff.com/files/this_does_not_exist.blablabla")
print (no_res)
try:
    print (no_res.raise_for_status())               # raises an error: requests.exceptions.HTTPError: 404 Client Error: Not Found
                                                    # if raise_for_status() usually gives an error if a "bad" download happens
except requests.exceptions.HTTPError:
    print ("no_res does not exist")
print ("\n\n")
print(len(res.text))
print (res.text[:250])

#for chunk in res.iter_content(100000):
#    print (chunk)
        # --> returns "chunks" of the text of 100000 bytes size each iteration
print ("\n\n\n")


"""
How to make beautiful soup:
    1. Realize that regexes do not work on html and I should not be thinking about it. Ever. https://stackoverflow.com/a/1732454/1893164/
    2. Search for the Element (information) you want to get in the Source Code
    3. Parse the HTML for the content you are looking for with a Parsing-Module like bs4 or selenium
    4. Profit???
"""
import bs4

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',}           # apparently google doesnt like webscraping (not my code, dunno EXCATLY what it does besides delivering a request with some additional infos on whos asking)
vienna_time_google = requests.get("https://www.google.com/search?client=firefox-b-d&q=vienna+time", headers = headers)
vienna_time_google.raise_for_status()
v_time_soup = bs4.BeautifulSoup(vienna_time_google.text, "html.parser")         # html.parser parser is python build in || faster alternative: lxml (pip install)
print (type(v_time_soup))

#Element to search: <div class="gsrt vk_bk dDoNo XcVN5d" aria-level="3" role="heading">11:03</div>
time_div = v_time_soup.find_all("div", attrs = {"class":"XcVN5d"})
print ((time_div))  
time = time_div[0].getText()
print (time)

# selenium to interact with websites more "humanlike" (but slower) 
import selenium

