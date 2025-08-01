# testers/test_user.py
from app.models.user import UserModel

user = UserModel(
    username="keneth123",
    gender="male",
    phone="8888-8888",
    photo="http://example.com/avatar.jpg"
)

print("🧪 Usuario creado:")
print(user)
print("🆔 ID generado:", user.id)
print("📦 JSON serializado:", user.model_dump(by_alias=True))
