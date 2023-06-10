from solutions.CHK.checkout_solution import checkout

class TestCheckoutR3():
    def test_checkout_f(self):
        assert checkout("F") == 10

    def test_checkout_2f(self):
        assert checkout("FF") == 20

    def test_checkout_3f(self):
        assert checkout("FFF") == 20

