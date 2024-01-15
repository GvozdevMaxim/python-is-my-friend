
class DigitRetrieve:
    def __call__(self, *args, **kwargs):
        temp_lst = []
        for i, x in enumerate(args[0]):
            if x in ('1234567890') or (x == '-' and i == 0):
                temp_lst.append(x)
        if len(args[0]) == len(temp_lst):
            return int(args[0])
        return None


dg = DigitRetrieve()
st = ["123", "abc", "-56.4", "0", "-5"]
digits = list(map(dg, st))  # [123, None, None, 0, -5]
print(digits)
