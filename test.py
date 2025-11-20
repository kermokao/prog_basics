"""Tests for solution."""
from solution import students_study, lottery, fruit_order


def test__students_study__night_with_coffee__no_studying():
    """During night with coffee students do not study."""
    assert students_study(3, True) is False


def test__students_study__night_without_coffee__no_studying():
    """During night with coffee students do not study."""
    assert students_study(3, False) is False


def test__students_study__night_coffee_true():
    """During night with coffee students do not study."""
    assert students_study(6, True) is True


def test__students_study__day_coffee_true():
    """During night with coffee students do not study."""
    assert students_study(6, False) is False


def test__students_study__evening_coffee_false():
    """During night with coffee students do not study."""
    assert students_study(20, False) is True


def test__students_study__evening_coffee_true():
    """During night with coffee students do not study."""
    assert students_study(20, True) is True


def test__students_study__evening_edge_case_coffee_true():
    """During night with coffee students do not study."""
    assert students_study(24, True) == students_study(18, True) is True


def test__students_study__evening_edge_case_coffee_false():
    """During night with coffee students do not study."""
    assert students_study(24, False) == students_study(18, False) is True


def test__students_study__night_edge_case_coffee_true():
    """During night with coffee students do not study."""
    assert students_study(1, True) == students_study(4, True) is False


def test__students_study__night_edge_case_coffee_false():
    """During night with coffee students do not study."""
    assert students_study(1, False) == students_study(4, False) is False


def test__students_study__day_edge_case_coffee_true():
    """During night with coffee students do not study."""
    assert students_study(5, True) == students_study(17, True) is True


def test__students_study__day_edge_case_coffee_false():
    """During night with coffee students do not study."""
    assert students_study(5, False) == students_study(17, False) is False


def test__lottery__all_fives():
    """During night with coffee students do not study."""
    assert lottery(5, 5, 5) == 10


def test__lottery__all_same_positive():
    """During night with coffee students do not study."""
    assert lottery(4, 4, 4) == 5


def test__lottery__all_same_negative():
    """During night with coffee students do not study."""
    assert lottery(-2, -2, -2) == 5


def test__lottery__all_same_zero():
    """During night with coffee students do not study."""
    assert lottery(0, 0, 0) == 5


def test__lottery__a_b_same_c_diff():
    """During night with coffee students do not study."""
    assert lottery(5, 5, 4) == 0


def test__lottery__a_c_same_b_diff():
    """During night with coffee students do not study."""
    assert lottery(5, 4, 5) == 0


def test__lottery__b_c_same_a_diff():
    """During night with coffee students do not study."""
    assert lottery(5, 4, 4) == 1


def test__lottery__all_diff():
    """."""
    assert lottery(3, 6, 4) == 1


def test__fruit_order__all_zero():
    """."""
    assert fruit_order(0, 0, 0) == 0


def test__fruit_order__zero_amount_zero_small():
    """."""
    assert fruit_order(0, 3, 0) == 0


def test__fruit_order__zero_amount_zero_big():
    """."""
    assert fruit_order(3, 0, 0) == 0


def test__fruit_order__zero_amount_others_not_zero():
    """."""
    assert fruit_order(3, 3, 0) == 0


def test__fruit_order__only_big_exact_match():
    """."""
    assert fruit_order(0, 1, 5) == 0


def test__fruit_order__only_big_not_enough_but_multiple_of_5():
    """."""
    assert fruit_order(0, 1, 10) == -1


def test__fruit_order__only_big_more_than_required_match():
    """."""
    assert fruit_order(0, 2, 5) == 0


def test__fruit_order__only_big_more_than_required_no_match():
    """."""
    assert fruit_order(0, 2, 7) == -1


def test__fruit_order__only_small_match_more_than_5_smalls():
    """."""
    assert fruit_order(10, 0, 10) == 10


def test__fruit_order__only_small_not_enough_more_than_5_smalls():
    """."""
    assert fruit_order(6, 0, 7) == -1


def test__fruit_order__only_small_more_than_required():
    """."""
    assert fruit_order(10, 0, 5) == 5


def test__fruit_order__match_with_more_than_5_smalls():
    """."""
    assert fruit_order(5, 1, 10) == 5


def test__fruit_order__match_with_more_than_5_smallls():
    """."""
    assert fruit_order(6, 1, 11) == 6


def test__fruit_order__use_all_smalls_some_bigs():
    """."""
    assert fruit_order(4, 3, 14) == 4


def test__fruit_order__use_some_smalls_all_bigs():
    """."""
    assert fruit_order(4, 2, 12) == 2


def test__fruit_order__use_some_smalls_some_bigs():
    """."""
    assert fruit_order(10, 3, 13) == 3


def test__fruit_order__not_enough():
    """."""
    assert fruit_order(3, 3, 40) == -1


def test__fruit_order__enough_bigs_not_enough_smalls():
    """."""
    assert fruit_order(2, 2, 8) == -1


def test__fruit_order__not_enough_with_more_than_5_smalls():
    """."""
    assert fruit_order(6, 2, 18) == -1


def test__fruit_order__enough_bigs_not_enough_smalls_large_numbers():
    """."""
    assert fruit_order(2, 600, 1158) == -1


def test__fruit_order__match_large_numbers():
    """."""
    assert fruit_order(200, 200, 1200) == 200