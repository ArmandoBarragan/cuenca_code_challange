from fastapi import APIRouter, HTTPException, status, Body
from app.schemas import BoardSizePayloadSchema, AllSolutionsSchema
from app.controllers.api_controller import APIController


router = APIRouter()
api_controller = APIController()


@router.post(
    "/solutions/", response_model=AllSolutionsSchema, status_code=status.HTTP_200_OK
)
def get_solutions(payload: BoardSizePayloadSchema = Body(...)):
    if payload.size < 4:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Board size has to be equal or greater than 4x4",
        )

    return api_controller.make_solutions(payload=payload)
