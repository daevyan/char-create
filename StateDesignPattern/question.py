import abc

from validator import *


class Question(object):
    def __init__(self, answers, question_name, question_text, confirmation_text, validator, list_name=None):
        self.question_name = question_name
        self.question_text = question_text
        self.confirmation_text = confirmation_text
        self.validator = validator
        self.answers = answers
        self.list_name = list_name

    console = Console()

    def get_answer(self):
        while True:
            answer = self.ask_question()
            if self.validator.validate(answer):
                self.answers.set_answer(self.question_name, answer)
                break
            else:
                continue

    def ask_question(self):
        self.console.display_text(self.question_text)
        answer = self.console.get_answer()
        return answer




