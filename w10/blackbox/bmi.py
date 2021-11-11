#!/usr/bin/python3

def bmi(w, h):
  return round(w/(h/100)**2, 2)

def bmi_to_text(bmi_value):
  if bmi_value<18.5:
    return "you are underweight"
  elif bmi_value<24.9:
    return "you are normal weight"
  elif bmi_value<29.9:
    return "you are overweight"
  else:
    return "you are obese"


def main():
  weight = int(input("weight in kg: "))
  height = int(input("height in cm: "))

  bmi_value = bmi(weight, height)
  print(f"bmi: {bmi_value}")
  print(bmi_to_text(bmi_value))


if __name__ == "__main__":
  main()
