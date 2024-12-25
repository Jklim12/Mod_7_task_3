class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = list(file_names)
    def get_all_words(self):
        all_words = {}
        punctuation_to_remove = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for file_name in self.file_names:
            words = []
            with open(file_name, 'r', encoding='utf-8') as file:
                for line in file:
                    line = line.lower()
                    for punkt in punctuation_to_remove:
                        if punkt == ' - ':
                            line = line.replace(punkt, ' ')
                        else:
                            line = line.replace(punkt, '')
                    words_in_line = line.split()
                    words.extend(words_in_line)
            all_words[file_name] =words
        return all_words

    def find(self, word):
        word = word.lower()
        all_words = self.get_all_words()
        result = {}
        for file_name, words in all_words.items():
            if word in words:
                index = words.index(word) + 1
                result[file_name] = index
        return result
    def count(self, word):
        word = word.lower()
        all_words = self.get_all_words()
        result = {}
        for file_name, words in all_words.items():
            count = words.count(word)
            if count > 0:
                result[file_name] = count
        return result
finder2 = WordsFinder('test_file.txt')

print(finder2.get_all_words()) # Все слова

print(finder2.find('TEXT')) # 3 слово по счёту

print(finder2.count('teXT')) # 4 слова teXT в тексте всего


