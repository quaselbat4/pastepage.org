import os
import time
import logging
from django.db.models import Q
from archive.models import Screenshot
from archive.tasks import backfill_to_internet_archive_batch
from django.core.management.base import BaseCommand
logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'Testing a backload of screenshot to the Internet Archive'

    def handle(self, *args, **options):
        # Query screenshots that are on Rackspace but not IA.
        seed_qs = Screenshot.objects.filter(
            Q(internetarchive_id='') & Q(internetarchive_batch_id='')
        ).filter(has_image=True)
        seed = seed_qs.order_by("?")[0]

        logger.debug("Getting batch for {}".format(seed))
        batch, created = seed.get_or_create_ia_batch()

        print("Getting all the screenshots that will go into that batch")
        obj_list = Screenshot.objects.rackspace_not_ia().filter(
            site=seed.site,
            timestamp__year=seed.timestamp.year,
            timestamp__month=seed.timestamp.month
        )
        logger.debug("{} found".format(len(obj_list)))

        for obj in obj_list:
            backfill_to_internet_archive_batch.delay(obj.id, batch.identifier)
