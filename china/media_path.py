# -*- coding: utf-8 -*-
import uuid


def banner_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/banners/images/<filename>
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return 'banners/images/{0}'.format(filename)


def service_path(istance, filename):
    # file will be uploaded to MEDIA_ROOT/services/images/<filename>
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return 'services/images/{0}'.format(filename)


def members_path(istance, filename):
    # file will be uploaded to MEDIA_ROOT/members/images/<filename>
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return 'members/images/{0}'.format(filename)


def news_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/news/images/<filename>
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return 'media/news/images/{0}'.format(filename)


def slider_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/news/images/<filename>
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return 'slider/images/{0}'.format(filename)
