#! python3
# pw.py - An insecure password locker program.


PASSWORDS = {'email': 'F7minlBDDuMJsdoijfosijsdfso',
             'blog': 'VmALveoi3089ueoijsdf0JAOI098',
             'luggage': '12355'}

import sys, pyperclip

if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]   # first command line arg is the account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account name ' + account + ' would you like to add it?')
    choice = input("Y/n: >>> ").lower()
    if choice.lower() == 'y':
        passw = input('What is the password for ' + account + '?')
        PASSWORDS[account] = passw
        print('Password for ' + account + 'saved!')

