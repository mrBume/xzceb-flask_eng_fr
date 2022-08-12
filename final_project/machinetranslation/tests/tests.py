import unittest

from translator import english_to_french, french_to_english

class TestEnglish(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour")
        self.assertEqual(english_to_french("Car"), "Voiture")
        self.assertEqual(english_to_french(""), "")

    def test2(self):
        self.assertEqual(english_to_french("hello my name is Tom"), "Bonjour mon nom est Tom")
        self.assertEqual(english_to_french("I'm testing my app"), "Je teste mon application")

class TestFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")
        self.assertEqual(french_to_english("Voiture"), "Car")
        self.assertEqual(french_to_english(""), "")

    def test2(self):
        self.assertEqual(french_to_english("Bonjour mon nom est Tom"), "Hello my name is Tom")
        self.assertEqual(french_to_english("Je teste mon application"), "I'm testing my application")

unittest.main()

