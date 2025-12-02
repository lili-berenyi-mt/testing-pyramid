from models import Duty
class DutyService:
    def __init__(self, repo):
        self.repo = repo

    def add(self, number, description):
        try:
            new_duty = Duty(number, description)
        except ValueError:
            return False
        
        duties = self.repo.get_all()
        if any(duty.equals(new_duty) for duty in duties):
            return False
        self.repo.add(Duty(number, description))
        return True
    
    def get_all(self):
        return self.repo.get_all()