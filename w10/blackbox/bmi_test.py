import bmi

def test_bmi():
  value = bmi.bmi(80, 180)
  assert value == 24.69

def test_bmi_to_text():
  text = bmi.bmi_to_text(24.69)
  assert text == "you are normal weight"
