# 5-7-Stadium-Seating
 Calculates gross sales of stadium tickets at 3 price points.

## Scope
There are three seating categories at a stadium. Class A seats cost $20, Class B seats cost $15, and Class C seats cost $10. Write a program that asks the ticket manager how many tickets for each class were sold for an event, then displays the amount of gross income was generated from ticket sales.

*Hints:* Set up global constants for each of the classes of seats, so Class A seats would equal 20, etc.  Ask the user (ticket manager) for the amount sold in each class, then pass those values into a function to calculate and display the results.

### Sample Run
    Enter count of A seats:  450
    Enter count of B seats:  500
    Enter count of C seats:  600
    Income from class A seats: $9000.00
    Income from class B seats: $7500.00
    Income from class C seats: $6000.00
    Total gross income from ticket sales: $22500.00

## Pseudocode
    START
      SET constant for CLASS_A to $20
      SET constant for CLASS_B to $15
      SET constant for CLASS_C to $10
      CALL main function
    END

### Main function
    START
      INPUT number of class A tickets
      INPUT number of class B tickets
      INPUT number of class C tickets
      CALL gross_income function
    END

### gross_income function
    START
      PASS IN: class A tickets, class B tickets, class C tickets
      CALCULATE class A revenue
        class A tickets * CLASS_A
      CALCULATE class B revenue
        class B tickets * CLASS_B
      CALCULATE class C revenue
        class C tickets * CLASS_C
      CALCULATE gross revenue
        class A revenue + class B revenue + class C revenue
      PRINT class A revenue
      PRINT class B revenue
      PRINT class C revenue
      PRINT gross revenue
    END
