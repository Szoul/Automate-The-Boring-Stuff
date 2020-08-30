#! python 3.8.3
# 2048_player.py : play the 2048 game with a simple up-right-down-left command loop on a html of that game

# open website (https://gabrielecirulli.github.io/2048/)
# use selenium to give arrow commands in loop
# stop if game has ended
    # bonus: copy the highest number

# problem: broser immediatly closes after opening; sometimes: error message for STALE ELEMENT REFERENCE EXCEPTION
# works fine if i type in code in python shell
# probably has to do with VS-Code_runner

import selenium, time
from selenium.webdriver.common.keys import Keys
browser = selenium.webdriver.Firefox()
browser.get("https://gabrielecirulli.github.io/2048/")
game_elem = browser.find_element_by_tag_name("html")

arrow_directions = [Keys.ARROW_UP, Keys.ARROW_RIGHT, Keys.ARROW_DOWN, Keys.ARROW_LEFT]

for arrow_key in arrow_directions:
    game_elem.send_keys(arrow_key)