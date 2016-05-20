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

    def get_answer(self):
        return raw_input(">")

    def display_text(self, text):
        print text

# class Engine(object):
#     def __init__(self, current_question, next_question):
#         self.current_question = current_question
#         self.next_question = next_question
#
#     def start(self):
#         current_question = start_question


