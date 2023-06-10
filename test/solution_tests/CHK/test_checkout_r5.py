from solutions.CHK.checkout_solution import checkout

class TestCheckoutR5():
    def test_checkout_stx(self):
        assert checkout("STX") == 45
