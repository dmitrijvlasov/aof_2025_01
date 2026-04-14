import pytest
from day_1_task_2 import move_left, move_right, move

testdata_positive = [
    (0, 16, 84, 0),
    (1, 16, 85, 1),
    (1, 1000, 1, 10),
    (0, 999, 1, 10),
    (0, 1001, 99, 10),
]

testdata_negative = [(-1, 12), (1, -12)]

testdata_bad = [(1, "a"), ("a", 1)]


@pytest.mark.parametrize(
    "current_position, step, exp_new_position, exp_zero_count", testdata_positive
)
def test_move_left_positive(current_position, step, exp_new_position, exp_zero_count):
    # arrange + act
    new_position, zero_count = move_left(current_position, step)
    # assert
    assert new_position == exp_new_position, "incorrect new position calculated"
    assert zero_count == exp_zero_count, "incorrect zero count calculated"

# @pytest.mark.parametrize(
#     "current_position, step, exp_new_position, exp_zero_count", testdata_positive
# )
# def test_move_right_positive(current_position, step, exp_new_position, exp_zero_count):
#     # arrange + act
#     new_position, zero_count = move_right(current_position, step)
#     # assert
#     assert new_position == exp_new_position, "incorrect new position calculated"
#     assert zero_count == exp_zero_count, "incorrect zero count calculated"

@pytest.mark.parametrize("current_position, step", testdata_negative)
def test_move_left_negative(current_position, step):

    # arrange + act + assert
    with pytest.raises(ValueError):
        _ = move_left(current_position, step)

@pytest.mark.parametrize("current_position, step", testdata_bad)
def test_move_left_bad(current_position, step):
    # arrange + act + assert
    with pytest.raises(ValueError):
        _ = move_left(current_position, step)

@pytest.mark.parametrize("direction, step", [("L", 1), ("R", 1)])
def test_move_positive(direction, step):

    with pytest.raises(ValueError):
        _ = move(direction, step)

@pytest.mark.parametrize("direction, step", [("S", 1), (1, "S")])    
def test_move_bad(direction, step):
    
    with pytest.raises(ValueError):
        _ = move(direction, step)

# todo: negative example: current_position is negative number
# todo: negative example: bad types
# pytest parametrize
