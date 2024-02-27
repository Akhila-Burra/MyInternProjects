class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def display_question(self, question):
        print(question['question'])
        for i, option in enumerate(question['options'], 1):
            print(f"{i}. {option}")
    
    def check_answer(self, question, answer):
        if answer.lower() == question['answer'].lower():
            print("Correct!")
            self.score += 1
        else:
            print("Incorrect!")
            print(f"The correct answer is: {question['answer']}")
        print()
    
    def run_quiz(self):
        print("Welcome to the Quiz!\n")
        for question in self.questions:
            self.display_question(question)
            user_answer = input("Enter your answer (1, 2, 3, etc.): ")
            while not user_answer.isdigit() or int(user_answer) not in range(1, len(question['options']) + 1):
                user_answer = input("Invalid input. Please enter a number corresponding to your choice: ")
            self.check_answer(question, question['options'][int(user_answer) - 1])
        print(f"Quiz completed! Your final score is: {self.score}/{len(self.questions)}")

# Example usage
questions = [
    {
        'question': "What is the capital of France?",
        'options': ["Paris", "London", "Berlin"],
        'answer': "Paris"
    },
    {
        'question': "What is the largest planet in our solar system?",
        'options': ["Jupiter", "Saturn", "Neptune"],
        'answer': "Jupiter"
    },
    {
        'question': "Who wrote 'Romeo and Juliet'?",
        'options': ["William Shakespeare", "Charles Dickens", "Jane Austen"],
        'answer': "William Shakespeare"
    }
]

quiz = Quiz(questions)
quiz.run_quiz()