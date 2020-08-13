


def Replace_Spaces(lst):
    '''Replaces all ` ` with `_` in each string in list.'''
    trim = {s.strip().replace(' ', '-') for s in lst}
    return trim
