import uuid

Host='host'
PORT='port'

class Mysql:
    def __init__(self,host,port):
        self.host=host
        self.port =port
    def tell_info(self):
        print(self.host,self.port)

    # @classmethod
    # def get

    @staticmethod
    def create_id():
        return uuid.uuid4()
