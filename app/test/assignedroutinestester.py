# testers/test_assigned_routines.py
from app.models.assignedroutines import AssignedRoutinesModel
from bson import ObjectId

# Crear IDs de prueba como ObjectId (no string)
coach_id = ObjectId()
client_id = ObjectId()
routine_id = ObjectId()

# Crear instancia del modelo
assigned = AssignedRoutinesModel(
    id_coach=coach_id,
    id_client=client_id,
    id_dailyroutineexercise=routine_id,  # <- nombre correcto del campo
    notes="Focus on form and breathing",
    done=False,
    dayofweek="lunes"
)

print("🧪 Rutina asignada creada:")
print(assigned)
print("🆔 ID generado:", str(assigned.id))

# Mostrar JSON serializado
print("📦 JSON serializado:", assigned.model_dump(by_alias=True))
