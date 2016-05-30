from console import Console


class Answer(object):
    def __init__(self):
        self.char_appearance = {}
        self.char_pronoun = []
        self.console = Console()

    def set_answer(self, question_name, answer):
        self.char_appearance[question_name] = answer
        if question_name == "gender":
            self.set_gender_pronoun(answer)
        elif question_name == "age":
            self.set_stage(answer)

    """ ------------------- Gender ------------------- """

    @staticmethod
    def get_gender_pronoun(answer):
        if answer == 'male':
            pronoun = ["he", "him", "his"]
        elif answer == 'female':
            pronoun = ["she", "her", "hers"]
        else:
            pronoun = None
            print "Cannot set pronoun"
        return pronoun

    def set_gender_pronoun(self, answer):
        gender_pronoun = self.get_gender_pronoun(answer)
        self.char_pronoun = gender_pronoun

    """ ------------------- Age ------------------- """

    age_stages = {
        "a kid": range(5, 11),
        "a teen": range(11, 18),
        "a young adult": range(18, 26),
        "an adult": range(26, 40),
        "middle aged": range(40, 66),
        "elderly": range(66, 121)
    }

    def get_range(self, value, range_dict):
        for range_name, range_value in range_dict.iteritems():
            if int(value) in range_value:
                return range_name
        else:
            self.console.display_text("Something, somewhere went awfully wrong. Sorry. %r not a value I can take."
                                      % value)
            return False

    def get_stage(self, age):
        stage = self.get_range(age, self.age_stages)
        return stage

    def set_stage(self, age):
        stage = self.get_stage(age)
        self.char_appearance["stage"] = stage
