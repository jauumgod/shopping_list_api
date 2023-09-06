import pytest
from flask import Flask
from ..services import user_service
from ..schemas import user_schemas
from unittest.mock import MagicMock
from ..views.user_view import UserListView

@pytest.fixture
def app():
    app = Flask(__name__)
    app.add_url_rule('/users', view_func=UserListView.as_view('user_list'))
    return app

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def mock_user_service():
    return MagicMock()

@pytest.fixture
def mock_user_schemas():
    return MagicMock()

def test_get_users(client, mock_user_service, mock_user_schemas):
    # Defina o comportamento do serviço UserService mockado
    mock_user_service.read_all.return_value = [{"id": 1, "nome": "Alice"}, {"id": 2, "nome": "Bob"}]

    # Defina o comportamento do esquema UserSchemas mockado
    mock_user_schemas.jsonify.return_value = "Mocked JSON response"

    # Substitua as implementações reais pelos mocks nas classes Flask
    user_service.UserService = mock_user_service
    user_schemas.UserSchemas = mock_user_schemas

    # Faça uma solicitação GET para a rota '/users'
    response = client.get('/users')

    # Verifique se a resposta tem o status code correto
    assert response.status_code == 201

    # Verifique se o serviço UserService mockado foi chamado
    mock_user_service.read_all.assert_called_once()

    # Verifique se o esquema UserSchemas mockado foi chamado com os parâmetros corretos
    mock_user_schemas.assert_called_once_with(many=True, only=("nome", "id"))

    # Verifique se a resposta é igual à resposta esperada do esquema mockado
    assert response.get_data(as_text=True) == "Mocked JSON response"
