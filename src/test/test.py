import pytest
from main import DiningExperienceManager

def test_valid_order_and_total_cost():
    dining_manager = DiningExperienceManager()

    # Mock user input for the test
    inputs = [
        "Burger", "3",    # Order 3 Burgers
        "Pizza", "5",     # Order 5 Pizzas
        "Big Mac 1", "2",  # Order 2 Special Meal 1 (with 5% surcharge)
        "done"
    ]
    dining_manager.get_valid_quantity = lambda: int(inputs.pop(0))
    dining_manager.input = lambda _: inputs.pop(0)

    total_cost = dining_manager.run()
    assert total_cost == 43  # 3*5 + 5*5 + (2*10)*(1+0.05)


def test_order_cancellation():
    dining_manager = DiningExperienceManager()

    # Mock user input for the test
    inputs = [
        "done"
    ]
    dining_manager.input = lambda _: inputs.pop(0)

    total_cost = dining_manager.run()
    assert total_cost == -1


def test_invalid_meal_selection():
    dining_manager = DiningExperienceManager()

    # Mock user input for the test
    inputs = [
        "Invalid Meal",  # Invalid meal selection
        "done"
    ]
    dining_manager.input = lambda _: inputs.pop(0)

    total_cost = dining_manager.run()
    assert total_cost == -1

def test_invalid_quantity_input():
    dining_manager = DiningExperienceManager()

    # Mock user input for the test
    inputs = [
        "Burger", "invalid", "3",  # Invalid quantity, then order 3 Burgers
        "done"
    ]
    dining_manager.get_valid_quantity = lambda: int(inputs.pop(0))
    dining_manager.input = lambda _: inputs.pop(0)

    total_cost = dining_manager.run()
    assert total_cost == 15  # 3*5