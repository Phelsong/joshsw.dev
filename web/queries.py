from pyodide.http import pyfetch

# base_url: str = "http://[::1]:8000"
base_url: str = "https://local.dev:8062"


# ----------------------------------------------------------------
async def query_ex(url: str) -> dict:
    try:
        response: str = await pyfetch(url)
        result: dict = await response.json()
        return result
    except Exception as e:
        result: dict = {"error": str(e)}
        return result


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
        response: str = await pyfetch(extension)
        result: dict = await response.text()
        return result
    except Exception as e:
        result: dict = {"error": str(e)}
        return result


# ----------------------------------------------------------------
