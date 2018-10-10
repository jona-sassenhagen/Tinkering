def make_string(input):
    '''
    Recursively convert all elements of a list or
    values in a dictionary into string.
    '''
    if type(input) == int:
        return str(input)
    elif type(input) == list:
        return [make_string(x) for x in input]
    elif type(input) == dict:
        out = dict()
        for k, v in input.items():
            out[k] = make_string(v)
        return out
