from solutions.CHK.checkout_solution import checkout


class TestCheckout():
    def test_checkout_a(self):
        assert checkout("A") == 50

    def test_checkout_b(self):
        assert checkout("B") == 30

    def test_checkout_abcd(self):
        assert checkout("ABCD") == 115

    def test_checkout_acccdd(self):
        assert checkout("ACCCDD") == 140

    def test_checkout_invalid(self):
        assert checkout("@") == -1

    def test_checkout_3a(self):
        assert checkout("AAA") == 130

    def test_checkout_2b(self):
        assert checkout("BB") == 45

    def test_checkout_4a(self):
        assert checkout("AAAA") == 180

    def test_checkout_5a(self):
        assert checkout("AAAAA") == 200

    def test_checkout_6a(self):
        assert checkout("AAAAAA") == 250

    def test_checkout_7a(self):
        assert checkout("AAAAAAA") == 300

    def test_checkout_multibuy_ab(self):
        assert checkout("AAABB") == 175
