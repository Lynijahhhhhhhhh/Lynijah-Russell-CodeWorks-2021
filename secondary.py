import sys
def intro():
    print("20 Questions by Lynijah Russell...\nAKA the better 20Q")

def menu():
    print(" ")
    print("The key words: ")
    print("(Y- yes)")
    print("(N- no)")
    print("(T- Thats it, you guessed it!)")


def animal():
    response=[]
    q1= input("(1, Can you buy it? (y,n)  ")
    q1=q1.lower()
    if q1=="y":
        q1=1
    if q1=="n":
        q1=0
    response.append(q1)

    q2= input("(2, Does it bark? (y,n)  ")
    q2=q2.lower()
    if q2=="y":
        q2=1
    if q2=="n":
        q2=0
    response.append(q2)

    q3= input("(3, Does it Meow? (y,n)  ")
    q3=q3.lower()
    if q3=="y":
        q3=1
    if q3=="n":
        q3=0
    response.append(q3)

    q4= input("(4, Does it hiss? (y,n)  ")
    q4=q4.lower()
    if q4=="y":
        q4=1
    if q4=="n":
        q4=0
    response.append(q4)

    q5= input("(5, Does it 'ribbit' ? (y,n)  ")
    q5=q5.lower()
    if q5=="y":
        q5=1
    if q5=="n":
        q5=0
    response.append(q5)

    q6= input("(6, Is it a common pet in the US? (y,n)  ")
    q6=q6.lower()
    if q6=="y":
        q6=1
    if q6=="n":
        q6=0
    response.append(q6)

    q7= input("(7, it Swim? (y,n)  ")
    q7=q7.lower()
    if q7=="y":
        q7=1
    if q7=="n":
        q7=0
    response.append(q7)

    q8= input("(8 Can it fly? (y,n)  ")
    q8=q8.lower()
    if q8=="y":
        q8=1
    if q8=="n":
        q8=0
    response.append(q8)

    q9= input("(9, Does it repeat things you say? (y,n)  ")
    q9=q9.lower()
    if q9=="y":
        q9=1
    if q9=="n":
        q9=0
    response.append(q9)

    q10= input("(10, Is it colorful? (y,n)  ")
    q10=q10.lower()
    if q10=="y":
        q10=1
    if q10=="n":
        q10=0
    response.append(q10)

    q11= input("(11, Does it have a known pattern on its body of skin/fur ? (y,n)  ")
    q11=q11.lower()
    if q11=="y":
        q11=1
    if q11=="n":
        q11=0
    response.append(q11)

    q12= input("(12, Can they survive in the desert? (y,n)  ")
    q12=q12.lower()
    if q12=="y":
        q12=1
    if q12=="n":
        q12=0
    response.append(q12)

    q13= input("(13, Can it camouflauge? (y,n)  ")
    q13=q13.lower()
    if q13=="y":
        q13=1
    if q13=="n":
        q13=0
    response.append(q13)

    q14= input("(14, Can it be found in a zoo? (y,n)  ")
    q14=q14.lower()
    if q14=="y":
        q14=1
    if q14=="n":
        q14=0
    response.append(q14)

    q15= input("(15, Is it known as non poisoness yet dangerous? (y,n)  ")
    q15=q15.lower()
    if q15=="y":
        q15=1
    if q15=="n":
        q15=0
    response.append(q15)

    q16= input("(16, Does it growl ? (y,n)  ")
    q16=q16.lower()
    if q16=="y":
        q16=1
    if q16=="n":
        q16=0
    response.append(q16)

    q17= input("(17, Is it known as the king of the jungle? (y,n)  ")
    q17=q17.lower()
    if q17=="y":
        q17=1
    if q17=="n":
        q17=0
    response.append(q17)

    q18= input("(18, Is it fast? (y,n)  ")
    q18=q18.lower()
    if q18=="y":
        q18=1
    if q18=="n":
        q18=0
    response.append(q18)

    q19= input("(19, Is it slow? (y,n)  ")
    q19=q19.lower()
    if q19=="y":
        q19=1
    if q19=="n":
        q19=0
    response.append(q19)

    q20= input("(20, Is it heavy? (y,n)  ")
    q20=q20.lower()
    if q20=="y":
        q20=1
    if q20=="n":
        q20=0
    response.append(q20)

    q21= input("(21, Is it tall? (y,n)  ")
    q21=q21.lower()
    if q21=="y":
        q21=1
    if q21=="n":
        q21=0
    response.append(q21)

    q22= input("(22, Does it say 'OU OU AH AH' ? (y,n)  ")
    q22=q22.lower()
    if q22=="y":
        q22=1
    if q22=="n":
        q22=0
    response.append(q22)

    q23= input("(23, Does it have a blue toungue? (y,n)  ")
    q23=q23.lower()
    if q23=="y":
        q23=1
    if q23=="n":
        q23=0
    response.append(q23)

    q24= input("(24, Does it have gills? (y,n)  ")
    q24=q24.lower()
    if q24=="y":
        q24=1
    if q24=="n":
        q24=0
    response.append(q24)

    print(response)
    return response
    
def animalList():
    dog=[1,1,0,0,0,1,1,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0]
    cat=[1,0,1,1,0,1,0,0,0,0,0,0,0,1,1,1,1,1,0,1,0,0,0,0]
    fish=[1,0,0,0,0,1,1,0,0,1,1,0,0,0,0,0,0,0,1,0,0,0,0,1]
    bird=[1,0,0,0,0,1,0,1,1,1,0,0,0,1,0,0,0,1,0,0,0,0,0,0]
    elephant=[0,0,0,0,0,0,1,0,0,0,0,1,0,1,0,0,0,0,1,1,0,0,0,0]
    girrafe=[0,0,0,0,0,0,0,0,0,1,1,0,1,0,0,0,0,1,1,1,0,1,0]
    lizard=[1,0,0,1,0,1,1,0,0,1,1,1,1,0,1,0,0,0,1,0,0,0,0,0]
    return dog,cat,fish,bird,elephant,girrafe,lizard

def hammingD(response,dog,cat,fish,bird,elephant,girrafe,lizard ):
    i = 0
    count = 0
 
    while(len(response) == len(dog)):
        if(str1[i] != str2[i]):
            count += 1
        i += 1
        print(count)

    while(len(response) == len(cat)):
        if(str1[i] != str2[i]):
            count += 1
        i += 1
        print(count)
    while(len(response) == len(fish)):
        if(str1[i] != str2[i]):
            count += 1
        i += 1
        print(count)
    while(len(response) == len(bird)):
        if(str1[i] != str2[i]):
            count += 1
        i += 1
        print(count)
    while(len(response) == len(elephant)):
        if(str1[i] != str2[i]):
            count += 1
        i += 1
        print(count)
    while(len(response) == len(girrafe)):
        if(str1[i] != str2[i]):
            count += 1
        i += 1
        print(count)

    while(len(response) == len(lizzard)):
        if(str1[i] != str2[i]):
            count += 1
        i += 1
        print(count)





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
        vegatable()
    if category=="m":
        mineral()

    hammingD(response,dog,cat,fish,bird,elephant,girrafe,lizard )
main()