"""
Simple test script to verify the setup and basic functionality
Run this script to test the application components without starting the full server
"""

import sys
import os
from datetime import datetime, timedelta
from uuid import uuid4

# Add the project root to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def test_imports():
    """Test that all required modules can be imported"""
    print("🧪 Testing imports...")
    
    try:
        from models.schemas import (
            Transaction, User, MLAnalysisResult, TransactionType,
            RiskCategory, SpendingStability
        )
        print("✅ Models imported successfully")
        
        from transaction_risk_model import TransactionRiskModel
        print("✅ ML model imported successfully")
        
        from services.supabase_service import SupabaseService
        print("✅ Supabase service imported successfully")
        
        from services.webhook_service import WebhookService
        print("✅ Webhook service imported successfully")
        
        from utils.helpers import (
            calculate_date_range, format_currency, 
            validate_account_number, validate_ifsc_code
        )
        print("✅ Utilities imported successfully")
        
        return True
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False


def test_ml_model():
    """Test the ML model with sample data"""
    print("\n🧪 Testing ML model...")
    
    try:
        from transaction_risk_model import TransactionRiskModel
        from models.schemas import Transaction, TransactionType
        
        # Create ML model instance
        model = TransactionRiskModel()
        print("✅ ML model instance created")
        
        # Create sample transactions
        sample_transactions = []
        user_id = uuid4()
        
        # Add some sample credit transactions (income)
        for i in range(5):
            transaction = Transaction(
                user_id=user_id,
                date=datetime.utcnow() - timedelta(days=i*30),
                description=f"Salary Credit {i+1}",
                amount=50000.0,
                type=TransactionType.CREDIT,
                category="salary",
                upi_app=None
            )
            sample_transactions.append(transaction)
        
        # Add some sample debit transactions (expenses)
        expense_data = [
            ("Grocery Shopping", 3000, "groceries"),
            ("Electricity Bill", 1500, "utilities"),
            ("Restaurant", 800, "food"),
            ("Movie Tickets", 600, "entertainment"),
            ("Fuel", 2000, "transport")
        ]
        
        for i, (desc, amount, category) in enumerate(expense_data):
            for month in range(3):  # 3 months of data
                transaction = Transaction(
                    user_id=user_id,
                    date=datetime.utcnow() - timedelta(days=month*30 + i),
                    description=desc,
                    amount=amount,
                    type=TransactionType.DEBIT,
                    category=category,
                    upi_app="GPay" if i % 2 == 0 else "PhonePe"
                )
                sample_transactions.append(transaction)
        
        print(f"✅ Created {len(sample_transactions)} sample transactions")
        
        # Run analysis
        result = model.analyze_transactions(sample_transactions)
        print("✅ ML analysis completed successfully")
        
        # Verify result structure
        assert hasattr(result, 'overall_risk_score')
        assert hasattr(result, 'risk_category')
        assert hasattr(result, 'loan_eligibility')
        assert hasattr(result, 'financial_summary')
        assert hasattr(result, 'behavioral_analysis')
        
        print(f"✅ Risk Score: {result.overall_risk_score}")
        print(f"✅ Risk Category: {result.risk_category}")
        print(f"✅ Loan Eligible: {result.loan_eligibility}")
        print(f"✅ Transaction Frequency: {result.financial_summary.transaction_frequency}")
        
        return True
        
    except Exception as e:
        print(f"❌ ML model test failed: {e}")
        return False


def test_utilities():
    """Test utility functions"""
    print("\n🧪 Testing utilities...")
    
    try:
        from utils.helpers import (
            validate_account_number, validate_ifsc_code,
            format_currency, calculate_date_range
        )
        
        # Test account number validation
        assert validate_account_number("1234567890") == True
        assert validate_account_number("12345") == False
        print("✅ Account number validation works")
        
        # Test IFSC code validation
        assert validate_ifsc_code("SBIN0001234") == True
        assert validate_ifsc_code("INVALID") == False
        print("✅ IFSC code validation works")
        
        # Test currency formatting
        formatted = format_currency(12345.67)
        assert "12,345.67" in formatted
        print("✅ Currency formatting works")
        
        # Test date range calculation
        start_date, end_date = calculate_date_range(30)
        assert (end_date - start_date).days == 30
        print("✅ Date range calculation works")
        
        return True
        
    except Exception as e:
        print(f"❌ Utilities test failed: {e}")
        return False


def test_pydantic_models():
    """Test Pydantic model validation"""
    print("\n🧪 Testing Pydantic models...")
    
    try:
        from models.schemas import User, Transaction, TransactionType
        
        # Test User model
        user = User(
            name="Test User",
            account_no="1234567890",
            ifsc_code="SBIN0001234"
        )
        assert user.name == "Test User"
        print("✅ User model validation works")
        
        # Test Transaction model
        transaction = Transaction(
            user_id=uuid4(),
            date=datetime.utcnow(),
            description="Test Transaction",
            amount=1000.0,
            type=TransactionType.DEBIT,
            category="test",
            upi_app="GPay"
        )
        assert transaction.amount == 1000.0
        print("✅ Transaction model validation works")
        
        return True
        
    except Exception as e:
        print(f"❌ Pydantic models test failed: {e}")
        return False


def test_environment_setup():
    """Test environment variable setup"""
    print("\n🧪 Testing environment setup...")
    
    try:
        # Check if .env.example exists
        if os.path.exists(".env.example"):
            print("✅ .env.example file exists")
        else:
            print("⚠️  .env.example file not found")
        
        # Check if .env file exists
        if os.path.exists(".env"):
            print("✅ .env file exists")
        else:
            print("⚠️  .env file not found (copy from .env.example)")
        
        # Test environment variable loading
        from dotenv import load_dotenv
        load_dotenv()
        
        supabase_url = os.getenv("SUPABASE_URL")
        supabase_key = os.getenv("SUPABASE_KEY")
        
        if supabase_url and supabase_key:
            print("✅ Supabase credentials configured")
        else:
            print("⚠️  Supabase credentials not configured")
        
        return True
        
    except Exception as e:
        print(f"❌ Environment setup test failed: {e}")
        return False


def main():
    """Run all tests"""
    print("🚀 Starting Transaction Risk Analytics Setup Test\n")
    
    tests = [
        ("Imports", test_imports),
        ("ML Model", test_ml_model),
        ("Utilities", test_utilities),
        ("Pydantic Models", test_pydantic_models),
        ("Environment Setup", test_environment_setup)
    ]
    
    results = []
    for test_name, test_func in tests:
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"❌ {test_name} test crashed: {e}")
            results.append((test_name, False))
    
    # Summary
    print("\n" + "="*50)
    print("📊 TEST SUMMARY")
    print("="*50)
    
    passed = 0
    for test_name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{test_name:20} {status}")
        if result:
            passed += 1
    
    print(f"\nTests passed: {passed}/{len(results)}")
    
    if passed == len(results):
        print("\n🎉 All tests passed! Your setup is ready.")
        print("\nNext steps:")
        print("1. Configure your .env file with Supabase credentials")
        print("2. Run: python app.py")
        print("3. Visit: http://localhost:8000/docs")
    else:
        print(f"\n⚠️  {len(results) - passed} test(s) failed. Please check the errors above.")
    
    return passed == len(results)


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
