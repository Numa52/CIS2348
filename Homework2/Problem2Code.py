#Ryan Nguyen PSID: 1805277


#PART A
#opening the inputDates.txt File
#input_file = open('C:\\Users\\nguye\\PycharmProjects\\CIS2348\\Homework2\\inputDates.txt', 'r')
#output_file = open('C:\\Users\\nguye\\PycharmProjects\\CIS2348\\Homework2\\inputDates.txt', 'w')

def find(in_date):
    #making a list of months
    #converting months to integers
    month_list={ "January":"1","February":"2", "March":"3","April":"4", "May":"5", "June":"6","July":"7", "August":"8", "September":"9","October":"10", "November":"11", "December":"12"}
    year = in_date.split(",")[-1].strip()
    month = in_date.split(",")[0].split()[0]
    day = in_date.split(",")[0].split()[-1]
    mm =  month_list[month]  # Convert month to integer
    return str(mm) + "/" + day + "/" + year

while True: #infinite loop
   inp = input() #take input from user
   if inp == "-1": #Check if input is -1
      break #Breaks out of the loop
   print(find(inp)) #Function call