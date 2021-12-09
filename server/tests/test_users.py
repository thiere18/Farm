from jose import jwt
import pytest
from app.schemas import user as userSchemas
from app.schemas import token as tokenSchemas
from app.config.config import settings
base_url = "/api/v1"

def test_root(client):
 
    res=client.get('/')
    assert res.json().get("message")=="Hello World"
    assert res.status_code == 200
    
def test_create_user(client):
    
    res=client.post(f'{base_url}/users/',json={"username":"thierno","email":"thierno@gmail.com","password":"thierno", })
    new_user=userSchemas.UserCreate(**res.json())
    assert new_user.username=="thierno"
    assert res.status_code == 201
    
def test_login_user(test_user,client):
    res=client.post(f'{base_url}/token',data={"username":test_user['email'],"password":test_user['password']})
    login_res=tokenSchemas.Token(**res.json())
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
def test_correct_incorrect_user(test_user,client,email,password,status_code):
    res=client.post(f'{base_url}/token',data={"username":email, "password":password})
    # assert res.json().get('detail')=="Invalid Credentials"
    assert res.status_code == status_code