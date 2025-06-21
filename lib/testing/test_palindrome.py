import pytest
from lib.palindrome import longest_palindromic_substring

def test():
    assert longest_palindromic_substring("Assess") == "ssess"
    assert longest_palindromic_substring("After hours of deciphering ancient scripts, the scholar paused and muttered, 'Step on no pets,' then returned to his studies.") == "tep on no pet"
    assert longest_palindromic_substring("") == ""
    assert longest_palindromic_substring("g") == "g"
    assert longest_palindromic_substring("god") == "g"