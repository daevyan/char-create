class Console(object):

    help = {
        "int": "one",
        "list": "two",
        "other": "three"
    }

    c_number = "number"
    c_list = "list"
    command_texts = {
        "help": ["help", "?", "halp"],
        "change": ["change", "rename", "modify"]
    }

    def change_command(self):
        pass

    def help_command(self, type, listname=None, question=None):
        if type is "number":
            print "You should write an integer - not text, not a floating number."
            print "No fractions. Or whitespaces. An integer. Like '3' or '57'."
        elif type is "list":
            print "I suggest using values from this list: %s" % ', '.join(listname)
        else:
            print question
        answer = raw_input(">")
        return answer

    commands = {
        "help": help_command,
        "change": change_command,
    }

    def run_command(self, command_name, *arg, **kwargs):
        print "A %s will be run. Eventually." % command_name
        self.commands[command_name](self, *arg, **kwargs)


alist = ['one', 'two', 'gods', "why"]

b = Console()
# answer = raw_input(">")
answer = "help"
b.run_command(answer, "list", alist, True)
