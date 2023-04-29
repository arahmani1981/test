# MULTIPLE LINES

# msg = """python
# programming
# files"""
# print(msg)

msg = "python \nprogramming \nfiles"

# strings are array chrcs
#           print(msg[4]): Will show 4th charc of the string

# Slicing:
#           print(msg[m:n]) will show m to n-1 of string
#           print(msg[m:]) will show m to the end of string
#           print(msg[:n]) will show from the start to n-1 of the string
#           print(msg[-m:-n]): az m-ta mande be akhar ta n-ta mande be akhar
#           print(msg[:-n]): whole string - last n characters
#           print(msg[-m:]): will show last m characters
# print(msg[-5:-2])

# LEN : will show count of charcs of the string
# print(len(msg))

print(msg.upper())
print(msg.lower())
print(msg.strip())
print(msg.replace("p", "X"))
print(msg.split(" "))
# CONCAT
print(msg + " files")

# FORMAT
# name = "Ahmad"
# age = 40
# msg = "man {} hastam va {} saalam shode"
# print(msg.format(name, age))

# TO ADD VALUES INSIDE THE STRING: %
name = "Ahmad"
age = 40
print("man %s hastam va %i saalam shode" % (name, age))
