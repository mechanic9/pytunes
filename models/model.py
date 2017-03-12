
class Model:

    #retrieve data
    def load(self, source):
        raise NotImplementedError

    #Return data by id
    def get(self, id):
        raise NotImplementedError

