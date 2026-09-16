import unittest

from main import FALLBACK, answer_question


class AnswerQuestionTests(unittest.TestCase):
    def test_answers_privacy_question(self):
        answer = answer_question("How should an AI protect personal privacy?")
        self.assertIn("Collect only what is needed", answer)

    def test_matches_case_insensitively(self):
        answer = answer_question("WHO IS ACCOUNTABLE FOR AN AI SYSTEM?")
        self.assertIn("Accountability belongs", answer)

    def test_uses_fallback_for_unknown_question(self):
        self.assertEqual(answer_question("What is the weather today?"), FALLBACK)

    def test_uses_fallback_for_empty_question(self):
        self.assertEqual(answer_question("..."), FALLBACK)


if __name__ == "__main__":
    unittest.main()
