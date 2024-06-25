#row = int(input(""))
#for x in range(row+1): #(1,2,3,4,5)
    
#  print("*" * x)
#for x in range(): 
#while True:
#    print("")

#l = True
#while True:
#    username = input("user:")
#    password =input("pass:")
#    if username == "spiderman" and password == "bossing":
#        print("Sucess Login")
#       log = False
#  else:
#     print("Log in Failed, Try Again!"


userad = input("Enter a word to check: ")
userad = userad.lower().replace("", "")

palindrome = ""

for i in userad:
    palindrome = i + palindrome

if palindrome == userad:
    print("This is palindrome")

else:
    print("This is not palindrome")
