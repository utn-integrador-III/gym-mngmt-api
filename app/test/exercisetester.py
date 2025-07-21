from app.models.exercise import ExerciseModel

exercise = ExerciseModel(
    name="Push Ups",
    description="Upper body exercise using body weight"
)

print("🧪 Ejercicio creado:")
print(exercise)
print("🆔 ID generado:", exercise.id)
print("📦 JSON serializado:", exercise.model_dump(by_alias=True))
