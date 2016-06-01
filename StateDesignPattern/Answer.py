from console import Console
from pprint import pprint
import os.path
import json


class Answer(object):
    def __init__(self):
        self.char_answers = {}
        self.char_gender_pronoun = []
        self.console = Console()

    save_path = "C:\Users\Anka\PycharmProjects\CharGen\StateDesignPattern\characters\\"

    """ ------------------ General ------------------- """
    def set_answer(self, question_name, answer):
        self.char_answers[question_name] = answer
        if question_name == "gender":
            self.set_gender_pronoun()
        elif question_name == "age":
            self.set_stage(answer)

    """ -------------------- Save --------------------- """

    def save_to_text_file(self):
        file_name = os.path.join(self.save_path, self.char_answers["name"] + ".txt")
        text_file = open(file_name, "w")

        text_file.write("Character: %s\n\n" % self.char_answers["name"])
        for k, v in self.char_answers.iteritems():
            if k == "gender_pronoun" or k == "stage":
                pass
            else:
                text_file.write(k + ": " + v + "\n")
        text_file.close()

    def save_dict(self):
        file_name = os.path.join(self.save_path, self.char_answers["name"] + ".json")

        with open(file_name, "w") as text_file:
            json.dump(self.char_answers, text_file, indent=4)

    """ -------------------- Load --------------------- """

    def load_from_file(self):
        self.console.display_text("Which character do you wish to load?")
        while True:
            try:
                file_name = str(self.save_path + raw_input(">") + ".json")
                with open(file_name, 'r') as json_data:
                    self.char_answers = json.load(json_data)
            except IOError:
                self.console.display_text("No such character file exists. Try again.")
            else:
                break
        self.set_gender_pronoun()
        pprint(self.char_answers)
        pprint(self.char_gender_pronoun)

    """ ------------------- Gender ------------------- """

    @staticmethod
    def get_gender_pronoun(gender):
        if gender == 'male':
            pronoun = ["he", "him", "his"]
        elif gender == 'female':
            pronoun = ["she", "her", "hers"]
        else:
            pronoun = None
            print "Cannot set gender pronoun"
        return pronoun

    def set_gender_pronoun(self):
        gender = self.char_answers["gender"]
        gender_pronoun = self.get_gender_pronoun(gender)
        self.char_gender_pronoun = gender_pronoun

    """ ------------------- Age ------------------- """

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
            if int(value) in range_value:
                return range_name
        else:
            self.console.display_text("Something, somewhere went awfully wrong. Sorry. %r not a value I can take."
                                      % value)
            return False

    def get_stage(self, age):
        stage = self.get_range(age, self.age_stages)
        return stage

    def set_stage(self, age):
        stage = self.get_stage(age)
        self.char_answers["stage"] = stage

# a = Answer()
# a.load_from_file()

"""omg"""

a = Answer()
print a.char_answers
print a.char_gender_pronoun

# class AnswerSaverJinja(object):
#
#     TEMPLATE_FILE = 'template.html'
#
#     TEMPLATE_CONTENT = """
# <html>
#     <head></head>
#     <body>
#         <h1>Hello {{ name if name else 'UNKNOWN NAME'}}</h1>
#         gender: {{ gender if gender else 'UNKNOWN GENDER' }}
#         age: {{ age if age else 'UNKNOWN AGE' }}
#
#         {% for dict_item in answer_dict %}
#            {% for key, value in dict_item.items() %}
#               <h1>Key: {{key}}</h1>
#               <h2>Value: {{value}}</h2>
#            {% endfor %}
#         {% endfor %}
#
#     </body>
# </html>
# """\
#
#     answer_dict = {'gender': 'female', 'age': '64', 'name': 'Whatever', 'stage': 'middle aged'}
#     @staticmethod
#     def save(answer_dict, filename):
#         env = Environment(loader=DictLoader({AnswerSaverJinja.TEMPLATE_FILE: AnswerSaverJinja.TEMPLATE_CONTENT}))
#         template = env.get_template(AnswerSaverJinja.TEMPLATE_FILE)
#         template.render(answer_dict)
#
#         with open(filename, 'w') as outfile:
#             outfile.write(template.render(answer_dict))
#
# answers = Answer()
# answers.char_appearance['name'] = 'Euzebiusz'
# AnswerSaverJinja.save(AnswerSaverJinja().answer_dict, 'test_jinja.html')