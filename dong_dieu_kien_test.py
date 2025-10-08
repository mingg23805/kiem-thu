from loan import check_loan
import unittest

class TestCheckLoan(unittest.TestCase):

    # TP1: 0 → 1 → (2)T → 3 → 7 → E
    def test_TC1_age_negative(self):
        self.assertEqual(check_loan(-1, 5000000), "Không hợp lệ")

    # TP1: 0 → 1 → (2)T → 3 → 7 → E
    def test_TC5_income_negative(self):
        self.assertEqual(check_loan(30, -1), "Không hợp lệ")

    # TP2: 0 → 1 → (2)F → (4)T → 5 → 7 → E
    def test_TC2_age_less_than_18(self):
        self.assertEqual(check_loan(17, 5000000), "Không đủ điều kiện")

    # TP2: 0 → 1 → (2)F → (4)T → 5 → 7 → E
    def test_TC3_income_less_than_3m(self):
        self.assertEqual(check_loan(30, 2000000), "Không đủ điều kiện")

    # TP2: 0 → 1 → (2)F → (4)T → 5 → 7 → E
    def test_TC6_age_greater_than_60(self):
        self.assertEqual(check_loan(65, 4000000), "Không đủ điều kiện")

    # TP3: 0 → 1 → (2)F → (4)F → 6 → 7 → E
    def test_TC4_valid(self):
        self.assertEqual(check_loan(30, 5000000), "Đủ điều kiện")


if __name__ == "__main__":
    unittest.main()