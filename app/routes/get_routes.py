from fastapi import APIRouter, HTTPException
from db_client import supabase
router = APIRouter()

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
