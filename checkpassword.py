import requests
import hashlib
import logging
import sys

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'{res.status_code} is not 200, check the API and try again')
    return res

def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0

def pwned_api_check(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_char)
    return get_password_leaks_count(response, tail)

def main(stored_passwords):
    try:
        with open(stored_passwords, 'r') as f:
            passwords = [line.strip() for line in f.readlines() if line.strip()]
    except FileNotFoundError:
        print(f'File {stored_passwords} not found. Check your spelling and try again.')
        return

    for password in passwords:
        count = pwned_api_check(password)
        if count:
            logging.info(f'Password {password} has {count} times leaks.')
        else:
            logging.info(f'Password {password} has no leaks.')
    return 'Done!'

if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))