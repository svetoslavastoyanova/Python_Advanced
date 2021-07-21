deposited_sum = float(input())
deposit_duration = int(input())
yearly_interest_percentage = float(input())

interest = deposited_sum*yearly_interest_percentage/100
monthly_interest = interest/12
total_sum = deposited_sum + deposit_duration * monthly_interest

print(total_sum)


