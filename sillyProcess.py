# This first line opens the file with the data
log_file = open("silly-server-01.txt")

# This function is a called sales_reports. The "def" will "define" the function. 
def sales_reports(log_file):
# For loop, that goes through every line of the file      
for line in log_file:
# it removes the white-space at the end of each line and resaves the line as the same variable as a string. 
        line = line.rstrip()
# defines a variable 'day' equal to first three charecters
        day = line[0:3]
# If the first three characters is "Mon" it will print the string
        if day == "Mon":
        print(line)

# calls the function
sales_reports(log_file)