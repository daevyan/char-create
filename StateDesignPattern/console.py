class Console(object):
    """ This is what the user sees, kinda. And what he can do. He can input text, that is a correct or incorrect answer,
    or a command"""

    @staticmethod
    def get_answer():
        answer = raw_input(">")
        return answer

    @staticmethod
    def display_text(text):
        print text
