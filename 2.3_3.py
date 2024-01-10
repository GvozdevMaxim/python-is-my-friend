class Model:
    def __init__(self, *args, **kwargs):

        print(kwargs)
        self.kw = kwargs

    def query(self, *args, **kwargs):
        self.kw = kwargs

    def __str__(self):
        res_lst = f"Model: "
        for k,v in self.kw.items():
            res_lst += f'{k} = {v}'
        return res_lst

    def __repr__(self):
        return f"Model"

model = Model()
model.query(id=1, fio='Sergey', old=33)
print(model)