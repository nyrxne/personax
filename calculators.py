class HealthCalculator:
    def __init__(self, profile):
        self.profile = profile

    def bmi(self):
        h = self.profile.height / 100
        return round(self.profile.weight / (h*h), 2)

    def bmi_category(self):
        bmi = self.bmi()

        if bmi < 18.5:
            return "Underweight"
        elif bmi < 25:
            return "Healthy"
        elif bmi < 30:
            return "Overweight"
        return "Obese"

    def age_months(self):
        return self.profile.age * 12

    def age_days(self):
        return self.profile.age * 365

    def water_requirement(self):
        return round(self.profile.weight * 0.033, 2)

    def max_heart_rate(self):
        return 220 - self.profile.age

    def sleep_duration(self):
        if self.profile.age < 18:
            return "8-9 hrs"
        return "7-8 hrs"