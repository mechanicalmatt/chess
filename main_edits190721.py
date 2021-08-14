import urllib.request
import ast
import tweepy
import time
import time

CONSUMER_KEY = '#######'
CONSUMER_SECRET = '####'
ACCESS_KEY = '#########'
ACCESS_SECRET = '######'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
user = api.me()
mentions = api.mentions_timeline()

file = "C:/Users/m_gray.DESKTOP-Q2TTLA7/Desktop/replied_to.txt"

t0 = mentions[0]
t0_id = t0.__dict__['id_str']

####

def get_author():
    tweet_author = mentions[0].__dict__['author'].__dict__['screen_name']
    return tweet_author
def get_username():
    chess_username = []
    for i in t0.__dict__['text'].split(' '):
        if '!' in i:
            chess_username = i.strip('!')
    return chess_username

####

def stats(username):
    webUrl = urllib.request.urlopen('https://api.chess.com/pub/player/{}/stats'.format(username))
    data = webUrl.read()
    a = ast.literal_eval(data.decode('utf-8'))
    lst = ""
    lst += str(username) + ' stats: ' + '\n'
    lst += ('Daily rating - ' + str(a['chess_daily']['last']['rating']) + '\n')
    lst += ('Rapid rating - ' + str(a['chess_rapid']['last']['rating']) + '\n')
    lst += ('Bullet rating - ' + str(a['chess_bullet']['last']['rating']) + '\n')
    lst += ('Blitz rating - ' + str(a['chess_blitz']['last']['rating']))
    return lst
print(stats('mechmartian'))
def stats_daily(username):
    webUrl = urllib.request.urlopen('https://api.chess.com/pub/player/{}/stats'.format(username))
    data = webUrl.read()
    a = ast.literal_eval(data.decode('utf-8'))
    lst = str(username) + ' daily rating: ' + str(a['chess_daily']['last']['rating'])
    return lst
print(stats_daily('mechmartian'))

def do_it():
    author = get_author()
    username = get_username()
    replies = ""
    # stats_ = stats(username)
    with open(file, 'r') as doc:
        info = doc.readlines()
    for i in info:
        replies += str(i)
    # print(replies)
    if t0_id not in replies and '!' in t0.__dict__['text']:
        # send tweet
        api.update_status('@mattytgray ' + str(stats(get_username())), mentions[0].__dict__['id'])
        with open(file, 'a') as doc:
            print(t0_id, file=doc)
        print('new tweet: working on it...')
    else:
        print('most recent tweet already replied to')