import random
import time
def mistake7():
    print("YOU GUESSED THE WRONG LETTER!")
    time.sleep(2)
    print("""
            +---+
            |   |
            |   O
            |  /|\\
            |  / \\
            |""")
    
def mistake6():
    print("YOU GUESSED THE WRONG LETTER!")
    time.sleep(2)
    print("""
            +---+
            |   |
            |   O
            |  /|\\
            |  / 
            |""")
def mistake5():
    print("YOU GUESSED THE WRONG LETTER!")
    time.sleep(2)
    print("""
            +---+
            |   |
            |   O
            |  /|\\
            |   
            |""")
def mistake4():
    print("YOU GUESSED THE WRONG LETTER!")
    time.sleep(2)
    print("""
            +---+
            |   |
            |   O
            |  /|
            |  
            |""")
def mistake3():
    print("YOU GUESSED THE WRONG LETTER!")
    time.sleep(2)
    print("""
            +---+
            |   |
            |   O
            |  /
            |""")
def mistake2():
    print("YOU GUESSED THE WRONG LETTER!")
    time.sleep(2)
    print("""
            +---+
            |   |
            |   O
            |  
            |""")
def mistake1():
    print("YOU GUESSED THE WRONG LETTER!")
    time.sleep(2)
    print("""
            +---+
            |   |
            |   
            |""")

def main():
    words_to_guess=["penguin","giraffe","kingdom","teacher","chicken","holiday","kitchen","morning","library","thunder"]
    word=random.choice(words_to_guess)
    if word == "penguin":
        print("HINT: THE WORD THAT YOU HAVE TO GUESS IS A LIVING THING AND BEGINS WITH LETTER P")
    elif word == "giraffe":
        print("HINT: THE WORD THAT YOU HAVE TO GUESS IS A LIVING THING AND BEGINS WITH LETTER G")
    elif word == "kingdom":
        print("HINT: THE WORD THAT YOU HAVE TO GUESS IS A PLACE AND BEGINS WITH LETTER K")
    elif word == "teacher":
        print("HINT: THE WORD THAT YOU HAVE TO GUESS IS A PROFESSION  AND BEGINS WITH LETTER T")
    elif word == "chicken":
        print("HINT: THE WORD THAT YOU HAVE TO GUESS IS A LIVING THING AND BEGINS WITH LETTER C")
    elif word == "holiday":
        print("HINT: THE WORD THAT YOU HAVE TO GUESS IS AN SPECIFIC OCASSION OR AN EVENT AND BEGINS WITH LETTER H")
    elif word == "kitchen":
        print("HINT: THE WORD THAT YOU HAVE TO GUESS IS A PLACE AND BEGINS WITH LETTER K")
    elif word == "morning":
        print("HINT: THE WORD THAT YOU HAVE TO GUESS IS A PHASE AND BEGINS WITH LETTER M")
    elif word == "library":
        print("HINT: THE WORD THAT YOU HAVE TO GUESS IS A PLACE AND BEGINS WITH LETTER L")
    elif word == "thunder":
        print("HINT: THE WORD THAT YOU HAVE TO GUESS IS A ACOUSTIC PHENOMENON AND BEGINS WITH LETTER T")
    
    mistake_count=0
    res_=["_"]*len(word)
    while(mistake_count!=7):
        user_letters=input(f"\n ENTER LETTER: ").lower()
        c=word.count(user_letters)
        if len(user_letters)>1:
            print("YOU CAN ONLY ENTER ONE LETTER AT A TIME! TRY AGAIN ")
        if user_letters in res_:
            print("YOU HAVE ALREADY GUESSED THIS LETTER! TRY AGAIN")
        else:
            if c==0:
                mistake_count+=1
                if mistake_count==1:
                    mistake1()
                elif mistake_count==2:
                    mistake2()
                elif mistake_count==3:
                    mistake3()
                elif mistake_count==4:
                    mistake4()
                elif mistake_count==5:
                    mistake5()
                elif mistake_count==6:
                    mistake6()
                elif mistake_count==7:
                    mistake7()
                    print("THE MAN IS HANGED! YOU LOST")
                    break  
            else:
                if c==1:
                    loc=word.find(user_letters)
                    res_.pop(loc)
                    res_.insert(loc,user_letters)
                    
                    
                elif c>1:
                    i=0
                    for times in range(0,c):
                        if i==0:
                            loc=word.find(user_letters)
                            res_.pop(loc)
                            res_.insert(loc,user_letters)
                            i=i+1
                        else: 
                            loc=word.find(user_letters,loc+1)
                            res_.pop(loc)
                            res_.insert(loc,user_letters)
                            
                res=''.join(res_)
                print(res)
                if "_" not in res_:
                    print("CONGRATULATIONSS!!!! YOU HAVE GUESSED THE RIGHT WORD!!! YOU WON!!!")
                    break          
main()

                    