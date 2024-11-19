from demo_project.application.dto import UserAuthInfo


def test_positive(default_user, security_service):
    user_api = UserAuthInfo(login='sliva', password='1234')
    security_service.user_repo.get_by_login.return_value = default_user
    token, exp = security_service.try_login(user_api)
    
    assert token is not None
    assert exp is not None
