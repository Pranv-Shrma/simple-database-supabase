import os
from supabase import create_client, Client

# url: str = os.environ.get("SUPABASE_URL")
# key: str = os.environ.get("SUPABASE_KEY")
url = "https://phbrwlmmwvuxjfkenpbs.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InBoYnJ3bG1td3Z1eGpma2VucGJzIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MjkzMzU3MTEsImV4cCI6MjA0NDkxMTcxMX0.qrKu35GHwlMAuhJVi4o1mLgEKSFvuPsYBVOQXaQH8xI"
supabase: Client = create_client(url, key)



def upload_data(first_name,last_name,age):
    supabase.table("details").insert({"first_name": first_name,"last_name": last_name,"age": age}).execute()
