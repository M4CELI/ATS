"""Punkt wejścia aplikacji (odpowiednik klasy Main z metodą main())."""

from gradebook import Gradebook


def main():
    """Tworzy przykładowy dzienniczek i wypisuje średnie."""
    gradebook = Gradebook()
    gradebook.add_subject("Math")
    gradebook.add_subject("Physics")
    gradebook.add_grade("Math", 5.0)
    gradebook.add_grade("Math", 4.0)
    gradebook.add_grade("Physics", 3.5)

    print("Przedmioty:", ", ".join(gradebook.get_subjects()))
    for subject, average in gradebook.calc_avg_for_all_subjects().items():
        print(f"Średnia {subject}: {average}")


if __name__ == "__main__":
    main()