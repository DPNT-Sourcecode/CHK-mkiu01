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

