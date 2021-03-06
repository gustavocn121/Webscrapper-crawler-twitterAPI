import tweepy
from tweepy_keys import *
import time
from datetime import datetime, timedelta


def get_timeline(user_screen):
    auth = tweepy.OAuthHandler(
        consumer_key=CONSUMER_API_KEY, consumer_secret=CONSUMER_API_KEY_SECRET)
    auth.set_access_token(ACESS_TOKEN, ACESS_TOKEN_SECRET)
    api = tweepy.API(auth, wait_on_rate_limit=True,
                     wait_on_rate_limit_notify=True)
    PAGE = 1
    try:
        tl = api.user_timeline(user_screen, include_rts=True,
                               exclude_replies=True, page=PAGE)
    except tweepy.TweepError as e:
        print(e.reason)
        input("Press any key to end...")
        raise tweepy.TweepError(e)
    tl_tt = []
    for t in tl:
        if t.text[:4] != 'RT @':
            tl_tt.append([str(t.created_at), t.id_str,
                          t.favorite_count, t.retweet_count, t.author.screen_name])
    today = str(datetime.now())
    today_fixed = f'{today[:4]}{today[5:7]}{today[8:10]}'
    tl_indx = 0
    print("searching timeline page...")
    end_paging = False
    while tl_tt != [] and not(end_paging):
        PAGE = PAGE + 1
        print(PAGE)
        last_tt_date_str = str(tl_tt[-1][0])
        last_date_fixed = f'{last_tt_date_str[:4]}{last_tt_date_str[5:7]}{last_tt_date_str[8:10]}'

        if ((int(today_fixed)) - (int(last_date_fixed)) > 1):
            end_paging = True
            break
        try:
            tl = api.user_timeline(
                user_screen, include_rts=True, exclude_replies=True, page=PAGE)
        except tweepy.TweepError as e:
            print(e.reason)
            input("Press any key to end...")
            raise tweepy.TweepError(e)

        for t in tl:
            if t.text[:4] != 'RT @':
                date_item = str(t.created_at)
                date_item_fixed = f'{date_item[:4]}{date_item[5:7]}{date_item[8:10]}'
                if (((int(today_fixed)) - int(date_item_fixed)) > 1):
                    end_paging = True
                else:
                    tl_tt.append(t.id_str)

    return tl_tt


if __name__ == '__main__':
    tl_tt = get_timeline('Khemeticchurch')
    for i in tl_tt:
        print(i)
