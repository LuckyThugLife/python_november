# 1.
# source list

student_roster = ["Emma", "Liam", "Olivia", "Noah", "Ava"]
print(student_roster)

# adding a William, Sophia student using the append method
student_roster.append("William")
student_roster.append("Sophia")
print(student_roster)

# adding a new list to the original list using the expend method
student_roster2 = ["James", "Isabella"]
student_roster.extend(student_roster2)
print(student_roster)


# 2ю
# adding Mia student to the 3rd order in the 
# list using the insert method and adding index 
# numbering in it as an attribute of the method
student_roster.insert(2, "Mia")
print(student_roster)

# deleting a Noah student using the 
# pop method and specifying the index
student_roster.pop(4)
print(student_roster)

# 3

# We count how many times the name "Emma" 
# appears in the list. using the count method
Emma = student_roster.count("Emma")
print(Emma)

# we find the index of the Ava name 
# using the Index method
iAva = student_roster.index("Ava")
print(iAva)

# 4
# deleting the last item in the list using 
# the pop method without specifying attributes
student_roster.pop()
print(student_roster)

# clearing the list of all elements using the clear method
student_roster.clear()
print(student_roster)
