from pyscript import fetch
from web.context import site


# ----------------------------------------------------------------
async def query_ex(url: str) -> dict:
    try:
        resp: str = await fetch(url).json()
        return resp
    except Exception as e:
        return {"error": str(e)}


# ----------------------------------------------------------------
async def send_data(data: dict):
    try:
        response = await pyfetch(
            url=data["callbackUrl"],
            method="POST",
            headers={"Content-type": "application/json"},
            body=json.dumps(data),
        )
    except Exception as e:
        print(e)


# ----------------------------------------------------------------
async def get_data_txt(extension: str):
    try:
        resp: str = await fetch(extension).text()
        return resp
    except Exception as e:
        return {"error": str(e)}


# ----------------------------------------------------------------
