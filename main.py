# libs
import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from uvicorn import Config as uvi_config, Server as uvi_server

# imports
from routers.nav import nav

# =============================================================================
# print(os.environ.get("SITE_ENV"))
server_config: uvi_config = uvi_config(
    app="main:app", host="0.0.0.0", port=8062, root_path="."
)

if os.environ.get("SITE_ENV") == "PRODUCTION":
    server_config.headers.append(("Cache-Control", "must-revalidate"))
    server_config.port = 8000
else:
    server_config.log_level = "debug"
    server_config.ssl_certfile = "./certs/dev-cert.pem"
    server_config.ssl_keyfile = "./certs/dev-key.pem"
    server_config.headers.append(("Cache-Control", "must-revalidate"))

server: uvi_server = uvi_server(server_config)
# -------------------------------------
app = FastAPI(root_path=".")
origins: list[str] = ["http://localhost", "http://127.0.0.1", "http://[::]", "https://*.joshsw.dev", "https://brave-cliff-0fa190610.1.azurestaticapps.net","jdev-beg0bfd8bhdxgxez.centralus-01.azurewebsites.net"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------------------------------------------------

app.mount(path="/public", app=StaticFiles(directory="public"), name="public")
app.mount(
    path="/senza",
    app=StaticFiles(directory="senza"),
    name="senza",
)
app.mount(
    path="/packages",
    app=StaticFiles(directory="packages"),
    name="packages",
)
# -----------
app.mount(
    path="/web",
    app=StaticFiles(directory="web"),
    name="web",
)
app.mount(
    path="/assets",
    app=StaticFiles(directory="assets"),
    name="assets",
)
# ---------------------------------------------------------
app.include_router(nav)
# ---------------------------------------------------------


@app.get("/status")
def get_status() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/favicon.ico")
def get_favicon() -> FileResponse:
    return FileResponse(path="public/favicon.ico", status_code=200)


# ------------------------------------------------------------------------------


if __name__ == "__main__":
    server.run()
