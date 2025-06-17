import pytest
import random

from algorithms import dynamicSolver, bruteForceSolver

@pytest.fixture
def sample_items():
    return {
        0: {'value': 60, 'weight': 10},
        1: {'value': 100, 'weight': 20},
        2: {'value': 120, 'weight': 30}
    }

def test_dynamic_solver(sample_items):
    capacity = 50
    max_profit, selected_items = dynamicSolver(sample_items, capacity)

    assert max_profit == 220
    assert set(selected_items) == {1, 2}

def test_brute_force_solver(sample_items):
    capacity = 50
    max_profit, selected_items = bruteForceSolver(sample_items, capacity)

    assert max_profit == 220
    assert set(selected_items) == {1, 2}

def test_random_problem_agreement():
    n = 8
    capacity = random.randint(20, 100)
    items = {i: {'value': random.randint(10, 100), 'weight': random.randint(1, 20)} for i in range(n)}

    dynamic_result = dynamicSolver(items, capacity)
    brute_result = bruteForceSolver(items, capacity)

    assert dynamic_result[0] == brute_result[0]
    assert sum(items[i]['value'] for i in dynamic_result[1]) == brute_result[0]
    assert sum(items[i]['value'] for i in brute_result[1]) == brute_result[0]
