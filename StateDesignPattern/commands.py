# from question import Question


class Commands(object):

    """
    def check_if_cmd(self, answer):     # Returns answer + True or False.
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
    """
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

    def help(self):
        print "Running help command... kinda"

    #     print "You should write an integer - not text, not a floating number."
    #     print "No fractions. Or whitespaces. An integer. Like '3' or '57'."
    #     print "I suggest using values from this list: %s" % ', '.join(list_name)
    #     print "To access the list of all commands, type 'commands' and press Enter"
    #     return Question().ask_question

        #  print a list of commands
        #  print help line for given question. Or - depending on the validator?
        #  if list, print list

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