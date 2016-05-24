from console import Console
from answer import Answer


class Validator(object):
    def __init__(self):
        self.answer = Answer()
        self.console = Console()

    def validate(self, *params):
        pass


class IntValidator(Validator):
    def validate(self, value):
        try:
            int_value = int(value)
        except ValueError:
            print("That's either not a whole number or not a number at all! Try again.")
            return False
        else:
            return True


class EmptyValidator(Validator):
    def validate(self, value):
        print "Value: %s." % value
        if not value or value is None:
            print "Error! Empty value."
            return False
        else:
            return True


class ListValidator(Validator):
    def validate(self, value, list_name):
        if value in list_name:
            print "Value available in list!"
            return True
        else:
            print "Value not in list!"
            return False


class AgeValidator(Validator):

    age_stages = {
        "a kid": range(5, 11),
        "a teen": range(11, 18),
        "a young adult": range(18, 26),
        "an adult": range(26, 40),
        "middle aged": range(40, 66),
        "elderly": range(66, 121)
    }

    def get_range(self, value, range_dict):
        for range_name, range_value in range_dict.iteritems():
            if value in range_value:
                return range_name
            else:
                self.console.display_text("Something, somwhere went awfully wrong. Sorry. %r not a value I can take."
                                          % value)
                return False

    def validate(self, age):
        if IntValidator().validate:
            if age in range(5, 121):
                stage = self.get_range(age, self.age_stages)
                self.console.display_text("So, your character is a %s years old. That would make %s %s." \
                      % (age, self.answer.char_pronoun[1], stage))
                return age, stage
            elif 0 >= age:
                self.console.display_text("Come on. A positive number, please?")
            elif 5 > age:
                self.console.display_text("Come on. You want a full character creation for a %r year old?\n" \
                                          "Well, not in this creator." % age)
            else:
                self.console.display_text("Come on, %r? Humans don't live that long... yet.\n" \
                                          "And it's a human character generator." % age)
            return False

validators = {
    'age': AgeValidator(),
    'name': EmptyValidator(),
    'gender': ListValidator()
}

# validators['age'].validate(2234)


#
# ev = EmptyValidator()
# v = Console().get_answer()
# print "Ze value is: %s." % v
# ev.validate(v)
#
