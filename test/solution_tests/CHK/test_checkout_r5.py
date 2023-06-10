from solutions.CHK.checkout_solution import checkout

class TestCheckoutR5():
    def test_checkout_k(self):
        assert checkout("K") == 70

    def test_checkout_2k(self):
        assert checkout("KK") == 120

    def test_checkout_stx(self):
        assert checkout("STX") == 45

