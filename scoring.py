class ScoreEngine:
    def __init__(self, profile):
        self.profile = profile

    def calculate(self):
        score = 0

        if self.profile.skills:
            score += 30
        if self.profile.hobbies:
            score += 20
        if self.profile.career_goals:
            score += 30
        if self.profile.education:
            score += 20

        return score