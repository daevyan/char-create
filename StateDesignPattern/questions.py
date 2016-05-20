from console import Console
from validator import *


class Answers(object):
    def __init__(self, char_appearance=None, char_pronoun=None):
        self.char_appearance = char_appearance
        self.char_appearance = {}
        self.char_pronoun = char_pronoun
        self.char_pronoun = []

    def get_gender_pronoun(self):
        if self.char_appearance["gender"] is "male":
            pronoun = ["he", "him", "his"]
        elif self.char_appearance["gender"] is "female":
            pronoun = ["she", "her", "hers"]
        else:
            pronoun = None
            print "Cannot set pronoun"
        return pronoun

    def set_gender_pronoun(self):
        gender_pronoun = self.get_gender_pronoun()
        self.char_pronoun = gender_pronoun

    def set_answer(self, question, answer):
        self.char_appearance[question] = answer


class Questions(object):
    def __init__(self, question_text, confirmation_text, error_text, validator):
        self.question_text = question_text
        self.confirmation_text = confirmation_text
        self.error_text = error_text
        self.validator = validator

    answers = Answers()
    console = Console()
    question_modules = {
        "appearance": Appearance(None, None, None),
        "personality": Personality(None, None, None),
        "background": Background(None, None, None)
    }

    # opening_question = "name"

    def get_current_question(self):
        
        return "question_key"

    def ask_question(self):
        self.console.display_text(self.question_text)
        question = self.get_current_question()
        while True:
            try:
                answer = self.console.get_answer()
            except Validator:
                self.console.display_text(self.error_text)
            else:
                self.answers.set_answer(answer)


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

    # validators['age'].validate(2234)

    # def get_question_list(self):
    #     return True
    #
    # def opening_question(self):
    #     return self.next_question(self.start_question)



# class Enginew(object):
#     def __init__(self, scene_map):
#         self.scene_map = scene_map
#
#     def play(self):
#         current_scene = self.scene_map.opening_scene()
#         last_scene = self.scene_map.next_scene('finished')
#
#         while current_scene != last_scene:
#             next_scene_name = current_scene.enter()
#             current_scene = self.scene_map.next_scene(next_scene_name)
#
#         # be sure to print out the last scene
#         current_scene.enter()
#
#
# class Map(object):
#     scenes = {
#         'central_corridor': CentralCorridor(),
#         'laser_weapon_armory': LaserWeaponArmory(),
#         'the_bridge': TheBridge(),
#         'escape_pod': EscapePod(),
#         'death': Death(),
#         'finished': Finished(),
#     }
#
#     def __init__(self, start_scene):
#         self.start_scene = start_scene
#
#     def next_scene(self, scene_name):
#         val = Map.scenes.get(scene_name)
#         return val
#
#     def opening_scene(self):
#         return self.next_scene(self.start_scene)


class Appearance(Questions):
    def __init__(self, question_text, confirmation_text, error_text, validator):
        super(Appearance, self).__init__(question_text, confirmation_text, error_text, validator)

    answers = Answers()
    appearance_questions = {
        "name": Questions("Let's start with naming your character:",
                          "Ok, so let's get on with it! We'll start with %s's Appearance, than go through\n"
                          "Personality, and finish with some kind of Background.\n" % answers.char_appearance["name"],
                          "Error, try again",
                          EmptyValidator()
                          ),
        "age": Questions("And how old is your character?",
                         "So, your character is a %s years old." % answers.char_appearance["age"],
                         "Error, try again",
                         AgeValidator()
                         ),

        "gender": Questions("Ok, what is %s's gender?" % answers.char_appearance["name"],
                            "Ah, a %s, OK." % answers.char_appearance["gender"],
                            "Error, try again",
                            ListValidator()
                            )
    }


class Personality(Questions):
    pass


class Background(Questions):
    pass