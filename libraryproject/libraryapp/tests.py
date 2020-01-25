# from django.test import TestCase
# from libraryapp.models import Author,Book,Record
#
# class AuthorTestCase(TestCase):
#     def setUp(self):
#         Author.objects.create(first_name="munshi",last_name='premchand')
#
#     def test_Author_test_case(self):
#
#         author = Author.objects.get(first_name="munshi", last_name='premchand')
#         self.assertEqual(author.fullname(),  "munshi premchand")
# #
# class BookTestCase(TestCase):
#     def setUp(self):
#         munshi= Author.objects.create(first_name='munshi',last_name='premchand')
#         Book.objects.create(name = 'Godan',
#                             isbn='87278878',
#                             price = '110',
#                             available = 'True',
#                             stock='9',
#                             returned_book='False',
#                             author_name=munshi)
#
#     def test_Author_test_case(self):
#
#         book1 = Book.objects.get(name = 'Godan',
#                                  isbn='87278878',
#                                  price = '110',
#                                  available = 'True',
#                                  stock='9',
#                                  returned_book='False',
#                                  author_name=Author.objects.get(first_name='munshi',last_name='premchand'))
#         self.assertEqual(book1.name,  'Godan')
#
# # class RecordTestCase(TestCase):
# #     def setUp(self):
# #         Record.objects.create(member='',b)
# #
# #     def test_record_test_case(self):
# #
# #         record1 = Record.objects.get()
# #         self.assertEqual(record1.update_stock(),  "munshi premchand")
#
#
#
#
# # Create your tests here.
