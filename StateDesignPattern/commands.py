from console import Console
import json
import os
from pprint import pprint
import abc


class Commands(object):
    PATH = "C:\Users\Anka\PycharmProjects\CharGen\StateDesignPattern\characters\\"

    def __init__(self, answers):
        self.answers = answers
        self.console = Console()
        self.commands = {
            # "change": ChangeCommand(),
            # "check": CheckCommand(),
            # "commands": CommandsList(),
            "help": HelpCommand(answers),
            "load": LoadCommand(answers, self.PATH),
            # "repeat": RepeatCommand(),
            # "restart": RestartCommand(),
            "save": SaveCommand(answers, self.PATH),
            # "quit": QuitCommand()
        }

    commands_list = ["change", "check", "commands", "help", "load", "pass", "repeat", "restart", "save", "quit"]
    command_texts = {
        "change": ["change", "rename", "modify"],   # change an answer to a chosen question
        "check": ["check", "status", "current"],    # print characters current key: value list
        "commands": ["commands", "cmd", "cmds"],    # print commands + descriptions of what they do
        "help": ["help", "?", "halp"],              # print help line for given question - or line depending on validator. For lists, print lists - only or along with all else
        "load": ["load"],                           # load a previously saved char from given txt file
        "repeat": ["repeat", "instruction"],        # print current question
        "restart": ["restart", "reset"],            # remove all answers, start from first question
        "save": ["save"],                           # save current answers to text file. File needs to be loadable. Name - charname+timestamp?
        "skip": ["pass", "skip"],                   # skip a question, don't save it
        "quit": ["quit"]                            # stop the application
    }
    validation_types = {
        "int": ["IntValidator", "AgeValidator"],
        "list": ["ListValidator", "GenderValidator"],
        "empty": ["EmptyValidator"]
    }

    def execute(self):
        pass

    def is_command(self, value):
        return value in self.commands_list

    def seek_command(self, command_name):
        return self.commands[command_name]

    def run_command(self, command_name):
        command_class = self.seek_command(command_name)
        command_class.execute()


class Command(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, answers):
        self.answers = answers
        self.console = Console()

    @abc.abstractmethod
    def execute(self):
        return


class SaveCommand(Command):
    def __init__(self, answers, path):
        super(SaveCommand, self).__init__(answers)
        self.path = path

    def execute(self):
        self.save_to_text_file()
        self.save_dict()

    def save_to_text_file(self):
        file_name = os.path.join(self.path, self.answers.char_answers["name"] + ".txt")
        text_file = open(file_name, "w")

        text_file.write("Character: %s\n\n" % self.answers.char_answers["name"])
        for k, v in self.answers.char_answers.iteritems():
            if k == "gender_pronoun":
                pass
            else:
                text_file.write(k + ": " + v + "\n")
            if k == "gender_pronoun" or k == "stage":
                pass
            else:
                text_file.write(k + ": " + v + "\n")
        text_file.close()

    def save_dict(self):
        file_name = os.path.join(self.path, self.answers.char_answers["name"] + ".json")

        with open(file_name, "w") as text_file:
            json.dump(self.answers.char_answers, text_file, indent=4)


class LoadCommand(Command):
    def __init__(self, answers, path):
        super(LoadCommand, self).__init__(answers)
        self.path = path

    def execute(self):
        self.load_from_file()

    def load_from_file(self):
        self.console.display_text("Which character do you wish to load?")
        while True:
            try:
                file_name = str(self.path + raw_input(">") + ".json")
                with open(file_name, 'r') as json_data:
                    self.answers.char_answers = json.load(json_data)
            except IOError:
                self.console.display_text("No such character file exists. Try again.")
            else:
                break
        self.answers.set_gender_pronoun()
        pprint(self.answers.char_answers)
        pprint(self.answers.char_gender_pronoun)


class HelpCommand(Command):
    def __init__(self, answers):
        super(HelpCommand, self).__init__(answers)

    def execute(self):
        self.help_command()

    help_list_thing = {
        "int": "Int help text",
        "list": "List help text",
        "other": "Other help text"
    }

    @staticmethod
    def help_command():
        print "Running help command... kinda"

    #     print "You should write an integer - not text, not a floating number."
    #     print "No fractions. Or whitespaces. An integer. Like '3' or '57'."
    #     print "I suggest using values from this list: %s" % ', '.join(list_name)
    #     print "To access the list of all commands, type 'commands' and press Enter"
    #     return Question().ask_question

    #  print a list of commands
    #  print help line for given question. Or - depending on the validator?
    #  if list, print list


    # @staticmethod
    # def help_command_old(data_type, list_name=None, question=None):
    #     if data_type is "number":
    #         print "You should write an integer - not text, not a floating number."
    #         print "No fractions. Or whitespaces. An integer. Like '3' or '57'."
    #     elif data_type is "list":
    #         print "I suggest using values from this list: %s" % ', '.join(list_name)
    #     else:
    #         print question
    #     answer = raw_input(">")
    #     return answer

class ResetCommand(Command):
    def __init__(self, answers):
        super(ResetCommand, self).__init__(answers)

    def execute(self):
        self.reset_command()

    def clear(self):
        self.answers.char_answers = {}
        self.answers.char_gender_pronoun = []

    def reset_command(self):
        pass
        # start over needed. No idea how to do it without refactor.
        # refactor - state machine? Need starting q, current q and next q


class ChangeCommand(Command):
    def __init__(self, answers):
        super(ChangeCommand, self).__init__(answers)

    def execute(self):
        self.change_command()

    def change_command(self):
        param_list = []
        for k, v in self.answers.char_answers:
            param_list.append(k)
        self.console.display_text("What do you wish to change? For list of current parameters type 'param-list'")
        while True:
            parameter = raw_input(">")
            if parameter in param_list:
                print "OK"
            elif parameter == "param-list":
                print ', '.join(param_list)
            else:
                self.console.display_text("No such parameter, try again.")

    def get_parameter(self):
        param_list = []
        for k, v in self.answers.char_answers:
            param_list.append(k)
        self.console.display_text("What do you wish to change? For list of current parameters type 'param-list'")
        while True:
            parameter = raw_input(">")
            if parameter in param_list:
                print "OK"
            elif parameter == "param-list":
                print ', '.join(param_list)
            else:
                self.console.display_text("No such parameter, try again.")

    def change_parameter_value(self, key):
        self.console.display_text("Ok, so you wish to change %s. Current value is %s. Type in what you wish to change it to.") % (key, self.answers.char_answers[key])
        new_value = raw_input(">")
        # NEEDS CHANGE WITH VALIDATION!!!
        self.answers.char_answers[key] = new_value
        self.console.display_text("Current %s value is %s") % (key, self.answers.char_answers[key])