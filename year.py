import string,time

name = raw_input('Enter your name:')
print('Hi, ' + name)

age = int(input("What's your age?\n"))

times = int(raw_input("Print the no. of times:"))

curr_year = int(time.strftime("%Y"))
result = curr_year - age + 99 

outstr = ("You will turn 100 in ", result) 
while times:
	print outstr
	times = times - 1
