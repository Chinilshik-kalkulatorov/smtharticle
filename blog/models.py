from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField  # если нужен CKEditor

class Article(models.Model):
    title = models.CharField(max_length=200)

    # Поле для HTML-контента (не обязательно, но если хотите CKEditor):
    content = RichTextUploadingField(blank=True, null=True)

    # Поле для .exe или любых других файлов
    # (upload_to='exes/' - файлы будут в папке media/exes/)
    exe_file = models.FileField(upload_to='exes/', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title