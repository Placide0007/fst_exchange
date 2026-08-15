from django.contrib import admin

from .models import Post
from .models import Category
from .models import Reaction
from .models import Comment


admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Reaction)
admin.site.register(Comment)