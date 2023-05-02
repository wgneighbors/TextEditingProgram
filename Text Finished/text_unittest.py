import unittest
from text import import_file, TextStats, TextEdit, TextCompare

class TestTextImport(unittest.TestCase):

    def test_import_file(self):
        text = import_file("test.txt")
        self.assertEqual(text, "Testing... Testing... Testing...")

    def test_import_nonexistent_file(self):
        with self.assertRaises(FileNotFoundError):
            import_file("nonexistent_file.txt")

    def test_import_empty_file(self):
        with open("empty.txt", "w") as f:
            f.write("")
        text = import_file("empty.txt")
        self.assertEqual(text, "")

class TestTextStats(unittest.TestCase):

    def test_word_count(self):
        text_stats = TextStats("This is a test file.")
        self.assertEqual(text_stats.word_count(), 5)

    def test_word_count_empty_string(self):
        text_stats = TextStats("")
        self.assertEqual(text_stats.word_count(), 0)

    def test_character_count(self):
        text_stats = TextStats("This is a test file.")
        self.assertEqual(text_stats.character_count(), 20)

    def test_character_count_empty_string(self):
        text_stats = TextStats("")
        self.assertEqual(text_stats.character_count(), 0)

    def test_sentence_count(self):
        text_stats = TextStats("This is a test file. It contains two sentences!")
        self.assertEqual(text_stats.sentence_count(), 2)

    def test_sentence_count_empty_string(self):
        text_stats = TextStats("")
        self.assertEqual(text_stats.sentence_count(), 0)

    def test_average_word_length(self):
        text_stats = TextStats("This is a test file.")
        self.assertAlmostEqual(text_stats.average_word_length(), 3, delta=0.1)

    def test_average_word_length_empty_string(self):
        text_stats = TextStats("")
        self.assertEqual(text_stats.average_word_length(), 0)

class TestTextEdit(unittest.TestCase):

    def test_text_edit_replace(self):
        text_edit = TextEdit("This is a test file.")
        text_edit.text_edit(old="test", new="sample", case_sensitive=True)
        self.assertEqual(text_edit.text, "This is a sample file.")

    def test_text_edit_replace_empty_string(self):
        text_edit = TextEdit("")
        text_edit.text_edit(old="test", new="sample")
        self.assertEqual(text_edit.text, "")

    def test_text_edit_remove(self):
        text_edit = TextEdit("This is a test file.")
        text_edit.text_edit(old="test", case_sensitive=True)
        self.assertEqual(text_edit.text, "This is a  file.")

    def test_text_edit_remove_case_sensitive(self):
        text_edit = TextEdit("This is a test file.")
        text_edit.text_edit(old="T", case_sensitive=True)
        self.assertEqual(text_edit.text, "his is a test file.")

    def test_text_edit_remove_all(self):
        text_edit = TextEdit("This is a test file.")
        text_edit.text_edit()
        self.assertEqual(text_edit.text, "")

    def test_remove_punctuation(self):
        text_edit = TextEdit("This is a test file!")
        text_edit.remove_punctuation()
        self.assertEqual(text_edit.text, "This is a test file")

    def test_remove_whitespace(self):
        text_edit = TextEdit("This is a test file.")
        text_edit.remove_whitespace()
        self.assertEqual(text_edit.text, "Thisisatestfile.")
if __name__ == '__main__':
    unittest.main()
    
