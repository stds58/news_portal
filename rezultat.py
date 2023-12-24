from sajt.models import *
import datetime

u1 = User.objects.create_user(username='ggg')
a1 = Author.objects.create(user = u1)
a1.rating
a1.update_rating()
p1 = Post.objects.create(head='head',tekst='tekst',author=a1)
c1 = Comment.objects.create(tekst='tekst',post=p1, user=a1.user)
p1.like()
a1.update_rating()
a1.rating
c1.like()
a1.rating


queryset = a1.update_rating()
print(queryset.query)

queryset = Post.objects.all()
queryset = Post.objects.filter(author = 5)
print(queryset.query)

autor_posts = Post.objects.filter(author = self)
print(autor_posts.query)


#Что вы должны сделать в консоли Django?

#Создать двух пользователей (с помощью метода User.objects.create_user('username')).
u1 = User.objects.create_user(username='Vasja')
u2 = User.objects.create_user(username='Fedja')

#Создать два объекта модели Author, связанные с пользователями.
a1 = Author.objects.create(user = u1)
a2 = Author.objects.create(user = u2)

#Добавить 4 категории в модель Category.
cat1 = Category.objects.create(name='мс счл')
cat2 = Category.objects.create(name='питон')
cat3 = Category.objects.create(name='дьянга')
cat4 = Category.objects.create(name='прочее')

#Добавить 2 статьи и 1 новость.
p1 = Post.objects.create(author = u1.author, type='статья', head='Lorem Ipsum', tekst='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum')
p2 = Post.objects.create(author = u2.author, type='статья', head='Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit...', tekst='Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?')
p3 = Post.objects.create(author = u2.author, head='de Finibus Bonorum et Malorum', tekst='At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi sint occaecati cupiditate non provident, similique sunt in culpa qui officia deserunt mollitia animi, id est laborum et dolorum fuga. Et harum quidem rerum facilis est et expedita distinctio. Nam libero tempore, cum soluta nobis est eligendi optio cumque nihil impedit quo minus id quod maxime placeat facere possimus, omnis voluptas assumenda est, omnis dolor repellendus. Temporibus autem quibusdam et aut officiis debitis aut rerum necessitatibus saepe eveniet ut et voluptates repudiandae sint et molestiae non recusandae. Itaque earum rerum hic tenetur a sapiente delectus, ut aut reiciendis voluptatibus maiores alias consequatur aut perferendis doloribus asperiores repellat')

# Присвоить им категории (как минимум в одной статье/новости должно быть не меньше 2 категорий).
pc1 = PostCategory.objects.create(post=p1, category=cat1)
pc2 = PostCategory.objects.create(post=p1, category=cat2)
pc3 = PostCategory.objects.create(post=p1, category=cat3)
pc4 = PostCategory.objects.create(post=p2, category=cat1)
pc5 = PostCategory.objects.create(post=p2, category=cat2)
pc6 = PostCategory.objects.create(post=p2, category=cat3)
pc7 = PostCategory.objects.create(post=p2, category=cat4)
pc8 = PostCategory.objects.create(post=p3, category=cat2)
pc9 = PostCategory.objects.create(post=p3, category=cat4)

# Создать как минимум 4 комментария к разным объектам модели Post (в каждом объекте должен быть как минимум один комментарий).
c1 = Comment.objects.create(tekst='отзыв1',post=p1, user=a1.user)
c2 = Comment.objects.create(tekst='отзыв2',post=p1, user=a2.user)
c3 = Comment.objects.create(tekst='отзыв 1',post=p2, user=a1.user)
c4 = Comment.objects.create(tekst='отзыв 2',post=p2, user=a1.user)
c5 = Comment.objects.create(tekst='отзыв 3',post=p2, user=a2.user)
c6 = Comment.objects.create(tekst='отзыв1',post=p3, user=a2.user)
c7 = Comment.objects.create(tekst='отзыв2',post=p3, user=a1.user)
c8 = Comment.objects.create(tekst='отзыв3',post=p3, user=a2.user)

# Применяя функции like() и dislike() к статьям/новостям и комментариям, скорректировать рейтинги этих объектов.
p1.like()
p1.dislike()
p1.like()
p1.like()

p2.like()

p3.dislike()
p3.dislike()
p3.dislike()

c1.like()
c2.like()
c3.dislike()
c4.like()
c5.dislike()
c6.dislike()
c7.like()
c8.dislike()
c8.dislike()

# Обновить рейтинги пользователей.
a1.update_rating()
a2.update_rating()

# Вывести username и рейтинг лучшего пользователя (применяя сортировку и возвращая поля первого объекта).
'username лучшего пользователя: '+Author.objects.order_by('-rating').values_list('user__username', flat=True).first()
'рейтинг лучшего пользователя: '+Author.objects.order_by('-rating').first().rating

# Вывести дату добавления, username автора, рейтинг, заголовок и превью лучшей статьи, основываясь на лайках/дислайках к этой статье.
'дата добавления лучшей статьи: '+Post.objects.order_by('-rating').first().datetime_in.strftime("%m/%d/%Y, %H:%M:%S")

id = Post.objects.order_by('-rating').first().id
author_id = Author.objects.filter(id = id).values('user')
user_id = author_id.values_list('user')[0][0]
'username автора: '+User.objects.filter(id = user_id).values('username').values_list('username')[0][0]
'username автора: '+Post.objects.order_by('-rating').values_list('author__user__username', flat=True).first()

'рейтинг лучшей статьи: '+str(Post.objects.order_by('-rating').first().rating)
'заголовок лучшей статьи: '+Post.objects.order_by('-rating').first().head
'предпросмотр лучшей статьи: '+Post.objects.order_by('-rating').first().preview()





