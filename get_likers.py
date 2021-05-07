from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from Selenium_keys import *
from selenium.webdriver.common.action_chains import ActionChains
import os
import re


def cls():
    if os.name == 'posix':
        return os.system('clear')
    else:
        return os.system('cls')


def get_likers(user_screen_name, id_list):
    print("Get likers Running...")
    driver = webdriver.Chrome(PATH)
   # driver.set_window_position(-10000, 0)

    URL = 'https://twitter.com/login'
    driver.get(URL)
    print("Webdriver opened")
    sleep(5)

    username = driver.find_element_by_xpath(
        '//input[@name="session[username_or_email]"]')
    username.send_keys(tt_username)
    password = driver.find_element_by_xpath(
        '//input[@name="session[password]"]')
    password.send_keys(tt_password)
    password.send_keys(Keys.ENTER)
    print("Logged in")
    likers_list = []
    screen_name = user_screen_name
    print(f'Screen_name: {screen_name}')
    print(f'Retrieving tweets info...')

    for ID in id_list:
        skip = False
        end_scroll = False
        print(f'[{id_list.index(ID)}] Scrapping likers username ...')
        status_id = ID
        url_tt = f'https://twitter.com/{screen_name}/status/{status_id}/likes'
        driver.get(url_tt)
        while not (end_scroll):
            sleep(5)

            profiles = driver.find_elements_by_xpath(
                '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/section/div/div/div')

            if profiles == []:
                skip = True
                end_scroll = True
            if not skip:
                i = 0
                profiles_text = []
                for profile in profiles:
                    if profile.text == '':
                        profiles.pop(i)
                        end_scroll = True
                    else:
                        profiles_text.append(profile.text)
                    i = i + 1
                for p in profiles_text:
                    lk = re.search(r"(@.*)", p)
                    likers_list.append(lk.group(1))
                if not end_scroll:
                    element = driver.find_element_by_xpath(
                        '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[2]/div')
                    scroll_y_by = 600
                    driver.execute_script(
                        "arguments[0].scrollBy(0, arguments[1]);", element, scroll_y_by)
                    sleep(2)
    print("Scrape Done!")
    driver.close()
    return set(likers_list)


if __name__ == "__main__":
    cls()
    id_list = ['a']
    likers = get_likers('KhemeticChurch', id_list)

    print("\n\n ----- Users that liked your tweets -----")
    """
    for item in likers:
        print(item)
    """
    ccc = 0
    for us in likers:
        print(us)
        ccc = ccc + 1

    print(ccc)
