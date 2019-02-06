from django.core.management.base import BaseCommand, CommandError
from game.models import *
import time
from django.conf import settings


class Command(BaseCommand):
    def handle(self, *args, **options):
        while True:
            stations = Station.objects.all()
            for station in stations:
                station.res0 = station.res0 + station.cron_res0
                station.res1 = station.res1 + station.cron_res1
                station.res2 = station.res2 + station.cron_res2
                station.res3 = station.res3 + station.cron_res3
                station.res4 = station.res4 + station.cron_res4
                station.res5 = station.res5 + station.cron_res5
                station.res6 = station.res6 + station.cron_res6
                station.res7 = station.res7 + station.cron_res7

                if station.res0 > station.cap_res0:
                    station.res0 = station.cap_res0

                if station.res1 > station.cap_res1:
                    station.res1 = station.cap_res1

                if station.res2 > station.cap_res2:
                    station.res2 = station.cap_res2

                if station.res3 > station.cap_res3:
                    station.res3 = station.cap_res3

                if station.res4 > station.cap_res4:
                    station.res4 = station.cap_res4

                if station.res5 > station.cap_res5:
                    station.res5 = station.cap_res5

                if station.res6 > station.cap_res6:
                    station.res6 = station.cap_res6

                if station.res7 > station.cap_res7:
                    station.res7 = station.cap_res7

                station.save()

            self.stdout.write("--- tick ---")
            time.sleep(settings.ENGINE_CRON_SPEED)
