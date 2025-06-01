# Write a function that computes the sum and average of a list of numbers.
def calc_sum_and_average(expenses):
    total_expenses = sum(expenses)
    average_expenses = total_expenses / len(expenses)
    return total_expenses, average_expenses

outing_expenses = [98, 47, 75, 24]
total, average = calc_sum_and_average(outing_expenses)

print("Total expenses:", total)
print("Average expenses:", average)
