from django.core.management.base import BaseCommand
from django.db import connection
from django.conf import settings
import MySQLdb


class Command(BaseCommand):
    help = 'Drops and recreates the database'

    def handle(self, *args, **options):
        db_name = settings.DATABASES['default']['NAME']
        db_user = settings.DATABASES['default']['USER']
        db_password = settings.DATABASES['default']['PASSWORD']
        db_host = settings.DATABASES['default']['HOST']
        db_port = settings.DATABASES['default']['PORT']

        connection.close()

        conn = MySQLdb.connect(
            host=db_host,
            user=db_user,
            passwd=db_password,
            port=int(db_port) if db_port else 3306
        )
        conn.autocommit(True)
        cursor = conn.cursor()

        cursor.execute(f"DROP DATABASE IF EXISTS {db_name}")
        cursor.execute(f"CREATE DATABASE {db_name}")

        cursor.close()
        conn.close()

        self.stdout.write(self.style.SUCCESS(
            'Successfully reset the database'))
