# RMBS Credit Rating Calculator

This Python solution calculates credit ratings for Residential Mortgage-Backed Securities (RMBS) based on the composition of underlying mortgages.

## Features

- Calculates credit ratings ("AAA", "BBB", or "C") based on mortgage attributes
- Comprehensive input validation
- Unit tested with various test cases
- Clear, well-documented code

## Installation

1. Ensure you have Python 3.8 or higher installed
2. Clone this repository
3. No additional dependencies are required beyond standard Python libraries

## Usage

```python
from credit_rating import calculate_credit_rating

# Sample mortgage data
mortgages_data = {
    "mortgages": [
        {
            "credit_score": 750,
            "loan_amount": 200000,
            "property_value": 250000,
            "annual_income": 60000,
            "debt_amount": 20000,
            "loan_type": "fixed",
            "property_type": "single_family"
        }
    ]
}

# Calculate credit rating
rating = calculate_credit_rating(mortgages_data)
print(f"Credit Rating: {rating}")