class Morph:
    def __init__(self, *args):
        self.list_var = [*args]

    def add_word(self, word):
        if word not in self.list_var:
            self.list_var.append(word)

    def get_words(self):
        return tuple(self.list_var)


    def __eq__(self, other):
        for i in self.list_var:
            if other.lower().strip() in i:
                return True

    def __ne__(self, other):
        for i in self.list_var:
            if other.lower().strip() != i:
                return True

dict_words = (Morph('связь', 'связи', 'связью', 'связей', 'связям', 'связями', 'связях'),
              Morph('формула', 'формулы', 'формуле', 'формулу', 'формулой', 'формул', 'формулам', 'формулами', 'формулах'),
              Morph('вектор', 'вектора', 'вектору', 'вектором', 'векторе', 'векторы', 'векторов', 'векторам', 'векторами', 'векторах'),
              Morph('эффект', 'эффекта', 'эффекту', 'эффектом', 'эффекте', 'эффекты', 'эффектов', 'эффектам', 'эффектами', 'эффектах'),
              Morph('день', 'дня', 'дню', 'днем', 'дне', 'дни', 'дням', 'днями', 'днях'))

text = input()
words = map(lambda x: x.strip("?!:;,.").lower(), text.split())
count = 0

for i in words:
    for j in dict_words:
        if i in j.list_var:
            count += 1

print(count)
