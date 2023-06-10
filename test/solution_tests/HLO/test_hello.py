from solutions.HLO.hello_solution import hello


class TestHello():
    def test_hello_world(self):
        assert hello("World") == "Hello, World!"

    def test_hello_mario(self):
        assert hello("Mario") == "Hello, Mario!"


