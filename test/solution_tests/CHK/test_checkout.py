from solutions.CHK.checkout_solution import checkout


class TestCheckout():
    def test_checkout(self):
        assert checkout("A") == 50
