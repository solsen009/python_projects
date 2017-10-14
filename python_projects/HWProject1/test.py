from sys import argv

script, filename = argv

target = open(filename, 'w')

print "What is your name? ",
name = raw_input()
print "How old are you? ",
age = raw_input()
print "What month were you born? ",
birth_month = raw_input()

line = ("They call you %s, you are %s years old and were born in %s." % (name, age, birth_month))

target.write(line)

target.close()

print line