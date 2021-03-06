import random

import allure
import pytest
from allure_commons.types import Severity


@allure.epic("Allure TestOps")
@allure.feature("BDD")
@allure.story("Labels")
def test_allure_bdd_labels():
    if not randomized_pass():
        assert False, "This is just a random failure"
    else:
        pass


@allure.parent_suite("Custom parent suite")
@allure.suite("Custom suite")
@allure.sub_suite("Custom sub suite")
def test_allure_suites():
    if not randomized_pass():
        assert False, "This is just a random failure"
    else:
        pass


@allure.label("allure-examples", "allure-pytest")
def test_allure_custom_labels():
    if not randomized_pass():
        assert False, "This is just a random failure"
    else:
        pass


@pytest.mark.parametrize("test_image", ["some-image:latest", "some-image:release"])
def test_dynamic_labels(test_image):
    allure.dynamic.label("test-image", test_image)


@pytest.mark.parametrize("severity", [*Severity])
def test_allure_severity(severity):
    allure.dynamic.severity(severity)


@allure.tag("Tagged test")
def test_allure_tags():
    allure.dynamic.tag("Dynamic tag")

def randomized_pass():
    return random.choice([True, False])