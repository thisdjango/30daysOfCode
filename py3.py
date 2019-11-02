def solve(meal_cost, tip_percent, tax_percent):
    one_percent = meal_cost / 100
    tip = tip_percent * one_percent
    tax = tax_percent * one_percent
    print(round(meal_cost + tip + tax))

if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    solve(meal_cost, tip_percent, tax_percent)
