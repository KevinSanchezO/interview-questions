def getMaxCount(people, status):
    if (not(1 <= len(people)) and not(len(people) <= 10**5)):
        return -1
    if (len(people) != len(status)):
        return -1
    if (not(verifyPeople(people)) and not(verifyStatus(status))):
        return -1
    
    register = {}
    for (a,b) in zip(people, status):
        if (b == '-'):
            if (not(a in register)):
                return -1
            elif (register[a] % 2 == 0):
                return -1
            else:
                register[a] = register[a] + 1
        else:
            if (not(a in register)):
                register[a] = 1
            elif (register[a] % 2 != 0):
                return -1
            else:
                register[a] = register[a] + 1
    return len(register)

def verifyPeople(people):
    for i in people:
        if (not(isinstance(i, int))):
            return False
    return True

def verifyStatus(status):
    for i in status:
        if (i != '-' and i != '+'):
            return False
    return True

if __name__ == '__main__':
    people = [1,2,1,3,1]
    status = ['+', '+', '-', '+', '+']
    print(getMaxCount(people, status))