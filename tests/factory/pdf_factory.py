import os


class PdfFactory():
    @classmethod
    def getPdf(cls, id: int = 1):
        dirname = os.path.dirname(__file__)
        path = os.path.join(dirname, f'../data/pdf{id}.pdf')
        with open(path, 'rb') as f:
            return f.read()

    @classmethod
    def getTxt(cls, id: int = 1):
        dirname = os.path.dirname(__file__)
        path = os.path.join(dirname, f'../data/texto.txt')
        with open(path, 'rb') as f:
            return f.read() 