from console import *

class State(object):
    pass


class QuestionAsked(State):
    """ A state for idle user.
    Totally not sure, if necessary"""
    def __init__(self, console):
        self.console = console
        self.question_asked_value = False
        self.answer_sent_value = False
        self.correct_answer_value = False
        self.incorrect_answer_value = False
        self.command_answer_value = False
        self.question_answered = False

    # after transitioning from question asked, question_asked needs to change to True

    def get_answer(self):
        answer = raw_input()
        self.question_asked_value = True
        self.console.state = self.console.answer_sent
        return answer


class AnswerSent(State):
    """Can be idle = False? or sent = True?
    When answer is sent, evaluate whether correct, incorrect or command answer.
    """
    def __init__(self, console):
        self.console = console
        self.question_asked_value = True
        self.answer_sent_value = False
        self.correct_answer_value = False
        self.incorrect_answer_value = False
        self.command_answer_value = False

    def check_answer(self):
        if answer is correct_answer:
            self.console.state = self.console.correct_answer
        elif answer is command_answer:
            self.console.state = self.console.command_answer
        else:  # answer is incorrect_answer:
            self.console.state = self.console.incorrect_answer

        self.answer_sent_value = True

# after transitioning from answer sent, answer_sent needs to change to True


class CorrectAnswer(State):
    """If answer is correct:
    - add answer to dictionary under question key.
    - run next question
    - (optional) print answer, so that user sees if a typo was made, answer is satisfactory etc."""

    def __init__(self, console):
        self.console = console
        self.question_asked_value = True
        self.answer_sent_value = True
        self.correct_answer_value = True
        self.incorrect_answer_value = False
        self.command_answer_value = False

    def add_answer_to_dict(self):
        pass

    def go_to_next_question(self):
        self.console.state = self.console.question_asked

        self.question_asked_value = False
        self.answer_sent_value = False
        self.correct_answer_value = False
        self.incorrect_answer_value = False
        self.command_answer_value = False

# after transitioning from correct answer, all values need to reset to False


class IncorrectAnswer(State):
    """If an answer is incorrect, open another input in console for the current question"""

    def __init__(self, console):
        self.console = console
        self.question_asked_value = True
        self.answer_sent_value = True
        self.correct_answer_value = False
        self.incorrect_answer_value = True
        self.command_answer_value = False

    # after transitioning from incorrect answer, incorrect_answer and answer_sent need to reset to False

    def go_to_current_question(self):
        self.console.state = self.console.question_asked

        self.question_asked_value = False
        self.answer_sent_value = False
        self.correct_answer_value = False
        self.incorrect_answer_value = False
        self.command_answer_value = False


class CommandAnswer(State):
    """If command answer was given:
     - run specified command
     - open another input in the console for the current question"""

    def __init__(self, console):
        self.console = console
        self.question_asked_value = True
        self.answer_sent_value = True
        self.correct_answer_value = False
        self.incorrect_answer_value = False  # after transitioning from incorrect answer, value needs to reset to False
        self.command_answer_value = True

    # after transitioning from command answer, command answer and answer_sent need to reset to False
