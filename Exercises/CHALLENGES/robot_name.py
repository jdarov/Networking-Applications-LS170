import random
import string

class Robot:

    USED_NAMES = set()

    def __init__(self):
        self._name = self._generate_unique_name()

    @property
    def name(self):
        return self._name

    def _generate_name(self):

        first_two_letters = (
            ''.join(random.choices(string.ascii_uppercase, k=2))
        )
        second_three_numbers = (
            ''.join(random.choices(string.digits, k=3))
        )

        return first_two_letters + second_three_numbers

    def _generate_unique_name(self):
        while True:
            name = self._generate_name()
            if name not in Robot.USED_NAMES:
                Robot.USED_NAMES.add(name)
                return name

    def reset(self):
        Robot.USED_NAMES.remove(self.name)
        self._name = self._generate_unique_name()
