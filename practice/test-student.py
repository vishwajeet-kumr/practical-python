# student_report.py

import csv
from typing import Optional


# ─────────────────────────────────────────
# LAYER 1 — Data reading (lowest level)
# ─────────────────────────────────────────

def read_students(filename: str) -> list[dict]:
    '''
    Read student data from a CSV file.
    Expected columns: name, marks, subject
    Returns a list of dicts: [{'name': str, 'marks': int, 'subject': str}, ...]
    '''
    students = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)               # skip header row
        for row in rows:
            if len(row) < 3:               # skip malformed rows
                continue
            students.append({
                'name':    row[0].strip(),
                'marks':   int(row[1]),
                'subject': row[2].strip()
            })
    return students


# ─────────────────────────────────────────
# LAYER 2 — Calculations (middle level)
# ─────────────────────────────────────────

def calculate_average(students: list[dict]) -> float:
    '''Returns the average marks. Returns 0.0 for empty list.'''
    if not students:
        return 0.0
    return sum(s['marks'] for s in students) / len(students)


def find_toppers(students: list[dict], threshold: int = 85) -> list[dict]:
    '''Returns students who scored >= threshold. Default threshold is 85.'''
    return [s for s in students if s['marks'] >= threshold]


def find_failures(students: list[dict], passing_marks: int = 40) -> list[dict]:
    '''Returns students who scored below passing_marks.'''
    return [s for s in students if s['marks'] < passing_marks]


def get_highest_scorer(students: list[dict]) -> Optional[dict]:
    '''Returns the student dict with the highest marks. None if list is empty.'''
    if not students:
        return None
    return max(students, key=lambda s: s['marks'])


# ─────────────────────────────────────────
# LAYER 3 — Display (output level)
# ─────────────────────────────────────────

def print_report(students: list[dict]) -> None:
    '''Prints a formatted table of all students.'''
    print(f"\n{'Name':<15} {'Marks':>6}  {'Subject':<15}")
    print('-' * 40)
    for s in students:
        print(f"{s['name']:<15} {s['marks']:>6}  {s['subject']:<15}")


def print_summary(students: list[dict]) -> None:
    '''Prints class summary: average, toppers count, failures count.'''
    average        = calculate_average(students)
    toppers        = find_toppers(students)
    failures       = find_failures(students)
    highest_scorer = get_highest_scorer(students)

    print(f"\n{'── CLASS SUMMARY ':─<40}")
    print(f"  Total Students : {len(students)}")
    print(f"  Class Average  : {average:.1f}")
    print(f"  Toppers (≥85)  : {len(toppers)}")
    print(f"  Failures  (<40): {len(failures)}")
    if highest_scorer:
        print(f"  Best Student   : {highest_scorer['name']} ({highest_scorer['marks']} marks)")
    print('─' * 40)


# ─────────────────────────────────────────
# LAYER 4 — Top-level orchestrator
# ─────────────────────────────────────────

def generate_report(filename: str) -> None:
    '''
    Full pipeline: read file → process → display report.
    This is the only function you call from outside.
    '''
    print(f"\n📋 Report for: {filename}")

    students = read_students(filename)

    if not students:
        print("No student data found.")
        return

    print_report(students)
    print_summary(students)


# ─────────────────────────────────────────
# ENTRY POINT — runs only when executed directly
# ─────────────────────────────────────────

if __name__ == '__main__':
    generate_report('practice/students.csv')