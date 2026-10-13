from sqlalchemy.orm import Session
from sqlalchemy import select
from schemas.event import Event,EventCreate
from repository.models.event import Event
from repository.models.user import User
from exceptions.user import InvalidPasswordException,SamePasswordException,UserAlreadyExistsException,UserCredentialsException,UserNotFoundException
from exceptions.event import EventNotFoundException

# event 등록 EventCreate(schemas) > 모델 모양으로 생성
def add_event(db: Session, data:EventCreate, current_user:User):
    event = Event(title=data.title, image=data.image, description=data.description, tags=data.tags, location=data.location, user_id=current_user:user_id)

    db.add(event)
    db.commit()
    db.refresh(event)
    return event


# 로그인 user의 모든 이벤트 가져오기 
def find_events_user_id(db:Session, current_user:User):
    stmt = select(Event).where(Event.user_id == current_user.user_id)
    events = db.scalar(stmt).all()
    return events

# 로그인 user의 특정 이벤트 삭제 
def delet_user_event(db:Session, id:int, current_user:User):
    # 삭제할 event 찾기
    event = db.get(Event, id)

    if not event:
        raise EventNotFoundException
    if current_user.user_id != event.user_id:
        raise UserCredentialsException

    db.delete(event)
    db.commit()
    return id