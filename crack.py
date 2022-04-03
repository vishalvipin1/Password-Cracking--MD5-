# Password Cracking using python
import hashlib

flag = 0

pass_hash = input("Enter md5 hash: ")

wordlist = input("File name: ")

try:
    passfile = open(wordlist, "r")
except:
    print("File not found")
    quit()

for word in passfile:
    enc_word = word.encode('utf-8')
    digest = hashlib.md5(enc_word.strip()).hexdigest()

    print(word)
    print(digest)
    print(pass_hash)

    if digest == pass_hash:
        print("Password Found")
        print("Password: "+word)
        flag = 1
        break

if flag == 0:
    print("Password not in list")
