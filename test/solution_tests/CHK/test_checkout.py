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
        assert checkout("Z") == -1

    def test_checkout_multibuy_a(self):
        assert checkout("AAA") == 130

    def test_checkout_multibuy_b(self):
        assert checkout("BB") == 45

    def test_checkout_multibuy_a_double(self):
        assert checkout("AAAAAA") == 260

    def test_checkout_multibuy_a_double_plus_another(self):
        assert checkout("AAAAAAA") == 310

    def test_checkout_multibuy_ab(self):
        assert checkout("AAABB") == 175





