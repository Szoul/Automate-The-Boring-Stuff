#! python 3.8.3
# 2048_player.py : play the 2048 game with a simple up-right-down-left command loop on a html of that game

# open website (https://gabrielecirulli.github.io/2048/)
# use selenium to give arrow commands in loop
# TODO <bonus>: stop if game has ended 
    # check how conditions manifest in a html script and how selenium can recognize that
# TODO <bonus>: copy the highest number/Game Result
    # if condition --> check html for line that prints the result


import selenium, time
from selenium.webdriver.common.keys import Keys
browser = selenium.webdriver.Firefox()
browser.get("https://gabrielecirulli.github.io/2048/")
game_elem = browser.find_element_by_tag_name("html")
time.sleep(5)                                               
#seems to only work with waiting time, otherwise:
    #selenium.common.exceptions.StaleElementReferenceException: Message: The element reference of <html> is stale; 
    #either the element is no longer attached to the DOM, it is not in the current frame context, or the document has been refreshed                 

arrow_keys = [Keys.ARROW_UP,Keys.ARROW_RIGHT,Keys.ARROW_DOWN,Keys.ARROW_LEFT]

while True:
    for arrow in arrow_keys:
        game_elem = browser.find_element_by_tag_name("html")
        game_elem.send_keys(arrow)