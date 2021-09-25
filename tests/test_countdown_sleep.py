from test.support import captured_stdout
from unittest.mock import patch

import pytest

from countdown_sleep.main import countdown_sleep


@patch("time.sleep", return_value=None)
def test_print_countdown_0(mock_sleep):
    n = 0
    expect_output = ""

    with captured_stdout() as stdout:
        countdown_sleep(n)

    assert stdout.getvalue() == expect_output


@patch("time.sleep", return_value=None)
def test_print_countdown_1(mock_sleep):
    n = 1
    expect_output = "\b \b\r1"

    with captured_stdout() as stdout:
        countdown_sleep(n)

    assert stdout.getvalue() == expect_output


@patch("time.sleep", return_value=None)
def test_print_countdown_10(mock_sleep):
    n = 10
    expect_output = "\b \b\r10\b \b\r9\b \b\r8\b \b\r7\b \b\r6\b \b\r5\b \b\r4\b \b\r3\b \b\r2\b \b\r1"

    with captured_stdout() as stdout:
        countdown_sleep(n)
    assert stdout.getvalue() == expect_output


@patch("time.sleep", return_value=None)
def test_call_sleep_0_times(mock_sleep):
    n = 0
    countdown_sleep(0)
    assert mock_sleep.call_count == 0


@patch("time.sleep", return_value=None)
def test_call_sleep_1_times(mock_sleep):
    n = 1
    countdown_sleep(n)
    assert mock_sleep.call_count == 1


@patch("time.sleep", return_value=None)
def test_call_sleep_10_times(mock_sleep):
    n = 10
    countdown_sleep(n)
    assert mock_sleep.call_count == 10


@patch("time.sleep", return_value=None)
def test_raise_value_error_negative_1(mock_sleep):
    n = -1
    with pytest.raises(ValueError):
        countdown_sleep(n)
