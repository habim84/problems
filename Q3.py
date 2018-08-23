def checkPalin(str):
    counter, flag, newStr = 0, True, str.lower()
    while counter <= int(len(newStr)/2):
        flag = False if newStr[counter] != newStr[len(str)-1-counter] else True
        if not flag:
            break
        counter = counter + 1
    return flag

