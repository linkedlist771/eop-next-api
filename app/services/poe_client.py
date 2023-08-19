from .poe_lib import Poe_Client
from database import Config
from utils import *


class Poe:
    client = Poe_Client("", "")


poe = Poe()


async def login_poe() -> JSONResponse | Response:
    p_b, formkey, proxy = await Config.get_setting()
    if proxy:
        logger.info(f"使用代理连接Poe {proxy}")
    else:
        proxy = None
    try:
        poe.client = await Poe_Client(p_b, formkey, proxy).create()
        return Response(status_code=204)
    except Exception as e:
        msg = "poe ai 登陆失败。" + str(e)
        logger.error(msg)
        return JSONResponse({"code": 3008, "msg": msg}, 500)
