from text_utils import StringUtils
import pytest

def test_change_case():
    assert StringUtils.change_case("Hello World", to_upper=True) == "HELLO WORLD"
    assert StringUtils.change_case("Hello World", to_upper=False) == "hello world"

def test_check_palindrome():
    assert StringUtils.check_palindrome("LOL") == True
    assert StringUtils.check_palindrome("Hello") == False

def test_count_words():
    assert StringUtils.count_words("Hello, world! This is a test.") == 6
    assert StringUtils.count_words("   ") == 0
    assert StringUtils.count_words("") == 0
    assert StringUtils.count_words("   Hello, word   ,  !") == 2

def test_type_of_string():
    assert StringUtils.type_of_string("123") == "Integer"
    assert StringUtils.type_of_string("123.45") == "Float"
    assert StringUtils.type_of_string("Hello") == "Alphabetic"
    assert StringUtils.type_of_string("Hello123") == "Alphanumeric"
    assert StringUtils.type_of_string("!@#") == "Unknown"

def test_split_string():
    assert StringUtils.split_string("Hello World") == ["Hello", "World"]
    assert StringUtils.split_string("Hello,World", ",") == ["Hello", "World"]
    assert StringUtils.split_string("NoDelimiterHere") == ["NoDelimiterHere"]

def test_combine_to_string():
    assert StringUtils.combine_to_string(["Hello", "World"]) == "Hello World"
    assert StringUtils.combine_to_string(["Hello", "World"], ", ") == "Hello, World"
    assert StringUtils.combine_to_string([]) == ""
    assert StringUtils.combine_to_string(["1", "2", "3", "4"], ": ") == "1: 2: 3: 4"

def test_replace_substring():
    assert StringUtils.replace_substring("Hello World", "World", "Python") == "Hello Python"
    assert StringUtils.replace_substring("Hello World", "Hello", "Hi") == "Hi World"
    assert StringUtils.replace_substring("Hello World", "NotHere", "Python") == "Hello World"

def test_is_start_with():
    assert StringUtils.is_start_with("Hello World", "Hello") == True
    assert StringUtils.is_start_with("Hello World", "World") == False
    assert StringUtils.is_start_with("", "Hello") == False
    with pytest.raises(ValueError):
        StringUtils.is_start_with("Hello World", "")

def test_trim_string():
    assert StringUtils.trim_string("Hello World", 5) == "Hello..."
    with pytest.raises(ValueError):
        assert StringUtils.trim_string("Hello World", 0) == "Hello World"
    with pytest.raises(ValueError):
        StringUtils.trim_string("Hello World", -1)
    assert StringUtils.trim_string("Short", 10) == "Short"
    assert StringUtils.trim_string("Trim this string", 4) == "Trim..."
