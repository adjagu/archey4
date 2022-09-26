"""`archey.test` module initialization file"""

import logging
import unittest

# Disable `WARNING` log level (internally used).
logging.disable(logging.WARNING)

# This global stops `unittest` from printing tracebacks _beyond_ our custom assertion.
# See <https://stackoverflow.com/a/49929579>.
__unittest = True  # pylint: disable=invalid-name


# From <https://stackoverflow.com/a/15868615>.
class CustomAssertions:
    """This class defines our custom assertion methods being used in Archey unit testing"""

    @staticmethod
    def assertListEmpty(obj):  # pylint: disable=invalid-name
        """Simple method to check that passed `obj` is an **empty** `list`"""
        if not isinstance(obj, list):
            raise AssertionError("First sequence is not a list: " + str(obj))

        if obj:
            raise AssertionError("First sequence is not empty: " + str(obj))

    @staticmethod
    def assertTupleEmpty(obj):  # pylint: disable=invalid-name
        """Simple method to check that passed `obj` is an **empty** `tuple`"""
        if not isinstance(obj, tuple):
            raise AssertionError("First sequence is not a tuple: " + str(obj))

        if obj:
            raise AssertionError("First sequence is not empty: " + str(obj))


class TestCustomAssertions(unittest.TestCase, CustomAssertions):
    """This class implements test cases for the custom Archey unit testing framework (#inception)"""

    def test_assert_list_empty(self):
        """Test cases for our `self.assertListEmpty` custom assertion"""
        self.assertListEmpty([])
        self.assertRaises(AssertionError, self.assertListEmpty, {})
        self.assertRaises(AssertionError, self.assertListEmpty, "test")
        self.assertRaises(AssertionError, self.assertListEmpty, ["test"])

    def test_assert_tuple_empty(self):
        """Test cases for our `self.assertTupleEmpty` custom assertion"""
        self.assertTupleEmpty(())
        self.assertRaises(AssertionError, self.assertTupleEmpty, {})
        self.assertRaises(AssertionError, self.assertTupleEmpty, "test")
        self.assertRaises(AssertionError, self.assertTupleEmpty, ("test",))
