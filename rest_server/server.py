import uvicorn
from config import *
from fastapi import FastAPI

# Initialize FastAPI server
app = FastAPI(debug=APP_DEBUG,
              title=APP_NAME,
              description=APP_DESCRIPTION,
              version=APP_VERSION,
              openapi_url="/api/{app_version}/schemas/openapi.json".format(
                  app_version=APP_VERSION))

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=9009)
