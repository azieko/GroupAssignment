#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Assign students to synchronous lecture groups"""

__author__ = "Azieko"

from random import sample


def read_classroll(filename="classroll.txt"):
    """Read classroll database file and return a list of students."""
    with open(filename) as datafile:
        students = [line.strip() for line in datafile]

    return students


def assign_groups(students, n_groups=3):
    """Return the group assigment (list of lists) based on random sampling"""
    groups = []
    group_size = (len(students) // n_groups)
    # Random shuffle to avoid selection bias
    shuffled = sample(students, len(students))
    group_begin, group_end = 0, group_size
    for i_group in range(n_groups):
        if len(students) % n_groups != 0:
            group = shuffled[group_begin:group_end]
            groups.append(group)
            group_size += 1
            group_begin, group_end = group_end, group_end + group_size
        else:
            group = shuffled[group_begin:group_end]
            groups.append(group)
            group_begin, group_end = group_end, group_end + group_size
    return groups


def main():
    days = "Monday", "Wednesday", "Friday"
    groups = assign_groups(read_classroll(), len(days))

    i = 0
    for student in sorted(groups):
        print('\n{}'.format(days[i]))
        for x in student:
            print("\n\t{}".format(x))
        i += 1
        print()


if __name__ == "__main__":
    main()
