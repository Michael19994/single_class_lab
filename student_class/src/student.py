class Student:
    
    def __init__(self, name, cohort):
        self.name = name
        self.cohort = cohort
        self.speech = "I can talk!"
        self.language = "I love "


    def talk(self):
        return self.speech

    def say_favourite_language(self, language):
        return self.language + language