import unittest
from app.models import Comment,User,Pitch
from app import db

class CommentModelTest(unittest.TestCase):


    def setUp(self):
            self.user_david = User(username = 'david',password = '1234', email = 'machngatia@gmail.com')
            self.new_comment = Comment(comment='All Kenyan All the Time',user = self.user_david,pitch_id=12 )

    def tearDown(self):
            Comment.query.delete()
            User.query.delete()

    def test_check_instance_variable(self):
            self.assertEquals(self.new_comment.comment,Great)
            self.assertEquals(self.new_comment.user,self.user_Carol)
            self.assertEquals(self.new_comment.pitch_id,12)

    def test_save_comment(self):
            self.new_comment.save_comment()
            self.assertTrue(len(Comment.query.all())>0)

    def test_get_comment_by_id(self):

            self.new_comment.save_comment()
            got_comments = Comment.get_comments(12)
            self.assertTrue(len(got_comments) == 1)
