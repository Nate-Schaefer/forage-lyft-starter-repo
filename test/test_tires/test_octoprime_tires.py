import unittest
from tires.octoprime_tires import OctoprimeTires


class TestCarriganTires(unittest.TestCase):
    def test_tires_should_be_serviced(self):
        tires = OctoprimeTires([1, 1, 0, 1])
        self.assertTrue(tires.needs_service())

    def test_tires_should_not_be_serviced(self):
        tire = OctoprimeTires([0.8, 0.8, 0.8, 0.8])
        self.assertFalse(tire.needs_service())