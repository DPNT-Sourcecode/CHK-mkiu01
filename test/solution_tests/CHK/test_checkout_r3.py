from solutions.CHK.checkout_solution import checkout

class TestCheckoutR3():
    def test_checkout_f(self):
        assert checkout("F") == 10
