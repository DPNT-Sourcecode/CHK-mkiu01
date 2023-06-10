from solutions.CHK.checkout_solution import checkout

class TestCheckoutR2():
    def test_checkout_e(self):
        assert checkout("E") == 40
