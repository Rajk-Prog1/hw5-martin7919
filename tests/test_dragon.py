import pytest
from tasks.dragon import dragon_solution
from jkg_evaluators import dragonfind_10_to_500

class TestDragon(object):
    def test_1(self):
        print(dragonfind_10_to_500.evaluate(dragon_solution))
        assert dragonfind_10_to_500.evaluate(dragon_solution, return_output = True) == True