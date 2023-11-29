# declaring variables age and grade
grade =87
age = 19

# setting evaluation criteria using logical operators
if grade == 90:
  print("Congratulations! You've earned a full scholarship to the Science Academy!")
elif grade >= 80 and grade < 90:
  print( "You qualify for admission to the Science Academy.")
elif grade < 80:
  print( "Unfortunately, your grades don't meet the requirements for admission.")

#setting age criteria using logical operators
if age == 18:
  print("You are just old enough to apply for the Science Academy!")
elif age < 18 and grade < 90:
  print( "You qualify for admission to the Science Academy.")
elif age > 18:
  print(  "You've surpassed the eligible age to apply for the Science Academy.")
