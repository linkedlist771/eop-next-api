from hashlib import sha256
from database import *
from models import *
from services import *
from utils import *
from utils.config import *

router = APIRouter()


@router.post(
    "/login",
    summary="登陆接口",
    responses={
        200: {
            "description": "登陆成功",
            "content": {
                "application/json": {
                    "example": {
                        "access_token": "eyJhbxxxxxxxxxxxxxxxxxxxxxxxx",
                        "token_type": "Bearer",
                    }
                }
            },
        },
    },
)
async def _(
    body: LoginBody = Body(examples=[{"user": "用户名", "passwd": "加密后的密码"}]),
):
    if not await User.check_user(body.user, body.passwd):
        return JSONResponse({"code": 1001, "msg": "认证失败"}, 401)

    token = create_token({"user": body.user})
    return JSONResponse({"access_token": token, "token_type": "Bearer"}, 200)


@router.get(
    "/bots",
    summary="拉取用户可用会话",
    responses={
        200: {
            "description": "会话列表",
            "content": {
                "application/json": {
                    "example": {
                        "bots": [
                            {
                                "handle": "bot_A_handle",
                                "alias": "AAA",
                                "model": "ChatGPT",
                                "prompt": "prompt_A",
                                "create_time": 1692695313,
                                "last_talk_time": 1692695313,
                            },
                            {
                                "handle": "bot_B_handle",
                                "alias": "BBB",
                                "model": "ChatGPT4",
                                "prompt": "prompt_B",
                                "create_time": 1692695313,
                                "last_talk_time": 1692695313,
                            },
                        ]
                    }
                }
            },
        },
    },
)
async def _(user_data: dict = Depends(verify_token)):
    user = user_data["user"]
    botList = await Bot.get_user_bots(user)
    return JSONResponse({"bots": botList}, 200)


@router.get(
    "/verifyAdmin",
    summary="判断是否为管理员",
    responses={
        200: {
            "description": "无相关响应",
        },
        204: {
            "description": "是管理员",
        },
    },
)
async def _(_: dict = Depends(verify_admin)):
    return Response(status_code=204)


@router.put(
    "/password",
    summary="修改密码",
    responses={
        200: {
            "description": "无相关响应",
        },
        204: {
            "description": "修改成功",
        },
    },
)
async def _(
    body: UpdatePasswdBody = Body(
        example={"old_passwd": "加密的旧密码", "new_passwd": "加密的新密码"}
    ),
    user_data: dict = Depends(verify_token),
):
    user = user_data["user"]
    if not await User.check_user(user, body.old_passwd):
        return JSONResponse({"code": 1001, "msg": "Wrong password"}, 401)

    await User.update_passwd(user, body.new_passwd)
    return Response(status_code=204)


@router.get("/getPasswd", summary="生成密码哈希（临时）")
async def _(passwd: str = Query(description="明文密码", example="this_is_a_password")):
    hash_object = sha256()
    hash_object.update(passwd.encode("utf-8"))
    hash_value = hash_object.hexdigest()
    return hash_value
