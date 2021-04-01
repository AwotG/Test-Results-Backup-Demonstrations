import logging
from enum import Enum

logger = logging.getLogger()
logger.setLevel(logging.INFO)


class PytestExitCodes(Enum):
    COLLECTED_PASSED = 0 # All tests were collected and passed successfully
    COLLECTED_MIXED_PASSED = 1 # Tests were collected and run but some of the tests failed
    TEST_INTERRUPTION = 2 # Test execution was interrupted by the user
    INTERNAL_ERROR = 3 # Internal error happened while executing tests
    CMDLINE_ERROR = 4 # pytest command line usage error
    NO_TESTS_COLLECTED = 5 # No tests were collected


class BehaveExitCodes(Enum):
    COLLECTED_PASSED = 0 # All tests were collected and passed successfully
    GENERAL_FAILURE = 1 # Unfortunately, this can be both successful run but some failed tests OR from the test run not even running
    TEST_INTERRUPTION = 2 # Test execution was interrupted by the user
    INTERNAL_ERROR = 3 # Internal error happened while executing tests
    CMDLINE_ERROR = 2 # pytest command line usage error
    NO_TESTS_COLLECTED = 5 # No tests were collected