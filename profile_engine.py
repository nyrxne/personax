class ProfileEngine:
    def __init__(
        self,
        profile,
        health,
        personality,
        recommendations
    ):
        self.profile = profile
        self.health = health
        self.personality = personality
        self.recommendations = recommendations

    def generate(self):
        return {
            "snapshot": f"{self.profile.name} is an aspiring {self.profile.occupation} passionate about {self.profile.favorite_language}.",

            "health_summary":
                f"BMI: {self.health.bmi()} ({self.health.bmi_category()})",

            "strengths":
                self.profile.skills[:3],

            "areas_to_improve":
                self.recommendations.next_skills(),

            "career_potential":
                self.recommendations.career_suggestions(),

            "quote":
                "Your future is built by what you do consistently."
        }