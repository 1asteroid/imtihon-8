import uuid
from django.db.models import TextChoices


class SaveImages(object):
    def product_images_path(instance, filename):
        image_extension = filename.split('.')[-1]
        return f"media/product/{uuid.uuid4()}.{image_extension}"


class SaveImagesTeam(object):
    def team_images_path(instance, filename):
        image_extension = filename.split('.')[-1]
        return f"media/team/{uuid.uuid4()}.{image_extension}"


class SaveImagesBlog(object):
    def blog_images_path(instance, filename):
        image_extension = filename.split('.')[-1]
        return f"media/blog/{uuid.uuid4()}.{image_extension}"
