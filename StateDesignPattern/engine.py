from question import Question
from validator import *
from answer import Answer


class Engine(object):

    def __init__(self):
        self.answers = Answer()
        self.question_list = [
            Question(self.answers, "name", "Let's start with naming your character:",
                     "Ok, so let's get on with it! We'll start with %s's Looks, than go through\n"
                     "Personality, and finish with some kind of Background.\n" % Answer().char_answers.get("name"),
                     EmptyValidator()
                     ),
            Question(self.answers, "gender", "Ok, what is %s's gender?" % Answer().char_answers.get("name"),
                     "Ah, a %s, OK." % Answer().char_answers.get("gender"),
                     GenderValidator(),
                     ),
            Question(self.answers, "age", "And how old is your character?",
                     "So, your character is a %s years old." % Answer().char_answers.get("age"),
                     AgeValidator()
                     )

        ]

    def start(self):
        for question in self.question_list:
            question.get_answer()
        print "Start method end point: %s" % self.answers.char_answers
        print "Char pronoun: %s" % self.answers.char_gender_pronoun
        self.answers.save_to_text_file()
        self.answers.save_dict()


Engine().start()



