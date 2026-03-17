from sqladmin import Admin, ModelView
from src.db.main import engine
from src.books.models import Book
from src.auth.models import User

class BookAdmin(ModelView, model=Book):
    column_list = ["uid", "title", "author", "publisher", "published_date", "page_count", "language", "created_at", "updated_at"]

class UserAdmin(ModelView, model=User):
    column_list = ["uid", "username", "email", "first_name", "last_name", "id_verified", "created_at", "updated_at"]

def setup_admin(app):
    admin = Admin(app, engine)
    admin.add_view(BookAdmin)
    admin.add_view(UserAdmin)
    return admin
