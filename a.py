from get_likers import get_tweets_likers
import time
if __name__ == "__main__":

    start_time = time.time()
    id_list = ['1393218104402927617', '1393070702979280896']*10
    likers = get_tweets_likers('KhemeticChurch', id_list)

    print("\n\n ----- Users that liked your tweets -----")

    for item in likers:
        print(item)

    duration = time.time() - start_time
    print('\n\nDuration: ' + str(duration))
