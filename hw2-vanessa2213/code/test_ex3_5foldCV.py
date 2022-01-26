from code import cv
import numpy
import pytest
import os


@pytest.fixture
def exercise_results():
    return cv.exercise_3_5fold('data/synthdata2021.csv', 'figures/synthetic2021-5fold-CV.png', seed=29)


def test_exercise_3_5fold(exercise_results):
    """
    NOTE: This test will only pass if you implement your solution
    to exercise_3_5fold similar to the reference solution.
    It is possible for you to have a valid soluiton that does not
    match these exact values.
    However, if you pass this test, you know you are done.
    :param exercise_results:
    :return:
    """
    k5_best_model_order, k5_best_CVtest_log_MSE_loss, k5_best_model_w = exercise_results
    target_w = numpy.array([18.27934516, 7.58594459, -3.70990554, -0.94480755])
    assert k5_best_model_order == 3
    assert k5_best_CVtest_log_MSE_loss == pytest.approx(4.929484691503239)
    assert numpy.allclose(k5_best_model_w, target_w)


def test_if_5foldCV_figure_exists():
    """
    NOTE: This test will only pass if you save your figure of the
    CV Train and Test plots as a single file with the name
        synthetic2019-5fold-CV.png
    If you save your plots a different way, you can ignore this
    test failure.
    :return:
    """
    assert os.path.exists('figures/synthetic2021-5fold-CV.png')
