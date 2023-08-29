#!/usr/bin/env python3

#USAGE
#python3 8char_passwd_list.py

#DESCTIPION
#This is a password list generator - mainly wifi password list - default 8 chars of all characters for password
#using multiple processes and doing parallel computation
#will generate its own files - of 1GB increments - easy for cat or awk to view

#CONDITIONS
#Both Uppercase and lowercase letters (e.g., a–z, A–Z)
#Base numbers and non-alphanumeric symbols 0123456789!@#$%^&*()~`_-=[]{}\|;':"<>?,./ 
#FULLLIST array USED: abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_+=~`[]{}|\:;"'<>,.?/ with a space.


import os
import random
import multiprocessing
from multiprocessing import Process
import time
import math

#set the time to start and see how long
start_time = time.perf_counter()

#function to generate list 
def gen_str():
    #entire list of chars in wifi password list
    alph_num_spec_arr = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','0','1','2','3','4','5','6','7','8','9','!','@','#','$','%','^','&','*','(',')','-','_','+','=','~','`','[',']','{','}','|','\\',':',';','\"','<','>',' ',',','.','?','/','\'']


    #write the file in 1GB increments
    x = 1
    while True:
        with open("8char_passlist_{}.txt".format(x),"a") as f:
            x += 1
            while os.fstat(f.fileno()).st_size < 1000000000: #size criteriunm

             #8 char list write to file   
             for aa in range(0, len(alph_num_spec_arr)):   #1 char 
              for bb in range(0, len(alph_num_spec_arr)):  #2 char
               for cc in range(0, len(alph_num_spec_arr)):  #3 char
                for dd in range(0, len(alph_num_spec_arr)):  #4 char
                 for ee in range(0, len(alph_num_spec_arr)):  #5 char
                  for ff in range(0, len(alph_num_spec_arr)):  #6 char
                   for gg in range(0, len(alph_num_spec_arr)):  #7 char
                    for hh in range(0, len(alph_num_spec_arr)):  #8 char
                     
                     #print the output to terminal or file with > wordlist with 1GB increments
                     f.write(alph_num_spec_arr[aa] + alph_num_spec_arr[bb] + alph_num_spec_arr[cc] + alph_num_spec_arr[dd] + alph_num_spec_arr[ee] + alph_num_spec_arr[ff] + alph_num_spec_arr[gg] + alph_num_spec_arr[hh] + "\n")#print all
                     f.flush()



#let start
if __name__ == '__main__':
    p1 = Process(target=gen_str)
    #start 
    p1.start()
    #join processes 
    p1.join()
