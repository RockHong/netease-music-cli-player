#!/usr/bin/env python
# encoding: UTF-8

'''
网易云音乐 Entry
'''

import curses, traceback
from menu import Menu
import argparse
import sys

version = "0.2.1.0"

def start():
    nembox_menu = Menu()
    try:
        nembox_menu.start_fork(version)
    except:
        # clean up terminal while failed
        nembox_menu.screen.keypad(1)
        curses.echo()
        curses.nocbreak()
        curses.endwin()
        traceback.print_exc()


if __name__ == '__main__':
    #start()
    ## Hong test
    import api
    import json
    import hashlib
    xxx = api.NetEase()
    # user log in
    account = 'focus@163.com'
    password = hashlib.md5( 'hdd').hexdigest()
    userinfo = xxx.login(account, password)
    #userinfo = xxx.phone_login('focus_on_one_thing@163.com', 'hzh123456wf')
    print json.dumps(userinfo,sort_keys=True,indent=2)
    # list playlists of a given user
    data = xxx.user_playlist(267877324);
    print json.dumps(data,sort_keys=True,indent=2)
    # list songs of a playlist
    print '--------------------------------'
    songs = xxx.playlist_detail(366139779)
    print json.dumps(songs,sort_keys=True,indent=2)
    # get url of song(s)
    print '----------22---------------------'
    urls = xxx.dig_info(songs, 'songs')
    print json.dumps(urls,sort_keys=True,indent=2)
    # play (and cache) song
    import player
    def do_nothing():
        print 'do nothing'
    ppp = player.Player()
    paras = urls[0]
    print paras
    print paras['song_name'].encode('utf-8')
    ppp.playing_flag = True
    ppp.popen_recall(do_nothing, paras)





parser = argparse.ArgumentParser()
parser.add_argument("-v", "--version", help="show this version and exit", action="store_true")
args = parser.parse_args()
if args.version:
    latest = Menu().check_version()
    curses.endwin()
    print 'NetEase-MusicBox installed version:' + version
    if latest != version:
        print 'NetEase-MusicBox latest version:' + latest
    sys.exit()
