import datetime

today_datetime = datetime.datetime.now()
print(today_datetime)

print("1. Date on week earlier:")
print("2. Date one month earlier:")

choice = int(input("enter your choice :"))

    
if choice == 1:
    result = today_datetime - datetime.timedelta(7)
    print("1 Date on week earlier:", result)
    
elif choice == 2:
    result = today_datetime - datetime.timedelta(30)
    print("2. Date one month earlier:" , result)
    
else:
    print("invalid option")