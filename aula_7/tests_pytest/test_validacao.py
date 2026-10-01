import pytest
from validacao import validar_quantidade


def test_comum():
    assert validar_quantidade(8) is True


def test_limite():
    assert validar_quantidade(0) is True


def test_invalido():
    with pytest.raises(ValueError):
        validar_quantidade(-1)
