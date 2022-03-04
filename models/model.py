from database.table import Table


class Model:
    
    @classmethod
    def create(cls, record):
        raise NotImplementedError
