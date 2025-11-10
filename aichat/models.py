from django.db import models
from django.conf import settings


class ChatMessage(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='chat_messages'
    )
    role = models.CharField(max_length=10, choices=[('user', 'User'), ('ai', 'AI')])
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return f'{self.user} - {self.role} - {self.message[:20]}'
