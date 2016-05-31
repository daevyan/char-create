from console import Console
import json
import os
from pprint import pprint

from engine import Engine


class Commands(object):
    def __init__(self):
        self.answers = Engine().answers
        self.console = Console()

    path = "C:\Users\Anka\PycharmProjects\CharGen\StateDesignPattern\characters\\"

    commands = ["change", "check", "commands", "help", "load", "pass", "repeat", "restart", "save", "quit"]
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


class SaveCommand(Commands):

    def save(self):
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
        text_file.close()

    def save_dict(self):
        file_name = os.path.join(self.path, self.answers.char_answers["name"] + ".json")

        with open(file_name, "w") as text_file:
            json.dump(self.answers.char_answers, text_file, indent=4)


class LoadCommand(Commands):

    def load(self):
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


class HelpCommand(Commands):

    def help(self):
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