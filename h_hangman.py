# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 23:17:21 2020

@author: PC
"""

import random 

def guess_letter():
    
    heroes_list=["iron man","spider-man","superman","hulk","deadpool","flash","thor","batman",
                 "wolverine","aquaman","cyborg","captain america","green lantern","nightwing"]
    random.shuffle(heroes_list)
    word=list(random.choice(heroes_list))
    display=[]
    display.extend(word)
          
    for letter in range(len(display)):
        if display[letter]==" ":
            display[letter]=" "
            
        elif display[letter]=="-":
            
            display[letter]="-"
        else:
             display[letter]="_"

    print("  ".join(display))   
    lives=3
    nums=0
    while nums<len(word) and lives>0:
        guess=input("guess a letter: ") 
        for letter in range(len(display)):
                  
            if word[letter]==guess:
                display[letter]=guess
                print(" ".join(display)) 
                    
            elif guess not in word and lives>0:           
                         
                lives=lives-1
                nums=nums+1
                print("Wrong letter,You have: "+str(lives)+" lives" )
                print(" ".join(display))
                if lives==0:
                    print("Game over")
                    break
                else:
                    guess=input("guess a letter: ")
        if word==display:
            print("You win!")
            guess_2=input(" Do you want yo play one more time? Y or N " )
            if guess_2=="N":
                print("Thanks for playing")
                break
            elif guess_2=="Y":
                guess_letter()
            else:
                print("Incorrect choice. Game over")
guess_letter()

