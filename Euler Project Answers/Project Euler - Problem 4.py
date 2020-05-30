# Enter question info here

def checkPal(value):
    value = str(value)
    palLength = len(value) // 2
    match = 0
    check = 0

    while match < palLength and value[check] == value[-check - 1]:
        match = match + 1
        check = check + 1

    palStatus = match == palLength
    return palStatus
