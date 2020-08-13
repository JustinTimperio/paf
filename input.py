#! /usr/bin/env python3
import re


def YN_Frame(prompt):
    '''Standard Y/N input frame. Returns True for Yes, False for No.'''
    while True:
        yn = input('\033[1m' + prompt + ' (y/n):' + '\033[0m')
        if yn.lower().strip() in ['y', 'yes']:
            return True
        elif yn.lower().strip() in ['no', 'n']:
            return False
        else:
            print('Please Respond With Yes/No!')


def Multi_Choice_Frame(options):
    '''
    Lets a user select between arbitrary number of options.
    Returns value the user selects. Input `exit` or `quit` or `skip` to return False.
    '''
    c_list = list(options)
    counter = 1
    while True:
        for o in c_list:
            print('(' + str(counter) + ') ' + o)
            counter += 1
        ans = input('\033[1m' + 'Enter Your Selection With an INT: ' + '\033[0m').strip()

        if re.findall(r'^([1-9]|0[1-9]|[1-9][0-9]|[1-9][1-9][0-9])$', ans) and int(ans) < counter:
            return c_list[int(ans) - 1]
        elif ans.lower() == 'quit' or ans.lower() == 'exit' or ans.lower() == 'skip':
            return False
        else:
            counter = 1
            print('Validate Int NOT Given! (Type `exit` to Skip)')


# Color Print Output
def prError(text):
    print("\u001b[31;1m{}\033[00m" .format(text))

def prSuccess(text):
    print("\u001b[32;1m{}\033[00m" .format(text))

def prWarning(text):
    print("\u001b[33;1m{}\033[0m" .format(text))

def prBold(text):
    print("\u001b[37;1m{}\u001b[0m" .format(text))

def prChanged(text):
    print("\u001b[35m{}\033[00m" .format(text))

def prRemoved(text):
    print("\033[31m{}\033[00m" .format(text))

def prAdded(text):
    print("\033[94m{}\033[00m" .format(text))
