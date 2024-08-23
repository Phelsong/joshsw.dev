# libs
# import libsql_client as turso
from fastapi import APIRouter, Query
import os
from typing import Annotated

# from fastapi.middlewares.session import SessionMiddleware
from fastapi.responses import (
    HTMLResponse,
    RedirectResponse,
    ORJSONResponse,
)
from pydantic import BaseModel, HttpUrl, Strict, AnyHttpUrl

# imports


# =============================================================================

nav = APIRouter(
    prefix="",
    tags=["site elements and redirects"],
    responses={404: {"description": "Not found"}},
)

SITE_ENV = os.environ["SITE_ENV"] if os.environ.get("SITE_ENV") else "development"

# =============================================================================


@nav.get("/", response_class=HTMLResponse)
async def dashboard() -> HTMLResponse:
    html = """
<!DOCTYPE pyscript>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <!-- ================================================================================== -->
    <link async defer
      rel="stylesheet"
      href="https://pyscript.net/releases/2024.8.2/core.css"
    />
    <script async
      type="module"
      src="https://pyscript.net/releases/2024.8.2/core.js"
    ></script>
    <link async defer rel="stylesheet" href="/public/index.css" />
    <!-- ================================================================================== -->
    <title>joshsw.dev</title>
  </head>
  <body>
    <!-- ==================================================== -->
    <script async defer type="mpy" src="web/repl.py" terminal worker></script>
    
    <script async type="py" src="/web/app.py" config="/web/pyscript.toml"></script>
  </body>
</html>
"""
    return HTMLResponse(html, media_type="text/html", status_code=200)
