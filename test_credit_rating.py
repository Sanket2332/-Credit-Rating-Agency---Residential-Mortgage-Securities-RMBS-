import unittest
import json
from credit_rating import RMBSRatingCalculator, calculate_credit_rating

class TestRMBSRatingCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = RMBSRatingCalculator()
        
    def test_aaa_rating(self):
        """Test a high-quality RMBS that should get AAA rating"""
        data = {
            "mortgages": [
                {
                    "credit_score": 750,
                    "loan_amount": 200000,
                    "property_value": 250000,
                    "annual_income": 60000,
                    "debt_amount": 20000,
                    "loan_type": "fixed",
                    "property_type": "single_family"
                },
                {
                    "credit_score": 720,
                    "loan_amount": 180000,
                    "property_value": 225000,
                    "annual_income": 55000,
                    "debt_amount": 15000,
                    "loan_type": "fixed",
                    "property_type": "single_family"
                }
            ]
        }
        self.assertEqual(self.calculator.calculate_credit_rating(data), "AAA")
        
    def test_bbb_rating(self):
        """Test a medium-quality RMBS that should get BBB rating"""
        data = {
            "mortgages": [
                {
                    "credit_score": 680,
                    "loan_amount": 200000,
                    "property_value": 220000,
                    "annual_income": 50000,
                    "debt_amount": 25000,
                    "loan_type": "adjustable",
                    "property_type": "condo"
                }
            ]
        }
        self.assertEqual(self.calculator.calculate_credit_rating(data), "BBB")
        
    def test_c_rating(self):
        """Test a low-quality RMBS that should get C rating"""
        data = {
            "mortgages": [
                {
                    "credit_score": 600,
                    "loan_amount": 200000,
                    "property_value": 200000,
                    "annual_income": 40000,
                    "debt_amount": 25000,
                    "loan_type": "adjustable",
                    "property_type": "condo"
                },
                {
                    "credit_score": 620,
                    "loan_amount": 180000,
                    "property_value": 180000,
                    "annual_income": 35000,
                    "debt_amount": 20000,
                    "loan_type": "adjustable",
                    "property_type": "condo"
                }
            ]
        }
        self.assertEqual(self.calculator.calculate_credit_rating(data), "C")
        
    def test_empty_mortgages(self):
        """Test with empty mortgages list"""
        with self.assertRaises(ValueError):
            self.calculator.calculate_credit_rating({"mortgages": []})
            
    def test_missing_field(self):
        """Test with missing required field"""
        data = {
            "mortgages": [
                {
                    "credit_score": 700,
                    "loan_amount": 200000,
                    # Missing property_value
                    "annual_income": 60000,
                    "debt_amount": 20000,
                    "loan_type": "fixed",
                    "property_type": "single_family"
                }
            ]
        }
        with self.assertRaises(ValueError):
            self.calculator.calculate_credit_rating(data)
            
    def test_invalid_credit_score(self):
        """Test with invalid credit score"""
        data = {
            "mortgages": [
                {
                    "credit_score": 200,  # Invalid
                    "loan_amount": 200000,
                    "property_value": 250000,
                    "annual_income": 60000,
                    "debt_amount": 20000,
                    "loan_type": "fixed",
                    "property_type": "single_family"
                }
            ]
        }
        with self.assertRaises(ValueError):
            self.calculator.calculate_credit_rating(data)
            
    def test_convenience_function(self):
        """Test the convenience function"""
        data = {
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
        self.assertEqual(calculate_credit_rating(data), "AAA")

if __name__ == "__main__":
    unittest.main()