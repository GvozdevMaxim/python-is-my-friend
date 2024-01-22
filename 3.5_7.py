filenames = ["boat.jpg", "ans.web.png", "text.txt", "www.python.doc", "my.ava.jpg", "forest.jpeg", "eq_1.png",
             "eq_2.xls"]

class FileAcceptor:
    def __init__(self, *args):
        self.ext = [*args]

    def __call__(self, filename):
        return filename[filename.rfind('.') + 1:] in self.ext

    def __add__(self, other):
        return FileAcceptor(*(self.ext + other.ext))

acceptor_images = FileAcceptor("jpg", "jpeg", "png")
acceptor_docs = FileAcceptor("txt", "doc", "xls")

filenames = list(filter((acceptor_images + acceptor_docs), filenames))
print(filenames)
