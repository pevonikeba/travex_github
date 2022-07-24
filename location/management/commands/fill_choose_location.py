from django.core.management.base import BaseCommand, CommandError
from loguru import logger

from cities.models import District, City, Subregion, Region
from location.models import ChooseLocation


def from_model_to_model(from_model, to_model, type_name: str):
    for from_obj in from_model.objects.all():
        try:
            to_obj = to_model.objects.get(pk=from_obj.pk)
            to_obj.name = from_obj.name
            to_obj.longitude = from_obj.longitude
            to_obj.latitude = from_obj.latitude
            to_obj.country_name = from_obj.country_name
            to_obj.type = type_name
            to_obj.save()
        except to_model.DoesNotExist:
            to_obj = to_model(
                    pk=from_obj.pk,
                    name=from_obj.name,
                    longitude=from_obj.longitude,
                    latitude=from_obj.latitude,
                    country_name=from_obj.country_name,
                    type=type_name,
            )
            to_obj.save()

        # to_model.objects.update_or_create(
        #     pk=obj.pk,
        #     name=obj.name,
        #     longitude=obj.longitude,
        #     latitude=obj.latitude,
        #     country_name=obj.country_name,
        #     type=type_name,
        # )


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    # def add_arguments(self, parser):
    #     parser.add_argument('poll_ids', nargs='+', type=int)

    def handle(self, *args, **options):
        # for poll_id in options['poll_ids']:
        #     try:
        #         poll = Poll.objects.get(pk=poll_id)
        #     except Poll.DoesNotExist:
        #         raise CommandError('Poll "%s" does not exist' % poll_id)
        #
        #     poll.opened = False
        #     poll.save()
        # ChooseLocation.objects.all().delete()
        from_model_to_model(from_model=District, to_model=ChooseLocation, type_name=ChooseLocation.DISTRICT)
        from_model_to_model(from_model=City, to_model=ChooseLocation, type_name=ChooseLocation.CITY)
        from_model_to_model(from_model=Subregion, to_model=ChooseLocation, type_name=ChooseLocation.SUBREGION)
        from_model_to_model(from_model=Region, to_model=ChooseLocation, type_name=ChooseLocation.REGION)
        for cl in ChooseLocation.objects.all()[:20]:
            logger.info(cl.pk)
        # self.stdout.write(self.style.SUCCESS('Successfully closed poll "%s"' % poll_id))
        self.stdout.write(self.style.SUCCESS("Successfully"))
