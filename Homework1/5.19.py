#Ryan Nguyen PSID: 1805277

print("Davy's auto shop services")
print("Oil change -- $35")
print("Tire rotation -- $19")
print("Car wash -- $7")
print("Car wax -- $12\n")
sum = 0

#asking user to select a service
first_service = input("Select first service:\n")
second_service = input("Select second service:\n")



#calculating price for first service
if(first_service == "Oil change"):
    first_service = first_service + ", $35"
    sum += 35
elif(first_service == "Tire rotation"):
    first_service = first_service + ", $19"
    sum += 19
elif(first_service == "Car wash"):
    first_service = first_service + ", $7"
    sum += 7
elif(first_service == "Car wax"):
    first_service = first_service + ", $12"
    sum += 12
elif(first_service == "-"):
    first_service = "No service"

#calculating price for second service
if(second_service == "Oil change"):
    second_service = second_service + ", $35"
    sum += 35
elif(second_service == "Tire rotation"):
    second_service = second_service + ", $19"
    sum += 19
elif(second_service == "Car wash"):
    second_service = second_service + ", $7"
    sum += 7
elif(second_service == "Car wax"):
    second_service = second_service + ", $12"
    sum += 12
elif(second_service == "-"):
    second_service = "No service"

#printing users selections and the total price
print("\nDavy's auto shop invoice\n")
print("Service 1:", first_service)
print("Service 2:", second_service +"\n")
print("Total: $" + str(sum))