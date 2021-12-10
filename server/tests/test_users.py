from jose import jwt
from app.schemas import  user as schemas
from app.schemas import  token as schemaToken
from app.config.config import settings
import pytest
import asyncio

def test_root(client):
    res=client.get('/')
    assert res.json().get("message")=="Hello World"
    assert res.status_code == 200
    

def test_create_user(client):
    # role= client.post("/api/v1/roles/",json={"name":"simplooe"})
    res=client.post(f'{settings.api_prefix}/users/',json={"username":"thierno","email":"thierno@gmail.com","password":"thierno","user_role": "simplooe"})
    new_user=schemas.UserBase(**res.json())
    # print(new_user)
    assert res.status_code ==201
    assert new_user.username=="thierno"
    
def test_login_user(test_user,client):
    res=client.post(f'{settings.api_prefix}/token',data={"username":test_user['email'],"password":test_user['password']})
    login_res=schemaToken.Token(**res.json())
    payload = jwt.decode(login_res.access_token, settings.secret_key, algorithms=[settings.algorithm])
    id=payload.get('user_id')
    assert id==test_user['id']
    assert login_res.token_type=="bearer"
    assert res.status_code==200

@pytest.mark.parametrize("email, password, status_code",[
    ('user@exampld.com', 'bearer',403),
    (None, 'bearer',422),
    ('string','string',200)
    
])
def test_incorrect_user(test_user,client,email,password,status_code):
    res=client.post(f'{settings.api_prefix}/token',data={"username":email, "password":password})
    # assert res.json().get('detail')=="Invalid Credentials"
    assert res.status_code == status_code