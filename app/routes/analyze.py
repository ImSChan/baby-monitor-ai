from fastapi import APIRouter, UploadFile, File

router = APIRouter(prefix="/analyze")


@router.post("/")
async def analyze(
    video: UploadFile = File(...),
    audio: UploadFile = File(...)
):
    # 파일 읽기 (껍데기)
    video_bytes = await video.read()
    audio_bytes = await audio.read()

    # TODO: 실제 모델 연결
    return {
        "state": "unknown",
        "confidence": 0.0,
        "message": "analyze endpoint placeholder"
    }