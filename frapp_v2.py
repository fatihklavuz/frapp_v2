#!/usr/bin/python3
# -*- coding: utf-8 -*-


import itertools

def mylogo():
    
    print("""
     \033[1;33mXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxX\n  
           \033[1;34mcreated fatih kılavuz\n
      \033[1;34mhttps://github.com/fatihklavuz\n
     \033[1;33mooooooooooooooooooooooooooooooooooo
     \033[1;33mo                                 o
     \033[1;33mo           frapp_v2              o
     \033[1;33mo                                 o
     \033[1;33mo          Generator              o
     \033[1;33mo                                 o
     \033[1;33mooooooooooooooooooooooooooooooooooo
     \n
          
          """)

mylogo()


new_pass=[]
name=input("Victim Name : ")
surname=input("Victim SurName : ")
birtday=input("Victim Birthday :" )
long_spec='!#$%&/()=?-_@<>.\' '
smp_spec="'-+*/.' '"
passleng=int(input("Enter Password Length (Sample 10) : "))

passques=input("You want Long Special Character Or Short l/s :")
passwrite=input("You want a create wordlist y/n : ")

if passwrite=='y':
    pass_file=(input("Write filename : "))
    word_list=open(pass_file+".txt","w")

    if passques=='l':
        
        
        new_pass="".join([name,surname,birtday,long_spec])
        for i in range(passleng):
            for n in itertools.product(new_pass,repeat=i):
             nowpass="".join(n)
             print(nowpass)
             word_list.write(nowpass+"\n")
    elif passques=='s':
       
         word_list=open(pass_file+".txt","w")
         new_pass="".join([name,surname,birtday,smp_spec])
         for i in range(passleng):
            for n in itertools.product(new_pass,repeat=i):
             nowpass="".join(n)
             print(nowpass)
             word_list.write(nowpass+"\n")
if passwrite =='n':
    if passques=='l':
        new_pass="".join([name,surname,birtday,long_spec])
        for i in range(passleng):
            for n in itertools.product(new_pass,repeat=i):
                nowpass="".join(n)
                print(nowpass)
    elif passques=='s':
        new_pass="".join([name,surname,birtday,smp_spec])
        for i in range(passleng):
            for n in itertools.product(new_pass,repeat=i):
                nowpass="".join(n)
                print(nowpass)
        
word_list.close()
