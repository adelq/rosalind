import ba10a
from nose.tools import assert_almost_equal


def test_dataset():
    return assert_almost_equal(ba10a.main('test_ba10a.txt'),
                               5.01732865318e-19, places=21)


def test_additional_dataset():
    return assert_almost_equal(ba10a.main('test_ba10a2.txt'),
                               3.26233331904e-21, places=21)
