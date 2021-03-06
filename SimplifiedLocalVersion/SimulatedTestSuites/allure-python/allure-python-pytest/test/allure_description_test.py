import random

import allure
import pytest


def test_docstring_description():
    """
    This is a test docstring
    It's will be shown as an allure test description
    Scenario:
     - pass
    """
    if not randomized_pass():
        assert False, "This is just a random failure"
    else:
        pass


@allure.description(
    """
This is test description from decorator\n
Scenario:
  - pass
  """)
def test_decorated_description():
    if not randomized_pass():
        assert False, "This is just a random failure"
    else:
        pass


@allure.description_html("""
This is <b>HTML</b> test description
<h2>Scenario:</h2>
<ul>
<li>pass</li>
</ul>
""")
def test_decorated_html_description():
    if not randomized_pass():
        assert False, "This is just a random failure"
    else:
        pass


@pytest.mark.parametrize("test_param", ["First param", "Second param"])
def test_dynamic_description(test_param):
    """
    Initial test description
    """
    allure.dynamic.description(test_dynamic_description.__doc__ +
                               f"\n This is dynamic description part based on {test_param}")

def randomized_pass():
    return random.choice([True, False])