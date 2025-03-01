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
else:
    server_config.log_level = "debug"
    server_config.ssl_certfile = "./certs/dev-cert.pem"
    server_config.ssl_keyfile = "./certs/dev-key.pem"
    server_config.headers.append(("Cache-Control", "must-revalidate"))

server: uvi_server = uvi_server(server_config)
# -------------------------------------
app = FastAPI(root_path=".")
origins: list[str] = [
    "http://localhost",
    "http://127.0.0.1",
    "http://[::]",
    "https://localhost",
    "https://127.0.0.1",
    "https://[::]",
    "https://dev.local",
    "https://*.joshsw.dev",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET"],
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

@app.get("/robots.txt")
def get_robots() -> FileResponse:
    return FileResponse(path="public/robots.txt", status_code=200)

@app.get("/sitemap.xml")
def get_sitemap() -> FileResponse:
    return FileResponse(path="public/sitemap.xml", status_code=200)

# ------------------------------------------------------------------------------


if __name__ == "__main__":
    server.run()
