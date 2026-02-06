from fastapi import APIRouter, HTTPException
from app.model.expense_model import Expense
from db_client import supabase
router = APIRouter()

@router.post("/expenses")
def create_expense(expense: Expense):
    try:
        data = {
            "amount": expense.amount,
            "category": expense.category,
            "description": expense.description,
            "date": expense.date.isoformat(),
            "payment_method": expense.payment_method,
        }
        
        response = supabase.table("expenses").insert(data).execute()
        
        if response.data:
            return {"success": True, "message": "Expense added", "data": response.data[0]}
        else:
            raise HTTPException(status_code=400, detail="Failed to add expense")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
