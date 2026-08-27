from app.modules.apartments.repository import ApartmentRepository


class ApartmentService:
    def __init__(self, repository: ApartmentRepository):
        self.repository = repository


    def get_all(self):
        apartments = self.repository.get_all()
        return apartments