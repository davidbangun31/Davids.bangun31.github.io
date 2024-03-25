class BMICalculator:
    def __init__(self, weight_pounds, height_feet):
        self.weight_pounds = weight_pounds
        self.height_feet = height_feet

    def calculate_bmi(self):
        weight_kg = self.weight_pounds * 0.453592  # konversi pound ke kilogram
        height_meters = self.height_feet * 0.3048  # konversi feet ke meter
        bmi = weight_kg / (height_meters ** 2)
        return bmi

    def bmi_status(self, bmi):
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi < 25:
            return "Normal weight"
        elif 25 <= bmi < 30:
            return "Overweight"
        else:
            return "Obesity"

    def display_bmi_info(self):
        bmi = self.calculate_bmi()
        status = self.bmi_status(bmi)
        print(f"Weight: {self.weight_pounds} pounds")
        print(f"Height: {self.height_feet} feet")
        print(f"BMI: {bmi:.2f}")
        print(f"Status: {status}")


# Input berat dan tinggi dari pengguna
weight = float(input("Enter your weight in pounds: "))
height = float(input("Enter your height in feet: "))

# Membuat instance BMICalculator
calculator = BMICalculator(weight, height)

# Menampilkan informasi BMI
calculator.display_bmi_info()
