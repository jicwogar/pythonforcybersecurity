#!/usr/bin/env python3
# Script that performs a dictionary attack against known password hashes
# Needs a dictionary file, suggested to use https://github.com/danielmiessler/SecLists/tree/master/Passwords/Common-Credentials
# By inyambe

#Import necessary Python modules
import crypt
import os

def test_password(hashed_password, algorithm_salt, plaintext_password):
    crypted_password = crypt.crypt(plaintext_password, algorithm_salt)
    #Compare hashed_password with the just created hash
    if hashed_password == crypted_password:
        return True
    return False

def read_dictionary(dictionary_file):
    #Open provided dictinary file
    script_path = os.path.realpath(__file__)
    script_folder = os.path.split(script_path)
    f = open(script_folder[0] + "/" + dictionary_file, "r")
    message = f.read()
    return message 

#Load dictionary file and prompt for has and algorithms/salt    
password_dictionary = read_dictionary("top1000.txt")
hashed_password = input("What is the hashed password?")
algorithm_salt = input("What is the algorithm and salt?")

#For each password in dictionary file, test against hashed_password
for password in password_dictionary.splitlines():
    result = test_password(hashed_password, algorithm_salt, password)
    if result:
        #if match is found, print it and quit
        print("Match found : {0}".format(password))
        break
