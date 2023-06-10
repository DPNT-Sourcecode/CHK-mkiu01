from solutions.CHK.checkout_solution import checkout

class TestCheckoutR4():
    def test_checkout_g(self):
        assert checkout("G") == 20

    def test_checkout_k(self):
        assert checkout("K") == 80

    def test_checkout_r(self):
        assert checkout("R") == 50

    def test_checkout_y(self):
        assert checkout("Y") == 10
