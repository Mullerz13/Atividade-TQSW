
import unittest
import numeroromano as nr


class TesteNumerosRomanos(unittest.TestCase):

    def test_I(self):
        self.assertEqual(nr.converte('I'), 1)

    def test_V(self):
        self.assertEqual(nr.converte('V'), 5)

    def test_II(self):
        self.assertEqual(nr.converte('II'), 2)

    def test_XXII(self):
        self.assertEqual(nr.converte('XXII'), 22)

    def test_IX(self):
        self.assertEqual(nr.converte('IX'), 9)

    def test_XXIV(self):
        self.assertEqual(nr.converte('XXIV'), 24)


if __name__ == '__main__':
    unittest.main()
