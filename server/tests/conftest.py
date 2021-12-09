# from fastapi.testclient import TestClient
# from sqlalchemy.engine import create_engine
# from sqlalchemy.orm.session import sessionmaker
# # from app import models
# from app.config.config import settings
# from app.config.database import Base, get_db
# from app.main import app
# import pytest
# from app.config.oauth2 import create_access_token
# import json
# SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}_test'

# engine = create_engine(SQLALCHEMY_DATABASE_URL)

# TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# # @pytest.fixture
# # def session():
# #     Base.metadata.drop_all(bind=engine)
# #     Base.metadata.create_all(bind=engine)
# #     db = TestingSessionLocal()
# #     try:
# #         yield db
# #     finally:
# #         db.close()

# # @pytest.fixture
# # def client(session):
# #     def override_get_db():
# #         try: 
# #             yield session
# #         finally:
# #             session.close()
# #     app.dependency_overrides[get_db]=override_get_db
# #     yield TestClient(app)

# # @pytest.fixtures
# # def test_role(client):
# #     res=client.post('/api/v1/roles',json={"name": "admin"})
# #     assert res.status_code == 200

# # @pytest.fixture
# # def test_user(test_role,client):
# #     user_data={"username":"string","email":"user@example.com","password":"string","role":test_role['id']}
# #     res=client.post('/api/v1/users/',json=user_data)
# #     assert res.status_code == 201
# #     new_user=res.json()
# #     new_user['password']=user_data['password']
# #     return new_user
# # @pytest.fixture
# # def token(test_user):
# #     return create_access_token({"user_id":test_user['id']})

# # @pytest.fixture
# # def authorized_client(client,token):
# #     client.headers={
# #         **client.headers,
# #         "Authorization":f"Bearer {token}"
# #         }
# #     return client
    
# @pytest.fixture()
# def session():
#     Base.metadata.drop_all(bind=engine)
#     Base.metadata.create_all(bind=engine)
#     db = TestingSessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# @pytest.fixture()
# def client(session):
#     def override_get_db():
#         try: 
#             yield session
#         finally:
#             session.close()
#     app.dependency_overrides[get_db]=override_get_db
#     yield TestClient(app)

# @pytest.fixtures
# def test_role(client):
#     res=client.post('/api/v1/roles',json={"name": "admin"})
#     assert res.status_code == 200
# @pytest.fixture()
# def test_user(test_role,client):
#     user_data={"username":"string","email":"user@example.com","password":"string","role_id":test_role['id']}
#     res=client.post('/api/v1/users/',json=user_data)
#     assert res.status_code == 201
#     new_user=res.json()
#     new_user['password']=user_data['password']
#     return new_user
    
# @pytest.fixture
# def token(test_user):
#     return create_access_token({"user_id":test_user['id']})

# @pytest.fixture
# def authorized_client(client,token):
#     client.headers={
#         **client.headers,
#         "Authorization":f"Bearer {token}"
#         }
#     return client

from fastapi.testclient import TestClient
from sqlalchemy.engine import create_engine
from sqlalchemy.orm.session import sessionmaker
# from app import models
from app.config.config import settings
from app.config.database import Base, get_db
from app.main import app
import pytest
from app.config.oauth2 import create_access_token
import json
SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}_test'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture()
def session():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

@pytest.fixture()
def client(session):
    def override_get_db():
        try: 
            yield session
        finally:
            session.close()
    app.dependency_overrides[get_db]=override_get_db
    yield TestClient(app)
    
    
@pytest.fixture
def test_role(client):
     res=client.post('/api/v1/roles',json={"name": "admin"})
     assert res.status_code == 200

@pytest.fixture
def test_user(test_role, client):
    # create a new role
    ro= client.post('/api/v1/roles/',json={"name": "admin"})
    user_data={"username":"string","email":"user@example.com","password":"string","role_id":test_role['id']}
    res=client.post('/api/v1/users/',json=user_data)
    assert res.status_code == 201
    new_user=res.json()
    new_user['password']=user_data['password']
    return new_user
    
@pytest.fixture
def token(test_user):
    return create_access_token({"user_id":test_user['id']})

@pytest.fixture
def authorized_client(client,token):
    client.headers={
        **client.headers,
        "Authorization":f"Bearer {token}"
        }
    return client
    