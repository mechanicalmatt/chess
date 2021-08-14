import urllib.request
import ast
import tweepy
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

t0 = mentions[0]
t0_id = t0.__dict__['id_str']

# RETRIEVE TWEETS ALREADY REPLIED TO, AND WRITE WORKING REPLY INTO DOC

file = "C:/Users/m_gray.DESKTOP-Q2TTLA7/Desktop/replied_to.txt"

####

def playerProfile(username):
    webUrl = urllib.request.urlopen('https://api.chess.com/pub/player/{}'.format(username))
    data = str(webUrl.read())
    split_data = data.split(',')
    print(data)
    for i in split_data:
        print(i)

# playerProfile('mechmartian')

import urllib.request
import ast

# print stats for all gametypes of a given gametype
def stats(username):
    webUrl = urllib.request.urlopen('https://api.chess.com/pub/player/{}/stats'.format(username))
    data = webUrl.read()
    a = ast.literal_eval(data.decode('utf-8'))
    b = username + ' stats:'
    c = 'Daily rating - ' + str(a['chess_daily']['last']['rating'])
    d = 'Rapid rating - ' + str(a['chess_rapid']['last']['rating'])
    e = 'Bullet rating - ' + str(a['chess_bullet']['last']['rating']) 
    f = 'Blitz rating - ' + str(a['chess_blitz']['last']['rating'])
    return b, c, d, e, f
for i in list(stats('mechmartian')):
    print(i)
def statsDaily(username):
    webUrl = urllib.request.urlopen('https://api.chess.com/pub/player/{}/stats'.format(username))
    data = webUrl.read()
    a = ast.literal_eval(data.decode('utf-8'))
    print('{} daily rating - '.format(username) + str(a['chess_daily']['last']['rating']))
def statsRapid(username):
    webUrl = urllib.request.urlopen('https://api.chess.com/pub/player/{}/stats'.format(username))
    data = webUrl.read()
    a = ast.literal_eval(data.decode('utf-8'))
    print('{} rapid rating - '.format(username) + str(a['chess_rapid']['last']['rating']))
def statsBullet(username):
    webUrl = urllib.request.urlopen('https://api.chess.com/pub/player/{}/stats'.format(username))
    data = webUrl.read()
    a = ast.literal_eval(data.decode('utf-8'))
    print('{} bullet rating - '.format(username) + str(a['chess_bullet']['last']['rating']))
def statsBlitz(username):
    webUrl = urllib.request.urlopen('https://api.chess.com/pub/player/{}/stats'.format(username))
    data = webUrl.read()
    a = ast.literal_eval(data.decode('utf-8'))
    print('{} blitz rating - '.format(username) + str(a['chess_blitz']['last']['rating']))
    
stats('mechmartian')

########

def playerGames(username):
    webUrl = urllib.request.urlopen('https://api.chess.com/pub/player/{}/games'.format(username))
    data = webUrl.read()
    a = ast.literal_eval(data.decode('utf-8'))
    print(a)

# list of tweet_id for mentions already replied to
replied = []

# tweet author
def get_author():
    tweet_author = mentions[0].__dict__['author'].__dict__['screen_name']
    return tweet_author
# chess username from tweet
def get_username():
    chess_username = []
    t0 = mentions[0]
    replied.append(mentions[0].__dict__['id'])
    for i in t0.__dict__['text'].split(' '):
        if '!' in i:
            chess_username = i.strip('!')
    return str(chess_username)

####
def do_it():
    author = get_author()
    username = get_username()
    replies = ""
    player_stats = stats(username)
    with open(file, 'r') as doc:
        info = doc.readlines()
    for i in info:
        replies += str(i)
    if t0_id not in replies:
        # send tweet
        with open(file, 'a') as doc:
            print(t0_id, file=doc)
    print(player_stats)
    print(author)

do_it()



