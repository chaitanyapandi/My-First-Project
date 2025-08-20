# BMI Calculator in Python

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        return f"Your BMI is {bmi:.2f} → Underweight"
    elif 18.5 <= bmi < 24.9:
        return f"Your BMI is {bmi:.2f} → Normal weight"
    elif 25 <= bmi < 29.9:
        return f"Your BMI is {bmi:.2f} → Overweight"
    else:
        return f"Your BMI is {bmi:.2f} → Obese"

# Example usage
print(calculate_bmi(60, 1.65))  # 60kg, 1.65m
