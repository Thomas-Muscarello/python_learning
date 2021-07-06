from Question import Question

question_prompts = [
    "What color are Bananas?\n(a) Yellow\n (b) Purple\n (c) Blue",
    "What color is the Ocean?\n(a) Yellow\n (b) Purple\n (c) Blue"
    "What color combo is the American Flag?\n(a) Yellow, Red, Black\n (b) Red, White, Blue\n (c) White, Black, Green",
]

questions = [
    Question(question_prompts[0],"a"),
    Question(question_prompts[0],"c"),
    Question(question_prompts[0],"b")
]