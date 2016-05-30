from question import Question
from answer import Answer
from validator import *


class Looks(object):
    def __init__(self):
        self.answers = Answer()

    """ -------------------- Lists -------------------- """

    """ -------------------- Questions -------------------- """

    appearance_questions = [
        Question(self.answers, "name", "Let's start with naming your character:",
                 "Ok, so let's get on with it! We'll start with %s's Looks, than go through\n"
                 "Personality, and finish with some kind of Background.\n" % Answer().char_appearance.get("name"),
                 EmptyValidator()
                 ),
        Question(self.answers, "gender", "Ok, what is %s's gender?" % Answer().char_appearance.get("name"),
                 "Ah, a %s, OK." % Answer().char_appearance.get("gender"),
                 GenderValidator(),
                 ),
        Question(self.answers, "age", "And how old is your character?",
                 "So, your character is a %s years old." % Answer().char_appearance.get("age"),
                 AgeValidator()
                 )

    ]

    def get_range(self, value, range_dict):
        for range_name, range_value in range_dict.iteritems():
            if value in range_value:
                return range_name
        raise ValueError("Something, somwhere went awfully wrong. Sorry. %r not a value I can take."
                         % value)


class Personality(Question):
    pass


class Background(Question):
    pass