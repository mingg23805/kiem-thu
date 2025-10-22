import unittest

from loan import check_loan


class TestCheckLoanAllUses(unittest.TestCase):

    def test_case1_invalid(self):
        """Bao phủ (2T) và (3→7): age âm hoặc income âm"""
        result = check_loan(-1, 1000)
        self.assertEqual(result, "Không hợp lệ")

    def test_case2_not_qualified(self):
        """Bao phủ (2F), (4T), (5→7): đủ tuổi nhưng thu nhập thấp"""
        result = check_loan(25, 2000000)
        self.assertEqual(result, "Không đủ điều kiện")

    def test_case3_qualified(self):
        """Bao phủ (2F), (4F), (6→7): đủ tuổi và thu nhập cao"""
        result = check_loan(25, 4000000)
        self.assertEqual(result, "Đủ điều kiện")


if __name__ == '__main__':
    unittest.main()
