def run_quiz(questions):
    score = 0
    for question in questions:
        print("\n" + question["question"])
        for option in question["options"]:
            print(option)
        answer = input("Enter your answer (A, B, C, or D): ").strip().upper()
        if answer == question["answer"]:
            print(" Correct!")
            score += 1
        else:
            print(f" Wrong! The correct answer was {question['answer']}")
    print(f"\nYour final score is {score} out of {len(questions)}")


quiz_questions = [
    {
        "question": "1. What is the capital of India?",
        "options": ["A. Kolkata", "B. New Delhi", "C. Mumbai", "D. Nagpur"],
        "answer": "B"
    },
    {
        "question": "2. What is 5 + 7?",
        "options": ["A. 10", "B. 12", "C. 14", "D. 15"],
        "answer": "B"
    },
    {
        "question": "3. What is the national sport of India'?",
        "options": ["A. Foot ball", "B. Cricket", "C. Hockey", "D. Batminton"],
        "answer": "C"
    }
]

run_quiz(quiz_questions)