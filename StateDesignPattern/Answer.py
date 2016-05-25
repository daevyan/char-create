class Answer(object):
    def __init__(self, char_appearance=None, char_pronoun=None):
        if char_appearance is None:
            self.char_appearance = {}
        else:
            self.char_appearance = char_appearance
        if char_pronoun is None:
            self.char_pronoun = []
        else:
            self.char_pronoun = char_pronoun

    # def get_gender_pronoun(self):
    #     if self.char_appearance["gender"] is "male":
    #         pronoun = ["he", "him", "his"]
    #     elif self.char_appearance["gender"] is "female":
    #         pronoun = ["she", "her", "hers"]
    #     else:
    #         pronoun = None
    #         print "Cannot set pronoun"
    #     return pronoun

    def set_gender_pronoun(self, gender_pronoun):
        # gender_pronoun = self.get_gender_pronoun()
        self.char_pronoun = gender_pronoun

    def set_answer(self, question_name, answer):
        self.char_appearance[question_name] = answer
        return answer