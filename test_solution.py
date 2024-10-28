import unittest

from solution import account_threshold_balancing


class TestAccountThresholdBalancing(unittest.TestCase):

    def test_account_threshold_balancing(self):
        result = account_threshold_balancing({"Acct1": 50}, 100)
        self.assertIsInstance(result, dict)

    def test_that_two_accounts_balance_and_there_is_a_reminder(self):
        result = account_threshold_balancing({"Acct1": 130, "Acct2": 90}, 100)
        self.assertEqual(
            result,
            {
                "Acct1 -> Acct2": 10,
                "reminder": 20,
            },
        )

    def test_that_three_accounts_would_balance_and_there_is_no_reminder(self):
        result = account_threshold_balancing({"Acct1": 130, "Acct2": 90, "Acct3": 80}, 100)
        self.assertEqual(
            result,
            {
                "Acct1 -> Acct2": 10,
                "Acct1 -> Acct3": 20,
                "reminder": 0,
            },
        )

    def test_that_four_accounts_would_balance_and_there_is_a_reminder(self):
        result = account_threshold_balancing({"Acct1": 130, "Acct2": 90, "Acct3": 120, "Acct4": 70}, 100)
        self.assertEqual(
            result,
            {
                "Acct1 -> Acct2": 10,
                "Acct1 -> Acct4": 20,
                "Acct3 -> Acct4": 10,
                "reminder": 10,
            },
        )


if __name__ == "__main__":
    unittest.main()
