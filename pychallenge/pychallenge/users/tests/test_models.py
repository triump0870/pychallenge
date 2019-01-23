from test_plus.test import TestCase
from django.db.utils import IntegrityError
from pychallenge.users.models import About


class AboutModelsTest(TestCase):
    def setUp(self):
        self.user = self.make_user("test_user1")
        self.other_user = self.make_user("other_test_user")
        self.published_about_me = About.objects.create(
            user=self.user,
            content="This is a sample about me",
            status='P'
        )
        self.not_published_about_me = About.objects.create(
            user=self.other_user,
            content="""This is a really good content, just if somebody
            published it, that would be awesome, but no, nobody wants to
            publish it, because they know this is just a test, and you
            know than nobody wants to publish a test, just a test;
            everybody always wants the real deal.""",
            status='D'
        )

    def test_object_instance(self):
        assert isinstance(self.published_about_me, About)
        assert isinstance(About.objects.get_published()[0], About)
        assert isinstance(About.objects.get_published()[0], About)
        assert isinstance(About.objects.get_published()[0], About)

    def test_dupliate_instance_not_allowed(self):
        with self.assertRaises(IntegrityError):
            About.objects.create(
                user=self.user,
                content='New Content',
                status='D'
            )

    def test_return_values(self):
        assert self.published_about_me.status == "P"
        assert self.published_about_me.status != "p"
        assert self.not_published_about_me.status == "D"
        assert str(self.published_about_me.content) == "This is a sample about me"
        assert self.published_about_me in About.objects.get_published()
        assert About.objects.get_published()[0].content == "This is a sample about me"
        assert self.not_published_about_me in About.objects.get_drafts()
