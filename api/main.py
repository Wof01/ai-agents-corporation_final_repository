from fastapi import FastAPI
from .idea_expander import router as idea_expander_router
from .writer import router as writer_router

app = FastAPI()

# Include the routers
app.include_router(idea_expander_router, prefix="/expand-idea")
app.include_router(writer_router, prefix="/write-chapter")
