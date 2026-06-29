class RecommendationEngine:
    def __init__(self, profile):
        self.profile = profile

    def career_suggestions(self):
        mapping = {
            "Python": ["Data Scientist", "AI Engineer"],
            "JavaScript": ["Frontend Developer", "Fullstack Developer"],
            "C++": ["Game Developer", "Systems Engineer"]
        }

        return mapping.get(
            self.profile.favorite_language,
            ["Software Engineer"]
        )

    def next_skills(self):
        return [
            "Cloud Computing",
            "System Design",
            "Machine Learning"
        ]

    def roadmap(self):
        return [
            "Foundation",
            "Intermediate",
            "Advanced",
            "Specialization",
            "Mastery"
        ]