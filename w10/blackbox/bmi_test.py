import bmi

#<18.5
#<24.9
#<29.9
#>29.9


def test_bmi():
  value = bmi.bmi(80, 180)
  assert value == 24.7
  value = bmi.bmi(65, 180)
  assert value == 20.1
  value = bmi.bmi(55, 165)
  assert value == 20.2
  value = bmi.bmi(75, 165)
  assert value == 27.5
  value = bmi.bmi(105, 170)
  assert value == 36.3

def test_bmi_underweight():
  correct = "you are underweight"
  text = bmi.bmi_to_text(18)
  assert text == correct
  text = bmi.bmi_to_text(18.4)
  assert text == correct
  text = bmi.bmi_to_text(18.49999999999)
  assert text == correct
  text = bmi.bmi_to_text(18.5)
  assert text != correct

def test_bmi_normal():
  correct = "you are normal weight"
  text = bmi.bmi_to_text(18.4)
  assert text != correct
  text = bmi.bmi_to_text(18.5)
  assert text == correct
  text = bmi.bmi_to_text(20)
  assert text == correct
  text = bmi.bmi_to_text(24.8999999999)
  assert text == correct
  text = bmi.bmi_to_text(24.9)
  assert text != correct

def test_bmi_overweight():
  correct = "you are overweight"
  text = bmi.bmi_to_text(24.8999)
  assert text != correct
  text = bmi.bmi_to_text(24.9)
  assert text == correct
  text = bmi.bmi_to_text(28)
  assert text == correct
  text = bmi.bmi_to_text(29.89999999)
  assert text == correct
  text = bmi.bmi_to_text(29.9)
  assert text != correct

def test_bmi_obese():
  correct = "you are obese"
  text = bmi.bmi_to_text(29.89)
  assert text != correct
  text = bmi.bmi_to_text(29.9)
  assert text == correct
  text = bmi.bmi_to_text(100)
  assert text == correct
