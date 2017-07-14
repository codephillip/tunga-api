from __future__ import unicode_literals

from django.db import models

from django.utils.encoding import python_2_unicode_compatible
from dry_rest_permissions.generics import allow_staff_or_superuser

from tunga import settings
from tunga_profiles.models import Skill


@python_2_unicode_compatible
class SkillPage(models.Model):
    keyword = models.CharField(max_length=100, primary_key=True)
    skill = models.ForeignKey(Skill, on_delete=models.DO_NOTHING)
    welcome_header = models.CharField(max_length=50)
    welcome_sub_header = models.CharField(max_length=100)
    welcome_cta = models.CharField(max_length=30)
    pitch_header = models.CharField(max_length=80)
    pitch_body = models.CharField(max_length=450)
    story_header = models.CharField(max_length=80)
    story_body = models.TextField()
    story_image = models.ImageField(upload_to='pages/uploads/%Y/%m/%d', blank=True, null=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} Page'.format(self.keyword)

    class Meta:
        ordering = ['-created_at']

    @allow_staff_or_superuser
    def has_object_read_permission(self, request):
        return True

    @allow_staff_or_superuser
    def has_object_write_permission(self, request):
        return request.user == self.user


@python_2_unicode_compatible
class SkillPageProfile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    page = models.ForeignKey(SkillPage, on_delete=models.CASCADE)
    intro = models.CharField(max_length=100)
    priority = models.IntegerField(default=100)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='skill_profiles_created', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} - {}'.format(self.user.get_short_name() or self.user.username, self.page)

    class Meta:
        unique_together = ('user', 'page')
        ordering = ['-priority', '-created_at']
        verbose_name = 'skill page profile'

    @allow_staff_or_superuser
    def has_object_read_permission(self, request):
        return True

    @allow_staff_or_superuser
    def has_object_write_permission(self, request):
        return self.has_object_write_permission(request)