
class Controller(object):
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def control(self):
        raise NotImplementedError

