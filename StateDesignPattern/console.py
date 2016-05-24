class Console(object):
    """ This is what the user sees, kinda. And what he can do. He can input text, that is a correct or incorrect answer,
    or a command"""

    def get_answer(self):
        answer = raw_input(">")
        return answer

    def display_text(self, text):
        print text
