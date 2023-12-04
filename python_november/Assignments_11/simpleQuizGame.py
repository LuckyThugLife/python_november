# list of question
questions = {
    "What color is the sky?": "blue",
    "What is 2 + 2?": "4",
    "Which month comes after April?": "May",
    "How many days are there in a week?": "7",
    "What is the capital of the United States?": "Washington D.C."
}

# assign 0 to a variable
score = 0

# Ask the questions and check the answers
for question, answer in questions.items():
    user_answer = input(question + " ")
    if user_answer == answer:
        print("Correct!")
        score += 1
    else:
        print("Incorrect.")

# Show the final score
print("You got", score, "out of", len(questions), "questions correct.")