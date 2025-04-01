import json
from typing import List, Dict

class RMBSRatingCalculator:
    """
    A class to calculate credit ratings for Residential Mortgage-Backed Securities (RMBS)
    based on the composition of underlying mortgages.
    """
    
    def calculate_credit_rating(self, mortgages_data: Dict) -> str:
        """
        Calculate the overall credit rating for an RMBS based on its constituent mortgages.
        
        Args:
            mortgages_data: A dictionary containing mortgage data in the specified JSON format
            
        Returns:
            str: The credit rating ("AAA", "BBB", or "C")
        """
        if not mortgages_data or "mortgages" not in mortgages_data:
            raise ValueError("Invalid input: mortgages data is missing or malformed")
            
        mortgages = mortgages_data["mortgages"]
        if not mortgages:
            raise ValueError("No mortgages provided in the input")
            
        total_risk_score = 0
        credit_scores = []
        
        for mortgage in mortgages:
            self._validate_mortgage(mortgage)
            risk_score = self._calculate_individual_risk_score(mortgage)
            total_risk_score += risk_score
            credit_scores.append(mortgage["credit_score"])
            
        # Apply adjustment based on average credit score
        avg_credit_score = sum(credit_scores) / len(credit_scores)
        if avg_credit_score >= 700:
            total_risk_score -= 1
        elif avg_credit_score < 650:
            total_risk_score += 1
            
        return self._determine_final_rating(total_risk_score)
        
    def _validate_mortgage(self, mortgage: Dict) -> None:
        """Validate that a mortgage contains all required fields with valid values."""
        required_fields = [
            "credit_score", "loan_amount", "property_value", 
            "annual_income", "debt_amount", "loan_type", "property_type"
        ]
        
        for field in required_fields:
            if field not in mortgage:
                raise ValueError(f"Missing required field: {field}")
                
        if not 300 <= mortgage["credit_score"] <= 850:
            raise ValueError("Credit score must be between 300 and 850")
            
        if mortgage["loan_type"] not in ["fixed", "adjustable"]:
            raise ValueError("Loan type must be either 'fixed' or 'adjustable'")
            
        if mortgage["property_type"] not in ["single_family", "condo"]:
            raise ValueError("Property type must be either 'single_family' or 'condo'")
            
        if mortgage["loan_amount"] <= 0 or mortgage["property_value"] <= 0:
            raise ValueError("Loan amount and property value must be positive")
            
    def _calculate_individual_risk_score(self, mortgage: Dict) -> int:
        """Calculate the risk score for an individual mortgage."""
        risk_score = 0
        
        # Calculate LTV ratio and add risk points
        ltv = (mortgage["loan_amount"] / mortgage["property_value"]) * 100
        if ltv > 90:
            risk_score += 2
        elif ltv > 80:
            risk_score += 1
            
        # Calculate DTI ratio and add risk points
        dti = (mortgage["debt_amount"] / mortgage["annual_income"]) * 100
        if dti > 50:
            risk_score += 2
        elif dti > 40:
            risk_score += 1
            
        # Add risk points based on credit score
        if mortgage["credit_score"] >= 700:
            risk_score -= 1
        elif mortgage["credit_score"] < 650:
            risk_score += 1
            
        # Add risk points based on loan type
        if mortgage["loan_type"] == "adjustable":
            risk_score += 1
        else:  # fixed
            risk_score -= 1
            
        # Add risk points based on property type
        if mortgage["property_type"] == "condo":
            risk_score += 1
            
        return risk_score
        
    def _determine_final_rating(self, total_risk_score: int) -> str:
        """Determine the final credit rating based on the total risk score."""
        if total_risk_score <= 2:
            return "AAA"
        elif 3 <= total_risk_score <= 5:
            return "BBB"
        else:
            return "C"


def calculate_credit_rating(mortgages_data: Dict) -> str:
    """
    Convenience function to calculate RMBS credit rating.
    
    Args:
        mortgages_data: A dictionary containing mortgage data in the specified JSON format
        
    Returns:
        str: The credit rating ("AAA", "BBB", or "C")
    """
    calculator = RMBSRatingCalculator()
    return calculator.calculate_credit_rating(mortgages_data)

if __name__ == "__main__":
    # Sample data that will show output when run directly
    sample_data = {
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
    print("Sample output:", calculate_credit_rating(sample_data))