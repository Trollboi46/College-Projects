import numpy as np
import time
import pickle
import json
import nltk
from datetime import datetime
from datetime import date
from nltk.stem import WordNetLemmatizer

now = datetime.now()
date = date.today()
current_t1 = now.strftime("%H")
current_t1_int = int(current_t1)
current_t2 = now.strftime("%H:%M:%S")
current_d1 = date.strftime("%B %d, %Y")

print("---------------------------------------------------------------------------------------------")
print("                                     COLLEGE CHATBOT                                   ")
print("---------------------------------------------------------------------------------------------")
print("Current Time : ",current_t2,"                                   Today's Date : ",current_d1)
print("\n")

print("Hello, I am an Artificial Intelligence ChatBot, VirtuIntelli.")
print("I was developed as a part of IT Workshop Project development.")
print("Currently i can assist you with Admission, Assignment, and Course related queries")
print("Since i am still under development, i may not be able to assist you with")
print("all your queries but i will forward them to my developer. Happy Chatting Ahead.")

print("\n")

if current_t1_int<12:
    print("Hello there, Good Morning.")
elif current_t1_int>=12 and current_t1_int<17:
    print("Hello there, Good Afternoon.")
elif current_t1_int>=17 and current_t1_int<24:
    print("Hello there, Good Evening.")

print("What is your name ?")
name = input()
print("\n")
time.sleep(1)

print("What is your age",name,"?")
age = int(input())
print("\n")
time.sleep(1)

cont = 1
x = 1
while cont==1:
    print("How can I help you",name,"?")
    ip1 = input()
    ip1 = ip1.lower()
    print("\n")
    time.sleep(1)

    if ip1.find('admission') != -1:
        print("What specifically you want to ask about Admission ?")
        ip2 = input()
        ip2 = ip2.lower()
        print("\n")
        time.sleep(1)

        if (ip2.find('procedure') != -1 or ip2.find('guideline')) and ip2.find('btech') != -1:
            print("Procedure for B.Tech admission is as follows : ")
            print("\n")
        
        elif (ip2.find('procedure') != -1 or ip2.find('guideline')) and ip2.find('mtech') != -1:
            print("Procedure for M.Tech admission is as follows : ")
            print("\n")
        
        elif (ip2.find('procedure') != -1 or ip2.find('guideline')) and ip2.find('phd') != -1:
            print("Procedure for PhD admission is as follows : ")
            print("\n")

        elif (ip2.find('procedure') != -1 or ip2.find('guideline')) and ip2.find('diploma') != -1:
            print("Procedure for Diploma admission is as follows : ")
            print("\n")
        x=x+1

    elif ip1.find('assignment') != -1:
        print("What specifically you want to ask about Assignment ?")
        ip3 = input()
        ip3 = ip3.lower()
        print("\n")
        time.sleep(1)

        if ip3.find('submit') != -1:
            print("Enter semester :")
            ip4 = int(input())
            print("\n")
            time.sleep(1)

            if ip4 == 1:
                print("")

            elif ip4 == 2:
                print("Hello")

            elif ip4 == 3:
                print("")
                
            elif ip4 == 4:
                print("")

            elif ip4 == 5:
                print("")

            elif ip4 == 6:
                print("")

            elif ip4 == 7:
                print("")

        elif ip3.find('status') != -1:
            print("Enter semester :")
            ip5 = int(input())
            print("\n")
            time.sleep(1)

            if ip5 == 1:
                print("")

            elif ip5 == 2:
                print("Hello")

            elif ip5 == 3:
                print("")
                
            elif ip5 == 4:
                print("")

            elif ip5 == 5:
                print("")

            elif ip5 == 6:
                print("")

            elif ip5 == 7:
                print("")


    elif ip1.find('course') != -1 or ip1.find('courses') != -1:
        print("What specifically you want to ask about Course ?")
        ip6 = input()
        ip6 = ip6.lower()
        print("\n")
        time.sleep(1)

        if ip6.find('syllabus') != -1 and ip6.find('cse'):
            print("")

        elif ip6.find('syllabus') != -1 and ip6.find('ece'):
            print("Hello")

    elif ip1.find('placement') != -1 or ip1.find('information') != -1:
        print("IIIT Nagpur")

    elif ip1.find('stop') != -1 or ip1.find('exit') != -1 or ip1.find('thank you') != -1:
        print("Thank you for your time.")
        cont = 0
        break
