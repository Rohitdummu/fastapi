
from app.models import UserModel, User
from app.schema import UserModelSQL, Base
from fastapi import FastAPI, Depends, UploadFile
from app.db import SessionLocal 
from app.dependency import get_deb
from sqlalchemy.orm import Session 
from app.db import engine
from fastapi.middleware.cors import CORSMiddleware
from app.utils.indexer import get_embedd, index_doc
from app.utils.retriver import retriver
from app.utils.llm import generate_ans

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"]
)

Base.metadata.create_all(bind=engine)

@app.get("/test")
def get_users():
    return {
        "msg": 'running'
    }

products = [
    User(id=1,name="rahul", email="rahul@mail.com"),
    User(id=2, name="rahul singh", email="rahulsingh@mail.com"),
    User(id=3, name="rahul roy", email="rahulroy@mail.com"),
    User(id=4, name="test", email="test@gmail")
]

def init_prod():
    db = SessionLocal()

    count = db.query(UserModelSQL).count()
    print(f'count of records {count}')
    if count == 0:
        for i in products:
            db.add(UserModelSQL(**i.model_dump()))
        db.commit()

init_prod()


@app.get("/all")
def get_all_products(db: Session = Depends(get_deb)):
    alp = db.query(UserModelSQL).all()
    return alp

@app.get("/prod/{id}")
def get_prod_id(id: int, db: Session = Depends(get_deb)):
    recd = db.query(UserModelSQL).filter(UserModelSQL.id == id).first()
    if recd:
        return recd
    return "not found"

@app.post("/add")
def add_user(prod: User, db: Session = Depends(get_deb)):
    new_prod = UserModelSQL(**prod.model_dump())
    db.add(new_prod)
    db.commit()
    db.refresh(new_prod)
    return new_prod

@app.put("/update")
def update_user(id: int, prod: User, db: Session = Depends(get_deb)):
    recd = db.query(UserModelSQL).filter(UserModelSQL.id == id).first()
    if recd:
        recd.name = prod.name
        recd.email = prod.email
        db.commit()
        return "update done"
    else:
        return "not found"

@app.delete("/delete")
def delete_user(id: int, db: Session = Depends(get_deb)):
    recd = db.query(UserModelSQL).filter(UserModelSQL.id == id).first()
    if recd:
        db.delete(recd)
        db.commit()
        return "delete done"
    else:
        return "not found"
    
@app.post("/upload")
async def upload_doc(file: UploadFile):
    text = (await file.read()).decode("utf-8")
    index_doc(text)
    return {
        "status": "success"
    }

@app.get("/retrive")
def get_doc(query: str):
    docs = retriver(query)
    return {
        "doc": docs
    }


@app.get("/chat")
def get_doc(query: str):
    docs = retriver(query)
    context = "\n".join(docs)
    answer = generate_ans(context, query)
    return {
        "answer": answer
    }

