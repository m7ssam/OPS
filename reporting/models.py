from django.db import models

# Projects meta data
# جدول تحديد حالات المشروع
class StatusDefinition(models.Model):
    id = models.AutoField(primary_key=True)
    status_definition = models.CharField(max_length=20)
    status_description = models.TextField(null=False, blank=False, default="Not specified")
    def __str__(self):
        return self.status_definition

# جداول البيانات الاساسية للمشروع
# الجدول لتجديد كود المشروع و الاسم والحالة
class Project(models.Model):
  recipient = models.CharField(primary_key=True, max_length=6)
  project_name = models.CharField(max_length=50)
  status = models.ForeignKey(StatusDefinition, on_delete=models.CASCADE)
  updated = models.DateTimeField(auto_now=True)
  created = models.DateTimeField(auto_now_add=True)
  def __str__(self):
      return self.recipient
