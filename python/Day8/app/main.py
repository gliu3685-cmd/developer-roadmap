from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from app.database import SessionLocal, engine
from app.models import Base, User
from app.schemas import UserCreate, UserResponse


app = FastAPI()


Base.metadata.create_all(bind=engine)



def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()



@app.get("/")
def home():

    return {
        "message":"User System Day8"
    }



# 创建用户
@app.post(
    "/users",
    response_model=UserResponse
)
def create_user(
        user: UserCreate,
        db: Session = Depends(get_db)
):

    db_user = User(
        name=user.name,
        age=user.age
    )


    db.add(db_user)

    db.commit()

    db.refresh(db_user)


    return db_user



# 查询全部用户
@app.get(
    "/users",
    response_model=list[UserResponse]
)
def get_users(
        db: Session = Depends(get_db)
):

    return db.query(User).all()
