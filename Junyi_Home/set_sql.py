__author__ = 'Junyi'

user = input("Please input the user:")
passwd = input("Please input the password:")
print("set user as : " + user + ", password as : " + passwd)

file_in = open('settings.py', 'r')

line = file_in.readline()
output = ""
while line :
    if line.find('\'USER\':') >= 0:
        output = output + '\t\t\'USER\': \'' + user + " ',\n"
    elif line.find('\'PASSWORD\':') >= 0:
        output = output + '\t\t\'PASSWORD\': \'' + passwd + " ',\n"
    else:
        output += line
    line = file_in.readline()

file_in.close()
file_out = open('settings.py', 'w')
file_out.write(output)
file_out.close()