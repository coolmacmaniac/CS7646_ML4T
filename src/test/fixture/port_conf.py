import os
import pytest
from test.model.port_schema import PortfolioConfig
from util.data import read_yaml


@pytest.fixture
def port_test_conf(request):
    """
    Parameters:
    -----------
        request: a conf yaml file name which contains portfolio test config details

    Returns:
    --------
        A pydantic BaseModel specialization class object loaded from the yaml file.
    """
    file_path = os.path.join(os.environ.get('SRC_ROOT_DIR'), 'test/config', request.param)
    port_conf = read_yaml(file_path, PortfolioConfig)
    return port_conf.portfolio


@pytest.fixture
def portfolio(port_test_conf):
    """Just a simpler alias for port_test_conf."""
    yield port_test_conf
