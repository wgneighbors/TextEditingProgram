"""
A simple text editing and analysis program.
"""
import string
import re

def import_file(file_path: str) -> str:
    """
    Imports text file.
    """
    with open(file_path, 'r', encoding = "utf-8") as file:
        text = file.read()
    return text

class TextStats:
    """
    Class for handling all text stats, such as word count and average word length.
    """
    def __init__(self, text: str):
        self.text = text

    def word_count(self) -> int:
        """
        Returns total number of words in text.
        """
        word_list = re.findall(r'\b\w+\b', self.text)
        return len(word_list)

    def character_count(self) -> int:
        """
        Returns total number of characters in text.
        """
        text_edit = TextEdit(self.text)
        return len(text_edit.text)

    def sentence_count(self) -> int:
        """
        Returns total number of sentence in text.
        """
        sentence_list = re.findall(r'[.!?]+', self.text)
        return len(sentence_list)

    def average_word_length(self) -> float:
        """
        Returns average length of words in text.
        """
        try:
            word_list = re.findall(r'\b\w+\b', self.text)
            total_length = sum(len(word) for word in word_list)
            return total_length / len(word_list)
        except ZeroDivisionError:
            return 0

class TextEdit:
    """
    Class to edit parts of the text, such as removing or changing words or removing punctuation.
    """
    def __init__(self, text):
        self.text = text

    def text_edit(self, old: str = None, new: str = None, case_sensitive: bool = False):
        """
        If only an old attribute is passed, delete all words that equal the old attribute.
        If both old and new attributes are passed, replaces all old with new.
        Uses overload.
        """
        if old is not None and new is not None:
            if not case_sensitive:
                self.text = self.text.lower().replace(old.lower(), new)
            else:
                self.text = self.text.replace(old, new)
        elif old is not None:
            if not case_sensitive:
                self.text = self.text.lower().replace(old.lower(), "")
            else:
                self.text = self.text.replace(old, "")
        else:
            self.text = ""

    def remove_punctuation(self) -> None:
        """
        Removes all punctuation from the text.
        """
        no_punct = self.text.translate(str.maketrans('', '', string.punctuation))
        self.text = no_punct

    def remove_whitespace(self) -> None:
        """
        Removes all whitespace from the text.
        """
        no_whitespace = self.text.replace(" ", "")
        self.text = no_whitespace

class TextCompare:
    """
    Class to take two texts and compare them.
    """
    def __init__(self, text1: str, text2: str):
        self.text1 = text1
        self.text2 = text2

    def compare(self) -> float:
        """
        Compares the two given texts using intersection and union.
        """
        words1 = set(self.text1.split())
        words2 = set(self.text2.split())
        similarity = len(words1.intersection(words2)) / len(words1.union(words2))
        return similarity
