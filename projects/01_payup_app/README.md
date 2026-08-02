<h1 align="center"> PayUp - Expense Splitter </h1>

<p align="center">PayUp is a simple Python command-line application that calculates how much each person should pay when splitting a bill.</p>

## Demo

![PayUp Demo](./assets/gif-do-projeto.gif)

## How It Works

The user enters information about the meal or event, the original cost, the service charge percentage, and the number of people. The application then displays a complete breakdown of the bill.

The application asks the user to enter:

- The type of meal
- The name of the event or occasion
- The original cost
- The service charge or tip percentage
- The number of people splitting the bill

It then calculates:

- The total service charge
- The grand total
- The amount each person must pay

## Example

```text
Welcome to PayUp

What type of meal was it? (e.g. lunch, dinner, brunch): dinner
What is the name of the event or occasion? Birthday Dinner
What is the cost of the event? Enter a whole number (e.g. 300 for $300): 300
Was there a tip or a service charge? Enter a whole number (e.g. 20 for 20%): 20
How many people are splitting the bill? 4

Here's the breakdown for dinner at Birthday Dinner:

Cost: $300.00
Service charges: $60.00
Group size: 4
Grand total: $360.00

Each person must PayUP: $90.00
```

## Concepts Practiced

- Variables
- Strings
- User input
- Type conversion
- Arithmetic operations
- Percentage calculations
- F-strings
- Decimal formatting

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/Chrysthy/scrimba-learn-python.git
```

2. Open the project directory:

```bash
cd scrimba-learn-python/projects/01_expense_splitter
```

3. Run the Python file:

```bash
python main.py
```

## Current Limitations

This first version does not validate the information entered by the user. Invalid values, such as text entered instead of a number or a group size of zero, may cause an error.

## Possible Improvements

- Validate user input
- Prevent division by zero
- Allow the user to perform another calculation
- Add support for different currencies

## Course

This project was developed as part of the **Learn Python** course by Scrimba.

---

[← Back to the main README](../../README.md)