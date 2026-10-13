from fastapi import APIRouter, HTTPException, status, Depends
from models.event import Event, EventCreate
from exceptions.user import InvalidPasswordException,SamePasswordException,UserAlreadyExistsException,UserCredentialsException,UserNotFoundException
from exceptions.event import EventNotFoundException
from sqlalchemy.orm import Session 
from services.event import delet_user_event 
from services.event import find_events_user_id
from schemas.event import EventCreate 
from repository.models.event import Event
from repository.models.user import User




event_router = APIRouter(tags=["Events"])

events = []


# 전체 이벤트 조회
# http://127.0.0.1:8000/evnet/ + get
@event_router.get("/", response_model=EventResponse)
async def get_events(db:Session= Depends(get_db), current_user: User = Depends(get_current_user)):

    events = find_events_user_id(db=db, current_user=current_user)
    
    return {"items":events}


# 특정 이벤트 조회
# http://127.0.0.1:8000/evnet/1 + get
@event_router.get("/{id}", response_model=Event)
async def get_event(id:int):
    for event in events:
        if event.id == id:
            return event
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="이벤트가 없습니다.")

# 이벤트 추가
# http://127.0.0.1:8000/evnet/new + post
@event_router.post("/new", response_model=Event)
async def post_event(data:EventCreate):
    new_id = len(events) + 1
    event = Event(id=new_id, title=data.title, image=data.image, description=data.description, tags=data.tags, location=data.location)
    events.append(event)
    return event

# 특정 이벤트 삭제
# http://127.0.0.1:8000/evnet/1 + delete 
@event_router.delete("/{id}", response_model=dict)
async def delete_event(id:int, db:Session= Depends(get_db), current_user: User = Depends(get_current_user) ):
    


    try:
        delet_user_event()
    except EventNotFoundException:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="제거할 이벤트가 없습니다.")
    except UserCredentialsException:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="삭제할 권한이 없습니다.")
    return {"message":f"evnet {id}번 삭제"} 


# 전체 이벤트 삭제
# http://127.0.0.1:8000/evnet/ + delete
@event_router.delete("/")
async def delete_all_events():
    events.clear()
    return {"message":"모든 Event 삭제 성공"}