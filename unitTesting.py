import unittest
from unittest import IsolatedAsyncioTestCase
from unittest.mock import MagicMock
from unittest.mock import patch

from gi import module
#
# events = []
#
#
# class AsyncConnection:
#     pass
#
#
# class Test(IsolatedAsyncioTestCase):
#
#
#     def setUp(self):
#         events.append("setUp")
#
#     async def asyncSetUp(self):
#         self._async_connection = await AsyncConnection()
#         events.append("asyncSetUp")
#
#     async def test_response(self):
#         events.append("test_response")
#         response = await self._async_connection.get("https://example.com")
#         self.assertEqual(response.status_code, 200)
#         self.addAsyncCleanup(self.on_cleanup)
#
#     def tearDown(self):
#         events.append("tearDown")
#
#     async def asyncTearDown(self):
#         await self._async_connection.close()
#         events.append("asyncTearDown")
#
#     async def on_cleanup(self):
#         events.append("cleanup")

# class TestStringMethods(unittest.TestCase):
#     def test_upper(self):
#         self.assertEqual('foo'.upper(), 'FOO')
#     def test_isupper(self):
#         # self.assertTrue('FOO'.isupper())
#         self.assertFalse('Foo'.isupper())
#     def test_split(self):
#         s = 'hello world'
#         self.assertEqual(s.split(), ['hello', 'world'])
#         with self.assertRaises(TypeError):
#             s.split(2)

#
# class WidgetTestCase(unittest.TestCase):
#     def setUp(self):
#         self.widget = widget('The widget')
#
#     def test_default_widget_size(self):
#         self.assertEqual(self.widget.size(), (50,50),
#                          'incorrect default size')
#
#     def test_widget_resize(self):
#         self.widget.resize(100,150)
#         self.assertEqual(self.widget.size(), (100,150),
#                          'wrong size after resize')
#
#     def tearDown(self):
#         self.widget.dispose()
# class ProductionClass:
#     pass
#
#
# thing = ProductionClass()
# thing.method = MagicMock(return_value=3)
# thing.method(3, 4, 5, key='value')
#
# thing.method.assert_called_with(3, 4, 5, key='value')
# @patch('module.ClassName2')
# @patch('module.ClassName1')
# def test(MockClass1, MockClass2):
#
#     module.ClassName1()
#     module.ClassName2()
#     assert MockClass1 is module.ClassName1
#     assert MockClass2 is module.ClassName2
#     assert MockClass1.called
#     assert MockClass2.called
#
# test()
# if __name__ == '__main__':
#     unittest.main()
class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")
    def test_sum_tuple(self):
        self.assertEqual(sum((1, 2, 2)),5, "Should be 6")


if __name__ == "__main__":
    unittest.main()
    print("Everything passed")

class WidgetTestCase(unittest.TestCase):
    def setUp(self, Widget):
        self.widget = Widget('The widget')

    def test_default_widget_size(self):
        self.assertEqual(self.widget.size(), (50,50),
                         'incorrect default size')

    def test_widget_resize(self):

        self.widget.resize(100,150)
        self.assertEqual(self.widget.size(), (100,150),
                         'wrong size after resize')
