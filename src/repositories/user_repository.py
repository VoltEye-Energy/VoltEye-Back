from src.bd.connect import connect
from src.schemas.user_schema import userCreate

class UserRepository:
    table_name = "users"

    def __init__(self):
        self.supabase =  connect()

        
    def create_user(self, usercreate: userCreate):
         return (
            self.supabase.table(self.table_name)
            .insert(usercreate.model_dump(mode="json"))
            .execute()
        )
    
    def get_user_by_email(self, email: str):
        return (
            self.supabase.table(self.table_name)
            .select("*")
            .eq("email", email)
            .execute()
        )