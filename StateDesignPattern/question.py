import abc
from validator import *
from commands import *


class Question(object):
    __metaclass__ = abc.ABCMeta

    console = Console()
    commands = Commands()

    def __init__(self, answers, validator):
        self.validator = validator
        self.answers = answers

    @abc.abstractmethod
    def get_name(self):
        return

    @abc.abstractmethod
    def get_question_text(self):
        return

    @abc.abstractmethod
    def get_confirmation_text(self):
        return

    def get_answer(self):
        while True:
            answer = self.ask_question()
            validator = self.validator.validate(answer)
            if validator:
                self.answers.set_answer(self.get_name(), answer)
                print self.answers.char_answers
                break
            elif not validator:
                print self.validator.validate(answer)
                self.console.display_text("Error!")
                continue
            else:
                print "Validator value is %s" % validator
                self.commands.run_command()
                continue

    def ask_question(self):
        self.console.display_text(self.get_question_text())
        answer = self.console.get_answer()
        return answer


class GenderQuestion(Question):
    def __init__(self, answer):
        super(GenderQuestion, self).__init__(answer, GenderValidator())

    def get_name(self):
        return "gender"

    def get_question_text(self):
        return "Ok, what is %s's gender?" % self.answers.char_answers.get("name")

    def get_confirmation_text(self):
        return "Ah, a %s, OK." % self.answers.char_answers.get("gender")


class AgeQuestion(Question):
    def __init__(self, answer):
        super(AgeQuestion, self).__init__(answer, AgeValidator())

    def get_name(self):
        return "age"

    def get_question_text(self):
        return "And how old is %s" % self.answers.char_answers.get("name")

    def get_confirmation_text(self):
        return "So, %s is a %s years old." % (self.answers.char_answers.get("name"), self.answers.char_answers.get("age"))


class NameQuestion(Question):
    def __init__(self, answer):
        super(NameQuestion, self).__init__(answer, EmptyValidator())

    def get_name(self):
        return "name"

    def get_question_text(self):
        return "Let's start with naming your character:"

    def get_confirmation_text(self):
        return "Ok, so let's get on with it! We'll start with %s's Looks, than go through\n" \
               "Personality, and finish with some kind of Background." % self.answers.char_answers.get("name")


class Question655(object):
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




