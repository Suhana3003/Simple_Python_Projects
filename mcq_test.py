from class_mcq import Questions

question_prompts = [
    "What is the colour of banana?\n(a) Green Red\n(b) Blue\n(c) Yellow\n\n",
    "What is the colour of apple?\n(a) Red\n(b) Blue\n(c) Yellow\n\n",
    "What is the colour of grapes?\n(a) Green \n(b) red\n(c) Yellow\n\n"
]

question = [ 
    Questions(question_prompts[0], "c"),
    Questions(question_prompts[1], "a"),
    Questions(question_prompts[2], "a"),
]

def run_test(question):
    score = 0
    for questions in question:
        answer = input(questions.prompt)
        if answer == questions.answer:
            score += 1
    print("You have scored " + str(score) + " out of " + str(len(question)))

run_test(question)