import pytest
from string_utils import StringUtils


string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("   skypro", "skypro"),
    (" Python", "Python"),
    (" 123","123")
])
def test_trim_pozitive(input_str, expected):
    assert string_utils.trim(input_str) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "skypro"),
    ("Python", "Python"),
    ("123","123")
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected




@pytest.mark.positive
@pytest.mark.parametrize("input_string, symbol", [
        ("skypro", "s"),
        ("Python", "t"),
        ("123", "2")
    ])
def test_contains_positive(input_string, symbol):
    assert string_utils.contains(input_string, symbol) == True

@pytest.mark.negative
@pytest.mark.parametrize("input_string, symbol", [
        ("skypro", "u"),
        ("Python", "Noon", ),
        ("123", " ")
    ])
def test_contains_negative(input_string, symbol ):
    assert string_utils.contains(input_string, symbol) == False



@pytest.mark.positive
@pytest.mark.parametrize("input_string, symbol", [
        ("skypro", "p"),
        ("Python", "hon"),
        ("123", "2")
    ])
def test_delete_symbol_positive(input_string, symbol):
    string = input_string.replace(symbol, "")
    assert string_utils.delete_symbol(input_string, symbol) == string

@pytest.mark.negative
@pytest.mark.parametrize("input_string, symbol", [
        ("skypro", "  "),
        ("Python", " "),
        ("123", None)
    ])
def test_delete_symbol_negative(input_string, symbol):
    result = input_string
    assert result == input_string
