
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



# needs moving, change, deletion
    def console(self, listname=None):
        if listname:
            while True:
                answer = raw_input(">")
                if answer in self.help_cmds:
                    self.help_list(answer, listname)
                elif answer in listname:
                    return answer
                else:
                    print "Sorry, your answer is not valid. Please try again or type '?' for help"

        else:
            # just a regular input, with no restrains
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
        # print "The question of gender. Here it's just biological gender, ok?\n" \
        #       "I really don't want to go into all of the intricacies of the different labels,\n" \
        #       "names, and the overall fluidity of this subject.\n" \
        #       "Just 'male' or 'female' please, and You'll take care of the rest\n" \
        #       "in Personality or Background room, later."
        gender = self.console(self.gender_list)
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
        height = self.console(self.height_list)
        self.char_appearance["height"] = height
        print "Got it."

    def build(self):
        print "How is %s built?" % self.char_pronoun[0]
        build = self.console(self.build_list)
        self.char_appearance["build"] = build
        print "Got it."

    def appearance(self):
        self.name()
        self.gender()
        self.age()
        self.height()
        self.build()

# a = Appearance()
# a.new_console("Text to print")
# a.appearance()
# print "Here is the character you created:"
# print "Name: %s" % a.char_appearance["name"]
# print "Gender: %s" % a.char_appearance["gender"]
# print "Age: %s, %s" % (a.char_appearance["age"], a.char_appearance["stage"])
# print "Build and height: %s is %s and of %s build" % ((str(a.char_pronoun[0])).title, a.char_appearance["height"], a.char_appearance["build"])
#
# print a.char_appearance
# print a.char_pronoun

# REMOVE NAME FROM HERE, GET IT SOMEWHERE ELSE MBY?
# GET THAT TITLE SHIT ON 140 RIGHT