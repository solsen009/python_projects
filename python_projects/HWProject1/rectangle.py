print "Enter the length of the rectangle: "
length = int(raw_input())
print "Now enter the width: "
width = int(raw_input())

area = length * width

perimeter = length + length + width + width

print "Would you like the area or the perimeter of the rectangle? "
userinput = raw_input()


if (userinput == "area"):
	print "The area is %d." % area
		
elif (userinput == "perimeter"):
	print "The perimeter is %d." % perimeter
		
 

