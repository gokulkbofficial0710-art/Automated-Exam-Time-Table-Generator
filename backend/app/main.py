from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.core.database import engine, Base, SessionLocal
from app.core.security import get_password_hash
from app.models.user import User
from app.models.room import Room
from app.services.demo_data import load_demo_dataset

# API Routers
from app.api.auth import router as auth_router
from app.api.exams import router as exams_router
from app.api.students import router as students_router
from app.api.rooms import router as rooms_router
from app.api.timeslots import router as timeslots_router
from app.api.timetable import router as timetable_router
from app.api.conflicts import router as conflicts_router
from app.api.analytics import router as analytics_router
from app.api.data_io import router as data_io_router
from app.api.backlogs import router as backlogs_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Initialize database tables
    Base.metadata.create_all(bind=engine)

    # Seed default admin user and demo dataset if database is fresh
    db = SessionLocal()
    try:
        admin = db.query(User).filter_by(username="admin").first()
        if not admin:
            admin_user = User(
                username="admin",
                email="admin@university.edu",
                hashed_password=get_password_hash("admin123"),
                full_name="University Scheduling Administrator",
                role="admin",
                is_active=True
            )
            db.add(admin_user)
            db.commit()

        # Check if rooms table is empty, auto-load demo data so user gets immediate out-of-the-box working experience
        if db.query(Room).count() == 0:
            load_demo_dataset(db)
    finally:
        db.close()

    yield

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="Intelligent Examination Timetable Generator powered by Google OR-Tools CP-SAT",
    lifespan=lifespan
)

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # In development allow all for easy frontend integration
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Health Check
@app.get("/api/health")
def health_check():
    return {
        "status": "HEALTHY",
        "app_name": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "environment": settings.ENVIRONMENT
    }

# Register API Routers
app.include_router(auth_router, prefix="/api")
app.include_router(exams_router, prefix="/api")
app.include_router(students_router, prefix="/api")
app.include_router(rooms_router, prefix="/api")
app.include_router(timeslots_router, prefix="/api")
app.include_router(timetable_router, prefix="/api")
app.include_router(conflicts_router, prefix="/api")
app.include_router(analytics_router, prefix="/api")
app.include_router(data_io_router, prefix="/api")
app.include_router(backlogs_router, prefix="/api")
