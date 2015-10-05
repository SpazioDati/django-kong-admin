# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators
import jsonfield2.fields


class Migration(migrations.Migration):

    dependencies = [
        ('kong_admin', '0006_auto_20150923_0818'),
    ]

    operations = [
        migrations.CreateModel(
            name='AclReference',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('kong_id', models.UUIDField(null=True, editable=False, blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated')),
                ('synchronized', models.BooleanField(default=False)),
                ('synchronized_at', models.DateTimeField(verbose_name='synchronized', null=True, editable=False, blank=True)),
                ('group', models.CharField(max_length=64)),
            ],
            options={
                'verbose_name': 'ACL Reference',
                'verbose_name_plural': 'ACL References',
            },
        ),
        migrations.AlterField(
            model_name='apireference',
            name='name',
            field=models.CharField(unique=True, default=None, validators=[django.core.validators.RegexValidator('^[\\w.~-]+$', 'Enter a valid username. This value may contain only letters, numbers and ~/./-/_ characters.', 'invalid')], max_length=32, blank=True, help_text='The API name. If none is specified, will default to the request_host or request_path.', null=True),
        ),
        migrations.AlterField(
            model_name='apireference',
            name='preserve_host',
            field=models.BooleanField(default=False, help_text='Preserves the original Host header sent by the client, instead of replacing it with the hostname of the upstream_url. By default is false.'),
        ),
        migrations.AlterField(
            model_name='apireference',
            name='request_host',
            field=models.CharField(null=True, default=None, max_length=32, blank=True, help_text='The public DNS address that points to your API. For example, mockbin.com. At least request_host or request_path or both should be specified.', unique=True),
        ),
        migrations.AlterField(
            model_name='apireference',
            name='request_path',
            field=models.CharField(default=None, max_length=32, null=True, help_text='The public path that points to your API. For example, /someservice. At least request_host or request_path or both should be specified.', blank=True),
        ),
        migrations.AlterField(
            model_name='apireference',
            name='strip_request_path',
            field=models.BooleanField(default=False, help_text='Strip the request_path value before proxying the request to the final API. For example a request made to /someservice/hello will be resolved to upstream_url/hello. By default is false.'),
        ),
        migrations.AlterField(
            model_name='apireference',
            name='upstream_url',
            field=models.URLField(help_text='The base target URL that points to your API server, this URL will be used for proxying requests. For example, https://mockbin.com.'),
        ),
        migrations.AlterField(
            model_name='basicauthreference',
            name='password',
            field=models.CharField(help_text='The password to use in the Basic Authentication', max_length=40),
        ),
        migrations.AlterField(
            model_name='basicauthreference',
            name='username',
            field=models.CharField(help_text='The username to use in the Basic Authentication', unique=True, max_length=32),
        ),
        migrations.AlterField(
            model_name='consumerreference',
            name='custom_id',
            field=models.CharField(help_text='Field for storing an existing ID for the consumer, useful for mapping Kong with users in your existing database. You must send either this field or username with the request.', max_length=48, unique=True, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='consumerreference',
            name='username',
            field=models.CharField(help_text='The username of the consumer. You must send either this field or custom_id with the request.', max_length=32, unique=True, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='keyauthreference',
            name='key',
            field=models.TextField(help_text='You can optionally set your own unique key to authenticate the client. If missing, the plugin will generate one.'),
        ),
        migrations.AlterField(
            model_name='oauth2reference',
            name='client_id',
            field=models.CharField(help_text='You can optionally set your own unique client_id. If missing, the plugin will generate one.', max_length=64, unique=True, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='oauth2reference',
            name='client_secret',
            field=models.TextField(help_text='You can optionally set your own unique client_secret. If missing, the plugin will generate one.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='oauth2reference',
            name='name',
            field=models.CharField(help_text='The name to associate to the credential. In OAuth 2.0 this would be the application name.', unique=True, max_length=32),
        ),
        migrations.AlterField(
            model_name='oauth2reference',
            name='redirect_uri',
            field=models.URLField(help_text='The URL in your app where users will be sent after authorization (RFC 6742 Section 3.1.2)'),
        ),
        migrations.AlterField(
            model_name='pluginconfigurationreference',
            name='api',
            field=models.ForeignKey(related_name='plugins', to='kong_admin.APIReference', help_text='The API on which to add a plugin configuration'),
        ),
        migrations.AlterField(
            model_name='pluginconfigurationreference',
            name='config',
            field=jsonfield2.fields.JSONField(default={}, help_text='The configuration properties for the Plugin which can be found on the plugins documentation page in the Plugin Gallery.'),
        ),
        migrations.AlterField(
            model_name='pluginconfigurationreference',
            name='consumer',
            field=models.ForeignKey(related_name='plugins', blank=True, to='kong_admin.ConsumerReference', help_text='The consumer that overrides the existing settings for this specific consumer on incoming requests.', null=True),
        ),
        migrations.AlterField(
            model_name='pluginconfigurationreference',
            name='plugin',
            field=models.IntegerField(default=13, help_text="The name of the Plugin that's going to be added. Currently the Plugin must be installed in every Kong instance separately."),
        ),
        migrations.AddField(
            model_name='aclreference',
            name='consumer',
            field=models.ForeignKey(to='kong_admin.ConsumerReference'),
        ),
    ]
