class PersonalityEngine:
    def __init__(self, profile):
        self.profile = profile

    def analyze(self):
        skill_count = len(self.profile.skills)

        return {
            "Analytical": min(skill_count * 15, 100),
            "Creativity": len(self.profile.hobbies) * 20,
            "Leadership": 70 if "leader" in self.profile.occupation.lower() else 40,
            "Discipline": 80 if self.profile.career_goals else 50,
            "Adaptability": 75
        }