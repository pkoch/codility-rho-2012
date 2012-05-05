import unittest

from main import hit_the_number, Node

class NodeTest(unittest.TestCase):
    def test_children_1(self):
        self.assertEqual(
            [Node(42,(1,2,))],
            Node(42, (1,)).generate_children(),
        )

    def test_children_2(self):
        self.assertEqual(
            [
                Node(42,(1,2, 3,)),
                Node(42,(1,2, 4,)),
            ],
            Node(42, (1, 2,)).generate_children(),
        )

    def test_children_3(self):
        self.assertEqual(
            [
                Node(42,(1,2, 3, 4,)),
                Node(42,(1,2, 3, 5,)),
                Node(42,(1,2, 3, 6,)),
            ],
            Node(42, (1, 2, 3,)).generate_children(),
        )

class HitTheTest(unittest.TestCase):
    def test_one(self):
        self.assertEqual(
            (1,),
            hit_the_number(1),
        )

    def test_7(self):
        self.assertEqual(
            5,
            len(hit_the_number(7)),
        )

    def test_211(self):
       self.assertEqual(
           11,
           len(hit_the_number(211)),
            # (1, 2, 4, 8, 16, 32, 48, 49, 81, 162, 211,),
        )

    def test_600(self):
       self.assertEqual(
           12,
           len(hit_the_number(600)),
            # (1, 2, 4, 8, 16, 32, 48, 49, 81, 162, 211,),
        )

    #  [ Sequence [1, 2, 4, 8, 16, 32, 64, 128, 132, 164, 165, 330, 495] is too long ]dd
    def test_495(self):
       self.assertEqual(
           12,
           len(hit_the_number(495)),
        )

    def test_310(self):
       self.assertEqual(
           12,
           len(hit_the_number(310)),
        )

if __name__ == '__main__':
    unittest.main()
