from fastapi import APIRouter
from fastapi_utils.cbv import cbv
from starlette.responses import StreamingResponse, JSONResponse
from fastapi import File, UploadFile

from api.core.controller import BaseController
from api.serializers.file_serializers import FileSerializer, FileInfoSerializer
from api.services.file_service import FileService

router = APIRouter()


@cbv(router)
class FileController(BaseController):

    def __init__(self) -> None:
        super(FileController, self).__init__()
        self.file_service = self.injector.get(FileService)

    @router.post('/file/upload')
    async def upload(self, file: UploadFile = File(...)) -> JSONResponse:
        file_id = await self.file_service.save_file(await file.read())
        return JSONResponse(content=FileSerializer(file_id=file_id))

    @router.get('/file/download')
    async def download(self, file_serializer: FileSerializer) -> StreamingResponse:
        file_iterator = await self.file_service.download_file(file_serializer)
        return StreamingResponse(file_iterator)

    @router.get('/file/information')
    async def get_information(self, file_serializer: FileSerializer) -> FileInfoSerializer:
        return await self.file_service.get_file_information(file_serializer)
