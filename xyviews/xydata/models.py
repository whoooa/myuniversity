from django.db import models


# 用户详细信息
class University(models.Model):
    name = models.CharField('名称', max_length=50, blank=True, null=True)
    bi = models.TextField('简介' , null=True, blank=True)
    tese = models.CharField('特色', max_length=10, blank=True, null=True)
    addr = models.CharField('位置', max_length=10, blank=True, null=True)
    xingzhi = models.CharField('性质', max_length=10, blank=True, null=True)
    leixing = models.CharField('类型', max_length=10, blank=True, null=True)
    lishu = models.CharField('隶属', max_length=10, blank=True, null=True)
    content = models.TextField("内容", null=True, blank=True)
    url = models.URLField('大学官网', max_length=250,  null=True, blank=True, )
    created = models.DateTimeField("创建时间", auto_now_add=True, blank=True)
    updated = models.DateTimeField("更新时间", auto_now=True, blank=True)

    class Meta:
        verbose_name = '大学'
        verbose_name_plural = '大学'
        db_table = "yw_university"

    def abs_url(self):
        if self.url:
            if not self.url.startswith("http"):
                return "http://%s" % self.url
        return self.url