class Students:
    def __init__(self, name, cohort):
        self.name = name
        self.cohort = cohort
        
    def talk(self):
        return print("I can talk!")
    
    def say_favourite_language(self, favourite_language):
        return (print("I love " + favourite_language))
