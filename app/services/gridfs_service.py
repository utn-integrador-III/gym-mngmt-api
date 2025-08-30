# app/services/gridfs_service.py
from motor.motor_asyncio import AsyncIOMotorDatabase, AsyncIOMotorGridFSBucket
from bson import ObjectId
from typing import Optional

class GridFSService:
    def __init__(self, database: AsyncIOMotorDatabase):
        """
        Inicializa el servicio de GridFS con la base de datos dada.
        """
        self.db = database
        self.bucket = AsyncIOMotorGridFSBucket(self.db, bucket_name="photos")  # bucket_name opcional

    async def upload_file(self, file_bytes: bytes, filename: str, content_type: Optional[str] = None) -> str:
        """
        Sube un archivo a GridFS.
        :param file_bytes: El contenido del archivo en bytes.
        :param filename: Nombre original del archivo.
        :param content_type: Tipo MIME opcional.
        :return: ID del archivo como string.
        """
        file_id = await self.bucket.upload_from_stream(
            filename=filename,
            source=file_bytes,
            metadata={"contentType": content_type} if content_type else None
        )
        return str(file_id)

    async def download_file(self, file_id: str) -> Optional[bytes]:
        """
        Descarga un archivo desde GridFS usando su ID.
        :param file_id: ID del archivo (ObjectId como string).
        :return: Contenido del archivo en bytes o None si no existe.
        """
        try:
            file_obj = await self.bucket.open_download_stream(ObjectId(file_id))
            chunks = []
            async for chunk in file_obj:
                chunks.append(chunk)
            return b"".join(chunks)
        except Exception:
            return None

    async def delete_file(self, file_id: str) -> bool:
        """
        Elimina un archivo de GridFS usando su ID.
        :param file_id: ID del archivo (ObjectId como string).
        :return: True si fue eliminado, False si no existía.
        """
        try:
            await self.bucket.delete(ObjectId(file_id))
            return True
        except Exception:
            return False
