from Question import Question

question_prompts = [
    "What color are Bananas?\n(a) Yellow\n(b) Purple\n(c) Blue\n\n",
    "What color is the Ocean?\n(a) Yellow\n(b) Purple\n(c) Blue\n\n",
    "What color combo is the American Flag?\n(a) Yellow, Red, Black\n (b) Red, White, Blue\n (c) White, Black, Green\n\n"
]

questions = [
    Question(question_prompts[0],"a"),
    Question(question_prompts[1],"c"),
    Question(question_prompts[2],"b")
]

def run_test(question):
    score = 0
    for question in questions:
        answer=input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got "+ str(score)+"/"+str(len(questions))+" Correct")

run_test(questions)