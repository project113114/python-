# author aman , ashish
import turtle 
import colorama 
from colorama import Fore, Back , Style
colorama.init(autoreset = True)

# has to use later 
def upcomming():
  object = turtle.Turtle()
  object.forward(200)
  object.pencolor("red")

# main for now 

print(f"{Fore.RED}ashish patel and aman choudhary")

logo_project = """

██████╗░██╗░░░██╗████████╗██╗░░██╗░█████╗░███╗░░██╗  ██████╗░██████╗░░█████╗░░░░░░██╗███████╗░█████╗░████████╗
██╔══██╗╚██╗░██╔╝╚══██╔══╝██║░░██║██╔══██╗████╗░██║  ██╔══██╗██╔══██╗██╔══██╗░░░░░██║██╔════╝██╔══██╗╚══██╔══╝
██████╔╝░╚████╔╝░░░░██║░░░███████║██║░░██║██╔██╗██║  ██████╔╝██████╔╝██║░░██║░░░░░██║█████╗░░██║░░╚═╝░░░██║░░░
██╔═══╝░░░╚██╔╝░░░░░██║░░░██╔══██║██║░░██║██║╚████║  ██╔═══╝░██╔══██╗██║░░██║██╗░░██║██╔══╝░░██║░░██╗░░░██║░░░
██║░░░░░░░░██║░░░░░░██║░░░██║░░██║╚█████╔╝██║░╚███║  ██║░░░░░██║░░██║╚█████╔╝╚█████╔╝███████╗╚█████╔╝░░░██║░░░
╚═╝░░░░░░░░╚═╝░░░░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░╚═╝░░╚══╝  ╚═╝░░░░░╚═╝░░╚═╝░╚════╝░░╚════╝░╚══════╝░╚════╝░░░░╚═╝░░░
"""

logo_py="""

██████╗░██╗░░░██╗████████╗██╗░░██╗░█████╗░███╗░░██╗
██╔══██╗╚██╗░██╔╝╚══██╔══╝██║░░██║██╔══██╗████╗░██║
██████╔╝░╚████╔╝░░░░██║░░░███████║██║░░██║██╔██╗██║
██╔═══╝░░░╚██╔╝░░░░░██║░░░██╔══██║██║░░██║██║╚████║
██║░░░░░░░░██║░░░░░░██║░░░██║░░██║╚█████╔╝██║░╚███║
╚═╝░░░░░░░░╚═╝░░░░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░╚═╝░░╚══╝
"""
print(logo_project)

# some options for opration 
print(f"{Fore.RED}OPTIONS"+ f"{Fore.GREEN} for oprations ")
#option 
print("1 "+f"{Fore.RED}Custom sms service ")
op = int(input("choose option :"))

# Download the helper library from https://www.twilio.com/docs/python/install



from twilio.rest import Client 
 
#function of message
def ma():
  account_sid ='ACdb26d19a478a3dfef65fbe4b0bb42f68'
  auth_token ='e99c7212ea1250bf71be657923a9eb2c'
  client = Client(account_sid, auth_token)

  message = client.messages.create(
                       body=m,
                       from_='+19793416442',
                       to='+91'+x
                 )
  print(message.sid)

  
                                    
                               
                        
 
 
 

 
if(op == 1):
  print(f"{Fore.GREEN}default country code +91")
  x = input(f"{Fore.BLUE}enter number : ")
  m = input(f"{Fore.GREEN}enter message :")
  multi = int(input(f"{Fore.RED}enter nnumber of time to send message :"))
  for i in range(multi):
    ma()
else:
  print("enter vailid number ")







