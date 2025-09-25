

orderData = {}
cont = 'y'
while cont !='n':
    print("""
    ****************Welcome TO FixTrack****************
        Enter Operation do u want to perform :
        1 : Order
        2 : Billing
    """)
    choice = int(input("enter your choice :"))
    if choice==1 :
        o_cont = 'y'
        while o_cont!='n':
            print("*********ORDER DESK**********")
            print("""
                    1 : Create new order
                    2 : View orders
                    """)
            o_choice = int(input("Enter your choice : "))
            if o_choice ==1:
                print("********Creater new Order*****")
                name = input("enter your name : ")
                device = input("Enter device name :")
                issue = input("Enter issue : ")
                date = input("Enter date : ")
                orderData.update({name:{"Device":device,"Issue":issue,"Date": date}})

            elif o_choice==2:
                print("*******Order details***********")
                for i,j in orderData.items():
                    print(f"Customer name : {i}")
                    for x,y in j.items():
                        print(f"{x} : {y}")
            else : 
                print("Invalid choice")
            o_cont = input("Do u want to contine with order ? y or n")

    elif choice==2:
        print("********BILLING DESK***********")
    else :
        print("Invalid choice")

    cont  = input("Do u want to continue ? y or n")