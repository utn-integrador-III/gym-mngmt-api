from app.models.dailyroutineexercises import DailyRoutineExercisesModel
from bson import ObjectId

# Crear IDs como strings válidos
coach_id = str(ObjectId())
exercise_id = str(ObjectId())

# Crear la rutina diaria de ejercicios
routine = DailyRoutineExercisesModel(
    id_coach=coach_id,
    id_exercise=exercise_id,
    name="Morning Upper Body Routine"
)

print("🧪 Rutina diaria de ejercicio creada:")
print(routine)
print("🆔 ID generado:", str(routine.id))

# Mostrar JSON serializado
print("📦 JSON serializado:", routine.model_dump(by_alias=True))
