from __future__ import annotations


def account_threshold_balancing(
    accounts_dict: dict[str, int], threshold: int
) -> dict[str, int]:
    """A function that takes an input of a dictionary of accounts and their balances,
    and a threshold value, then it adjusts the balances so that they all meet the threshold value
    by transferring funds between accounts.
    """
    current_balance: int = 0
    greater_balance: dict[str, int] = {}
    final_balance: dict[str, int] = {}

    for key, value in accounts_dict.items():
        # Check if account balance is greater than threshold
        if value > threshold:
            diff = value - threshold
            current_balance += diff
            greater_balance[key] = diff

        if value < threshold:
            # Check if account balance is less than threshold
            diff = threshold - value
            current_balance -= diff
            for greater_key, greater_value in greater_balance.items():
                if greater_value <= 0:
                    continue

                # Calculate balance to transfer from the greater balance account
                balance_to_use = (
                    greater_balance[greater_key]
                    + 100
                    - value
                    - abs(greater_balance[greater_key] - 100 + value)
                ) // 2

                # Choose the minimum value between the balance to use and the difference
                balance_to_use = min(balance_to_use, diff)

                # Update the final balance dictionary, the greater balance dictionary
                # and the difference with the balance to use
                final_balance[f"{greater_key} -> {key}"] = balance_to_use
                greater_balance[greater_key] -= balance_to_use
                diff -= balance_to_use

    # Add the remaining balance to the final balance dictionary
    final_balance["reminder"] = current_balance

    return final_balance


# print(account_threshold_balancing({"Acct1": 130, "Acct2": 90, "Acct3": 120, "Acct4": 70}, 100))
