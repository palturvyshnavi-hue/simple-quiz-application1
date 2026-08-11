class Quiz:
    def __init__(self):
        self.questions = [
            {
                "question": "What is the capital of India?",
                "options": ["A. Mumbai", "B. Delhi", "C. Chennai", "D. Kolkata"],
                "answer": "B"
            },
            {
                "question": "Which language is used to create this application?",
                "options": ["A. Java", "B. C++", "C. Python", "D. HTML"],
                "answer": "C"
            },
            {
                "question": "How many days are there in a week?",
                "options": ["A. 5", "B. 6", "C. 7", "D. 8"],
                "answer": "C"
            },
            {
                "question": "Which planet is known as the Red Planet?",
                "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Venus"],
                "answer": "B"
            },
            {
                "question": "What is 10 + 5?",
                "options": ["A. 12", "B. 13", "C. 14", "D. 15"],
                "answer": "D"
            }
        ]

    def calculate_score(self, answers):
        score = 0

        for question, user_answer in zip(self.questions, answers):
            if user_answer.upper() == question["answer"]:
                score += 1

        return score

    def get_result(self, score):
        total = len(self.questions)
        percentage = (score / total) * 100

        if percentage >= 80:
            result = "Excellent!"
        elif percentage >= 60:
            result = "Good job!"
        elif percentage >= 40:
            result = "Keep practicing!"
        else:
            result = "Better luck next time!"

        return percentage, result

    def start_quiz(self):
        print("=" * 50)
        print("             SIMPLE QUIZ APPLICATION")
        print("=" * 50)

        print(f"\nThere are {len(self.questions)} questions.")
        print("Enter A, B, C, or D for each question.\n")

        answers = []

        for number, question in enumerate(self.questions, start=1):
            print("-" * 50)
            print(f"Question {number}: {question['question']}")

            for option in question["options"]:
                print(option)

            while True:
                answer = input("Your answer: ").strip().upper()

                if answer in ["A", "B", "C", "D"]:
                    answers.append(answer)
                    break

                print("Invalid answer. Please enter A, B, C, or D.")

        score = self.calculate_score(answers)
        percentage, result = self.get_result(score)

        print("\n" + "=" * 50)
        print("                 QUIZ RESULT")
        print("=" * 50)
        print(f"Correct Answers : {score}")
        print(f"Wrong Answers   : {len(self.questions) - score}")
        print(f"Total Questions : {len(self.questions)}")
        print(f"Score           : {percentage:.2f}%")
        print(f"Result          : {result}")
        print("=" * 50)

        print("\nThank you for playing!")


if __name__ == "__main__":
    quiz = Quiz()
    quiz.start_quiz()