test_score = 85

if test_score >= 90:
    print("A")
elif test_score >= 80:
    print("B")
elif test_score >= 70:
    print("C")
elif test_score >= 60:
    print("D")
else:
    print("F")


# Challenge: Wi-Fi Signal
# You're building a feature for a coffee shop that has spotty wi-fi. The feature should give
# customers a discount based on how many signal bars they're getting.
# Write an if/elif/else chain that prints a message for the customer's discount:
#   0 bars: "50% off, sorry about the Wi-Fi!"
#   1 or 2 bars: "25% off"
#   3 or 4 bars: "10% off"
#   5 bars: "Full bars, no discount today!"

signal = 2  # out of 5 bars

if signal == 0:
    print("50% off, sorry about the Wi-Fi!")
elif signal <= 2:
    print("25% off")
elif signal <= 4:
    print("10% off")
else:
    print("Full bars, no discount today!")
