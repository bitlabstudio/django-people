# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import filer.fields.file


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0013_urlconfrevision'),
        ('filer', '0002_auto_20150606_2003'),
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.URLField(verbose_name='URL')),
            ],
        ),
        migrations.CreateModel(
            name='LinkType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.SlugField(help_text='Use this field to define a simple identifier that can be used to style the different link types (i.e. assign social media icons to them)', max_length=256, verbose_name='Slug', blank=True)),
                ('ordering', models.PositiveIntegerField(null=True, verbose_name='Ordering', blank=True)),
            ],
            options={
                'ordering': ['ordering'],
            },
        ),
        migrations.CreateModel(
            name='LinkTypeTranslation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256, verbose_name='Name')),
                ('language_code', models.CharField(max_length=15, db_index=True)),
                ('master', models.ForeignKey(related_name='translations', editable=False, to='people.LinkType', null=True)),
            ],
            options={
                'managed': True,
                'abstract': False,
                'db_table': 'people_linktype_translation',
                'db_tablespace': '',
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='Nationality',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'verbose_name_plural': 'Nationalities',
            },
        ),
        migrations.CreateModel(
            name='NationalityTranslation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128, verbose_name='Name')),
                ('language_code', models.CharField(max_length=15, db_index=True)),
                ('master', models.ForeignKey(related_name='translations', editable=False, to='people.Nationality', null=True)),
            ],
            options={
                'managed': True,
                'abstract': False,
                'db_table': 'people_nationality_translation',
                'db_tablespace': '',
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('roman_first_name', models.CharField(max_length=256, verbose_name='Roman first name', blank=True)),
                ('roman_last_name', models.CharField(max_length=256, verbose_name='Roman last name', blank=True)),
                ('non_roman_first_name', models.CharField(max_length=256, verbose_name='Non roman first name', blank=True)),
                ('non_roman_last_name', models.CharField(max_length=256, verbose_name='Non roman last name', blank=True)),
                ('gender', models.CharField(blank=True, max_length=16, verbose_name='Gender', choices=[(b'male', 'male'), (b'female', 'female')])),
                ('title', models.CharField(blank=True, max_length=16, verbose_name='Title', choices=[(b'Dr', 'Dr'), (b'Prof', 'Prof'), (b'Prof Dr', 'Prof Dr')])),
                ('chosen_name', models.CharField(max_length=256, verbose_name='Chosen name', blank=True)),
                ('phone', models.CharField(max_length=32, verbose_name='Phone', blank=True)),
                ('email', models.EmailField(max_length=254, verbose_name='Email', blank=True)),
                ('ordering', models.PositiveIntegerField(null=True, verbose_name='Ordering', blank=True)),
                ('nationality', models.ForeignKey(verbose_name='Nationality', blank=True, to='people.Nationality', null=True)),
                ('picture', filer.fields.file.FilerFileField(verbose_name='Picture', blank=True, to='filer.File', null=True)),
            ],
            options={
                'ordering': ['ordering'],
                'verbose_name_plural': 'People',
            },
        ),
        migrations.CreateModel(
            name='PersonPluginModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('display_type', models.CharField(max_length=256, verbose_name='Display type', choices=[(b'small', 'small'), (b'big', 'big')])),
                ('person', models.ForeignKey(verbose_name='Person', to='people.Person')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='PersonTranslation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('short_bio', models.TextField(max_length=512, verbose_name='Short bio', blank=True)),
                ('bio', models.TextField(max_length=4000, verbose_name='Biography', blank=True)),
                ('language_code', models.CharField(max_length=15, db_index=True)),
                ('master', models.ForeignKey(related_name='translations', editable=False, to='people.Person', null=True)),
            ],
            options={
                'managed': True,
                'abstract': False,
                'db_table': 'people_person_translation',
                'db_tablespace': '',
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RoleTranslation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256, verbose_name='Role')),
                ('role_description', models.TextField(max_length=4000, verbose_name='Role description', blank=True)),
                ('language_code', models.CharField(max_length=15, db_index=True)),
                ('master', models.ForeignKey(related_name='translations', editable=False, to='people.Role', null=True)),
            ],
            options={
                'managed': True,
                'abstract': False,
                'db_table': 'people_role_translation',
                'db_tablespace': '',
                'default_permissions': (),
            },
        ),
        migrations.AddField(
            model_name='person',
            name='role',
            field=models.ForeignKey(verbose_name='Role', blank=True, to='people.Role', null=True),
        ),
        migrations.AddField(
            model_name='link',
            name='link_type',
            field=models.ForeignKey(verbose_name='Link type', to='people.LinkType'),
        ),
        migrations.AddField(
            model_name='link',
            name='person',
            field=models.ForeignKey(verbose_name='Person', to='people.Person'),
        ),
        migrations.AlterUniqueTogether(
            name='roletranslation',
            unique_together=set([('language_code', 'master')]),
        ),
        migrations.AlterUniqueTogether(
            name='persontranslation',
            unique_together=set([('language_code', 'master')]),
        ),
        migrations.AlterUniqueTogether(
            name='nationalitytranslation',
            unique_together=set([('language_code', 'master')]),
        ),
        migrations.AlterUniqueTogether(
            name='linktypetranslation',
            unique_together=set([('language_code', 'master')]),
        ),
    ]
