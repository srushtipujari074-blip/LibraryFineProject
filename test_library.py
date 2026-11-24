import pytest
from library import days_late, fine, is_overdue, receipt


def test_days_late_positive():
    assert days_late("01-11-2026", "06-11-2026") == 5


def test_days_late_zero():
    assert days_late("01-11-2026", "01-11-2026") == 0


def test_days_late_before_due_date():
    assert days_late("10-11-2026", "05-11-2026") == 0


def test_fine_for_five_days():
    assert fine(5) == 10


def test_fine_for_zero_days():
    assert fine(0) == 0


def test_fine_negative_days_raises_error():
    with pytest.raises(ValueError):
        fine(-1)


def test_is_overdue_true():
    assert is_overdue("01-11-2026", "02-11-2026") is True


def test_is_overdue_false():
    assert is_overdue("01-11-2026", "01-11-2026") is False


def test_receipt_contains_fine():
    result = receipt("01-11-2026", "06-11-2026")
    assert "Total fine: Rs. 10" in result