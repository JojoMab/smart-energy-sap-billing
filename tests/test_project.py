import unittest
from main import Reading, monthly_cost, co2_kg, recommendation

class EnergyTest(unittest.TestCase):
    def test_cost_and_co2(self):
        r = Reading('business','2026-01',1000,31)
        self.assertEqual(monthly_cost(r), 310.0)
        self.assertEqual(co2_kg(r), 380.0)
        self.assertEqual(recommendation(r), 'check efficiency potential')

if __name__ == '__main__': unittest.main()
