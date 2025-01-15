class WordsFinder():

    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        punctuation = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for file_name in self.file_names:
            with open(file_name, encoding='utf-8') as file:
                string = file.read()

            clear_string = ''.join([char for char in string if char not in punctuation])
            all_words[file_name] = clear_string.lower().split()
        return all_words

    def find(self, word):
        res = {}
        for elem in self.get_all_words().items():
            if word.lower() in elem[1]:
                res[elem[0]] = elem[1].index(word.lower()) + 1
                return res

    def count(self, word):
        res = {}

        for elem in self.get_all_words().items():
            res[elem[0]] = elem[1].count(word.lower())
        else:
            return res

        # counter = 0
        # for elem in self.get_all_words().items():
        #     for w in elem[1]:
        #         if w == word.lower():
        #             counter += 1
        #     else:
        #         res[elem[0]] = counter
        # else:
        #     return res


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего

