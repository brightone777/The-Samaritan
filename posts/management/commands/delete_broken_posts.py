from django.core.management.base import BaseCommand
from posts.models import Post


class Command(BaseCommand):
    help = 'Delete posts with broken/missing image files'

    def handle(self, *args, **options):
        count = 0
        for post in Post.objects.all():
            try:
                if post.image and not post.image.name:
                    post.delete()
                    count += 1
                else:
                    _ = post.image.url  # Force check
            except:
                post.delete()
                count += 1
        self.stdout.write(self.style.SUCCESS(f"Deleted {count} broken posts."))
