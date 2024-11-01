
from src.back.api.ReservApp.multicharfield import MultiCollationCharField

#https://docs.djangoproject.com/en/5.1/ref/databases/
#utf8_general_ci debe ir und-x-icu
entitytype = MultiCollationCharField(
        db_column='EntityType',
        max_length=100,
        blank=True,
        null=True,
        db_collations={
            'sqlite': 'BINARY',
            'mysql': 'utf8mb4_bin',
            'postgresql_psycopg2':'und-x-icu',
        }
    )

from django.db import models

class MultiCollationCharField(models.CharField):
    def __init__(self, *args, db_collations=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.db_collations = db_collations or {}

    def db_parameters(self, connection):
        db_params = models.Field.db_parameters(self, connection)

        # Now determine collation based on DB vendor (e.g. 'sqlite', 'mysql')
        if connection.vendor in self.db_collations:
            db_params["collation"] = self.db_collations[connection.vendor]

        return db_params

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        if self.db_collations:
            kwargs['db_collations'] = self.db_collations
        return name, path, args, kwargs