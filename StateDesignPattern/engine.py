from question import *
from answer import Answer


class Engine(object):

    def __init__(self):
        self.answers = Answer()
        self.question_list = [
            NameQuestion(self.answers),
            GenderQuestion(self.answers),
            AgeQuestion(self.answers)
        ]

    def start(self):
        for question in self.question_list:
            question.get_answer()
        print "Start method end point: %s" % self.answers.char_answers
        print "Char pronoun: %s" % self.answers.char_gender_pronoun
        self.answers.save_to_text_file()
        self.answers.save_dict()


Engine().start()



