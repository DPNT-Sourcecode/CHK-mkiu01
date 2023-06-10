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

    def test_checkout_10h(self):
        assert checkout("HHHHHHHHHH") == 80

    def test_checkout_3n_m(self):
        assert checkout("NNNM") == 120

    def test_checkout_3u(self):
        assert checkout("UUU") == 120

    def test_checkout_4u(self):
        assert checkout("UUUU") == 120


