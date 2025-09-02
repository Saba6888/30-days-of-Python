# Simple Quiz Application

def quiz():
    # List of questions with options and correct answers
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"],
            "answer": "C"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Venus"],
            "answer": "B"
        },
        {
            "question": "Who wrote 'To Kill a Mockingbird'?",
            "options": ["A. Harper Lee", "B. J.K. Rowling", "C. Ernest Hemingway", "D. Mark Twain"],
            "answer": "A"
        }
    ]

    # Initialize score
    score = 0

    # Loop through each question
    for i, q in enumerate(questions, start=1):
        print(f"\nQuestion {i}: {q['question']}")
        for option in q["options"]:
            print(option)

        # Get user's answer
        answer = input("Your answer (A, B, C, or D): ").strip().upper()

        # Check if the answer is correct
        if answer == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The correct answer is {q['answer']}.")

    # Show final score
    print(f"\nYou scored {score} out of {len(questions)}.")

# Run the quiz
quiz()
