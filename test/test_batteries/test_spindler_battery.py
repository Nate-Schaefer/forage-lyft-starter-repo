import unittest
from datetime import datetime
from batteries.spindler_battery import SpindlerBattery


class TestSpindlerBattery(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)

        battery = SpindlerBattery(today, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 2)

        battery = SpindlerBattery(today, last_service_date)
        self.assertFalse(battery.needs_service())