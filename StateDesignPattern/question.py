from answer import Answer
from validator import *


class Question(object):
    def __init__(self, question_name, question_text, confirmation_text, validator, list_name=None):
        self.question_name = question_name
        self.question_text = question_text
        self.confirmation_text = confirmation_text
        self.validator = validator
        self.list_name = list_name

    answers = Answer()
    console = Console()
    '''
    question_modules = {
        "appearance": Looks(None, None, None, None),
        "personality": Personality(None, None, None),
        "background": Background(None, None, None)
    }'''
    # opening_question = "name"

    def get_answer(self):
        while True:
            answer = self.ask_question()
            validate_value = self.validate_answer(answer)
            if validate_value:
                return answer
            else:
                continue

    def ask_question(self):
        self.console.display_text(self.question_text)
        answer = self.console.get_answer()
        return answer

    def validate_answer(self, answer):
        try:
            validate_value = self.validator.validate(answer)
            print validate_value
        except self.validator.validate(answer) is False:
            self.console.display_text("Error!")
            return False
        if validate_value:
            return True

    def ask_question_previous(self):
        self.console.display_text(self.question_text)
        while True:
            answer = self.console.get_answer()
            try:
                validate_value = self.validator.validate(answer)
                print validate_value
            except self.validator.validate(answer) is False:
                self.console.display_text("Error!")
                continue
            if validate_value:
                return answer
# def __str__(self):
#     return "Q(q=%s, c=%s, e=%s, v=%s)" % (self.question_text,  self.confirmation_text, self.error_text, self.validator)
#
# def __repr__(self):
#     return self.__str__()




