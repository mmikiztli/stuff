import unittest
from garbage import Garbage
from paper_garbage import PaperGarbage
from plastic_garbage import PlasticGarbage
from dustbin import Dustbin
from dustbin_content_error import DustbinContentError


class Tester(unittest.TestCase):

    def test_instantiating_garbage(self):
        garbage_name = "Rotten food from the fridge"
        garbage = Garbage(garbage_name)
        self.assertEqual(garbage.name, garbage_name)

    def test_instantiating_plastic_garbage(self):
        garbage_name = "Empty coke bottle"
        plastic_garbage = PlasticGarbage(garbage_name, False)
        self.assertEqual(plastic_garbage.name, garbage_name)
        self.assertEqual(plastic_garbage.is_clean, False)

    def test_instantiating_paper_garbage(self):
        garbage_name = "An empty milk carton"
        paper_garbage = PaperGarbage(garbage_name, False)
        self.assertEqual(paper_garbage.name, garbage_name)
        self.assertEqual(paper_garbage.is_squeezed, False)

    def test_squeeze_on_paper_garbage(self):
        paper_garbage = PaperGarbage("Paper garbage", False)
        paper_garbage.squeeze()
        self.assertEqual(paper_garbage.is_squeezed, True)

    def test_clean_on_plastic_garbage(self):
        plastic_garbage = PlasticGarbage("Plastic garbage", False)
        plastic_garbage.clean()
        self.assertEqual(plastic_garbage.is_clean, True)

    def test_dustbin_out_paper_garbage(self):
        paper_garbage = PaperGarbage("Paper garbage", True)
        dustbin = Dustbin("red")
        dustbin.throw_out_garbage(paper_garbage)
        self.assertEqual(len(dustbin.paper_content), 1)
        self.assertEqual(len(dustbin.plastic_content), 0)
        self.assertEqual(len(dustbin.house_waste_content), 0)

    def test_dustbin_out_plastic_garbage(self):
        plastic_garbage = PlasticGarbage("Plastic garbage", True)
        dustbin = Dustbin("red")
        dustbin.throw_out_garbage(plastic_garbage)
        self.assertEqual(len(dustbin.paper_content), 0)
        self.assertEqual(len(dustbin.plastic_content), 1)
        self.assertEqual(len(dustbin.house_waste_content), 0)

    def test_dustbin_out_house_waste_garbage(self):
        garbage = Garbage("House waste garbage")
        dustbin = Dustbin("red")
        dustbin.throw_out_garbage(garbage)
        self.assertEqual(len(dustbin.paper_content), 0)
        self.assertEqual(len(dustbin.plastic_content), 0)
        self.assertEqual(len(dustbin.house_waste_content), 1)

    def test_dustbin_out_unsqueezed_paper_garbage(self):
        paper_garbage = PaperGarbage("Paper garbage", False)
        dustbin = Dustbin("red")
        self.assertRaises(DustbinContentError, lambda: dustbin.throw_out_garbage(paper_garbage))

    def test_dustbin_out_uncleaned_plastic_garbage(self):
        plastic_garbage = PlasticGarbage("Plastic garbage", False)
        dustbin = Dustbin("red")
        self.assertRaises(DustbinContentError, lambda: dustbin.throw_out_garbage(plastic_garbage))

    def test_dustbin_out_something_which_is_not_a_garbage(self):
        my_string = "This is NOT a garbage, right???"
        dustbin = Dustbin("red")
        self.assertRaises(DustbinContentError, lambda: dustbin.throw_out_garbage(my_string))

    def test_dustbin_out_something_which_is_not_a_garbage(self):
        my_string = "This is NOT a garbage, right???"
        dustbin = Dustbin("red")
        self.assertRaises(DustbinContentError, lambda: dustbin.throw_out_garbage(my_string))

    def test_empty_contents_on_dustbin(self):
        garbage_list = [
            PlasticGarbage("Plastic garbage", True),
            PaperGarbage("Paper garbage", True),
            Garbage("House waste garbage")
        ]

        dustbin = Dustbin("red")
        for garbage in garbage_list:
            dustbin.throw_out_garbage(garbage)

        dustbin.empty_contents()

        self.assertEqual(len(dustbin.paper_content), 0)
        self.assertEqual(len(dustbin.plastic_content), 0)
        self.assertEqual(len(dustbin.house_waste_content), 0)


def main():
    unittest.main()

if __name__ == '__main__':
    main()
