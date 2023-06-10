from solutions.CHK.checkout_solution import checkout

class TestCheckoutR2():
    def _test_checkout_e(self):
        assert checkout("E") == 40

    def _test_checkout_2e_b(self):
        assert checkout("EEB") == 80

    def _test_checkout_4e_b(self):
        assert checkout("EEEEB") == 160

    def _test_checkout_4e_2b(self):
        assert checkout("EEEEBB") == 160
