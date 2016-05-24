from question import Question
from answer import Answer
from looks_questions import Looks


class Engine(object):

    # appearance = Looks()
    # answers = Answer()
    # question_list = appearance.appearance_questions

    def __init__(self):
        self.answers = Answer()
        self.appearance = Looks()
        self.question_list = self.appearance.appearance_questions

    def start(self):
        for question in self.question_list:
            question_value = question.ask_question()
            self.answers.set_answer(question.question_name, question_value)
        print "Start method end point: %s" % self.answers.char_appearance



Engine().start()
