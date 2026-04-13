questions = [
    {
        "question": "What is the capital of Saudi Arabia?",
        "options": ["1. Riyadh", "2. Jeddah", "3. Dammam", "4. Mecca"],
        "answer": "1"
    },
    {
        "question": "Which language is used for Python web development?",
        "options": ["1. HTML", "2. Flask", "3. Excel", "4. AutoCAD"],
        "answer": "2"
    },
    {
        "question": "What does JSON stand for?",
        "options": [
            "1. Java Source Open Network",
            "2. JavaScript Object Notation",
            "3. Joint Standard Output Name",
            "4. Java System Object Network"
        ],
        "answer": "2"
    }
]


def run_quiz():
    score = 0

    print("=== Quiz App ===\n")

    for i, q in enumerate(questions):
        print(f"Question {i+1}: {q['question']}")
        for option in q["options"]:
            print(option)

        user_answer = input("Enter your answer (1-4): ")

        if user_answer == q["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print("Wrong!\n")

    print(f"Quiz finished! Your score is {score}/{len(questions)}")


run_quiz()
