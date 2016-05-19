

class CharCreator(object):

    def __init__(self):
        pass

    def start_game(self):
        print "Welcome to the Character Creation Tool for handicapped people like me.\n"


class Commands(object):
    def __init__(self):
        self.commands = {
            "help": HelpCommand(),
            "change": ChangeCommand(),
            "check": CheckCommand(),
            "repeat": RepeatCommand()
        }

    command_texts = {
        "help": ["help", "?", "halp"],
        "change": ["change", "rename", "modify"],
        "check": ["check", "status", "current"],
        "repeat": ["repeat", "instruction"]
    }

    def run_command(self, command_name, *arg, **kwargs):  # Runs a cmd from dict if present.
                                                        # Returns answer
        print "A %s will be run. Eventually." % command_name
        self.commands[command_name](*arg, **kwargs)
        answer = raw_input(">")
        return answer

    def console_cmd(self, answer):  # Checks if cmd. If True, runs cmd.
        # Returns answer
        command_name, is_cmd = self.check_if_cmd(answer)
        if is_cmd:
            return self.run_command(command_name)
        else:
            return answer

    def check_if_cmd(self, answer):  # Returns answer + True or False.
        # True if answer is a command, False if it is not
        for command_name, v in self.command_texts.iteritems():
            values = v
            if answer in values:
                print "It's a command"
                return command_name, True
            else:
                pass
        print "Not a command"
        return answer, False


class HelpCommand(Commands):
    help = {
        "int": "one",
        "list": "two",
        "other": "three"
    }

    def help_command(self, data_type, list_name=None, question=None):
        if data_type is "number":
            print "You should write an integer - not text, not a floating number."
            print "No fractions. Or whitespaces. An integer. Like '3' or '57'."
        elif data_type is "list":
            print "I suggest using values from this list: %s" % ', '.join(list_name)
        else:
            print question
        answer = raw_input(">")
        return answer


class ChangeCommand(Commands):
    def change_command(self):
        pass


class CheckCommand(Commands):
    pass


class RepeatCommand(Commands):
    pass


class Console(object):

    c_number = "number"
    c_list = "list"


    def input_int(self):
        new_value = int(raw_input(">"))
        return new_value




    def console_list(self, answer, finite=False, listname=None):
        while finite:
            if answer in listname:
                return answer
            else:
                print "Your answer is not valid. Type 'help' for available answers"
                answer = raw_input(">")

    def check_if_list(self, data_type=None):
        if data_type is "list":
            return True
        else:
            return False

    def check_answer_type(self):
        pass

    def console(self, data_type=None, finite=False, listname=None):
        answer = raw_input(">")
        answer = self.console_cmd(answer)
        if True:
            self.check_if_int(answer, data_type)

        return answer


class IntConsole(Console):

    def console_int(self, answer, data_type, answer_range=None, range_dict=None):  # Check if answer in range


        int_answer, is_int = check_if_int()
        if is_int and answer_range is not None:
            return check_if_in_range(int_answer)
        else:
            pass

    def check_if_should_be_int(self, data_type):
        if data_type is "number":
            print "It should be a number!"
            self.check_if_int()
        else:
            pass

    def check_if_int(self, answer):
        try:
            Commands.console_cmd(answer)
            int(answer)
        except ValueError:
            print("That's either not a whole number or not a number at all! Try again.")
            return False
        else:
            return True

    def check_if_in_range(self, int_answer, data_type, answer_range, range_dict=None):
        if int_answer in answer_range:
            if range_dict is not None:
                self.get_range_name(int_answer, range_dict)
            else:
                return int_answer
        else:
            print "This value is not in range. Range is %s to %s." \
                  % (answer_range[0], answer_range[-1])
            new_int_answer = self.check_if_int(raw_input(">"))
            self.check_if_in_range(new_int_answer)

    def get_range_name(self, int_answer, range_dict):
        for range_name, range_value in range_dict.iteritems():
            if int_answer in range_value:
                return int_answer, range_name



# a_list = ['one', 'two', 'gods', "why"]
le_answer = raw_input(">")
# le_answer = raw_input(">")
b = Console()
# b.run_command(le_answer, "list", a_list, True)
le_answer_range = range(20, 150)
le_range_dict = {
    "a kid": range(5, 11),
    "a teen": range(11, 18),
    "a young adult": range(18, 26),
    "an adult": range(26, 40),
    "middle aged": range(40, 66),
    "elderly": range(66, 121)
}
thing = b.console_int(le_answer, "number", le_answer_range)
print thing

# if le_answer in le_answer_range:
#     print le_answer
# else:
#     print "U fail"