import abc


class ValidationError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class Console(object):
    def __int__(self):
        pass

    @staticmethod
    def display(message):
        print message

    @staticmethod
    def get_answer():
        return raw_input(">")

console = Console()


class ParamReader(object):

    __metaclass__ = abc.ABCMeta

    def __int__(self):
        pass

    @abc.abstractmethod
    def get_param_name(self):
        return

    @abc.abstractmethod
    def get_param_value(self, answer):
        return


class NameReader(ParamReader):
    def __init__(self):
        pass

    def get_param_name(self):
        return "name"

    def get_param_value(self, answer):
        console.display("Ok, so let's get on with it! We'll start with %s's Appearance, than go through\nPersonality, and finish with some kind of Background.\n" % answer)
        return answer


class GenderReader(ParamReader):
    def __init__(self):
        self.gender_list = ['male', 'female']

    def get_param_name(self):
        return "gender"

    def get_param_value(self, answer):
        if answer in self.gender_list:
            return answer
        else:
            raise ValidationError("You answer is not valid. It should be one of %r" % self.gender_list)


class AgeReader(ParamReader):
    def __init__(self):
        self.age_stages = {
            "a kid": range(5, 11),
            "a teen": range(11, 18),
            "a young adult": range(18, 26),
            "an adult": range(26, 40),
            "middle aged": range(40, 66),
            "elderly": range(66, 121)
        }

    def get_param_name(self):
        return "age"

    def get_param_value(self, answer):
        try:
            age = int(answer)
        except ValueError:
            raise ValidationError('Age must be int')

        if age in range(5, 121):
            stage = self.__get_range(age)
            console.display("So, your character is a %s years old. That would make %s %s." % (age, self.char_pronoun[1], stage))
            return age, stage
        elif 0 >= age:
            raise ValidationError("Come on. A positive number, please?")
        elif 5 > age:
            raise ValidationError("Come on. You want a full character creation for a %r year old?\n" \
                                  "Well, not in this creator." % age)
        else:
            raise ValidationError("Come on, %r? Humans don't live that long... yet.\n" \
                                  "And it's a human character generator." % age)

    def __get_range(self, age):
        for range_name, range_value in self.age_stages.iteritems():
            if age in range_value:
                return range_name
        raise ValidationError("Something, somwhere went awfully wrong. Sorry. %r not a value I can take." % age)


class Question(object):
    def __init__(self, param_reader, main_question, correction_question=None):
        self.main_question = main_question
        self.correction_question = correction_question
        self.param_reader = param_reader

    def ask(self):
        console.display(self.main_question)
        while True:
            try:
                answer = console.get_answer()
                return self.param_reader.get_param_name(), self.param_reader.get_param_value(answer)
            except ValidationError as e:
                console.display(e.message)
                if self.correction_question:
                    console.display(self.correction_question)


result = {}

questions = [
    Question(NameReader(), "First of all name your character"),
    Question(AgeReader(), "What is your age", "Wrong age?"),
    Question(GenderReader(), "Ok, what is %s's gender?", "Are you sure?"),
]

for q in questions:
    param_name, param_value = q.ask()
    result[param_name] = param_value

print result
