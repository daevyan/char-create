from questions import *

class Engine(object):

    questions = Questions()

    def start(self):
        for q in questions:
            question_name = "age"
            question_value = q.ask_question
