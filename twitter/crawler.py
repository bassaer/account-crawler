"""This is a test program."""
import requests

def send_request(acount):
    """
    check whether specified account already exists or not.
    """
    url = 'https://twitter.com/' + acount
    request = requests.get(url)
    return request.status_code

print(send_request('bassaer_'))
print(send_request('q;wjefjqefiwejfojf'))
