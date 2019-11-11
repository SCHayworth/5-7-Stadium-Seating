# 5-7 Stadium Seating
# Shaun Hayworth
# CIS 2
# mm-dd-2019
# Source code and revision history are available at
#   https://github.com/SCHayworth/5-7-Stadium-Seating

# Program calculates and displays the gross revenue of stadium seating tickets
#   sold at three price points using a void function.

# Initialize constants for stadium seating price points.
# Change these values when the ticket pricing changes.
CLASS_A = 20.0
CLASS_B = 15.0
CLASS_C = 10.0

# The main() function executes the mainline program logic.
def main():
    # Prompt user for the number of tickets sold for each class of seat.
    tickets_a = int(input('Enter count of A seats: '))
    tickets_b = int(input('Enter count of B seats: '))
    tickets_c = int(input('Enter count of C seats: '))

    # Pass the ticket amounts to the gross_income() function.
    gross_income(tickets_a, tickets_b, tickets_c)

# The gross_income() function accepts ticket quantities for each class and
#   claculates the gross revenue for each class, as well as the total gross
#   income from all tickets together.
def gross_income(a_seats, b_seats, c_seats):
    # Calculate the gross revenue for each class of seat, and the total gross
    revenue_a = a_seats * CLASS_A
    revenue_b = b_seats * CLASS_B
    revenue_c = c_seats * CLASS_C
    gross_total = revenue_a + revenue_b + revenue_c

    # Print the totals to the screen.
    print(f'Income from class A seats: ${revenue_a:,.2f}')
    print(f'Income from class B seats: ${revenue_b:,.2f}')
    print(f'Income from class C seats: ${revenue_c:,.2f}')
    print(f'Total gross income from ticket sales: ${gross_total:,.2f}')

# Call the main() function to execute the program.
main()
