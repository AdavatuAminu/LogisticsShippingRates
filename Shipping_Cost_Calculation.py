# Shipping Cost Calculator

## Input package weight and shipping rate
Weight = float(input("Enter the package weight in kiligram: "))
rate = float(input("Enter the shipping rate per kilogram: "))

## Calculation shipping cost
shipping_cost = weight * rate 

## Display the result
Print(f"Shipping Cost: {shipping_cost} USD")
