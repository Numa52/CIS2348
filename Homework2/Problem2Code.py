#Ryan Nguyen PSID: 1805277


#PART A
#opening the inputDates.txt File
#input_file = open('C:\\Users\\nguye\\PycharmProjects\\CIS2348\\Homework2\\inputDates.txt', 'r')
#output_file = open('C:\\Users\\nguye\\PycharmProjects\\CIS2348\\Homework2\\inputDates.txt', 'w')

def find(in_date):
    #making a list of months
    #converting months to integers
    month_list={ "January":"1","February":"2", "March":"3","April":"4", "May":"5", "June":"6","July":"7", "August":"8", "September":"9","October":"10", "November":"11", "December":"12"}
    try:
        year = in_date.split(",")[-1].strip()
        month = in_date.split(",")[0].split()[0]
        day = in_date.split(",")[0].split()[-1]
        mm =  month_list[month]  # Convert month to integer
        int(year) #making sure year is a number
        int(day)  #making sure day is also a number
        return str(mm) + "/" + day + "/" + year #returning the values as a string put together
    except:
        return ""

with open('C:\\Users\\nguye\\PycharmProjects\\CIS2348\\Homework2\\inputDates.txt') as f: #Reading inputDates.txt
    for x in f.readlines():
        if x.strip() != "-1":  # Check if -1 is entered
            res = find(x.strip()) #printing result
            if res != "":  #seeing if result is valid
                with open("parsedDates.txt", "a+") as w:
                    w.write(res + "\n")  # Writes to a new file

