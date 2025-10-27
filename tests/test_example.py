import pytest
def test_stack():
    stack = []
    assert not stack
    stack.append('one')
    stack.append('two')
    stack.pop()
    stack.pop()
    with pytest.raises(IndexError):
        stack.pop()