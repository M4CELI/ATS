import pytest
from gradebook import Gradebook


@pytest.fixture
def gradebook():
    # odpowiednik @BeforeEach - nowy dzienniczek dla każdego testu
    return Gradebook()


# ---------- Zadanie 1: istniejące testy ----------

def test_add_subject(gradebook):
    gradebook.add_subject("Physics")
    assert gradebook.get_subjects() == ["Physics"]


def test_add_grade_to_subject(gradebook):
    gradebook.add_subject("Math")
    gradebook.add_grade("Math", 5.0)
    assert gradebook.get_grades() == {"Math": [5.0]}


# ---------- Zadanie 1: test dynamiczny dla przedmiotów ----------

SUBJECT_GRADES = {
    "Math": ([5.0, 4.0, 3.5], 4.17),
    "Chemistry": ([3.0, 3.0], 3.0),
    "Biology": ([4.5], 4.5),
    "Physics": ([2.0, 3.0, 4.0, 5.0], 3.5),
    "History": ([4.0, 5.0], 4.5),
}


@pytest.mark.parametrize("subject", list(SUBJECT_GRADES))
def test_dynamic_for_subjects(gradebook, subject):
    for s in SUBJECT_GRADES:
        gradebook.add_subject(s)

    grades, expected_average = SUBJECT_GRADES[subject]
    for g in grades:
        gradebook.add_grade(subject, g)

    assert len(gradebook.get_grades()[subject]) == len(grades), \
        f"Test amount of grades for subject: {subject}"

    actual_average = gradebook.calc_avg_for_subject(subject)
    assert actual_average == pytest.approx(expected_average, abs=0.001), \
        f"Grade average test for subject: {subject}"


# ---------- Zadanie 2: calc_avg_for_all_subjects ----------

def test_calc_avg_for_all_subjects(gradebook):
    gradebook.add_subject("Math")
    gradebook.add_subject("Physics")
    gradebook.add_grade("Math", 5.0)
    gradebook.add_grade("Math", 4.0)
    gradebook.add_grade("Physics", 3.0)
    assert gradebook.calc_avg_for_all_subjects() == pytest.approx({"Math": 4.5, "Physics": 3.0})


def build_all_avg_cases():
    # (nazwa testu, oceny w dzienniczku, oczekiwany wynik)
    return [
        ("two_subjects", {"Math": [5.0, 4.0], "Physics": [3.0]}, {"Math": 4.5, "Physics": 3.0}),
        ("rounding", {"Math": [5.0, 4.0, 4.0]}, {"Math": 4.33}),
        ("subject_without_grades_skipped", {"Math": [5.0], "Biology": []}, {"Math": 5.0}),
        ("empty_gradebook", {}, {}),
        ("history_counted", {"History": [4.0, 5.0]}, {"History": 4.5}),
    ]


def pytest_generate_tests(metafunc):
    # test dynamiczny - przypadki generowane w trakcie zbierania testów
    if "all_avg_case" in metafunc.fixturenames:
        cases = build_all_avg_cases()
        metafunc.parametrize("all_avg_case", [c[1:] for c in cases], ids=[c[0] for c in cases])


def test_dynamic_calc_avg_for_all_subjects(gradebook, all_avg_case):
    data, expected = all_avg_case
    for subject, grades in data.items():
        gradebook.add_subject(subject)
        for g in grades:
            gradebook.add_grade(subject, g)
    assert gradebook.calc_avg_for_all_subjects() == pytest.approx(expected)


# ---------- Zadanie dodatkowe ----------

def test_add_grade_unknown_subject_raises(gradebook):
    with pytest.raises(ValueError, match="Art not found"):
        gradebook.add_grade("Art", 5.0)


def test_avg_unknown_subject_raises(gradebook):
    with pytest.raises(ValueError, match="Subject not in subjects"):
        gradebook.calc_avg_for_subject("Art")


def test_avg_without_grades_raises(gradebook):
    gradebook.add_subject("Math")
    with pytest.raises(ValueError, match="No grades found"):
        gradebook.calc_avg_for_subject("Math")


def test_duplicate_subject_raises_and_keeps_grades(gradebook):
    gradebook.add_subject("Math")
    gradebook.add_grade("Math", 5.0)
    with pytest.raises(ValueError, match="already exists"):
        gradebook.add_subject("Math")
    assert gradebook.get_subjects() == ["Math"]
    assert gradebook.get_grades()["Math"] == [5.0]


def test_getters_return_copies(gradebook):
    gradebook.add_subject("Math")
    gradebook.get_subjects().append("Hack")
    gradebook.get_grades()["Math"].append(1.0)
    assert gradebook.get_subjects() == ["Math"]
    assert gradebook.get_grades() == {"Math": []}


def test_rounding_half_up(gradebook):
    gradebook.add_subject("Math")
    gradebook.add_grade("Math", 4.125)
    assert gradebook.calc_avg_for_subject("Math") == 4.13