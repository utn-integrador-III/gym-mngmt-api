from app.models.dailyroutineexercise import DailyRoutineExerciseModel
from bson import ObjectId

daily_routine = DailyRoutineExerciseModel(
    id_coach=ObjectId("66abcdef1234567890abcdef"),
    id_exercise=ObjectId("66abcdef0987654321fedcba"),
    name="Morning Routine A"
)

print("🧪 Rutina creada:")
print(daily_routine)
print("🆔 ID generado:", daily_routine.id)
print("📦 JSON serializado:", daily_routine.model_dump(by_alias=True))
