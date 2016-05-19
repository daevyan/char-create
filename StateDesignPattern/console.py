from state import *


class Console(object):
    """ This is what the user sees, kinda. And what he can do. He can input text, that is a correct or incorrect answer,
    or a command"""
    def __init__(self):
        self.question_asked = QuestionAsked(Console)
        self.answer_sent = AnswerSent(Console)
        self.command_answer = CommandAnswer(Console)
        self.incorrect_answer = IncorrectAnswer(Console)
        self.correct_answer = CorrectAnswer(Console)
        self.state = self.question_asked

    pass
