import unittest
from translate import translate

class TestTranslate(unittest.TestCase):

    def test_number_inputs(self):
        self.assertEquals(translate(1), '1')
        self.assertEquals(translate(12), '12')
        self.assertEquals(translate(123), '123')
        self.assertEquals(translate(1234), '1,234')
        self.assertEquals(translate(12345), '12,345')
        self.assertEquals(translate(123456), '123,456')
        self.assertEquals(translate(1234567), '1,234,567')
        self.assertEquals(translate(12345678), '12,345,678')
        self.assertEquals(translate(123456789), '123,456,789')

    def test_number_as_string_inputs(self):
        self.assertEquals(translate('1'), '1')
        self.assertEquals(translate('12'), '12')
        self.assertEquals(translate('123'), '123')
        self.assertEquals(translate('1234'), '1,234')
        self.assertEquals(translate('12345'), '12,345')
        self.assertEquals(translate('123456'), '123,456')
        self.assertEquals(translate('1234567'), '1,234,567')
        self.assertEquals(translate('12345678'), '12,345,678')
        self.assertEquals(translate('123456789'), '123,456,789')

    def test_not_a_number(self):
        with self.assertRaises(ValueError):
            translate('hola')
