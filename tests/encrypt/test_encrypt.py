from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    with pytest.raises(TypeError):
        encrypt_message(3, 3)  # message invalid

    with pytest.raises(TypeError):
        encrypt_message("bola", "P")  # key invalid

    assert encrypt_message("wesley", -1) == "yelsew"  # key negative
    assert encrypt_message("wesley", 3) == "sew_yel"  # key impar
    assert encrypt_message("wesley", 2) == "yels_ew"  # key par
