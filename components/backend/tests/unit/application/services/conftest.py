import pytest
from unittest.mock import Mock, MagicMock
from demo_project.application import interfaces
from demo_project.application import services
from demo_project.application.entities import *


@pytest.fixture
def user_repo_mock() -> MagicMock:
    return MagicMock(interfaces.UserRepo)


@pytest.fixture
def email_repo_mock() -> MagicMock: 
    return MagicMock(interfaces.EmailRepo)


@pytest.fixture
def lib_event_repo_mock() -> MagicMock:
    return MagicMock(interfaces.LibraryEventRepo)


@pytest.fixture
def lib_repo_mock() -> MagicMock:
    return MagicMock(interfaces.LibraryRepo)



@pytest.fixture
def security_service(user_repo_mock) -> services.SecurityService:
    return services.SecurityService(user_repo=user_repo_mock)


@pytest.fixture
def email_service(email_repo_mock) -> services.EmailService:
    return services.EmailService(email_repo=email_repo_mock)


@pytest.fixture
def lib_event_service(lib_event_repo_mock) -> services.LibraryEventService:
    return services.LibraryEventService(library_event_repo=lib_event_repo_mock)


@pytest.fixture
def lib_service(lib_repo_mock) -> services.LibraryService:
    return services.LibraryService(library_repo=lib_repo_mock)

@pytest.fixture
def user_service(user_repo_mock) -> services.UserService:
    return services.UserService(user_repo=user_repo_mock)



@pytest.fixture
def default_user() -> User: 
    return User(
        id=1, login='sliva',
        password='03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4',
        email_address='529hubabuba@gmail.com', 
        created_at=datetime.now()
    )