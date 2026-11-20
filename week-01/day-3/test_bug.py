import unittest
from unittest.mock import patch
from io import StringIO

from env_check import (
    in_virtualenv,
    check_version,
    describe_interpreter,
)


class TestEnvCheck(unittest.TestCase):

    def test_not_in_virtualenv(self):
        self.assertFalse(in_virtualenv("python", "python"))

    def test_in_virtualenv(self):
        self.assertTrue(in_virtualenv("venv", "python"))

    def test_version_ok(self):
        self.assertEqual(check_version("3.13.7"), "ok")

    def test_old_version(self):
        result = check_version("3.8.10")
        self.assertIn("too old", result)

    def test_describe_interpreter(self):
        with patch("sys.stdout", new_callable=StringIO) as output:
            version = describe_interpreter()

        self.assertIn(version, output.getvalue())
        self.assertIn("interpreter:", output.getvalue())


if __name__ == "__main__":
    unittest.main()