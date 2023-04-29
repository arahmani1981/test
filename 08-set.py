# DEFINE: name = {"object1", "object2", "object2", "object3"}
set = {"title", "author", "date", "subject"}
print(set)

# ADD: name.add("object") , Point: repeat is not allowed! and just ONE argument could be added.
set.add("ISBN")
print(set)

# ADD MULTIPLE ARGUMENTS: name.update([arguments]) , added argumrnts should be as LIST!
set.update([1, 2, 3, 4, 5])
print(set)

# REMOVE
set.remove("date")
print(set)
