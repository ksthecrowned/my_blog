from django.contrib import admin
from .models import Post, Comment, Author
from django.contrib.auth.models import Group

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
  list_display = ('title', 'slug', 'author', 'publish', 'status')
  list_filter = ('status', 'created', 'publish', 'author')
  search_fields = ('title', 'body')
  prepopulated_fields = {'slug': ('title',)}
  raw_id_fields = ('author',)
  date_hierarchy = 'publish'
  ordering = ('status', 'publish')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
  list_display = ('name', 'email', 'post', 'created', 'active')
  list_filter = ('active', 'created', 'updated')
  search_fields = ('name', 'email', 'body')

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
  list_display = ('complete_name', 'email', 'created')
  list_filter = ('complete_name', 'email', 'updated')
  search_fields = ('complete_name', 'email')

admin.site.unregister(Group)