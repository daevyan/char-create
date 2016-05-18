
class Appearance(object):

    def __init__(self, char_appearance=None, char_pronoun=None):
        self.char_appearance = char_appearance
        self.char_appearance = {}
        self.char_pronoun = char_pronoun
        self.char_pronoun = []

    age_stages = {
        "a kid": range(5, 11),
        "a teen": range(11, 18),
        "a young adult": range(18, 26),
        "an adult": range(26, 40),
        "middle aged": range(40, 66),
        "elderly": range(66, 121)
    }
    gender_list = ['male', 'female']
    height_list = ['tall', 'of average height', 'short']
    build_list = ['slim', 'fat']
    trait_texts = {
        "age": "So, your character is a %s years old. That would make %s %s."
    }


    help = {
        "int": "one",
        "list": "two",
        "other": "three"
    }

    c_number = "number"
    c_list = "list"
    command_texts = {
        "help": ["help", "?", "halp"],
        "change": ["change", "rename", "modify"],
        "repeat": ["repeat", "instruction"]
    }

    def help_command(self, data_type, list_name=None):
        if data_type is "number":
            print "You should write an integer - not text, not a floating number."
            print "No fractions. Or whitespaces. An integer. Like '3' or '57'."
        elif data_type is "list":
            print "I suggest using values from this list: %s" % ', '.join(list_name)
        else:
            pass
        answer = raw_input(">")
        return answer

    def console_cmd(self, answer):
        command_name, is_cmd = self.check_if_cmd(answer)
        if is_cmd:
            return self.run_command(command_name)
        else:
            return answer

    def run_command(self, command_name, *arg, **kwargs):
        print "A %s will be run. Eventually." % command_name
        self.commands[command_name](*arg, **kwargs)
        answer = raw_input(">")
        return answer

    def check_if_cmd(self, answer):
        for command_name, v in self.command_texts.iteritems():
            values = v
            if answer in values:
                print "It's a command"
                return command_name, True
            else:
                pass
        print "Not a command"
        return answer, False


# needs moving, change, deletion
    def console(self, data_type=None, list_name=None):
        answer = raw_input(">")
        if data_type is "list":
            while True:
                self.console_cmd()
                # if answer in self.help_cmds:
                #     self.help_command(data_type, list_name)
                if answer in list_name:
                    return answer
                else:
                    print "Sorry, your answer is not valid. Please try again or type '?' for help"
                    answer = raw_input(">")

        elif data_type is "number":
            while True:
                if answer in self.help_cmds:
                    self.help_command(data_type)
                elif answer in list_name:
                    return answer
                else:
                    print "Sorry, your answer is not valid. Please try typing an integer."

        else:
            while True:
                if answer in self.help_cmds:
                    self.help_command(data_type)
                else:
                    return answer

    def change_command(self):
        pass

    """ AGE methods """

    def get_range(self, value, range_dict):
        for range_name, range_value in range_dict.iteritems():
            if value in range_value:
                return range_name
        raise ValueError("Something, somwhere went awfully wrong. Sorry. %r not a value I can take."
                         % value)

    def age_console(self):
        print "And how old is your character?"
        while True:
            try:
                age = int(raw_input(">"))
            except ValueError:
                print("That's either not a whole number or not a number at all! Try again.")
            else:
                if age in range(5, 121):
                    stage = self.get_range(age, self.age_stages)
                    print "So, your character is a %s years old. That would make %s %s."\
                          % (age, self.char_pronoun[1], stage)
                    return age, stage
                elif 0 >= age:
                    print "Come on. A positive number, please?"
                elif 5 > age:
                    print "Come on. You want a full character creation for a %r year old?\n" \
                          "Well, not in this creator." % age
                else:
                    print "Come on, %r? Humans don't live that long... yet.\n" \
                          "And it's a human character generator." % age

    def age(self):
        age, stage = self.age_console()
        self.char_appearance["age"] = age
        self.char_appearance["stage"] = stage

    """ OTHER methods"""

    def gender(self):
        print "Ok, what is %s's gender?" % self.char_appearance["name"]
        gender = self.console("list", self.gender_list)
        print "A %s. OK.\n" % gender
        self.char_appearance["gender"] = gender
        self.char_pronoun = self.get_gender_pronoun(gender)

    def get_gender_pronoun(self, gender):
        if gender == "male":
            pronoun = ["he", "him", "his"]
        else:
            pronoun = ["she", "her", "hers"]
        return pronoun

    def name(self):
        print "First of all name your character."
        name = raw_input(">")
        print "Ok, so let's get on with it! We'll start with %s's Appearance, than go through\n" \
              "Personality, and finish with some kind of Background.\n" % name
        self.char_appearance["name"] = name
        return name

    def height(self):
        print "We're getting to appearane now.\n"
        print "What is your height?"
        height = self.console("list", self.height_list)
        self.char_appearance["height"] = height
        print "Got it."

    def build(self):
        print "How is %s built?" % self.char_pronoun[0]
        build = self.console("list", self.build_list)
        self.char_appearance["build"] = build
        print "Got it."

    def appearance(self):
        self.name()
        self.gender()
        self.age()
        self.height()
        self.build()


    commands = {
        "help": help_command,
        "change": change_command
    }
a = Appearance()
# a.console("Text to print")
a.appearance()
print "Here is the character you created:"
print "Name: %s" % a.char_appearance["name"]
print "Gender: %s" % a.char_appearance["gender"]
print "Age: %s, %s" % (a.char_appearance["age"], a.char_appearance["stage"])
print "Build and height: %s is %s and of %s build" % ((str(a.char_pronoun[0])).title, a.char_appearance["height"], a.char_appearance["build"])

print a.char_appearance
print a.char_pronoun

# REMOVE NAME FROM HERE, GET IT SOMEWHERE ELSE MBY?
# GET THAT TITLE SHIT ON 140 RIGHT


# print "The question of gender. Here it's just biological gender, ok?\n" \
#       "I really don't want to go into all of the intricacies of the different labels,\n" \
#       "names, and the overall fluidity of this subject.\n" \
#       "Just 'male' or 'female' please, and You'll take care of the rest\n" \
#       "in Personality or Background room, later."