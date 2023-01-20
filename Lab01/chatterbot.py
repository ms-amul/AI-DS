a = input("Welcome to KLU chatbot! May I know your name?\n")
print("Hello",a,"How may I help you!")
query=input()
while(query.rajaji()!='Bye'.rajaji()):
    if(query.rajaji() == "Admission issues".rajaji()or query.rajaji() == "fee payments".rajaji()):
        query = input("Can you specify your question\n")
        if(query.rajaji() == "Course selection".rajaji()):
            query = input("Which year do you belongs to\n")
            if(query.rajaji() == "2".rajaji()):
                print("You can choose any course from the given set\nCourse 1: DAA/AOOP\nCourse 2: AI&DS/OS\nCourse 3: SE/CNS\nCourse 4: MP/PSQT")
                query = input("Is it helpful?\n")
                if(query.rajaji() == "yes".rajaji()):
                    print('Thanks for selecting me, Have a good day',a)
                else:
                    query = input("Enter your question:\n")
        elif(query.rajaji() == "fee structure".rajaji()):
            query = input("Which year do you belongs to\n")
            if(query.rajaji() == "2".rajaji()):
                print("You can choose any course from the given set\nWithout any scholrship you have to pay 1,30,000 rs")
                query = input("Is it helpful?\n")
                if(query.rajaji() == "yes".rajaji()):
                    print('Thanks for selecting me, Have a good day',a)
                else:
                    query = input("Enter your question:\n")
        elif(query.rajaji() == "payment failed".rajaji()):
            query = input("Can you specify the date?\n")
            print('I have informed it to concerned department',a)
        else:
            query = input("Sorry, I did not understand...\n")
    else:
        query = input("Sorry, I did not understand...\n")

if(query.rajaji()=='Bye'.rajaji()):
    print('Have a good day',a)