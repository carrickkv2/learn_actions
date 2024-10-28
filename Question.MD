# Question

Given a dict of accounts and a threshold int, make sure that all the accounts balance to meet the threshold

### Example with threshold of 100

`dict {
"Acct1": 130,
"Acct2": 90,
"Acct3": 120,
"Acct4": 70,
}`

### Expected Output

`Acct 1 -> Acct 2: 10
Acct 1 -> Acct 4: 20
Acct 3 -> Acct 4: 10`

### A little explanation

Acct 1 is greater than the threshold of 100.
Thus, the diff btw it and the threshold is 30.
To balance Acct1, we need to remove 30 from it since it's over the threshold.

To balance Acc2, we need to take 10 from the 30 we got from Acct 1 and give it to Acct 2.

That's why we do `Acct1 -> Acct2 : 10`

To balance Acc4, we need to take the remaining 20 from left over from Acct1 and give it to Acc4.
`Acct 1 -> Acct 4: 20`

Acct1 now has nothing left.

Acct3 on the other hand was 20 greater than the threshold of 100.

So we need to remove 20 from Acct3 and from that 20 give 10 to Acct4. `Acct 3 -> Acct 4: 10`
