from loan import check_loan
import unittest

class TestCheckLoan(unittest.TestCase):
    def test_tc1_invalid_age(self):
        # Path: 1(T)
        self.assertEqual(check_loan(-1, 1000000), "Không hợp lệ")

    def test_tc2_age_under_18(self):
        # Path: 1(F) → 2(T)
        self.assertEqual(check_loan(17, 4000000), "Không đủ điều kiện")

    def test_tc3_income_under_3m(self):
        # Path: 1(F) → 2(F) → 3(T)
        self.assertEqual(check_loan(40, 2000000), "Không đủ điều kiện")

    def test_tc4_eligible(self):
        # Path: 1(F) → 2(F) → 3(F)
        self.assertEqual(check_loan(30, 4000000), "Đủ điều kiện")


if __name__ == '__main__':
    unittest.main()