def nameUpper(name):
    return 'user' + name.upper()
def nameLower(name):
    return 'user' + name.lower()
def makeLog(userName, maker):
    return maker(userName)

user = input('Input your name:')
userAnsw = input('Select login-maker: 1-lower case; 2-upper case')
if userAnsw == '1':
    print(makeLog(user, nameLower))
elif userAnsw == '2':
    print(makeLog(user, nameUpper))
else:
    print('Wrong input!')
