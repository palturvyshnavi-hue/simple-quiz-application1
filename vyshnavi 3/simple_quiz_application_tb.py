import unittest
from simple_quiz_application import Quiz


class TestQuiz(unittest.TestCase):

    def setUp(self):
        self.quiz = Quiz()

    def test_number_of_questions(self):
        self.assertEqual(len(self.quiz.questions), 5)

    def test_all_correct_answers(self):
        answers = ["B", "C", "C", "B", "D"]

        score = self.quiz.calculate_score(answers)

        self.assertEqual(score, 5)

    def test_all_wrong_answers(self):
        answers = ["A", "A", "A", "A", "A"]

        score = self.quiz.calculate_score(answers)

        self.assertEqual(score, 0)

    def test_partial_score(self):
        answers = ["B", "A", "C", "A", "D"]

        score = self.quiz.calculate_score(answers)

        self.assertEqual(score, 3)

    def test_lowercase_answers(self):
        answers = ["b", "c", "c", "b", "d"]

        score = self.quiz.calculate_score(answers)

        self.assertEqual(score, 5)

    def test_percentage(self):
        percentage, result = self.quiz.get_result(4)

        self.assertEqual(percentage, 80.0)
        self.assertEqual(result, "Excellent!")

    def test_good_result(self):
        percentage, result = self.quiz.get_result(3)

        self.assertEqual(percentage, 60.0)
        self.assertEqual(result, "Good job!")


if __name__ == "__main__":
    unittest.main(verbosity=2)