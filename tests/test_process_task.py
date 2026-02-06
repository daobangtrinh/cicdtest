from modules.process_task import calculator
from modules.use_pool import calculator_usepool

def test_caculator():
    assert calculator() == 500500

def test_use_pool():
    assert calculator_usepool() == 500500