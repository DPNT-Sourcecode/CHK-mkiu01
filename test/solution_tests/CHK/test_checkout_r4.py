from solutions.CHK.checkout_solution import checkout

class TestCheckoutR4():
    def test_checkout_g(self):
        assert checkout("G") == 20
