import ChainingHashTableMap

class InvertedFile:
    def __init__(self, file_name):
        self.data = ChainingHashTableMap.ChainingHashTableMap()
        word_lst = []
        f = open(file_name, 'r')
        for line in f:
            word_lst.extend(line.split())

        f.close()

        for word in word_lst:
            clean_word = word.strip(",!!.'/"'').lower()
            self.data[clean_word] = []

        index = 0

        for word in word_lst:
            clean_word = word.strip(",!!.'/"'').lower()
            self.data[clean_word].append(index)
            index += 1

    def indices(self, word):
        clean_word = word.lower()
        index = self.data.hash_function(word)
        if self.data.table[index] is not None:
            for item in self.data.table[index]:
                if clean_word == item:
                    return self.data.table[index][clean_word]

        return []
