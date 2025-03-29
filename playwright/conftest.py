import pytest


#request is a global parameter, that help  you access global/local variables
#request.param will check if the function has any parameter defined, as mentiond in th annotation
@pytest.fixture(scope = "session")
def user_credentials(request):
    return request.param
