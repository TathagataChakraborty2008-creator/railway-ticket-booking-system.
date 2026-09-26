# fare of the passenger.
def fare_cost(com):
    if com =="general" :
        return 2500
    elif com =="AC 1 TIER":
        return 3200
    elif com =="AC 2 TIER":
        return 3500
    elif com =="AC 3 TIER":
        return 3700
    else:
        print("enter the corrct compartment ")
        return 0
#railway reservation code.
def data_enter(n):
    print("*"*10)
    print()
    for i in range(n):
        pnr=input("Enter the passenger id number: ")
        name=input("Enter the name of the passenger: ")
        sex=input("Enter the sex of the passenger: ")
        print("Available compartments are: general / AC 1 TIER / AC 2 TIER / AC 3 TIER ")
        com=input("Enter which compartment you want: ")
        sourse=input("Enter the source of the passenger: ")
        des=input("Enter the destination of the passenger: ")
        fare=fare_cost(com)
        temp=[pnr, name, sex, com, sourse, des, fare]
        main.append(temp)
        print("-"*10,"Your Ticket Is Booked...")
    print()
    print("all passengers: ",main)
    print("--"*10)
#searching the source and the destination of the passenger.
def search_data(ask):
    if ask in'yY':
        passg_name=input("enter the passenger_id of the passenger you want to search: ")
        found=False
        for name in main:
            if name[0]==passg_name:
                print("id of the passenger: ",name[0])
                print("name of the passenger: ",name[1])
                print("sex of the passenger: ",name[2])
                print("compartment of the passenger: ",name[3])
                print("sourse of the passenger is: ",name[4])
                print("destination of the passenger is:",name[5])
                found=True
                break
        if not found:
            print("the passenger doesn't found")
    else:
        pass
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
            if int(name[6]) > int(highest_p[6]):
                highest_p=name
        print("id of the passenger: ",name[0])
        print("name of the passenger: ",name[1])
        print("sex of the passenger: ",name[2])
        print("compartment of the passenger: ",name[3])
        print("sourse of the passenger is: ",name[4])
        print("destination of the passenger is:",name[5])
        print("fair of the passenger is:",name[6])
    print("--"*10)  
    print()
#claculate the average fair.
def average_fair(avgfair):
    if avgfair.lower() =='y':
        if not main:
            print("NO passenger is available")
            return
        sum=0
        count=0
        for fair in main:
            count+=1
            sum+=int(fair[6])
        avg_fair=sum/count
        print("entered average fair of the total passengers ticket is: ",avg_fair)
        print("--"*10)  
        print()
    else:
        pass
#ticket display.
line_single = "+" + "-" * 85 + "+"
line_double = "+" + "=" * 85 + "+"
def print_row(text, align="left"):
    if align == "center":
        print(f"| {text.center(85)} |")
    else:
        print(f"| {text.ljust(85)} |")

# Displaying the e-ticket
def my_ticket():
    for i in range(len(main)):
        print(line_double)
        print_row("INDIAN RAILWAYS E-TICKET", align="center")
        print(line_double)
        print_row(f"PNR NUMBER: {str(main[i][0]).ljust(35)} | BOOKING TIME: 2026-09-23 19:14:53")
        print(line_double)
        print_row(f"TRAIN: 12424 - Rajdhani Express".ljust(35) + f"| CLASS: {str(main[i][3]).ljust(35)}")
        print_row(f"FROM: {str(main[i][4]).ljust(35)} | TO:  {str(main[i][5])}")
        print(line_double)
        print_row("PASSENGER DETAILS:")
        print_row(f"Name: {str(main[i][1]).ljust(35)} | Age/Sex: {str(main[i][2])}")
        print(line_double)
        print_row("STATUS: CONFIRMED")
        print_row("COACH: A5".ljust(20) + "| SEAT: 5".ljust(36) + f"| PRICE : {str(main[i][6]).ljust(10)}")
        print(line_double)
        print_row("*** WISHING YOU A SAFE AND HAPPY JOURNEY ***", align="center")
        print(line_double)

        print()
        print()
        
#ticket cancellation.
def cancelticket(z):
    found = False
    for ticket in main:
        if ticket[0] == z:
            main.remove(ticket) 
            print("This ticket has been deleted successfully.")
            found = True
            break  
            
    if not found:
        print("No ticket found with that Passenger ID.")
    print("-" * 10)
    print()
    print("new ticket are ")
    print()
    my_ticket()
            

# main programe.

print("***Welcome To Railway Ticket Booking Code***")
print()
main=[]           
n=int(input("Enter the number of passengers for booking ticket: "))
data_enter(n)
                  
ask=input("Do you want to search for any passenger source and destination then type Y if not type N : ")
search_data(ask)
                      
askhighstfair=input("are you want to search for any passenger who pay the highest fair then type Y if not type N : ")
serch_data(askhighstfair)
                
avgfair=input("Do you wanna to find the average fair then type Y if not type N : ")
average_fair(avgfair)
                 
a=0
while a<1:
    re_ask=input("Do you want to enter more data ?If yes then type 'Y' or'y'.If not then type n or N: ")
    if re_ask in'yY':
        v=1
        data_enter(v)
    else:
        break
    a-=1
        
print("-"*10)
print()
print("Do you want ticket now !! then,")
ticket=input("Enter y/Y if you want to print the ticket for the pessenger. else type n/N")
if ticket in "yY":
    my_ticket()

remove_ticket=input("Do you want to cancel you ticket?If yes then type 'Y' or'y'.If not then type 'n' or 'N': ")
if remove_ticket in'yY':
    z=input("enter the passenger id of the passenger that you want to cancel the ticket:-")
    cancelticket(z)
    print("ThanYou Over!!")
