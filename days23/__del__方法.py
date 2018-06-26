class MyOpen:
    def __init__(self,filepath,mode,encoding):
        self.filepath=filepath
        self.mode=mode
        self.encoding=encoding
        self.fobj=open(filepath,mode=mode,encoding=encoding)
    def __del__(self):
        print('guan')

m=MyOpen()

type()