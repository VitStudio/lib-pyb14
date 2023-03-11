from sngtolib import sngto

def test_check_prime_number():
    assert check_prime_number(1) == 0
    assert check_prime_number(2) == 1
    assert check_prime_number(3) == 1
    assert check_prime_number(4) == 0
    assert check_prime_number(5) == 1
    assert check_prime_number(6) == 0
    assert check_prime_number(7) == 1
    assert check_prime_number(8) == 0
    assert check_prime_number(9) == 0
    assert check_prime_number(10) == 0
    assert check_prime_number(11) == 1
    assert check_prime_number(12) == 0
    assert check_prime_number(13) == 1
    assert check_prime_number(14) == 0
    assert check_prime_number(15) == 0
    assert check_prime_number(16) == 0
    assert check_prime_number(17) == 1
    assert check_prime_number(18) == 0
    assert check_prime_number(19) == 1
    assert check_prime_number(20) == 0

test_check_prime_number()
