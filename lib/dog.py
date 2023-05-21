#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]


class Person:
    approved_jobs = [
        "Admin",
        "Customer Service",
        "Human Resources",
        "ITC",
        "Production",
        "Legal",
        "Finance",
        "Sales",
        "General Management",
        "Research & Development",
        "Marketing",
        "Purchasing"
    ]

    def __init__(self):
        self._name = ""

    def name(self):
        return self._name

    def name(self, value):
        if type(value) == str and len(value) <= 25:
            self._name = value.title()
        else:
            print("Name must be a string under 25 characters.")

    def job(self):
        return self._job

    def job(self, value):
        if value in self.approved_jobs:
            self._job = value
        else:
            print("Job must be in the list of approved jobs.")
