def not_string(str):
    if len(str) >= 3 and str[:3] == 'not':
        return str
    return 'not ' + str

not_string('test')
not_string('no test')
not_string('nottingham')
