from fastapi import APIRouter, Body
from typing import Union, Annotated
from models import Main_User, Main_UserDB, New_Response

router_users = APIRouter()

def codding_pass(code: str) -> str:
    result = code * 2
    return result
    
list_users = []

def find_user(id:int) -> Union[Main_UserDB, None]:
    for user in list_users:
        if user.id == id:
            return user
    return None

@router_users.get("/users", response_model=Union[list[Main_User],None])
def get_users():
    return list_users

@router_users.get("/users/{id}", response_model=Union[Main_User, New_Response])
def get_user(id: int):
    user = find_user(id)
    if user ==None:
        return New_Response(message="Пользователь не найден")
    return user

@router_users.delete("/users/{id}", response_model=Union[Main_User, New_Response])
def get_user(id: int):
    user = find_user(id)
    if user ==None:
        return New_Response(message="Пользователь не найден")
    else:
        for e in range(len(list_users) - 1, -1, -1):
            if list_users[e] == user:
                list_users.pop(e)
        return New_Response(message="Пользователь удален")

@router_users.post("/users", response_model=Union[Main_User, New_Response])
def create_user(item: Annotated[Main_User, Body(embed=True, description="Новый пользователь")]):
    user = Main_UserDB(name=item.name, id=item.id, password=codding_pass(item.name))
    list_users.append(user)
    return user

@router_users.put("/users", response_model=Union[Main_User, New_Response])
def edit_user(item: Annotated[Main_User, Body(embed=True, description="Изменение данных по id")]):
    user = find_user(item.id)
    if user ==None:
        return New_Response(message="Пользователь не найден")
    user.id = item.id
    user.name = item.name
    return user

    
    
    