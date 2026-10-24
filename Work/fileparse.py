# fileparse.py
#
# Exercise 3.3

import csv
from pprint import pprint


def parse_csv(filename, select=None, types=None, has_headers=None, delimiter=','):
    with open(filename) as f:
        rows = csv.reader(f, delimiter=" ")
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
                raise RuntimeError("Select requires column headers")
            else:
                Indices = []

        records = []
        for row in rows:
            if not row:
                continue
            if Indices:
                row = [row[index] for index in Indices]
            if types:
                row = [func(val) for func, val in zip(types, row)]
            if has_headers:
                record = dict(zip(headers, row))
                records.append(record)
            else:
                records.append(tuple(row))

        return records


share_held = parse_csv(
    "Work/Data/portfolio.dat",types=[str, int, float], has_headers=True, delimiter=' '
)

pprint(share_held)
