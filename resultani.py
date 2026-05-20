def collect_marks(count=5):
    marks = []
    while len(marks) < count:
        try:
            value = float(input(f"Enter marks for student {len(marks) + 1}: "))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
            continue
        marks.append(value)
    return marks


def average_marks(marks):
    return sum(marks) / len(marks) if marks else 0


def highest_mark(marks):
    return max(marks) if marks else None


def lowest_mark(marks):
    return min(marks) if marks else None


def passed_students(marks, threshold=40):
    return [mark for mark in marks if mark > threshold]


if __name__ == "__main__":
    marks = collect_marks(5)
    print("\nMarks entered:", marks)
    print("Average:", average_marks(marks))
    print("Highest:", highest_mark(marks))
    print("Lowest:", lowest_mark(marks))
    print("Passed students (>40):", passed_students(marks))
