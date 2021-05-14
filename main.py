from logging import error, exception
import PySimpleGUI as sg
from get_ids import get_timeline
from get_likers import get_tweets_likers
import csv
import pandas as pd
from more_itertools import unique_everseen


def cleanExport():
    with open('users.csv', 'r') as f, open('users.csv', 'w') as out_file:
        out_file.writelines(unique_everseen(f))


sg.theme('DarkAmber')
layout = [[sg.Text('Get list of who liked your tweets posted in the last 2 days!')],
          [sg.Text('Enter your username(@)'), sg.InputText(focus=True)],
          [sg.Button('Search', size=(10, 0)), sg.Button('Cancel')]]
end_all = False
window = sg.Window('Twitter Bot - Likers', layout)
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        end_all = True
        break
    if values[0] != "":
        username_at = values[0]

        break
    else:
        sg.Popup("User can't be blank")

window.close()
if end_all == False:
    sg.Popup("Click the 'OK' button bellow to start the script...")
    print("Searching for tweets ids...")
    tl_tt = get_timeline(username_at)
    print("Get tweets id - OK")
    if tl_tt == []:
        print("id list returned empty")
        raise exception
    print("Searching for 'likers'")
    with open(f'./users.csv', 'w', newline='', encoding='UTF-8') as f:
        csv_writer = csv.writer(f, delimiter=';')
        csv_writer.writerow(
            ['users_@'])
    likers = []
    likers.append(get_tweets_likers(username_at, tl_tt))
    with open(f'./users.csv', 'w', newline='', encoding='UTF-8') as f:
        csv_writer = csv.writer(f, delimiter=';')
        for i in likers:
            csv_writer.writerow(
                [i])
    cleanExport()
    print("Likers search done - OK")
    sg.Popup("Done!!\n\nData saved to : '(./users.csv)\n'")
