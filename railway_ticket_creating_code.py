#railway reservation code.
def data_enter(n):
    print("*"*10)
    print()
    for i in range(n):
        pnr=input("Enter the passenger id number: ")
        name=input("Enter the name of the passenger: ")
        age=input("Enter the sex of the passenger: ")
        sourse=input("Enter the source of the passenger: ")
        des=input("enter the destination of the passenger: ")
        fare=int(input("enter the fare of the passenger: "))
        temp=[pnr, name, age, sourse, des, fare]
        main.append(temp)
        print("-"*10,"your ticket is booked...")
    print()
    print("all passengers: ",main)
    print("--"*10)
#searching the source and the destination of the passenger.
def search_data(ask):
    if ask in'yY':
        passg_name=input("enter the name of the passenger u want to search: ")
        found=False
        for name in main:
            if name[1]==passg_name:
                print("id of the passenger: ",name[0])
                print("name of the passenger: ",name[1])
                print("sex of the passenger: ",name[2])
                print("sourse of the passenger is: ",name[3])
                print("destination of the passenger is:",name[4])
                print("fair of the passenger is:",name[5])
                found=True
                break
        if not found:
            print("the passenger doesn't found")
        print("--"*10)  
        print()
#find out which passenger paid the hight fair.
def serch_data(askhighstfair):
    if askhighstfair in'yY':
        if not main:
            print("NO passenger is available")
            return
        highest_p=main[0]
        for name in main:
            if int(name[5])>int(highest_p[5]):
                highest_p=name
        print("id of the passenger: ",name[0])
        print("name of the passenger: ",name[1])
        print("sex of the passenger: ",name[2])
        print("sourse of the passenger is: ",name[3])
        print("destination of the passenger is:",name[4])
        print("fair of the passenger is:",name[5])
        print("the highest value fair is: ",highest_p)
        print("--"*10)
        print()
#claculate the average fair.
def average_fair(avgfair):
    if avgfair in'yY':
        sum=0
        count=0
        for fair in main:
            count+=1
            sum+=int(fair[5])
        avg_fair=sum/count
        print("entered average fair of the total passengers ticket is: ",avg_fair)
        print("--"*10)
#ticket display.
line_single = "+" + "-" * 85 + "+"
line_double = "+" + "=" * 85 + "+"
def print_row(text, align="left"):
    if align == "center":
        print(f"| {text.center(72)} |")
    else:
        print(f"| {text.ljust(72)} |")

# Displaying the e-ticket
def my_ticket():
    for i in range(len(main)):
        print(line_double)
        print_row("INDIAN RAILWAYS E-TICKET", align="center")
        print(line_double)
        print_row(f"PNR NUMBER: {str(main[i][0]).ljust(35)} | BOOKING TIME: 2026-09-23 19:14:53")
        print(line_double)
        print_row(f"TRAIN: 12424 - Rajdhani Express".ljust(35) + f"| CLASS: AC 3 TIER")
        print_row(f"FROM: {str(main[i][3]).ljust(35)} | TO:  {str(main[i][4])}")
        print(line_double)
        print_row("PASSENGER DETAILS:")
        print_row(f"Name: {str(main[i][1]).ljust(35)} | Age/Sex: {str(main[i][2])}")
        print(line_double)
        print_row("STATUS: CONFIRMED")
        print_row("COACH: A5".ljust(20) + "| SEAT: 5".ljust(36) + f"| PRICE : {str(main[i][5]).ljust(35)}")
        print(line_double)
        print_row("*** WISHING YOU A SAFE AND HAPPY JOURNEY ***", align="center")
        print(line_double)

        print()
        print()

# main programe.

main=[]           
n=int(input("Enter the number of passengers: "))
data_enter(n)
                  
ask=input("Do you want to search for any passenger source and destination then type Y if not type N : ")
search_data(ask)
                      
askhighstfair=input("are you want to search for any passenger who pay the highest fair then type Y if not type N : ")
serch_data(askhighstfair)
                
avgfair=input("DO you wanna to find the average fair then type Y if not type N : ")
average_fair(avgfair)
                 
a=0
while a<1:
    re_ask=input("Do you want to enter more data ?If yes then type 'Y' or'y'.If not then type n or N: ")
    if re_ask in'yY':
        v=1
        data_enter(v)
    else:
        print("ThanYou Over!!")
        break
    a-=1
        
print("Do you want ticket now !! then,")
ticket=input("Enter y/Y if you want to print the ticket for the pessenger. else type n/N")
if ticket in "yY":
    my_ticket()
