#Lynijah Russell CodeWorks2021
#August 2,2021
#lynijahr@gmail.com

##############################################
import sys

def intro():
    print("**20 Questions by Lynijah Russell** \nAKA the better 20Q")

def menu():
    print(" ")
    print("The key words: ")
    print("(Y- yes)")
    print("(N- no)")



def animal():
    q1= input("(1, Can you buy it? (y,n)  ")
    q1=q1.lower()
    if q1=="y":
        print("Clue: Able to be bought. ")
    if q1=="n":
        print("Clue: Not able to be bought. ")
    

    q2= input("(2, Does it bark? (y,n)  ")
    q2=q2.lower()
    if q2=="y":
        print("Clue: Barks. ")
        g1= input("Hmmm...dog? (y,n)")
        if g1=="y":
            print("Yay I guessed, it! I win!")
            c1=input("Would you like to play again? (y,n) ")
            if c1=="y":
                main()
            if c1=="n":
                print("Okay cya lata loser! ")
                sys.exit()
        if g1=="n":
            print("Okay lets continue...")
    if q2=="n":
        print("Clue: Does not bark. ")
    
    

    q3= input("(3, Does it Meow? (y,n)  ")
    q3=q3.lower()
    if q3=="y":
        print("Clue: Meows. ")
        g1= input("Hmmm....some type of cat? (y,n)")
        if g1=="y":
            print("Yay I guessed, it! I win!")
            c1=input("Would you like to play again? (y,n) ")
            if c1=="y":
                main()
            if c1=="n":
                print("Okay cya lata loser! ")
                sys.exit()
        if g1=="n":
            print("Okay lets continue...")
    if q3=="n":
        print("Clue: Does not meow. ")
    

    q4= input("(4, Does it hiss? (y,n)  ")
    q4=q4.lower()
    if q4=="y":
        print("Clue: Hisses. ")
        g1= input("Hmmmm...a snake? (y,n)")
        if g1=="y":
            print("Yay I guessed, it! I win!")
            c1=input("Would you like to play again? (y,n) ")
            if c1=="y":
                main()
            if c1=="n":
                print("Okay cya lata loser! ")
                sys.exit()
        if g1=="n":
            print("Okay lets continue...")
    if q4=="n":
       print("Clue: Does not hiss. ")
    
    q5= input("(5, Does it 'ribbit' ? (y,n)  ")
    q5=q5.lower()
    if q5=="y":
        print("Clue: Ribbits. ")
        g1= input("Hmmm... a frog? (y,n)")
        if g1=="y":
            print("Yay I guessed, it! I win!")
            c1=input("Would you like to play again? (y,n) ")
            if c1=="y":
                main()
            if c1=="n":
                print("Okay cya lata loser! ")
                sys.exit()
        if g1=="n":
            print("Okay lets continue...")
    if q5=="n":
        print("Clue: Does not ribbit. ")
    

    q6= input("(6, Is it a common pet in the US? (y,n)  ")
    q6=q6.lower()
    if q6=="y":
        print("Clue: Common pet. ")
    if q6=="n":
        print("Clue: Less common pet. ")
    

    q7= input("(7, it Swim? (y,n)  ")
    q7=q7.lower()
    if q7=="y":
        print("Clue: Able to swim. ")
        g1= input("Hmmmm...Sea creature? (y,n) ")
        if g1=="y":
            print("Yay I guessed, it! I win!")
            c1=input("Would you like to play again? (y,n) ")
            if c1=="y":
                main()
            if c1=="n":
                print("Okay cya lata loser! ")
                sys.exit()
        if g1=="n":
            print("Okay lets continue...")
    if q7=="n":
        print("Clue: Does not swim. ")
    

    q8= input("(8 Can it fly? (y,n)  ")
    q8=q8.lower()
    if q8=="y":
        print("Clue: Is able to fly. ")
        g1= input("Hmmmm some kind of bird? (y,n)")
        if g1=="y":
            print("Yay I guessed, it! I win!")
            c1=input("Would you like to play again? (y,n) ")
            if c1=="y":
                main()
            if c1=="n":
                print("Okay cya lata loser! ")
                sys.exit()
        if g1=="n":
            print("Okay lets continue...")
    if q8=="n":
        print("Clue: Not able to fly. ")
    

    q9= input("(9, Does it repeat things you say? (y,n)  ")
    q9=q9.lower()
    if q9=="y":
        print("Clue: Repeats what you say... hmm annoying..  ")
        g1= input("Hmmm... a child? HAHAHAH (y,n)")
        if g1=="y":
            print("Yay I guessed, it! I win!")
            c1=input("Would you like to play again? (y,n) ")
            if c1=="y":
                main()
            if c1=="n":
                print("Okay cya lata loser! ")
                sys.exit()
        if g1=="n":
            print("Okay lets continue...")
    if q9=="n":
        print("Clue: Minds their business")
    

    q10= input("(10, Is it colorful? (y,n)  ")
    q10=q10.lower()
    if q10=="y":
        print("Clue: Colorful. ")
    if q10=="n":
        print("Clue: Normal colors. ")
    

    q11= input("(11, Does it have a known pattern on its body or skin/fur ? (y,n)  ")
    q11=q11.lower()
    if q11=="y":
        print("Clue: Unique pattern. ")
        g1= input("Hmmm....a Zebra? (y,n)")
        if g1=="y":
            print("Yay I guessed, it! I win!")
            c1=input("Would you like to play again? (y,n) ")
            if c1=="y":
                main()
            if c1=="n":
                print("Okay cya lata loser! ")
                sys.exit()
        if g1=="n":
            print("Okay lets continue...")
    if q11=="n":
        print("Clue: Regular Shmegular ")
    
    q12= input("(12, Amphibian? (y,n)  ")
    q12=q12.lower()
    if q12=="y":
        q12=1
    if q12=="n":
        q12=0
    

    q13= input("(13, Can it camouflauge? (y,n)  ")
    q13=q13.lower()
    if q13=="y":
        print("Clue: Able to camouflauge. ")
        g1= input("Hmmm.... some type of lizard (y,n)")
        if g1=="y":
            print("Yay I guessed, it! I win!")
            c1=input("Would you like to play again? (y,n) ")
            if c1=="y":
                main()
            if c1=="n":
                print("Okay cya lata loser! ")
                sys.exit()
        if g1=="n":
            print("Okay lets continue...")
    if q13=="n":
        print("Clue: Not able to camouflauge. ")
    

    q14= input("(14, Can it be found in a zoo? (y,n)  ")
    q14=q14.lower()
    if q14=="y":
        print("Clue: Found in zoos. ")
    if q14=="n":
        print("Clue: Not in zoos. ")
   

    q15= input("(15, Is it known as non poisoness yet dangerous? (y,n)  ")
    q15=q15.lower()
    if q15=="y":
        print("Clue: Dangerrr. ")
        g1= input("Hmmm.. a Hippo? (y,n) ")
        if g1=="y":
            print("Yay I guessed, it! I win!")
            c1=input("Would you like to play again? (y,n) ")
            if c1=="y":
                main()
            if c1=="n":
                print("Okay cya lata loser! ")
                sys.exit()
        if g1=="n":
            print("Okay lets continue...")
    if q15=="n":
        print("Clue: Not dangerous")
    

    q16= input("(16, Does it growl ? (y,n)  ")
    q16=q16.lower()
    if q16=="y":
        print("Clue: Growls. ")
    if q16=="n":
        print("Clue: Does not growl")
    

    q17= input("(17, Is it known as the king of the jungle? (y,n)  ")
    q17=q17.lower()
    if q17=="y":
        print("Clue: King of the jungle! ")
        g1= input("Hmmm... a Lion? (y,n) ")
        if g1=="y":
            print("Yay I guessed, it! I win!")
            c1=input("Would you like to play again? (y,n) ")
            if c1=="y":
                main()
            if c1=="n":
                print("Okay cya lata loser! ")
                sys.exit()
        if g1=="n":
            print("Okay lets continue...")
    if q17=="n":
        print("Clue: Peasant of the jungle. ")
    

    q18= input("(18, Is it fast? (y,n)  ")
    q18=q18.lower()
    if q18=="y":
        print("Clue: SUPA SPEED. ")
        g1= input("Hmmmm... a cheetah? (y,n)")
        if g1=="y":
            print("Yay I guessed, it! I win!")
            c1=input("Would you like to play again? (y,n) ")
            if c1=="y":
                main()
            if c1=="n":
                print("Okay cya lata loser! ")
                sys.exit()
        if g1=="n":
            print("Okay lets continue...")
    if q18=="n":
        print("Clue: Slow poke ")
        g1= input("Hmmm... a Turtle? (y,n)")
        if g1=="y":
            print("Yay I guessed, it! I win!")
            c1=input("Would you like to play again? (y,n) ")
            if c1=="y":
                main()
            if c1=="n":
                print("Okay cya lata loser! ")
                sys.exit()
        if g1=="n":
            print("Okay lets continue...")

    

    q20= input("(20, Is it heavy? (y,n)  ")
    q20=q20.lower()
    if q20=="y":
        print("Clue: Heavy ")
        g1= input("Hmmm... an Elephant? (y,n)")
        if g1=="y":
            print("Yay I guessed, it! I win!")
            c1=input("Would you like to play again? (y,n) ")
            if c1=="y":
                main()
            if c1=="n":
                print("Okay cya lata loser! ")
                sys.exit()
        if g1=="n":
            print("Okay lets continue...")
    if q20=="n":
         print("Clue: Light ")
    

    q21= input("(21, Is it tall? (y,n)  ")
    q21=q21.lower()
    if q21=="y":
        print("Clue: Tall ")
        g1= input("Hmmm... a Giraffe? (y,n)")
        if g1=="y":
            print("Yay I guessed, it! I win!")
            c1=input("Would you like to play again? (y,n) ")
            if c1=="y":
                main()
            if c1=="n":
                print("Okay cya lata loser! ")
                sys.exit()
        if g1=="n":
            print("Okay lets continue...")
    if q21=="n":
         print("Clue: Short ")
    

    q22= input("(22, Does it say 'OU OU AH AH' ? (y,n)  ")
    q22=q22.lower()
    if q22=="y":
        print("Clue: Giving tarzan..bool ")
        g1= input("Hmmmm... a monkey,chimp or ape? (y,n)")
        if g1=="y":
            print("Yay I guessed, it! I win!")
            c1=input("Would you like to play again? (y,n) ")
            if c1=="y":
                main()
            if c1=="n":
                print("Okay cya lata loser! ")
                sys.exit()
        if g1=="n":
            print("Okay lets continue...")
    if q22=="n":
         print("Clue: Not a monkey")
    

    q24= input("(23, Does it have gills? (y,n)  ")
    q24=q24.lower()
    if q24=="y":
        print("Clue: Has Gills ")
        g1= input("Hmmm... a fish? (y,n)")
        if g1=="y":
            print("Yay I guessed, it! I win!")
            c1=input("Would you like to play again? (y,n) ")
            if c1=="y":
                main()
            if c1=="n":
                print("Okay cya lata loser! ")
                sys.exit()
        if g1=="n":
            print("Okay lets continue...")
    if q24=="n":
        print("Clue: No Gills ")
        print("Aww man, I could'nt guess it! I guess you winnnn!!!")
        c1=input("Would you like to play again? (y,n) ")
        if c1=="y":
            main()
        if c1=="n":
            print("Okay cya lata cheetah *rolls eye* ")
            sys.exit()
         

    
    
    
def vegetable():
    
     
    q1= input("(1, Is it green? (y,n)  ")
    #Just a starter question
    
    

    q2= input("(2, Can it be served with fillings, toppings or condiments? (y,n)  ")
    q2=q2.lower()
    if q2=="y":
        print(" ")
        g1= input("Hmmm...Potato? (y,n)")
        if g1=="y":
            print("Yay I guessed, it! I win!")
            c1=input("Would you like to play again? (y,n) ")
            if c1=="y":
                main()
            if c1=="n":
                print("Okay cya lata loser! ")
                sys.exit()
        if g1=="n":
            print("Okay lets continue...")
    if q2=="n":
        print(" ")
    
    

    q3= input("(3, Does it used to make speghetti sauce? (y,n)  ")
    q3=q3.lower()
    if q3=="y":
        print(" ")
        g1= input("Hmmm....some tomato?  (Not a veggie btw)(y,n)")
        if g1=="y":
            print("Yay I guessed, it! I win!")
            c1=input("Would you like to play again? (y,n) ")
            if c1=="y":
                main()
            if c1=="n":
                print("Okay cya lata loser! ")
                sys.exit()
        if g1=="n":
            print("Okay lets continue...")
    if q3=="n":
        print(" ")
    

    q4= input("(4, Does it make you cry? (y,n)  ")
    q4=q4.lower()
    if q4=="y":
        print(" ")
        g1= input("Hmmmm...an onion? (y,n)")
        if g1=="y":
            print("Yay I guessed, it! I win!")
            c1=input("Would you like to play again? (y,n) ")
            if c1=="y":
                main()
            if c1=="n":
                print("Okay cya lata loser! ")
                sys.exit()
        if g1=="n":
            print("Okay lets continue...")
    if q4=="n":
       print(" ")
    
    q5= input("(5, Is it said to help with vision ? (y,n)  ")
    q5=q5.lower()
    if q5=="y":
        print(" ")
        g1= input("Hmmm... a carrot? (y,n)")
        if g1=="y":
            print("Yay I guessed, it! I win!")
            c1=input("Would you like to play again? (y,n) ")
            if c1=="y":
                main()
            if c1=="n":
                print("Okay cya lata loser! ")
                sys.exit()
        if g1=="n":
            print("Okay lets continue...")
    if q5=="n":
        print(" ")
    

    q6= input("(6, Is it a common  in the US? (y,n)  ")
    q6=q6.lower()
    if q6=="y":
       print(" ")
    if q6=="n":
        print(" ")
    

    q7= input("(7, Tree like? (y,n)  ")
    q7=q7.lower()
    if q7=="y":
        print(" ")
        g1= input("Hmmmm...Broccoli? (y,n)")
        if g1=="y":
            print("Yay I guessed, it! I win!")
            c1=input("Would you like to play again? (y,n) ")
            if c1=="y":
                main()
            if c1=="n":
                print("Okay cya lata loser! ")
                sys.exit()
        if g1=="n":
            print("Okay lets continue...")
    if q7=="n":
        print(" ")
    

    q8= input("(8, Do your grandmother make it with turkey necks or gizzards? (y,n)  ")
    q8=q8.lower()
    if q8=="y":
        print(" ")
        if g1=="y":
            print("Yay I guessed, it! I win!")
            c1=input("Would you like to play again? (y,n) ")
            if c1=="y":
                main()
            if c1=="n":
                print("Okay cya lata loser! ")
                sys.exit()
        if g1=="n":
            print("Okay lets continue...")
    if q8=="n":
        print(" ")
    

    q9= input("(9, Is it yellow and when its growing, it can be used as a maze (y,n)  ")
    q9=q9.lower()
    if q9=="y":
        print(" ")
        
        if g1=="y":
            print("Yay I guessed, it! I win!")
            c1=input("Would you like to play again? (y,n) ")
            if c1=="y":
                main()
            if c1=="n":
                print("Okay cya lata loser! ")
                sys.exit()
        if g1=="n":
            print("Okay lets continue...")
    if q9=="n":
        print(" ")
        
    

    q10= input("(10, Is it tasty? (y,n)  ")
    q10=q10.lower()
    if q10=="y":
        print(" ")
        
    if q10=="n":
        print(" ")
        
    

    q11= input("(11, Did you hate it as a kid? (y,n)  ")
    q11=q11.lower()
    if q11=="y":
        print(" ")
        
        g1= input("Hmmm....Asparagus/Brussel Sprouts? (y,n)")
        if g1=="y":
            print("Yay I guessed, it! I win!")
            c1=input("Would you like to play again? (y,n) ")
            if c1=="y":
                main()
            if c1=="n":
                print("Okay cya lata loser! ")
                sys.exit()
        if g1=="n":
            print("Okay lets continue...")
    if q11=="n":
        print(" ")
        
    
    q12= input("(12, Hard to cook? (y,n)  ")
    q12=q12.lower()
    if q12=="y":
        print(" ")
        
    if q12=="n":
        print(" ")
        
    

    q13= input("(13, White? (y,n)  ")
    q13=q13.lower()
    if q13=="y":
        g1= input("Hmmm....Colliflower? (y,n)")
        if g1=="y":
            print(" ")

            print("Yay I guessed, it! I win!")
            c1=input("Would you like to play again? (y,n) ")
            if c1=="y":
                main()
            if c1=="n":
                print("Okay cya lata loser! ")
                sys.exit()
        if g1=="n":
            print("Okay lets continue...")
    if q13=="n":
        print(" ")
        
        
    

    q14= input("(14, Disgusting? (y,n)  ")
    q14=q14.lower()
    if q14=="y":
        print(" ")
        
    if q14=="n":
        print(" ")
        
   

    q15= input("(15, Could it intoxicate you? (y,n)  ")
    q15=q15.lower()
    if q15=="y":
        print(" ")
        
        g1= input("Hmmm.. Mushrooms (y,n)")
        if g1=="y":
            print("Yay I guessed, it! I win!")
            c1=input("Would you like to play again? (y,n) ")
            if c1=="y":
                main()
            if c1=="n":
                print("Okay cya lata loser! ")
                sys.exit()
        if g1=="n":
            print("Okay lets continue...")
    if q15=="n":
        print(" ")
        
    

    q16= input("(16, Does it smell bad ? (y,n)  ")
    q16=q16.lower()
    if q16=="y":
        print(" ")
        
    if q16=="n":
        print(" ")
        
    

    q17= input("(17, Pre Pickle? (y,n)  ")
    q17=q17.lower()
    if q17=="y":
        print(" ")

        g1= input("Hmmm... Cucumber? (y,n)")
        if g1=="y":
            print("Yay I guessed, it! I win!")
            c1=input("Would you like to play again? (y,n) ")
            if c1=="y":
                main()
            if c1=="n":
                print("Okay cya lata loser! ")
                sys.exit()
        if g1=="n":
            print("Okay lets continue...")
    if q17=="n":
        print(" ")
        

    q18= input("(18, Is it a metaphore ? (y,n)  ")
    q18=q18.lower()
    if q18=="y":
        print(" ")
        
        g1= input("Hmmmm... peas (y,n)")
        if g1=="y":
            print("Yay I guessed, it! I win!")
            c1=input("Would you like to play again? (y,n) ")
            if c1=="y":
                main()
            if c1=="n":
                print("Okay cya lata loser! ")
                sys.exit()
        if g1=="n":
            print("Okay lets continue...")
    if q18=="n":
        g1= input("Hmmm... a Green Beans? (y,n)")
        if g1=="y":
            print("Yay I guessed, it! I win!")
            c1=input("Would you like to play again? (y,n) ")
            if c1=="y":
                main()
            if c1=="n":
                print("Okay cya lata loser! ")
                sys.exit()
        if g1=="n":
            print(" ")
            

    

    q20= input("(20, Does it make your breath smell deadly? (y,n)  ")
    q20=q20.lower()
    if q20=="y":
        print(" ")
        
        g1= input("Hmmm... Garlic?? (y,n)")
        if g1=="y":
            print("Yay I guessed, it! I win!")
            c1=input("Would you like to play again? (y,n) ")
            if c1=="y":
                main()
            if c1=="n":
                print("Okay cya lata loser! ")
                sys.exit()
        if g1=="n":
            print("Okay lets continue...")
    if q20=="n":
        print(" ")
        

    q21= input("(21, Is it for animals ? (y,n)  ")
    q21=q21.lower()
    if q21=="y":
        print(" ")
        
        g1= input("Hmmm... a Bamboo? (y,n)")
        if g1=="y":
            print("Yay I guessed, it! I win!")
            c1=input("Would you like to play again? (y,n) ")
            if c1=="y":
                main()
            if c1=="n":
                print("Okay cya lata loser! ")
                sys.exit
        if g1=="n":
            print("Okay lets continue...")
    if q21=="n":
        print(" ")
        
    

    q22= input("(22, Slimy ? (y,n)  ")
    q22=q22.lower()
    if q22=="y":
        print(" ")

        g1= input("Hmmmm... Ocra? (y,n)")
        if g1=="y":
            print("Yay I guessed, it! I win!")
            c1=input("Would you like to play again? (y,n) ")
            if c1=="y":
                main()
            if c1=="n":
                print("Okay cya lata loser! ")
                sys.exit()
        if g1=="n":
            print("Okay lets continue...")
    if q22=="n":
        print(" ")
        

    q24= input("(23, Does it have seeds ? (y,n)  ")
    q24=q24.lower()
    if q24=="y":
        print(" ")
        
        g1= input("Hmmm... Its not a vegetable then! Did you know that? (y,n)")
        if g1=="y":
            print("Yay I guessed, it! I win!")
            c1=input("Would you like to play again? (y,n) ")
            if c1=="y":
                main()
            if c1=="n":
                print("Okay cya lata loser! ")
                sys.exit()
        if g1=="n":
            print("Okay lets continue...")
    if q24=="n":
        print(" ")
        
        print("Aww man, I could'nt guess it! I guess you winnnn!!!")
        c1=input("Would you like to play again? (y,n) ")
        if c1=="y":
            main()
        if c1=="n":
            print("Okay cya lata cheetah *rolls eye* ")
            sys.exit()
         
    
def mineral():
    
     
    q1= input("(1, Is it common in the US? (y,n)  ")
    #Just a starter question
    
    

    q2= input("(2, Does it strengthen bones? (y,n)  ")
    q2=q2.lower()
    if q2=="y":
        print(" ")
        g1= input("Hmmm... Calcium? (y,n)")
        if g1=="y":
            print("Yay I guessed, it! I win!")
            c1=input("Would you like to play again? (y,n) ")
            if c1=="y":
                main()
            if c1=="n":
                print("Okay cya lata loser! ")
                sys.exit()
        if g1=="n":
            print("Okay lets continue...")
    if q2=="n":
        print(" ")
    
    

    q3= input("(3, Does it help form bones and teeth? (y,n)  ")
    q3=q3.lower()
    if q3=="y":
        print(" ")
        g1= input("Hmmm....Phosphorus?  (Not a veggie btw)(y,n)")
        if g1=="y":
            print("Yay I guessed, it! I win!")
            c1=input("Would you like to play again? (y,n) ")
            if c1=="y":
                main()
            if c1=="n":
                print("Okay cya lata loser! ")
                sys.exit()
        if g1=="n":
            print("Okay lets continue...")
    if q3=="n":
        print(" ")
    

    q4= input("(4, Is it a type of electrolyte? (y,n)  ")
    q4=q4.lower()
    if q4=="y":
        print(" ")
        g1= input("Hmmmm...Potassium (y,n)")
        if g1=="y":
            print("Yay I guessed, it! I win!")
            c1=input("Would you like to play again? (y,n) ")
            if c1=="y":
                main()
            if c1=="n":
                print("Okay cya lata loser! ")
                sys.exit()
        if g1=="n":
            print("Okay lets continue...")
    if q4=="n":
       print(" ")
    
    q5= input("(5, chemical element with the symbol Na? (y,n)  ")
    q5=q5.lower()
    if q5=="y":
        print(" ")
        g1= input("Hmmm... Sodium? (y,n)")
        if g1=="y":
            print("Yay I guessed, it! I win!")
            c1=input("Would you like to play again? (y,n) ")
            if c1=="y":
                main()
            if c1=="n":
                print("Okay cya lata loser! ")
                sys.exit()
        if g1=="n":
            print("Okay lets continue...")
    if q5=="n":
        print(" ")
    

    q6= input("(6, Can it be liquified? (y,n)  ")
    q6=q6.lower()
    if q6=="y":
       print(" ")
    if q6=="n":
        print(" ")
    

    q7= input("(7,  a negatively charged ion that works with other electrolytes? (y,n)  ")
    q7=q7.lower()
    if q7=="y":
        print(" ")
        g1= input("Hmmmm...Chloride (y,n)")
        if g1=="y":
            print("Yay I guessed, it! I win!")
            c1=input("Would you like to play again? (y,n) ")
            if c1=="y":
                main()
            if c1=="n":
                print("Okay cya lata loser! ")
                sys.exit()
        if g1=="n":
            print("Okay lets continue...")
    if q7=="n":
        print(" ")
    

    q8= input("(8, Does it play a role in over 300 enzyme reactions in the human body? (y,n)  ")
    q8=q8.lower()
    if q8=="y":
        print(" ")
        g1= input("Is it Magnesium? ")
        if g1=="y":
            print("Yay I guessed, it! I win!")
            c1=input("Would you like to play again? (y,n) ")
            if c1=="y":
                main()
            if c1=="n":
                print("Okay cya lata loser! ")
                sys.exit()
        if g1=="n":
            print("Okay lets continue...")
    if q8=="n":
        print(" ")
    

    q9= input("(9, is it part of hemoglobin, a protein which carries oxygen from our lungs throughout our bodies.(y,n)  ")
    q9=q9.lower()
    if q9=="y":
        print(" ")
        g1= input("Is it Iron? ")
        if g1=="y":
            print("Yay I guessed, it! I win!")
            c1=input("Would you like to play again? (y,n) ")
            if c1=="y":
                main()
            if c1=="n":
                print("Okay cya lata loser! ")
                sys.exit()
        if g1=="n":
            print("Okay lets continue...")
    if q9=="n":
        print(" ")
        
    

    q10= input("(10, Is it a slightly brittle metal at room temperature and has a silvery-greyish appearance when oxidation is removed? (y,n)  ")
    q10=q10.lower()
    if q10=="y":
        print(" ")
        g1= input("Hmmm....Zinc? (y,n)")
        if g1=="y":
            print("Yay I guessed, it! I win!")
            c1=input("Would you like to play again? (y,n) ")
            if c1=="y":
                main()
            if c1=="n":
                print("Okay cya lata loser! ")
                sys.exit()
        if g1=="n":
            print("Okay lets continue...")
        
    if q10=="n":
        print(" ")
        
    

    q11= input("(11, Does the body need it but cannot make it? (y,n)  ")
    q11=q11.lower()
    if q11=="y":
        print(" ")
        
        g1= input("Hmmm....Iodine? (y,n)")
        if g1=="y":
            print("Yay I guessed, it! I win!")
            c1=input("Would you like to play again? (y,n) ")
            if c1=="y":
                main()
            if c1=="n":
                print("Okay cya lata loser! ")
                sys.exit()
        if g1=="n":
            print("Okay lets continue...")
    if q11=="n":
        print(" ")
        
    
    q12= input("(12, Is it 'rocky' ? (y,n)  ")
    q12=q12.lower()
    if q12=="y":
        print(" ")
        
    if q12=="n":
        print(" ")
        
    

    q13= input("(13, Nonmetallic chemical element belonging to the oxygen group ? (y,n)  ")
    q13=q13.lower()
    if q13=="y":
        g1= input("Hmmm....Sulfur? (y,n)")
        if g1=="y":
            print(" ")

            print("Yay I guessed, it! I win!")
            c1=input("Would you like to play again? (y,n) ")
            if c1=="y":
                main()
            if c1=="n":
                print("Okay cya lata loser! ")
                sys.exit()
        if g1=="n":
            print("Okay lets continue...")
    if q13=="n":
        print(" ")
        
        
    

    q14= input("(14, You sure its a mineral? (y,n)  ")
    q14=q14.lower()
    if q14=="y":
        print(" ")
        
    if q14=="n":
        print(" ")
        
   

    q15= input("(15,  Is it found in the Earth's crust only in a chemically combined form, save for small deposits found in alloys of natural meteoric iron. (y,n)  ")
    q15=q15.lower()
    if q15=="y":
        print(" ")
        
        g1= input("Hmmm.. Cobalt(y,n)")
        if g1=="y":
            print("Yay I guessed, it! I win!")
            c1=input("Would you like to play again? (y,n) ")
            if c1=="y":
                main()
            if c1=="n":
                print("Okay cya lata loser! ")
                sys.exit()
        if g1=="n":
            print("Okay lets continue...")
    if q15=="n":
        print(" ")
        
    

    q16= input("(16, Used to make coins ? (y,n)  ")
    q16=q16.lower()
    if q16=="y":
        print(" ")
        
    if q16=="n":
        print(" ")
        
    

    q17= input("(17, Is it a reddish, extremely ductile metal?  (y,n)  ")
    q17=q17.lower()
    if q17=="y":
        print(" ")

        g1= input("Hmmm... Copper? (y,n)")
        if g1=="y":
            print("Yay I guessed, it! I win!")
            c1=input("Would you like to play again? (y,n) ")
            if c1=="y":
                main()
            if c1=="n":
                print("Okay cya lata loser! ")
                sys.exit()
        if g1=="n":
            print("Okay lets continue...")
    if q17=="n":
        print(" ")
        

    q18= input("(18, Does it occur naturally and is released from rocks into the soil, water, and air? (y,n)  ")
    q18=q18.lower()
    if q18=="y":
        print(" ")
        
        g1= input("Hmmmm... Fluoride? (y,n)")
        if g1=="y":
            print("Yay I guessed, it! I win!")
            c1=input("Would you like to play again? (y,n) ")
            if c1=="y":
                main()
            if c1=="n":
                print("Okay cya lata loser! ")
                sys.exit()
        if g1=="n":
            print("Okay lets continue...")

    if q18=="n":
        g1= input("Hmmm... Manganese (y,n)")
        if g1=="y":
            print("Yay I guessed, it! I win!")
            c1=input("Would you like to play again? (y,n) ")
            if c1=="y":
                main()
            if c1=="n":
                print("Okay cya lata loser! ")
                sys.exit()
        if g1=="n":
            print(" ")
            

    

    q20= input("(20, Is it a nonmetal with properties that are intermediate between the elements above and below in the periodic table, sulfur and tellurium, and also has similarities to arsenic? (y,n)  ")
    q20=q20.lower()
    if q20=="y":
        print(" ")
        
        g1= input("Hmmm... Selenium? (y,n)")
        if g1=="y":
            print("Yay I guessed, it! I win!")
            c1=input("Would you like to play again? (y,n) ")
            if c1=="y":
                main()
            if c1=="n":
                print("Okay cya lata loser! ")
                sys.exit()
        if g1=="n":
            print("Okay lets continue...")
    if q20=="n":
        print(" ")
        

    q21= input("(21, Is it an essential trace mineral.? (y,n)  ")
    q21=q21.lower()
    if q21=="y":
        print(" ")
        
        g1= input("Hmmm... Molybdenum? (y,n)")
        if g1=="y":
            print("Yay I guessed, it! I win!")
            c1=input("Would you like to play again? (y,n) ")
            if c1=="y":
                main()
            if c1=="n":
                print("Okay cya lata loser! ")
                sys.exit
        if g1=="n":
            print("Okay lets continue...")
    if q21=="n":
        print(" ")
        
    

    q22= input("(22, Is it a soft, ductile, silvery-white metal that tarnishes slowly when exposed to air. (y,n)  ")
    q22=q22.lower()
    if q22=="y":
        print(" ")

        g1= input("Hmmmm... Lanthanum? (y,n)")
        if g1=="y":
            print("Yay I guessed, it! I win!")
            c1=input("Would you like to play again? (y,n) ")
            if c1=="y":
                main()
            if c1=="n":
                print("Okay cya lata loser! ")
                sys.exit()
        if g1=="n":
            print("Okay lets continue...")
    if q22=="n":
        print(" ")
        

    q24= input("(23, Is it a rare-earth element with a metallic silver luster? (y,n)  ")
    q24=q24.lower()
    if q24=="y":
        print(" ")
        
        g1= input("Hmmm... Dysprosium? (y,n)")
        if g1=="y":
            print("Yay I guessed, it! I win!")
            c1=input("Would you like to play again? (y,n) ")
            if c1=="y":
                main()
            if c1=="n":
                print("Okay cya lata loser! ")
                sys.exit()
        if g1=="n":
            print("Okay lets continue...")
    if q24=="n":
        print(" ")
        
        print("Aww man, I could'nt guess it! I guess you winnnn!!!")
        c1=input("Would you like to play again? (y,n) ")
        if c1=="y":
            main()
        if c1=="n":
            print("Okay cya lata cheetah *rolls eye* ")
            sys.exit()
         



def main():
    intro()
    menu()
    print(" ")
    print("Lets begin! ")
    category= input("Is it classified as an animal,  vegetable or Mineral? \n(Respond with A,V, or M)>> ")
    category=category.lower()
    print(" ")
    if category=="a":
        subject="Animal"
    if category=="v":
        subject="Vegetable"
    if category=="m":
        subject="Mineral"
    print("It is classified as a", subject, ".")
    if category=="a":
        animal() 
    if category=="v":
        vegetable()
    if category=="m":
        mineral()

main()