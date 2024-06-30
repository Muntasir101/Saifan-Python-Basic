# BMI (Body Mass Index)
height_meter = 1.76
weight_kg = 75

BMI = weight_kg / height_meter ** 2
print("Actual:", BMI)
formatted_BMI = f"{BMI:.3f}"
print("Formatted: ", formatted_BMI)
print("Round: ", round(BMI))