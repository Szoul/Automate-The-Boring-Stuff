#! python 3.8
# image_site_downloader.py: Search for a specific tag and download any picture on a (any) photo-sharing-website (with a search bar)
# for now: on imgur.com


# request website at search result URL
    # https://imgur.com/search?q=[item to search, spacebar == +]
# look for identifier in Source code for every search result picture
    # under: class = "cards"
        # class = post
            # class = "image-list-link"
            # src: "image.jpg" (smaller than original, but ok for thius task, alternatively i could go to every linked post and download the original pictures)
# download pictures (request picture link)



import requests, bs4, os
from pathlib import Path

search_term = input().replace(" ", "+")
website = "https://imgur.com/search?q="
search_url = website+search_term

res = requests.get(search_url)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, "lxml")
pictures = soup.find_all("img")

# TODO: only scrap img's inside <div> class = "cards" </div> (though this right now only adds one .gif that is at the end of page)

goal_dir_path = Path(Path.cwd()/"image_site_downloader")
os.mkdir(goal_dir_path)
picture_nmb = 0
for picture in pictures:
    picture_link = "https:" + str(picture.get("src"))
    picture_res = requests.get(picture_link)
    picture_res.raise_for_status()
    picture_nmb += 1
    test_img = open(goal_dir_path/f"test_image{picture_nmb}.jpg", "wb")
    for chunk in picture_res.iter_content(100000):
        test_img.write(chunk)

