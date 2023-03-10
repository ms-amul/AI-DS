spe=["Software Modelling &DevOps","Internet Of Things","Cloud & EdgeComputing","Graphics,Gaming & UX Design","Cyber Security & BlockchainTechnology","Artificial Intelligence & Intelligence Process Automation","Data Science and BigData Analytics","Computer Communications" ]
cer=["Professional scrum Master","None","Linux Essential(101-160)","UnityDeveloper Advance Certification","ETHERIUM Developer AdvanceCertification","PCAP|CertifiedAssociatePythonProgramming","C100DEV:MongoDB certified DeveloperAssociate","None"]
print("Hello student, I am student advisor")
print("May I know your name?")
name=input()
print("Thank you", name)
print("I am here to help you explore through the specialisations offered inCSE Department of K L University.")
print("Here are the list of specialisations")
for i in range(0,8):
 print((i),".",spe[i])
print("Choose any specialisation")
ch=int(input())
print("Your courses are:")
print("Specialisation choose:",spe[ch],",","GlobalCertification:",cer[ch])
