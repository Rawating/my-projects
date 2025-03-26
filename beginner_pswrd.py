
var_web = input("Website name: ")
var_user = input("User name: ")
var_password = input("Password: ")

class func: 
    def __init__(self, website_name, user_name, pass_word):
        self.website_name = website_name
        self.user_name = user_name
        self.pass_word = pass_word
    def final(self):
        return f'\nWebsite name: {self.website_name}, User name: {self.user_name}, Password: {self.pass_word}'


pass_1 = func(var_web, var_user, var_password)

save = func.final(pass_1)


with open('info_doc.txt','a') as file:
    file.write(save)
file.close()   
