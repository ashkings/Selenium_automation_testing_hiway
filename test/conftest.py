import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="Chrome", help="my option: Chrome or Firefox"
    )


@pytest.fixture
def browser_name(request):
    return request.config.getoption("--browser")
