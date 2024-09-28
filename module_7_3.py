class WordsFinder:
    def __init__(self, *file_names: str):
        self._file_names = file_names

    def get_all_words(self):
        file_words = {}
        for file_name in self._file_names:
            with open(file_name, "r", encoding="utf-8") as f:
                words = []
                for line in f.readlines():
                    line = line.strip().lower()
                    for symbol in (",", ".", "=", "!", "?", ";", ":", " - "):
                        line = line.replace(symbol, " ")
                    words.extend([l for l in line.split(" ") if l])
            file_words[file_name] = words
        return file_words

    def find(self, word):
        all_words = self.get_all_words()
        result = {}
        for file, words in all_words.items():
            if word.lower() in words:
                result[file] = words.index(word.lower())
        return result

    def count(self, word):
        all_words = self.get_all_words()
        result = {}
        for file, words in all_words.items():
            if word.lower() in words:
                result[file] = words.count(word.lower())
        return result

finder2 = WordsFinder('test.txt', 'test2.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('a')) # 3 слово по счёту
print(finder2.count('c')) # 4 слова teXT в тексте всего
