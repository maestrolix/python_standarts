from falcon import Request

from ssd_libs.http_auth import Group, Permission, strategies


class Permissions:
    FULL_CONTROL = Permission('full_control')
    READ_CONTROL = Permission('read_control')


class Groups:
    ADMINS = Group('Admin', permissions=(Permissions.FULL_CONTROL, ))
    USERS = Group('All', permissions=(Permissions.READ_CONTROL, ))


secret_key = 'KFjldjf2341klfjs'
decoding_options = {'verify_exp': 'verify_signature', 'require': ['exp']}
jwt_strategy = strategies.JWT(secret_key=secret_key, decoding_options=decoding_options)

ALL_GROUPS = (
    Groups.ADMINS,
    Groups.USERS,
)
