from models import Duty

def test_duty_can_display_name():
    duty = Duty(1, "Test 1")
    assert duty.get_name() == "Duty 1"

    duty = Duty(2, "Test 2")
    assert duty.get_name() == "Duty 2"

def test_duty_can_return_summary():
    duty1 = Duty(1, "Test description 1")
    assert duty1.get_summary() == "Duty 1: Test description 1"
    duty2 = Duty(2, "Test description 2")
    assert duty2.get_summary() == "Duty 2: Test description 2"
    