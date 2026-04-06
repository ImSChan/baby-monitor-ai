from fastapi import APIRouter, Body
import uuid

router = APIRouter(prefix="/stream")

# 임시 세션 저장
SESSIONS = {}


# 1️⃣ 세션 시작
@router.post("/start")
def start_session():
    session_id = str(uuid.uuid4())

    SESSIONS[session_id] = {
        "frames": [],
        "audio": []
    }

    return {
        "session_id": session_id
    }


# 2️⃣ 스트림 데이터 수신
@router.post("/push")
def push_stream(data: dict = Body(...)):

    session_id = data.get("session_id")
    frame = data.get("frame")        # base64 or blob
    audio_chunk = data.get("audio")  # base64 or blob

    if session_id not in SESSIONS:
        return {"error": "invalid session"}

    # 저장 (껍데기)
    SESSIONS[session_id]["frames"].append(frame)
    SESSIONS[session_id]["audio"].append(audio_chunk)

    return {"status": "received"}


# 3️⃣ 현재 분석 결과 조회
@router.get("/result/{session_id}")
def get_result(session_id: str):

    if session_id not in SESSIONS:
        return {"error": "invalid session"}

    # TODO: 실제 분석 연결
    return {
        "state": "unknown",
        "confidence": 0.0,
        "message": "stream result placeholder"
    }


# 4️⃣ 세션 종료
@router.post("/end")
def end_session(data: dict = Body(...)):

    session_id = data.get("session_id")

    if session_id in SESSIONS:
        del SESSIONS[session_id]

    return {"status": "ended"}
import uuid

router = APIRouter(prefix="/stream")

# 임시 세션 저장
SESSIONS = {}


# 1️⃣ 세션 시작
@router.post("/start")
def start_session():
    session_id = str(uuid.uuid4())

    SESSIONS[session_id] = {
        "frames": [],
        "audio": []
    }

    return {
        "session_id": session_id
    }


# 2️⃣ 스트림 데이터 수신
@router.post("/push")
def push_stream(data: dict = Body(...)):

    session_id = data.get("session_id")
    frame = data.get("frame")        # base64 or blob
    audio_chunk = data.get("audio")  # base64 or blob

    if session_id not in SESSIONS:
        return {"error": "invalid session"}

    # 저장 (껍데기)
    SESSIONS[session_id]["frames"].append(frame)
    SESSIONS[session_id]["audio"].append(audio_chunk)

    return {"status": "received"}


# 3️⃣ 현재 분석 결과 조회
@router.get("/result/{session_id}")
def get_result(session_id: str):

    if session_id not in SESSIONS:
        return {"error": "invalid session"}

    # TODO: 실제 분석 연결
    return {
        "state": "unknown",
        "confidence": 0.0,
        "message": "stream result placeholder"
    }


# 4️⃣ 세션 종료
@router.post("/end")
def end_session(data: dict = Body(...)):

    session_id = data.get("session_id")

    if session_id in SESSIONS:
        del SESSIONS[session_id]

    return {"status": "ended"}