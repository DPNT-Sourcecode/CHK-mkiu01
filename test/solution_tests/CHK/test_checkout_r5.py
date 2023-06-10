from solutions.CHK.checkout_solution import checkout

class TestCheckoutR5():
    def test_checkout_2k(self):
        assert checkout("KK") == 120

    def test_checkout_x(self):
        assert checkout("X") == 17

    def test_checkout_stx(self):
        assert checkout("STX") == 45

    def test_checkout_5s(self):
        assert checkout("SSSSS") == 85

    def test_checkout_6s(self):
        assert checkout("SSSSSS") == 90

    def test_checkout_sty_x(self):
        assert checkout("STXY") == 45 + 17

    def test_checkout_sty_x2(self):
        assert checkout("XSTY") == 45 + 17

    def test_checkout_stxyz(self):
        assert checkout("STXYZ") == 45 + 17 + 20

    def test_checkout_stxyz(self):
        assert checkout("SSXXYYZZ") == 45 * 2 + 17 * 2
