from address import extract_city, extract_state, extract_zipcode
import pytest

def test_extract_city():
    """
    This is a function that test the return of the extract_city function
    """
    assert extract_city("525 S Center St, Rexburg, ID 83460") == "Rexburg"
def test_extract_state():
    """
    This is a function that test the return of the extract_state function
    """
    assert extract_state("525 S Center St, Rexburg, ID 83460") == "ID"
def test_extract_zipcode():
    """
    This is a function that test the return of the extract_zipcode function
    """
    assert extract_zipcode("525 S Center St, Rexburg, ID 83460") == "83460"

pytest.main(["-v", "--tb=line", "-rN", "test_address.py"])
