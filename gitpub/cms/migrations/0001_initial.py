# Generated by Django 2.1 on 2018-10-09 20:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ('course', 'period', 'name'),
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=140)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=140)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=140)),
            ],
        ),
        migrations.CreateModel(
            name='Period',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(choices=[(2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018)])),
                ('semester', models.IntegerField(choices=[(1, 'First'), (2, 'Second')])),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=140)),
                ('views', models.IntegerField(default=0)),
                ('classroom', models.ManyToManyField(to='cms.Classroom')),
            ],
        ),
        migrations.CreateModel(
            name='AnonymousUser',
            fields=[
                ('customuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='cms.CustomUser')),
            ],
            bases=('cms.customuser',),
        ),
        migrations.CreateModel(
            name='RegisteredUser',
            fields=[
                ('customuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='cms.CustomUser')),
                ('registry', models.IntegerField()),
                ('email', models.CharField(max_length=150)),
                ('password', models.CharField(max_length=80)),
                ('token', models.CharField(max_length=150)),
            ],
            bases=('cms.customuser',),
        ),
        migrations.AddField(
            model_name='course',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms.CustomUser'),
        ),
        migrations.AddField(
            model_name='comment',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms.Project'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms.CustomUser'),
        ),
        migrations.AddField(
            model_name='classroom',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms.Course'),
        ),
        migrations.AddField(
            model_name='classroom',
            name='enrolled_user',
            field=models.ManyToManyField(to='cms.CustomUser'),
        ),
        migrations.AddField(
            model_name='classroom',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner_user', to='cms.CustomUser'),
        ),
        migrations.AddField(
            model_name='classroom',
            name='period',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms.Period'),
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('registereduser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='cms.RegisteredUser')),
            ],
            bases=('cms.registereduser',),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('registereduser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='cms.RegisteredUser')),
            ],
            bases=('cms.registereduser',),
        ),
    ]
