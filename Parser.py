# http://tartarus.org/~martin/PorterStemmer/python.txt
import re
from nltk.tokenize import word_tokenize
from PorterStemmer import PorterStemmer
import jieba


class Parser:
    """A processor for removing the commoner morphological and inflexional endings from words in English."""

    def __init__(self):
        self.stemmer = PorterStemmer()

        # English stopwords from ftp://ftp.cs.cornell.edu/pub/smart/english.stop
        try:
            with open("english.stop", "r") as f:
                self.stopwords = f.read().split()
        except FileNotFoundError:
            print("Error: 'english.stop' file not found.")
            self.stopwords = []

    def clean(self, string):
        """Remove any unwanted characters from the string."""
        string = string.replace(".", "")
        string = re.sub(r"\s+", " ", string)  # 使用正則表達式替換多個空格
        string = string.lower()
        return string

    def removeStopWords(self, word_list):
        """Remove common words which have no search value."""
        return [word for word in word_list if word not in self.stopwords]

    def tokenise(self, string):
        """Break string up into tokens and stem words."""
        string = self.clean(string)
        words = word_tokenize(string)  # 使用 nltk 的 word_tokenize 進行分詞
        return [
            self.stemmer.stem(word, 0, len(word) - 1) for word in words
        ]  # 進行詞幹提取

    def chinese_tokenise(self, text):
        return list(jieba.cut(text))  # 使用 jieba 進行中文分詞


# 測試分詞功能
# parser = Parser()  # Create an instance of the Parser class
# sample_text_zh = "我愛編程的方法"
# sample_text_en = "I love the method of programming"
# sample_text_en = "Typhoon Taiwan war"
# sample_text = "Jimmy 玩一個電腦遊戲。"
# print(
#     "中文分詞:", parser.segment_text(sample_text_zh)
# )  # Call the method on the instance
# print(
#     "英文分詞:", parser.segment_text(sample_text_en)
# )  # Call the method on the instance
# wordlist = parser.tokenise(sample_text_en)
# print("英文分詞2", parser.removeStopWords(wordlist))
