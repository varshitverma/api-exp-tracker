import os
from fastapi import APIRouter, HTTPException
from db_client import supabase
import requests

router = APIRouter()

# Exchange rate API configuration. 
# please generate your own API key & update the .env file.
# https://app.exchangerate-api.com/
EXCHANGE_RATE_API_URL = os.environ.get("EXCHANGE_RATE_API_URL")

@router.get("/expenses")
def get_expenses():
    try:
        response = supabase.table("expenses").select("*").execute()
        
        if response.data:
            return {"success": True, "data": response.data}
        else:
            return {"success": True, "data": []}
    except Exception as e:
        raise HTTPException(status_code= 500, detail=str(e))


@router.get("/expenses/{expense_id}")
def get_expense(expense_id: int):
    try:
        response = supabase.table("expenses").select("*").eq("id", expense_id).execute()
        
        if response.data:
            return {"success": True, "data": response.data[0]}
        else:
            raise HTTPException(status_code = 404, detail="Expense not found")
    except Exception as e:
        raise HTTPException(status_code = 500, detail=str(e))


@router.get("/expenses/convert/{target_currency}")
def convert_expenses_to_currency(target_currency: str):
    try:
        # Fetch all expenses
        response = supabase.table("expenses").select("*").execute()
        
        if not response.data:
            return {
                "success": True,
                "data": [],
                "total_in_target_currency": 0,
                "exchange_rate": None,
                "target_currency": target_currency
            }
        
        base_currency = "INR"
        
        try:
            exchange_response = requests.get(f"{EXCHANGE_RATE_API_URL}/{base_currency}")
            exchange_response.raise_for_status()
            exchange_data = exchange_response.json()
            
            if exchange_data.get("result") != "success":
                raise HTTPException(status_code=400, detail="Invalid currency code or API error")
            
            rates = exchange_data.get("conversion_rates", {})
            exchange_rate = rates.get(target_currency.upper())
            
            if not exchange_rate:
                raise HTTPException(status_code=400, detail=f"Target currency '{target_currency}' not supported")
            
        except requests.exceptions.RequestException as e:
            raise HTTPException(status_code=502, detail=f"Failed to fetch exchange rates: {str(e)}")
        
        # Convert expenses
        converted_expenses = []
        total_in_target_currency = 0
        
        for expense in response.data:
            converted_amount = expense.get("amount", 0) * exchange_rate
            total_in_target_currency += converted_amount
            
            converted_expense = {
                **expense,
                "original_amount": expense.get("amount"),
                "original_currency": base_currency,
                "converted_amount": round(converted_amount, 2),
                "target_currency": target_currency.upper()
            }
            converted_expenses.append(converted_expense)
        
        return {
            "success": True,
            "data": converted_expenses,
            "total_in_target_currency": round(total_in_target_currency, 2),
            "exchange_rate": exchange_rate,
            "target_currency": target_currency.upper(),
            "base_currency": base_currency
        }
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
