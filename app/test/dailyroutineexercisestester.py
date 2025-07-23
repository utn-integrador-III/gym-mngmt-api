# testers/test_daily_routine_exercise.py
from app.models.dailyroutineexercises import DailyRoutineExercisesModel
from bson import ObjectId

# Crear IDs válidos como ObjectId
coach_id = ObjectId()
exercise_ids = [ObjectId(), ObjectId()]  # lista de ejercicios

# Crear la rutina diaria de ejercicios
routine = DailyRoutineExercisesModel(
    id_coach=coach_id,
    id_exercise=exercise_ids,
    name="Morning Upper Body Routine"
)

print("🧪 Rutina diaria de ejercicio creada:")
print(routine)
print("🆔 ID generado:", str(routine.id))

# Mostrar JSON serializado
print("📦 JSON serializado:", routine.model_dump(by_alias=True))
