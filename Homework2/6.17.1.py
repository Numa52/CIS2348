#Ryan Nguyen PSID: 1805277

#assign variables

password = input()

mod_password =' '

#use .replace to remove and put in new characters

password = password.replace('i','!')
password = password.replace('a','@')
password = password.replace('m','M')
password = password.replace('B','8')
password = password.replace('o','.')

#adding q*s to password
mod_password = password + "q*s"

print(mod_password)