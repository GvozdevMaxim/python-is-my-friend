stich = ["Я к вам пишу – чего же боле?",
         "Что я могу еще сказать?",
         "Теперь, я знаю, в вашей воле",
         "Меня презреньем наказать.",
         "Но вы, к моей несчастной доле",
         "Хоть каплю жалости храня,",
         "Вы не оставите меня."]

lst_in = [s.translate({ord(i): None for i in '–?!,.;'}).split() for s in stich]
lst_text = []


class StringText:
    lst_text = []

    def __len__(self):
        count = 0
        for i in self.lst_words:
            count += 1
        return count

    def __init__(self, lst_words):
        self.lst_words = lst_words

    def __gt__(self, other):
        return len(self.lst_words) > len(other.lst_words)

    def __ge__(self, other):
        return len(self.lst_words) >= len(other.lst_words)

    def __lt__(self, other):
        return len(self.lst_words) < len(other.lst_words)

    def __le__(self, other):
        return len(self.lst_words) <= len(other.lst_words)


st1 = StringText(lst_in[0])
st2 = StringText(lst_in[1])
st3 = StringText(lst_in[2])
st4 = StringText(lst_in[3])
st5 = StringText(lst_in[4])
st6 = StringText(lst_in[5])
lst_text.append(st1)
lst_text.append(st2)
lst_text.append(st3)
lst_text.append(st4)
lst_text.append(st5)
lst_text.append(st6)

lst_text_sorted = sorted(lst_text, key=len, reverse=True)

temp = []
for x in lst_text_sorted:
    temp.append(" ".join(x.lst_words))

lst_text_sorted = temp
print(temp)