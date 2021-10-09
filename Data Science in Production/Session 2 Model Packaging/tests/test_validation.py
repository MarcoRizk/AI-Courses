from unittest import TestCase

from cov19.model import CovidModel


class TestValidation(TestCase):
    def setUp(self):
        self.model = CovidModel('cov19/cov19model.joblib', ['test_feature'])

    def test_validation_fail(self):
        self.assertRaises(TypeError, self.model.validate_input, list())

    def test_validation_success(self):
        self.model.validate_input(dict())
