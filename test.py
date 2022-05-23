class DictionaryItem:
    def __init__(self, w, d):
        self.word = w
        self.meaning = d
    
    def __repr__(self):
        return f"DictionaryItem('{self.word}', '{self.meaning}')"

    def __str__(self):
        return f"{self.word}: {self.meaning}"

euph = DictionaryItem("euphoric", "intensely happy")
print(euph)
print([euph])