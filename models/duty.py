class Duty:
    def __init__(self, number, description):
        self.number = number
        self.description = description

    def get_name(self):
        return f"Duty {self.number}"
    
    def get_summary(self):
        return f"{self.get_name()}: {self.description}"