from fastapi import APIRouter

router = APIRouter(prefix="/state")

CURRENT_STATE = {
    "state": "sleeping",
    "confidence": 0.9
}


@router.get("/current")
def get_current():
    return CURRENT_STATE


@router.get("/history")
def get_history():
    return [
        {"state": "sleeping", "time": "10:00"},
        {"state": "crying", "time": "10:05"},
    ]