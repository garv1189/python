import random

questions = [
    {
        "question": "What is the capital of India?",
        "options": ["New Delhi", "Berlin", "London", "Madrid"],
        "answer": "New Delhi",
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Venus", "Jupiter"],
        "answer": "Mars",
    },
    {
        "question": "What is cube of 2?",
        "options": ["3", "4", "5", "8"],
        "answer": "8",
    },
]

random.shuffle(questions)

score = 0

def quiz_game():
    global score
    for i, question in enumerate(questions, 1):
        print(f"Question {i}: {question['question']}")
        for j, option in enumerate(question["options"], 1):
            print(f"{j}. {option}")

        user_answer = input("Your answer by option name: ")
        if user_answer == question["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is {question['answer']}\n")

    print(f"Quiz completed! Your score is {score}/{len(questions)}")


# Start the game
if __name__ == "__main__":
    print("Welcome to the Python Quiz Game!\n")
    quiz_game()

