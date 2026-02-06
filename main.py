import os
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.api_routes import api_router


load_dotenv()

app = FastAPI()

app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["GET", "PUT", "POST", "DELETE"],
        allow_headers=["*"],
    )


@app.get("/")
def root():
    return {"message": "This is Hello from root "}

app.include_router(api_router, prefix="/api/v1")




# python -m uvicorn main:app --reload
# pip freeze > requirements.txt

# npx supabase migration new create_expenses_table
# npx supabase login // please login with you supabase account
# npx supabase link (Here select the proejct you created on supabase for this app)
# NOTE: Do not create and table manually on supabase dashboard We are doing it here create the table using migration file
# npx supabase db push (This will push the migration to your supabase project and create the expenses table in your database)
# npx supabase migration up

# npx supabase db reset --linked (This will reset your database and run all the migrations again, use this if you want to start fresh with the database in case of any issues and run all commands above again to set up the database)



