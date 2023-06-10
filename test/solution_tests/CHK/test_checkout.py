from solutions.CHK.checkout_solution import checkout


class TestCheckout():
    def test_checkout_a(self):
        assert checkout("A") == 50

    def test_checkout_b(self):
        assert checkout("B") == 30

    def test_checkout_abcd(self):
        assert checkout("ABCD") == 115

    def test_checkout_invalid(self):
        assert checkout("Z") == -1


