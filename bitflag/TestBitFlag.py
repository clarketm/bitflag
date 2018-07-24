"""BitFlag module"""

import unittest
from bitflag.BitFlag import BitFlag


class TestBitFlag(unittest.TestCase):
    """BitFlag class tests."""

    @classmethod
    def setUp(cls):
        cls.f = BitFlag("a", "b", "c")

    def test_has_should_return_false_for_initialized_bit_flags(self):
        """Test "has" should return false for initialized bit flags."""
        self.assertEqual(TestBitFlag.f.has("a"), False)
        self.assertEqual(TestBitFlag.f.has("b"), False)
        self.assertEqual(TestBitFlag.f.has("c"), False)

    def test_set_should_turn_on_bit_flag(self):
        """Test "set" should turn on bit flag."""
        TestBitFlag.f.set("a")
        self.assertEqual(TestBitFlag.f.has("a"), True)

    def test_unset_should_turn_off_bit_flag(self):
        """Test "unset" should turn off bit flag."""
        TestBitFlag.f.unset("a")
        self.assertEqual(TestBitFlag.f.has("a"), False)

    def test_toggle_should_turn_off_bit_flag_if_currently_on(self):
        """Test "toggle" should turn off bit flag if currently on."""
        TestBitFlag.f.set("b")
        TestBitFlag.f.toggle("b")
        self.assertEqual(TestBitFlag.f.has("b"), False)

    def test_toggle_should_turn_on_bit_flag_if_currently_off(self):
        """Test "toggle" should turn on bit flag if currently off."""
        TestBitFlag.f.unset("c")
        TestBitFlag.f.toggle("c")
        self.assertEqual(TestBitFlag.f.has("c"), True)

    def test_reset_should_turn_off_all_bit_flags(self):
        """Test "reset" should turn off all bit flags."""
        TestBitFlag.f.set("a")
        TestBitFlag.f.set("b")
        TestBitFlag.f.set("c")
        TestBitFlag.f.reset()
        self.assertEqual(TestBitFlag.f.has("a"), False)
        self.assertEqual(TestBitFlag.f.has("b"), False)
        self.assertEqual(TestBitFlag.f.has("c"), False)

    def test_flip_should_invert_all_bit_flags(self):
        """Test "flip" should invert all bit flags."""
        TestBitFlag.f.set("a")
        TestBitFlag.f.unset("b")
        TestBitFlag.f.set("c")
        TestBitFlag.f.flip()
        self.assertEqual(TestBitFlag.f.has("a"), False)
        self.assertEqual(TestBitFlag.f.has("b"), True)
        self.assertEqual(TestBitFlag.f.has("c"), False)


if __name__ == '__main__':
    unittest.main()
