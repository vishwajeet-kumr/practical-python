# fileparse.py
#
# Exercise 3.3

import csv
from pprint import pprint


def parse_csv(filename, select=None, types=None, has_headers=None, delimiter=",", silence_error=False):
    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter)
        headers = []
        if has_headers:
            headers = next(rows)
            if select:
                Indices = [headers.index(colname) for colname in select]
                headers = select
            else:
                Indices = []
        else:
            if select:
                raise RuntimeError("Select requires column headers: OK...")
            else:
                Indices = []

        records = []
        for rowno, row in enumerate(rows):
            if not row:
                continue
            if Indices:
                row = [row[index] for index in Indices]
            if types:
                try:
                    row = [func(val) for func, val in zip(types, row)]
                except ValueError as e:
                    if not silence_error:
                        print(f"Row {rowno}: Couldn't convert {row}")
                        print(f"Row {rowno}: Reason {e}")
                        continue

            if has_headers:
                record = dict(zip(headers, row))
                records.append(record)
            else:
                records.append(tuple(row))

        return records


share_held = parse_csv("Work/Data/missing.csv", types=[str, int, float], silence_error=True)

pprint(share_held)
