
import pytest
from unittest.mock import Mock
from order import (
    calculate_total,
    can_accept_order,
    process_payment
)


# Test 1: Bill below ₹300
def test_bill_below_300():
    assert calculate_total(200) == 210.00


# Test 2: Bill exactly ₹300
def test_bill_exactly_300():
    assert calculate_total(300) == 315.00


# Test 3: Bill above ₹300
def test_bill_above_300():
    assert calculate_total(400) == 378.00


# Test 4: Zero bill
def test_zero_bill():
    assert calculate_total(0) == 0.00


# Test 5: Negative bill
def test_negative_bill():
    with pytest.raises(ValueError):
        calculate_total(-100)


# Test 6: Empty pickup slot
def test_empty_slot():
    assert can_accept_order(0) is True


# Test 7: Slot with 39 orders
def test_39_orders():
    assert can_accept_order(39) is True


# Test 8: Slot with 40 orders
def test_40_orders():
    assert can_accept_order(40) is False


# Test 9: Slot with 41 orders
def test_41_orders():
    assert can_accept_order(41) is False


# Test 10: Successful payment
def test_successful_payment():
    fake_gateway = Mock()
    fake_gateway.charge.return_value = True

    result = process_payment(fake_gateway, 378.00)

    assert result is True
    fake_gateway.charge.assert_called_once_with(378.00)


# Test 11: Failed payment
def test_failed_payment():
    fake_gateway = Mock()
    fake_gateway.charge.return_value = False

    result = process_payment(fake_gateway, 378.00)

    assert result is False

# Test 12: Negative order count is rejected
def test_negative_order_count():
    with pytest.raises(ValueError):
        can_accept_order(-1)


# Test 13: Negative payment amount is rejected
def test_negative_payment():
    fake_gateway = Mock()

    with pytest.raises(ValueError):
        process_payment(fake_gateway, -50)

    fake_gateway.charge.assert_not_called()
