import urllib.request
import ast
import tweepy
import time

CONSUMER_KEY = 'EcceTMfViq54zGJrRvrdIUru9'
CONSUMER_SECRET = 'FJKgoWoowQ2T0m7dg8t466ql8O0PbAQLyBHqts3zrU0xaLpik0'
ACCESS_KEY = '1409557697662316545-CJtJ4MoqtJY8NEhdqERv3sx3eaGdcr'
ACCESS_SECRET = 'fxDdpCrU2OkiTdiYv89IhiH2ouvrlY7DBw74uM1EY4bPR'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
user = api.me()
mentions = api.mentions_timeline()

t0 = mentions[0]

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
    print(username + ' stats:')
    print('Daily rating - ' + str(a['chess_daily']['last']['rating']))
    print('Rapid rating - ' + str(a['chess_rapid']['last']['rating']))
    print('Bullet rating - ' + str(a['chess_bullet']['last']['rating']))
    print('Blitz rating - ' + str(a['chess_blitz']['last']['rating']))
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
    return chess_username

def send_reply():
    author = get_author()
    user = get_username()
    print(t0.__dict__['id'])
    if t0.__dict__['id'] in replied:
        print('replying...')
    print('b', replied, author, user)
send_reply()
