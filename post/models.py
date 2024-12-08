from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _



class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Post.StatusPost.PUBLISHED)

class Post(models.Model):

    class StatusPost(models.TextChoices):
        
        PUBLISHED = 'published', _('Published')
        DRAFT = 'draft', _('Draft')

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='posts'
    )
    content = models.TextField(_('Content'))
    created_at = models.DateTimeField(_('Created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated at'), auto_now=True)
    image = models.ImageField(_('image'), upload_to='images/posts', null=True, blank=True)
    status = models.CharField(_('Status'), max_length=20, choices=StatusPost.choices, default=StatusPost.DRAFT)

    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        
        content_preview = self.content[:20] + '...' if self.content else 'No content'
        return f'{self.author} ({self.get_status_display()}): {content_preview}'
    
    def is_published(self):
        return self.status == self.StatusPost.PUBLISHED
