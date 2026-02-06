from db_client import supabase
from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.delete("/expenses/{expense_id}")
def delete_expense(expense_id: int):
    try: 
        response = supabase.table("expenses").delete().eq("id", expense_id).execute()
        
        if response.data:
            return {"success": True, "message": "Expense deleted"}
        else:
            raise HTTPException(status_code=404, detail="Expense not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))