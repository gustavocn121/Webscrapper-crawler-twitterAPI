from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from Selenium_keys import *
import os
import re
import concurrent.futures
import csv
import time
from itertools import repeat
import PySimpleGUI as sg


def cls():
    if os.name == 'posix':
        return os.system('clear')
    else:
        return os.system('cls')


def login_tt():
    print("Get likers Running...")
    driver = webdriver.Chrome(PATH)
    driver.set_window_position(-10000, 0)

    URL = 'https://twitter.com/login'
    driver.get(URL)
    sleep(2)

    username = driver.find_element_by_xpath(
        '//input[@name="session[username_or_email]"]')
    username.send_keys(tt_username)
    password = driver.find_element_by_xpath(
        '//input[@name="session[password]"]')
    password.send_keys(tt_password)
    password.send_keys(Keys.ENTER)
    return driver


def get_likers(user_screen_name, ID):
    print(str(ID) + '\n')
    driver = login_tt()
    likers_list = []
    screen_name = user_screen_name
    skip = False
    end_scroll = False
    status_id = ID

    url_tt = f'https://twitter.com/{screen_name}/status/{status_id}/likes'
    driver.get(url_tt)
    while not (end_scroll):
        sleep(2)
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

    driver.close()
    for it in likers_list:
        lks.append(it)


def get_tweets_likers(screen_name_usr, id_list):
    global lks
    lks = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
        executor.map(get_likers, repeat(screen_name_usr), id_list)
    print('\n\n\n\n\n\n\nhjfbshefhjsefhjkvgesfvghsfvkghkvghsfvse\n\n\n')

    with open(f'./users.csv', 'w', newline='', encoding='UTF-8') as f:
        csv_writer = csv.writer(f, delimiter=';')
        for i in lks:
            csv_writer.writerow([i])
    print("Likers search done - OK")
    sg.Popup("Done!!\n\nData saved to : '(./users.csv)\n'")


if __name__ == "__main__":
    cls()
    start_time = time.time()
    id_list = ['1393218104402927617', '1393070702979280896']
    likers = get_tweets_likers('KhemeticChurch', id_list)

    print("\n\n ----- Users that liked your tweets -----")

    for item in likers:
        print(item)

    duration = time.time() - start_time
    print('\n\nDuration: ' + str(duration))
