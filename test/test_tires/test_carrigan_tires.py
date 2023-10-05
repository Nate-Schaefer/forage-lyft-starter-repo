import unittest
from tires.carrigan_tires import CarriganTires


class TestCarriganTires(unittest.TestCase):
    def test_tires_should_be_serviced(self):
        tires = CarriganTires([1, 0, 0, 0])
        self.assertTrue(tires.needs_service())

    def test_tires_should_not_be_serviced(self):
        tire = CarriganTires([0.8, 0.8, 0.8, 0.8])
        self.assertFalse(tire.needs_service())