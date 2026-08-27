from supabase import Client


class ApartmentRepository: 
    def __init__(self, db: Client):
        self.db = db
        self.table = 'apartments'

    def get_all(self):
        response = self.db.table(self.table).select('*').execute()
        return response.data
