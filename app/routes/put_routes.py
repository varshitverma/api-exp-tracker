from fastapi import APIRouter, HTTPException
from app.model.expense_model import Expense
from db_client import supabase

router = APIRouter()

@router.put("/expenses/{expense_id}")
def update_expense(expense_id: int, expense: Expense):
    try:
        data = {
            "amount": expense.amount,
            "category": expense.category,
            "description": expense.description,
            "date": expense.date.isoformat(),
            "payment_method": expense.payment_method,
        }
        
        response = supabase.table("expenses").update(data).eq("id", expense_id).execute()
        
        if response.data:
            return {"success": True, "message": "Expense updated", "data": response.data[0]}
        else:
            raise HTTPException(status_code=404, detail="Expense not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
