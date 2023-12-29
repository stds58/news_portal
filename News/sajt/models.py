from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Author(models.Model):
    rating = models.IntegerField(default = 0)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def update_rating(self):
        autor_posts_rating = 0
        autor_comments_rating = 0
        posts_coments_rating = 0

        autor_posts = Post.objects.filter(author = self)
        for p in autor_posts:
            autor_posts_rating += p.rating

        autor_comments = Comment.objects.filter(user = self.user)
        for c in autor_comments:
            autor_comments_rating += c.rating

        posts_comments = Comment.objects.filter(post__author = self)
        for pc in posts_comments:
            posts_coments_rating += pc.rating

        # print(autor_posts_rating)
        # print('------')
        # print(autor_comments_rating)
        # print('------')
        # print(posts_coments_rating)
        # print('------')
        # print(autor_posts.query)

        self.rating = autor_posts_rating*3 + autor_comments_rating + posts_coments_rating
        self.save()


class Category(models.Model):
    name = models.CharField(max_length = 255, unique = True)


class Post(models.Model):
    artikul = 'AR'
    news = 'NE'
    POSITIONS = [
        (artikul, 'статья'),
        (news, 'новость'),
    ]

    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    type = models.CharField(max_length = 2, choices = POSITIONS, default=news)
    datetime_in = models.DateTimeField(auto_now_add = True)
    head = models.CharField(max_length = 255)
    tekst = models.TextField()
    rating = models.IntegerField(default = 0)
    category = models.ManyToManyField(Category, through='PostCategory')

    def preview(self):
        small_text = self.tekst[0:124]+'...'
        return small_text

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def avtor(self):
        u = User.objects.filter(author__id=Post.objects.filter(author__id=self.author).values("id")[0]['id']).values("username")[0]['username']
        return f'{u}'

    #список всех новостей
    def __str__(self):
        return f'{self.head.title()}: {self.tekst}' #.title() делает все первые буквы в каждом слове заглавными


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tekst = models.TextField()
    datetime_in = models.DateTimeField(auto_now_add = True)
    rating = models.IntegerField(default = 0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()











