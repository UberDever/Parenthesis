import unittest
from program import ParenthesisVerifier

class TestParenthesisVerifier(unittest.TestCase):

    def setUp(self):
        self.verifier = ParenthesisVerifier()
        
    def test_verify_empty_string_return_false(self):
        self.assertFalse(self.verifier.verify(""))

    def test_verify_string_len_is_odd_return_false(self):
        self.assertFalse(self.verifier.verify("{}["))
        self.assertFalse(self.verifier.verify("{sd}_+["))
        self.assertFalse(self.verifier.verify("{}ge12["))
        self.assertFalse(self.verifier.verify("{}[4444"))
        
    def test_verify_contains_incorrect_symbols_return_false(self):
        self.assertFalse(self.verifier.verify("{}[]_+"))
        self.assertFalse(self.verifier.verify("{(abcd[])}"))
        self.assertFalse(self.verifier.verify("array[0]"))

    def test_verify_closed_came_before_opened_return_false(self):
        self.assertFalse(self.verifier.verify("]{}()"))
        self.assertFalse(self.verifier.verify("{}{}}"))
        self.assertFalse(self.verifier.verify("{)"))

    def test_verify_opened_count_not_match_with_closed_count_return_false(self):
        self.assertFalse(self.verifier.verify("{}(()]"))
        self.assertFalse(self.verifier.verify("]]]]]"))
        self.assertFalse(self.verifier.verify("{{([]))}}"))

    def test_verify_correct_examples_return_true(self):
        self.assertTrue(self.verifier.verify("{}"))
        self.assertTrue(self.verifier.verify("{[()]}"))
        self.assertTrue(self.verifier.verify("{}[][][][]()(){{{[]}}}"))

    # Given examples
    def test_verify_correct_return_true(self):
        self.assertTrue(self.verifier.verify("([])"))

    def test_verify_incorrect_return_false(self):
        self.assertFalse(self.verifier.verify("{[(]}"))

if __name__ == '__main__':
    unittest.main()