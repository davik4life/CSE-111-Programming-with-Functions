from names import make_full_name, extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    """
    This is a function that returns the full name.
    """
    assert make_full_name("Victor", "Adeshile") == "Adeshile; Victor"
    assert make_full_name("Matilda", "Adeshile") == "Adeshile; Matilda"
    assert make_full_name("Faith", "Adeshile") == "Adeshile; Faith"
    assert make_full_name("Co-Owner", "SomeBody") == "SomeBody; Co-Owner"
    assert make_full_name("Victor", "Adeshile_With_Extra_Length") == "Adeshile_With_Extra_Length; Victor"
    
    
def test_extract_family_name():
    """
    This is a function that extracts the family name.
    """
    assert extract_family_name("Adeshile; Victor") == "Adeshile"
    assert extract_family_name("Matilda; Adeshile") == "Matilda"
    assert extract_family_name("Co-Owner; SomeBody") == "Co-Owner"
    assert extract_family_name("Adeshile_Happy_Coder; Victor") == "Adeshile_Happy_Coder"
    
def test_extract_given_name():
    """
    This is a function that extracts the given name.
    """
    assert extract_given_name("Adeshile; Victor") == "Victor"
    assert extract_given_name("Co-Owner; SomeBody") == "SomeBody"
    assert extract_given_name("Faith; Adeshile") == "Adeshile"
    assert extract_given_name("Adeshile; Victor_The _Better_Programmer") == "Victor_The _Better_Programmer"
    
pytest.main(["-v", "--tb=line", "-rN", "test_names.py"])
