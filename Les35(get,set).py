class UserMail:


    def __init__(self, login, email):
        self.login = login
        self.__email = email

    def get_email(self):
        return self.__email

    def set_email(self, value):
        if isinstance(value, str) \
            and value.count('@') == 1 \
            and '.' in value[value.find('@'):]:
            self.__email = value
        else:
            print('It is not email')

    email = property(fget=get_email,fset=set_email)

user1 = UserMail('qwerty', 'user@gmail.com')

user1.email = 'user3@gmail.com'
print(user1.email)



