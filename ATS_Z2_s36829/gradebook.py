"""Dzienniczek ocen ucznia."""

import math


class Gradebook:
    """Przechowuje przedmioty i oceny oraz liczy średnie."""

    def __init__(self):
        self._subjects = []
        self._subjects_grades = {}

    def add_subject(self, subject):
        """Dodaje nowy przedmiot. Duplikat powoduje ValueError."""
        if subject in self._subjects_grades:
            raise ValueError(f"{subject} already exists")
        self._subjects.append(subject)
        self._subjects_grades[subject] = []

    def add_grade(self, subject, grade):
        """Dodaje ocenę do istniejącego przedmiotu."""
        if subject not in self._subjects_grades:
            raise ValueError(f"{subject} not found in list of subjects")
        self._subjects_grades[subject].append(grade)

    def calc_avg_for_subject(self, subject):
        """Zwraca średnią ocen z przedmiotu zaokrągloną do 2 miejsc."""
        if subject not in self._subjects_grades:
            raise ValueError("Subject not in subjects")
        grades = self._subjects_grades[subject]
        if not grades:
            raise ValueError("No grades found for subject")
        return self._round2(sum(grades) / len(grades))

    def calc_avg_for_all_subjects(self):
        """Zwraca średnie dla wszystkich przedmiotów, które mają oceny."""
        return {
            subject: self.calc_avg_for_subject(subject)
            for subject in self._subjects
            if self._subjects_grades[subject]
        }

    def get_subjects(self):
        """Zwraca kopię listy przedmiotów."""
        return list(self._subjects)

    def get_grades(self):
        """Zwraca kopię słownika ocen."""
        return {s: list(g) for s, g in self._subjects_grades.items()}

    @staticmethod
    def _round2(value):
        # zaokrąglenie "half up" jak Math.round w Javie
        return math.floor(value * 100 + 0.5) / 100
    