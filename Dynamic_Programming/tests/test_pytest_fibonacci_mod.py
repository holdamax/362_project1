"""PyTest for fibonacci_mod.py."""
import pytest
import Dynamic_Programming.code.fibonacci_mod as f_mod


@pytest.mark.parametrize("inputs, outputs", [(1, 1), (3, 1), (4, 2), (6, 4), (17, 277), (45, 12322413)])
def test_fibo_positive(inputs, outputs):
    """Test of calculating fibonacci number with different inputs."""
    assert f_mod.fibo(inputs) == outputs


@pytest.mark.parametrize("inputs, outputs", [(3.4, RecursionError),
                                             (0, RecursionError),
                                             (-1, RecursionError),
                                             ((3, 2, 1, 5, 8), TypeError),
                                             ([1, 2, 3, 6, 2], TypeError),
                                             ('gcfty', TypeError),
                                             ('?/*', TypeError),
                                             ('', TypeError)])
def test_fibo_wrong(inputs, outputs):
    """Test on wrong input type."""
    with pytest.raises(outputs):
        f_mod.fibo(inputs)


@pytest.mark.parametrize("inputs", [(46), (3000)])
def test_fibo_negative(inputs):
    """Test of calculating fibonacci number with wrong inputs numbers."""
    assert f_mod.fibo(inputs) is None
