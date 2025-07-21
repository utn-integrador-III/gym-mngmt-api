from app.models.assigned_routines import AssignedRoutinesModel
from bson import ObjectId

# Crear IDs de prueba como strings
coach_id = str(ObjectId())
client_id = str(ObjectId())
routine_id = str(ObjectId())

# Crear instancia del modelo
assigned = AssignedRoutinesModel(
    id_coach=coach_id,
    id_client=client_id,
    id_routineexercise=routine_id,
    notes="Focus on form and breathing",
    done=False,
    dayofweek="lunes"
)

print("🧪 Rutina asignada creada:")
print(assigned)
print("🆔 ID generado:", str(assigned.id))

# Mostrar JSON serializado
print("📦 JSON serializado:", assigned.model_dump(by_alias=True))
