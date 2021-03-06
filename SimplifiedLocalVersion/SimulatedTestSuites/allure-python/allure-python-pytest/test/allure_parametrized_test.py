import random

import allure
import pytest


@pytest.mark.parametrize("test_param", ["First name", "Second name"], ids=["first", "second"])
@allure.title("test_allure_parametrized_test [{test_param}]")
def test_allure_parametrized_test(test_param):
    with allure.step("Step inside parametrized test"):
        pass
    with allure.step(f"Test parameter: {test_param}"):
        pass


@pytest.fixture(params=["First fixture param", "Second fixture param"], ids=["first", "second"])
def parametrized_fixture(request):
    with allure.step(f"Fixture parameter: {request.param}"):
        if not randomized_pass():
            assert False, "This is just a random failure"
        else:
            pass


def test_allure_parametrized_fixture(parametrized_fixture):
    if not randomized_pass():
        assert False, "This is just a random failure"
    else:
        pass

def randomized_pass():
    return random.choice([True, False])