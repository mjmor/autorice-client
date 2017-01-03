from autorice.applications.riceable import Riceable


class I3WM(Riceable):
    def __init__(self):
        super(I3WM, self).__init__()
        self.app_name = 'i3'
        self.files = {'.i3': 'config'}
