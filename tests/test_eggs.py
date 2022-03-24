import pytest
from tasks.eggs import eggs_solution
from jkg_evaluators import eggdrop_100floor_2egg

class TestEggs(object):
    def test_1(self):
        print(eggdrop_100floor_2egg.evaluate(eggs_solution))
        assert eggdrop_100floor_2egg.evaluate(eggs_solution, return_output = True) == True