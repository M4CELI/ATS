import math


class Gradebook:
    def __init__(self):
        self._subjects = []
        self._subjects_grades = {}

    def add_subject(self, subject):
        if subject in self._subjects_grades:
            raise ValueError(f"{subject} already exists")
        self._subjects.append(subject)
        self._subjects_grades[subject] = []

    def add_grade(self, subject, grade):
        if subject not in self._subjects_grades:
            raise ValueError(f"{subject} not found in list of subjects")
        self._subjects_grades[subject].append(grade)

    def calc_avg_for_subject(self, subject):
        if subject not in self._subjects_grades:
            raise ValueError("Subject not in subjects")
        grades = self._subjects_grades[subject]
        if not grades:
            raise ValueError("No grades found for subject")
        return self._round2(sum(grades) / len(grades))

    def calc_avg_for_all_subjects(self):
        return {
            subject: self.calc_avg_for_subject(subject)
            for subject in self._subjects
            if self._subjects_grades[subject]
        }

    def get_subjects(self):
        return list(self._subjects)

    def get_grades(self):
        return {s: list(g) for s, g in self._subjects_grades.items()}

    @staticmethod
    def _round2(value):
        # zaokrąglenie "half up" jak Math.round w Javie (round() w Pythonie zaokrągla do parzystej)
        return math.floor(value * 100 + 0.5) / 100