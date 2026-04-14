"""Test hobbies examples."""
import pytest
from moodle_OOP_hobbies import *
@pytest.fixture(autouse=True)


def init_tests():
    person1 = Person("Mari", "Kukk", ["dancing", "biking", "programming"])
    person2 = Person("Jeff", "Bezos", ["money", "hair", "late_capitalism", "space", "unions"])
    person3 = Person("Elon", "Musk", ["late_capitalism", "space", "cars"])
    print("Test start")
    yield person1, person2, person3
    print("Test done")

def test_sort_by_most_hobbies():
    MariKukk, JeffBezos, ElonMusk = init_tests()
    assert sort_by_most_hobbies(people) == ["JeffBezos", "MariKukk", "ElonMusk"]

def test_sort_by_least_hobbies():
    MariKukk, JeffBezos, ElonMusk = init_tests()
    assert sort_by_least_hobbies(people) == ["ElonMusk", "MariKukk", "JeffBezos"]

def test_filter_by_hobby():
    people = init_tests()
    assert test_filter_by_hobby(people, "space") == ["ElonMusk", "JeffBezos"]

def test_sort_people_and_hobbies():
    people = init_tests()
    assert sort_people_and_hobbies(people) == ["ElonMusk", "MariKukk", "JeffBezos"]

def test_person_get_hobbies():
    person1 = Person("Mari", "Kukk", ["dancing", "biking", "programing"])
    assert person1.hobbies == ["biking", "dancing", "programming"]