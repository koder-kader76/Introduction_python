# 8. Assume you have $1,000.00 in the bank, and you've somehow managed to find a bank that pays you 5% (this is a wish-fulfillment fantasy) compounded interest every year. After one year, you will have $1,050 ($1,000 times 1.05). After two years, you will have $1,050 times 1.05, or $1102.50. Create a variable named balance that contains the amount of money you will have after 5 years, then print the result. Use a single expression if you can to set balance to the correct value.

amount = 1000
interest = 1.05
balance = amount * (interest**5)
print(balance)

# 9. Repeat the previous question but, this time, use augmented assignment to compute the final result, one year at a time.

amount_2 = 1000
interest_2 = 1.05
balance_2 = amount_2 * interest_2
balance_2 *= interest_2
balance_2 *= interest_2
balance_2 *= interest_2
balance_2 *= interest_2
print(balance_2)