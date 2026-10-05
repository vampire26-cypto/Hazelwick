# Make a ticket calculator. Ask for ticket quantity and price. Calculate total.​
# Add a fixed £3 booking fee. Print the full cost.​
# If stuck: Start with tickets = int(input("Tickets: ")); print(tickets * 5). Then add the price variable.​
ticket =  float(input("how much does one ticket cost: "))
number = int(input("how many tickets do you need:"))

ans = ticket * number
answer = ans + 3
print(answer)