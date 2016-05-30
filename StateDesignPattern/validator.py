from console import Console
# from answer import Answer
# from commands import Commands


class Validator(object):
    def __init__(self):
        # self.answer = Answer()
        self.console = Console()

    def validate(self, *params):
        pass


class IntValidator(Validator):
    def validate(self, value):
        if EmptyValidator().validate(value):
            try:
                int(value)
            except ValueError:
                print("That's either not a whole number or not a number at all! Try again.")
                return False
            else:
                return True
        else:
            return False


class EmptyValidator(Validator):
    def validate(self, value):
        if not value or value is None:
            print "Error! Empty value."
            return False
        elif CMDValidator().validate(value):
            print "It's a command, cmd will be run... eventually"
        else:
            return True


class ListValidator(Validator):
    def __init__(self, list_name):
        super(ListValidator, self).__init__()
        self.list_name = list_name

    def validate(self, value):
        if EmptyValidator().validate(value):
            if value in self.list_name:
                print "Value available in list!"
                return True
            else:
                print "Value not in list!"
                return False


class GenderValidator(Validator):
    def __init__(self):
        super(GenderValidator, self).__init__()
        self.gender_list_validator = ListValidator(["male", "female"])

    """This is not exactly a validator only, but also an additional parameter setter."""
    def validate(self, value):
        if self.gender_list_validator.validate(value):
            return True
        else:
            return False


class AgeValidator(Validator):

   def validate(self, age):
        logic_value = IntValidator().validate(age)
        age = int(age)
        if logic_value:
            if age in range(5, 121):
                self.console.display_text("Confirmation: %s years old.")
                return True
            elif 0 >= age:
                self.console.display_text("Come on. A positive number, please?")
            elif 5 > age:
                self.console.display_text("Come on. You want a full character creation for a %r year old?\n"
                                          "Well, not in this creator." % age)
            else:
                self.console.display_text("Come on, %r? Humans don't live that long... yet.\n"
                                          "And it's a human character generator." % age)
            return False


class CMDValidator(Validator):

    # command_texts = {
    #     "change": ["change", "rename", "modify"],
    #     "check": ["check", "status", "current"],
    #     "commands": ["commands", "cmd", "cmds"],
    #     "help": ["help", "?", "halp"],
    #     "load": ["load"],
    #     "repeat": ["repeat", "instruction"],
    #     "restart": ["restart", "reset"],
    #     "save": ["save"],
    #     "quit": ["quit"]
    # }

    commands = ["change", "check", "commands", "help", "load", "repeat", "restart", "save", "quit"]

    def validate(self, value):
        if value in self.commands:
            print "It's a command!"
            return True
        else:
            print "Not a command"
            return False
