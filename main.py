import PySimpleGUI as sg
from get_ids import get_timeline
from get_likers import get_likers
import csv

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
    id_list = []
    print("Cleaning extracted info")
    for T in tl_tt:
        try:
            id_list.append(T[1])
            print(f"[{tl_tt.index(T)}] id: {T[1]} likes: {T[2]}")
        except:
            break
    print("Searching for 'likers'")
    likers = get_likers(username_at, id_list)
    print("Likers search done - OK")
    with open(f'./users.csv', 'w', newline='', encoding='UTF-8') as f:
        csv_writer = csv.writer(f, delimiter=';')
        csv_writer.writerow(
            ['users_@'])
        for user_liker in likers:
            csv_writer.writerow([user_liker])

    sg.Popup("Done!!\n\nData saved to : '(./users.csv)\n'")
