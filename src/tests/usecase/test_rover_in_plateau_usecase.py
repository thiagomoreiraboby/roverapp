import logging
import pytest
from usecase.rover_in_plateau_usecase import _create_plateau, _create_rover, read_file


def test_read_file_with_file_path_null():
    with pytest.raises(Exception):
        read_file(None)

def test_read_file_with_file_path_empty():
    with pytest.raises(FileNotFoundError):
        read_file("")


def test_read_file_with_file_path_sucess():
    result = read_file("src/tests/test_files/testefile.txt")
    assert result is not None
    assert result[0] == "1 3 N"
    assert result[1] == "5 1 E"


def test_read_file_with_off_the_plateau(caplog):
    result = read_file("src/tests/test_files/testefile_faul.txt")
    assert result is not None
    assert result[0] == "0 0 S"
    assert caplog.at_level(logging.ERROR)


def test_read_file_with_plateau_faul(caplog):
    result = read_file("src/tests/test_files/testefile_pateau_faul.txt")
    assert len(result) == 0
    assert caplog.at_level(logging.ERROR)

def test_read_file_with_rover_faul(caplog):
    result = read_file("src/tests/test_files/testefile_rover_faul.txt")
    assert len(result) == 0
    assert caplog.at_level(logging.ERROR)


def test_create_plateau(caplog):
    _create_plateau(None)
    assert caplog.at_level(logging.ERROR)


def test_create_rover(caplog):
    _create_rover(None)
    assert caplog.at_level(logging.ERROR)

        