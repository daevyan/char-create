class Validator(object):
    def validate(self, value):
        pass


class IntValidator(Validator):
    def validate(self, value):
        pass


class EmptyValidator(Validator):
    def validate(self, value):
        pass


class ListValidator(Validator):
    def validate(self, value):
        pass


class AgeValidator(Validator):
    def validate(self, value):
        return True


validators = {
    'age': AgeValidator(),
    'name': EmptyValidator(),
    'gender': ListValidator()
}

# validators['age'].validate(2234)