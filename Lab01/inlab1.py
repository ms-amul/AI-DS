print('Hi I am Student Advisor Chat Bot')
name = input("May I Know your Name")

print("Hello", name)
print(
    'I am here to explore you about the core courses required for the specialization offered in KL University,'
    'CSE Department')
print('Here are the specializations offered by KL University,CSE Department ')
print('1.Software Modelling & Devops')
print('2.Internet of Things')
print('3.Graphics,Gaming & UX Design')
print('4.Cyber Security & BlockChain Technology')
print('5.Data Science & Big Data Analytics')
print('6.Artificial Intelligence & Intelligence Process automation')
print('7.Cloud and Edge Computing')
print('8.Computer Communications')
print('9.Exit')
while True:
    opt = input('Choose Any Option ')
    if opt == '1':
        print(
            'Global Certification: PCAP|Certified associate in python programming , Core Course in this Sem : Software '
            'Engineering')
    elif opt == '2':
        print('Global Certification: PCAP|Certified associate in python programming , Core Course in this Sem : ')
    elif opt == '3':
        print('Global Certification: PCAP|Certified associate in python programming , Core Course in this Sem : '
              'Engineering Graphice')
    elif opt == '4':
        print(
            'Global Certification: PCAP|Certified associate in python programming , Core Course in this Sem : Computer '
            'Networks & Security')
    elif opt == '5':
        print('Global Certification: PCAP|Certified associate in python programming , Core Course in this Sem : '
              'Artificial Intellegence & Data Science')
    elif opt == '6':
        print('Global Certification: PCAP|Certified associate in python programming , Core Course in this Sem : '
              'Artificial Intellegence & Data Science')
    elif opt == '7':
        print(
            'Global Certification: PCAP|Certified associate in python programming , Core Course in this Sem : '
            'Operating '
            'System')
    elif opt == '8':
        print(
            'Global Certification: PCAP|Certified associate in python programming , Core Course in this Sem : Computer '
            'Organization & ARchitecture')
    elif opt == '9':
        print('Exit.........')
        exit(0)
    else:
        print('ENTER CORRECT CHOICE!')


