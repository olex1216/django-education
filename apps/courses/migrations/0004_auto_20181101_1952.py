# Generated by Django 2.1.2 on 2018-11-01 19:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0003_auto_20181031_1851'),
        ('courses', '0003_auto_20181101_1742'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='organization.Teacher', verbose_name='讲师'),
        ),
        migrations.AddField(
            model_name='course',
            name='teacher_tell',
            field=models.CharField(default='什么都可以学到,按时交作业,不然叫家长', max_length=300, verbose_name='老师告诉你'),
        ),
        migrations.AddField(
            model_name='course',
            name='you_need_know',
            field=models.CharField(default='一颗勤学的心是本课程必要前提', max_length=300, verbose_name='课程须知'),
        ),
        migrations.AddField(
            model_name='video',
            name='learn_times',
            field=models.IntegerField(default=0, verbose_name='学习时长(分钟数)'),
        ),
        migrations.AddField(
            model_name='video',
            name='url',
            field=models.CharField(default='http://blog.mtianyan.cn/', max_length=200, verbose_name='访问地址'),
        ),
    ]
