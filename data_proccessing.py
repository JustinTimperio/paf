#! /usr/bin/env python3


def replace_spaces(lst, replacement='-'):
    '''
    Replaces spaces with the defined replacement string
    for every occurance and every string in a list.
    '''
    return {s.strip().replace(' ', replacement) for s in lst}
