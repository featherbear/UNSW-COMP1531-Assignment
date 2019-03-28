import pytest
from .Exceptions import NoItemError

def testRaiser():
    with pytest.raises(NoItemError):
        raise NoItemError