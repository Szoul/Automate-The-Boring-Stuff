#! python 3.8
# link_verification.py: downloads every linked page on a given URL; Flags pages with 404 error

# Take URL input either in a input() function, via pyperclip, or as a sys.argv[1] command
    # check if URL is valid
# Check for linked pages (<a> </a>)
    # what a beatiful day for soup
    # since it could lead to a lot of pages, use requests instead of selenium so it works faster
# download html of every link
    # to a new Folder in cwd named "link_verification_folder" and print out path to folder
        # dont forget to iterate file with res.iter_content()
# check each download iteration if side is valid
# try/except Error 404: save link to error-page into a list and print that list at end
    # add that list as a txt document in link_verification folder


#TODO Problems:
    # some href's are like : "../text" and refer to the same side except for the last URL-part [adress]/text (Protocol//Domain/Path/[last part of Path]
        # how to deal with it if additionally it has info to port/parameters/fragments?
    # some href "links" (calibre) just scroll down the current side to a certain point and return the value "None"
    # a lot of 404 error messages come from a link, that is : <a>[href: "link"] [class: x] [same/different link] </a> and those 2 links get just added to each other even though 2nd one is not part of href
        # IS there a module that can check any links made/ a simple way to capture all links inside a href (with all the exceptions)??



import requests, os, bs4
from pathlib import Path 

main_url = "https://automatetheboringstuff.com/2e/chapter12/"
main_res = requests.get(f"{main_url}")
main_res.raise_for_status()

ver_folder_path = Path(Path.cwd()/"link_verification_folder")
if ver_folder_path.exists():
    pass
else:
    os.mkdir("link_verification_folder")


soup = bs4.BeautifulSoup(main_res.text, "lxml")
list_of_links = []
for link_line in soup.find_all("a"):
    list_of_links.append(link_line.get("href"))


dict_of_error_links = {}
filenmb = 0
for link in list_of_links:

    if link is None:
        print (link)
        print ("NONE TYPE")
        continue
    elif link[0:4] is not "https":
        link = "https://automatetheboringstuff.com/2e/" + link
    print (link)

    current_url = requests.get(f"{link}")
    filenmb += 1
    try:
        current_url.raise_for_status()
        new_file = open(ver_folder_path/f"{filenmb}.txt", "wb")
        for chunk in current_url.iter_content(100000):
            new_file.write(chunk)
        new_file.close()
    except requests.exceptions.HTTPError as exc:
        dict_of_error_links[link] = exc                
    except Exception as exc2:
        dict_of_error_links[link] = exc2 

error_log_file = open(ver_folder_path/"error_log.txt", "a")
for error_message in dict_of_error_links.keys():
    error_log_file.write(("\n\n" + str(error_message) + " " + str(dict_of_error_links[error_message])))
error_log_file.close()