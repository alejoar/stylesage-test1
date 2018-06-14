import unittest
from translate import translate

class TestTranslate(unittest.TestCase):

    def test_number_inputs(self):
        self.assertEquals(translate(1), '1')
        self.assertEquals(translate(12), '12')
        self.assertEquals(translate(123), '123')
        self.assertEquals(translate(1234), '1,234')

    def test_number_as_string_inputs(self):
        self.assertEquals(translate('1'), '1')
        self.assertEquals(translate('12'), '12')
        self.assertEquals(translate('123'), '123')
        self.assertEquals(translate('1234'), '1,234')

    def test_not_a_number(self):
        with self.assertRaises(ValueError):
            translate('hola')

