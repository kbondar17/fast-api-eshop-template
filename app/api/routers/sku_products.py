from corecrud import Options, Where
from fastapi import APIRouter
from fastapi.exceptions import HTTPException
from fastapi.param_functions import Body
from fastapi.responses import Response
from sqlalchemy.orm import selectinload
from starlette import status

from core.app import crud
from core.depends import AuthJWT, Authorization, AuthorizationRefresh, DatabaseSession
from core.security import check_hashed_password
from orm import UserModel, SkuModel
from schemas import ApplicationResponse, BodyLoginRequest, User
from typing_ import RouteReturnT
from utils.cookies import set_and_create_tokens_cookies

router = APIRouter()


@router.get(
    path="/",
    summary="Get get products through orders.",
    response_model=ApplicationResponse[bool],
    status_code=status.HTTP_200_OK,
)
async def get_orders_products(
    response: Response, session: DatabaseSession, user: Authorization
) -> RouteReturnT:
    ...
    надо добавить в бд order with sku, order_sku_product
    и потом попробовать дойти до продуктов через ордера
