import abc


class Console(object):
    def __int__(self):
        pass

    @staticmethod
    def display(message):
        print message

    @staticmethod
    def get_answer():
        return raw_input(">")


class Validator(object):
    def validate(self, answer):
        if answer == 'dupa':
            return True
        return False

console = Console()




class ConsoleParamReader(object):

    __metaclass__ = abc.ABCMeta

    def __int__(self):
        pass

    @abc.abstractmethod
    def validate(self, answer):
        return

    @abc.abstractmethod
    def get_param(self, answer):
        return


class AgeParamReader(ConsoleParamReader):
    def __init__(self):
        self.age_stages = {
            "a kid": range(5, 11),
            "a teen": range(11, 18),
            "a young adult": range(18, 26),
            "an adult": range(26, 40),
            "middle aged": range(40, 66),
            "elderly": range(66, 121)
        }

    def validate(self, answer):
        try:
            age = int(answer)
        except ValueError:
            return False
        else:
            if age in range(5, 121):
                stage = self.get_range(age, self.age_stages)
                console.display("So, your character is a %s years old. That would make %s %s." \
                      % (age, self.char_pronoun[1], stage))
                return age, stage
            elif 0 >= age:
                print "Come on. A positive number, please?"
            elif 5 > age:
                print "Come on. You want a full character creation for a %r year old?\n" \
                      "Well, not in this creator." % age
            else:
                print "Come on, %r? Humans don't live that long... yet.\n" \
                      "And it's a human character generator." % age

    def get_param(self, answer):
        return int(answer)


class Question(object):
    def __init__(self, main_question, correction_question, param_reader):
        self.main_question = main_question
        self.correction_question = correction_question
        self.param_reader = param_reader

    def ask(self):
        console.display(self.main_question)
        while True:
            answer = console.get_answer()
            if self.param_reader.validate(answer):
                param = self.param_reader.get_param(answer)
                console.display(param)
                return answer
            else:
                console.display(self.correction_question)



v = Validator()

q1 = Question("What is your name", "Are you sure?", v)
q2 = Question("What is your age", "Wrong age?", v)

questions = [q1, q2]

for q in questions:
    q.ask()

