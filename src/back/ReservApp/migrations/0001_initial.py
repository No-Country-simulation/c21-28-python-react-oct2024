# Generated by Django 5.1.2 on 2024-10-12 02:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cities',
            fields=[
                ('cityid', models.IntegerField(db_column='CityId', primary_key=True, serialize=False)),
                ('description', models.CharField(db_collation='utf8_general_ci', db_column='Description', max_length=100)),
                ('isactive', models.SmallIntegerField(db_column='IsActive')),
                ('createdat', models.DateTimeField(db_column='CreatedAt')),
                ('updatedat', models.DateTimeField(blank=True, db_column='UpdatedAt', null=True)),
                ('deletedat', models.DateTimeField(blank=True, db_column='DeletedAt', null=True)),
                ('createdby', models.CharField(db_collation='utf8_general_ci', db_column='CreatedBy', max_length=50)),
                ('updatedby', models.CharField(blank=True, db_collation='utf8_general_ci', db_column='UpdatedBy', max_length=50, null=True)),
                ('deletedby', models.CharField(blank=True, db_collation='utf8_general_ci', db_column='DeletedBy', max_length=50, null=True)),
            ],
            options={
                'db_table': 'cities',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Companies',
            fields=[
                ('companyid', models.IntegerField(db_column='CompanyId', primary_key=True, serialize=False)),
                ('denomination', models.CharField(db_collation='utf8_general_ci', db_column='Denomination', max_length=100)),
                ('isactive', models.SmallIntegerField(db_column='IsActive')),
                ('createdat', models.DateTimeField(db_column='CreatedAt')),
                ('updatedat', models.DateTimeField(blank=True, db_column='UpdatedAt', null=True)),
                ('deletedat', models.DateTimeField(blank=True, db_column='DeletedAt', null=True)),
                ('createdby', models.CharField(db_collation='utf8_general_ci', db_column='CreatedBy', max_length=50)),
                ('updatedby', models.CharField(blank=True, db_collation='utf8_general_ci', db_column='UpdatedBy', max_length=50, null=True)),
                ('deletedby', models.CharField(blank=True, db_collation='utf8_general_ci', db_column='DeletedBy', max_length=50, null=True)),
            ],
            options={
                'db_table': 'companies',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Currencies',
            fields=[
                ('currencyid', models.AutoField(db_column='CurrencyId', primary_key=True, serialize=False)),
                ('description', models.CharField(db_collation='utf8_general_ci', db_column='Description', max_length=100)),
                ('code', models.CharField(db_collation='utf8_general_ci', db_column='Code', max_length=100, unique=True)),
                ('symbol', models.CharField(db_collation='utf8_general_ci', db_column='Symbol', max_length=100, unique=True)),
                ('currenciesimage', models.CharField(blank=True, db_collation='utf8_general_ci', db_column='CurrenciesImage', max_length=100, null=True)),
                ('isactive', models.SmallIntegerField(db_column='IsActive')),
                ('createdat', models.DateTimeField(db_column='CreatedAt')),
                ('updatedat', models.DateTimeField(blank=True, db_column='UpdatedAt', null=True)),
                ('deletedat', models.DateTimeField(blank=True, db_column='DeletedAt', null=True)),
                ('createdby', models.CharField(db_collation='utf8_general_ci', db_column='CreatedBy', max_length=50)),
                ('updatedby', models.CharField(blank=True, db_collation='utf8_general_ci', db_column='UpdatedBy', max_length=50, null=True)),
                ('deletedby', models.CharField(blank=True, db_collation='utf8_general_ci', db_column='DeletedBy', max_length=50, null=True)),
            ],
            options={
                'db_table': 'currencies',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Genders',
            fields=[
                ('genderid', models.IntegerField(db_column='GenderId', primary_key=True, serialize=False)),
                ('description', models.CharField(db_collation='utf8_general_ci', db_column='Description', max_length=100)),
                ('isactive', models.SmallIntegerField(db_column='IsActive')),
                ('createdat', models.DateTimeField(db_column='CreatedAt')),
                ('updatedat', models.DateTimeField(blank=True, db_column='UpdatedAt', null=True)),
                ('deletedat', models.DateTimeField(blank=True, db_column='DeletedAt', null=True)),
                ('createdby', models.CharField(db_collation='utf8_general_ci', db_column='CreatedBy', max_length=50)),
                ('updatedby', models.CharField(blank=True, db_collation='utf8_general_ci', db_column='UpdatedBy', max_length=50, null=True)),
                ('deletedby', models.CharField(blank=True, db_collation='utf8_general_ci', db_column='DeletedBy', max_length=50, null=True)),
            ],
            options={
                'db_table': 'genders',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Countries',
            fields=[
                ('countryid', models.IntegerField(db_column='CountryId', primary_key=True, serialize=False)),
                ('description', models.CharField(db_collation='utf8_general_ci', db_column='Description', max_length=100)),
                ('phoneareacode', models.CharField(db_collation='utf8_general_ci', db_column='PhoneAreaCode', max_length=3, unique=True)),
                ('iso_3166_numeric_1', models.CharField(db_collation='utf8_general_ci', db_column='Iso_3166_numeric_1', max_length=3, unique=True)),
                ('iso_3166_alpha_2', models.CharField(db_collation='utf8_general_ci', db_column='Iso_3166_alpha_2', max_length=2, unique=True)),
                ('iso_3166_alpha_3', models.CharField(db_collation='utf8_general_ci', db_column='Iso_3166_alpha_3', max_length=3, unique=True)),
                ('identityindividual', models.CharField(db_collation='utf8_general_ci', db_column='IdentityIndividual', max_length=20, unique=True)),
                ('identitylegal', models.CharField(db_collation='utf8_general_ci', db_column='IdentityLegal', max_length=20, unique=True)),
                ('identityother', models.CharField(db_collation='utf8_general_ci', db_column='IdentityOther', max_length=20, unique=True)),
                ('identitycode', models.SmallIntegerField(db_column='IdentityCode', unique=True)),
                ('countriesimage', models.CharField(blank=True, db_collation='utf8_general_ci', db_column='CountriesImage', max_length=100, null=True)),
                ('isactive', models.SmallIntegerField(db_column='IsActive')),
                ('createdat', models.DateTimeField(db_column='CreatedAt')),
                ('updatedat', models.DateTimeField(blank=True, db_column='UpdatedAt', null=True)),
                ('deletedat', models.DateTimeField(blank=True, db_column='DeletedAt', null=True)),
                ('createdby', models.CharField(db_collation='utf8_general_ci', db_column='CreatedBy', max_length=50)),
                ('updatedby', models.CharField(blank=True, db_collation='utf8_general_ci', db_column='UpdatedBy', max_length=50, null=True)),
                ('deletedby', models.CharField(blank=True, db_collation='utf8_general_ci', db_column='DeletedBy', max_length=50, null=True)),
                ('currencyid', models.ForeignKey(db_column='CurrencyId', on_delete=django.db.models.deletion.DO_NOTHING, to='ReservApp.currencies')),
            ],
            options={
                'db_table': 'countries',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Departaments',
            fields=[
                ('departamentid', models.IntegerField(db_column='DepartamentId', primary_key=True, serialize=False)),
                ('description', models.CharField(db_collation='utf8_general_ci', db_column='Description', max_length=100)),
                ('isactive', models.SmallIntegerField(db_column='IsActive')),
                ('createdat', models.DateTimeField(db_column='CreatedAt')),
                ('updatedat', models.DateTimeField(blank=True, db_column='UpdatedAt', null=True)),
                ('deletedat', models.DateTimeField(blank=True, db_column='DeletedAt', null=True)),
                ('createdby', models.CharField(db_collation='utf8_general_ci', db_column='CreatedBy', max_length=50)),
                ('updatedby', models.CharField(blank=True, db_collation='utf8_general_ci', db_column='UpdatedBy', max_length=50, null=True)),
                ('deletedby', models.CharField(blank=True, db_collation='utf8_general_ci', db_column='DeletedBy', max_length=50, null=True)),
                ('cityid', models.ForeignKey(db_column='CityId', on_delete=django.db.models.deletion.DO_NOTHING, to='ReservApp.cities')),
            ],
            options={
                'db_table': 'departaments',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('contactid', models.BigAutoField(db_column='ContactId', primary_key=True, serialize=False)),
                ('firstname', models.CharField(db_collation='utf8_general_ci', db_column='FirstName', max_length=100)),
                ('middlename', models.CharField(db_collation='utf8_general_ci', db_column='MiddleName', max_length=100)),
                ('lastname', models.CharField(db_collation='utf8_general_ci', db_column='LastName', max_length=100)),
                ('birthdate', models.DateTimeField(blank=True, db_column='BirthDate', null=True)),
                ('phone', models.CharField(db_collation='utf8_general_ci', db_column='Phone', max_length=100)),
                ('email', models.CharField(db_collation='utf8_general_ci', db_column='Email', max_length=100)),
                ('note', models.CharField(db_collation='utf8_general_ci', db_column='Note', max_length=2000)),
                ('imgpath', models.CharField(blank=True, db_collation='utf8_general_ci', db_column='ImgPath', max_length=250, null=True)),
                ('ischecked', models.SmallIntegerField(db_column='IsChecked')),
                ('isactive', models.SmallIntegerField(db_column='IsActive')),
                ('createdat', models.DateTimeField(db_column='CreatedAt')),
                ('updatedat', models.DateTimeField(blank=True, db_column='UpdatedAt', null=True)),
                ('deletedat', models.DateTimeField(blank=True, db_column='DeletedAt', null=True)),
                ('createdby', models.CharField(db_collation='utf8_general_ci', db_column='CreatedBy', max_length=50)),
                ('updatedby', models.CharField(blank=True, db_collation='utf8_general_ci', db_column='UpdatedBy', max_length=50, null=True)),
                ('deletedby', models.CharField(blank=True, db_collation='utf8_general_ci', db_column='DeletedBy', max_length=50, null=True)),
                ('companyid', models.ForeignKey(db_column='CompanyId', on_delete=django.db.models.deletion.DO_NOTHING, to='ReservApp.companies')),
                ('genderid', models.ForeignKey(db_column='GenderId', on_delete=django.db.models.deletion.DO_NOTHING, to='ReservApp.genders')),
            ],
            options={
                'db_table': 'contacts',
                'managed': True,
                'unique_together': {('companyid', 'firstname', 'middlename', 'lastname', 'birthdate')},
            },
        ),
        migrations.CreateModel(
            name='Itemtypes',
            fields=[
                ('itemtypeid', models.IntegerField(db_column='ItemTypeId', primary_key=True, serialize=False)),
                ('description', models.CharField(db_collation='utf8_general_ci', db_column='Description', max_length=100)),
                ('isactive', models.SmallIntegerField(db_column='IsActive')),
                ('createdat', models.DateTimeField(db_column='CreatedAt')),
                ('updatedat', models.DateTimeField(blank=True, db_column='UpdatedAt', null=True)),
                ('deletedat', models.DateTimeField(blank=True, db_column='DeletedAt', null=True)),
                ('createdby', models.CharField(db_collation='utf8_general_ci', db_column='CreatedBy', max_length=50)),
                ('updatedby', models.CharField(blank=True, db_collation='utf8_general_ci', db_column='UpdatedBy', max_length=50, null=True)),
                ('deletedby', models.CharField(blank=True, db_collation='utf8_general_ci', db_column='DeletedBy', max_length=50, null=True)),
                ('companyid', models.ForeignKey(db_column='CompanyId', on_delete=django.db.models.deletion.DO_NOTHING, to='ReservApp.companies')),
                ('parentid', models.ForeignKey(blank=True, db_column='ParentId', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='ReservApp.itemtypes')),
            ],
            options={
                'db_table': 'itemtypes',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Items',
            fields=[
                ('itemid', models.AutoField(db_column='ItemId', primary_key=True, serialize=False)),
                ('description', models.CharField(db_collation='utf8_general_ci', db_column='Description', max_length=100)),
                ('isactive', models.SmallIntegerField(db_column='IsActive')),
                ('createdat', models.DateTimeField(db_column='CreatedAt')),
                ('updatedat', models.DateTimeField(blank=True, db_column='UpdatedAt', null=True)),
                ('deletedat', models.DateTimeField(blank=True, db_column='DeletedAt', null=True)),
                ('createdby', models.CharField(db_collation='utf8_general_ci', db_column='CreatedBy', max_length=50)),
                ('updatedby', models.CharField(blank=True, db_collation='utf8_general_ci', db_column='UpdatedBy', max_length=50, null=True)),
                ('deletedby', models.CharField(blank=True, db_collation='utf8_general_ci', db_column='DeletedBy', max_length=50, null=True)),
                ('companyid', models.ForeignKey(blank=True, db_column='CompanyId', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='ReservApp.companies')),
                ('parentid', models.ForeignKey(blank=True, db_column='ParentId', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='ReservApp.items')),
                ('itemtypeid', models.ForeignKey(blank=True, db_column='ItemTypeId', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='ReservApp.itemtypes')),
            ],
            options={
                'db_table': 'items',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Locations',
            fields=[
                ('locationid', models.AutoField(db_column='LocationId', primary_key=True, serialize=False)),
                ('description', models.CharField(db_collation='utf8_general_ci', db_column='Description', max_length=100)),
                ('ccode', models.CharField(db_collation='utf8_general_ci', db_column='CCode', max_length=5, unique=True)),
                ('ncode', models.SmallIntegerField(db_column='NCode', unique=True)),
                ('isroot', models.SmallIntegerField(db_column='IsRoot')),
                ('isactive', models.SmallIntegerField(db_column='IsActive')),
                ('createdat', models.DateTimeField(db_column='CreatedAt')),
                ('updatedat', models.DateTimeField(blank=True, db_column='UpdatedAt', null=True)),
                ('deletedat', models.DateTimeField(blank=True, db_column='DeletedAt', null=True)),
                ('createdby', models.CharField(db_collation='utf8_general_ci', db_column='CreatedBy', max_length=50)),
                ('updatedby', models.CharField(blank=True, db_collation='utf8_general_ci', db_column='UpdatedBy', max_length=50, null=True)),
                ('deletedby', models.CharField(blank=True, db_collation='utf8_general_ci', db_column='DeletedBy', max_length=50, null=True)),
                ('companyid', models.ForeignKey(db_column='CompanyId', on_delete=django.db.models.deletion.DO_NOTHING, to='ReservApp.companies')),
                ('parentid', models.ForeignKey(blank=True, db_column='ParentId', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='ReservApp.locations')),
            ],
            options={
                'db_table': 'locations',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('noteid', models.AutoField(db_column='NoteId', primary_key=True, serialize=False)),
                ('entitytype', models.CharField(blank=True, db_collation='utf8_general_ci', db_column='EntityType', max_length=100, null=True)),
                ('rowid', models.BigIntegerField(db_column='RowId')),
                ('text', models.CharField(db_collation='utf8_general_ci', db_column='Text', max_length=2000)),
                ('isactive', models.SmallIntegerField(db_column='IsActive')),
                ('createdat', models.DateTimeField(db_column='CreatedAt')),
                ('updatedat', models.DateTimeField(blank=True, db_column='UpdatedAt', null=True)),
                ('deletedat', models.DateTimeField(blank=True, db_column='DeletedAt', null=True)),
                ('createdby', models.CharField(db_collation='utf8_general_ci', db_column='CreatedBy', max_length=50)),
                ('updatedby', models.CharField(blank=True, db_collation='utf8_general_ci', db_column='UpdatedBy', max_length=50, null=True)),
                ('deletedby', models.CharField(blank=True, db_collation='utf8_general_ci', db_column='DeletedBy', max_length=50, null=True)),
                ('title', models.CharField(db_collation='utf8_general_ci', db_column='Title', max_length=100)),
                ('companyid', models.ForeignKey(db_column='CompanyId', on_delete=django.db.models.deletion.DO_NOTHING, to='ReservApp.companies')),
            ],
            options={
                'db_table': 'notes',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Partners',
            fields=[
                ('partnerid', models.AutoField(db_column='PartnerId', primary_key=True, serialize=False)),
                ('isactive', models.SmallIntegerField(db_column='IsActive')),
                ('createdat', models.DateTimeField(db_column='CreatedAt')),
                ('updatedat', models.DateTimeField(blank=True, db_column='UpdatedAt', null=True)),
                ('deletedat', models.DateTimeField(blank=True, db_column='DeletedAt', null=True)),
                ('createdby', models.CharField(db_collation='utf8_general_ci', db_column='CreatedBy', max_length=50)),
                ('updatedby', models.CharField(blank=True, db_collation='utf8_general_ci', db_column='UpdatedBy', max_length=50, null=True)),
                ('deletedby', models.CharField(blank=True, db_collation='utf8_general_ci', db_column='DeletedBy', max_length=50, null=True)),
                ('contactid', models.ForeignKey(db_column='ContactId', on_delete=django.db.models.deletion.DO_NOTHING, to='ReservApp.contacts')),
            ],
            options={
                'db_table': 'partners',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Postalcodes',
            fields=[
                ('postalcodeid', models.IntegerField(db_column='PostalCodeId', primary_key=True, serialize=False)),
                ('code', models.CharField(db_collation='utf8_general_ci', db_column='Code', max_length=10)),
                ('isactive', models.SmallIntegerField(db_column='IsActive')),
                ('createdat', models.DateTimeField(db_column='CreatedAt')),
                ('updatedat', models.DateTimeField(blank=True, db_column='UpdatedAt', null=True)),
                ('deletedat', models.DateTimeField(blank=True, db_column='DeletedAt', null=True)),
                ('createdby', models.CharField(db_collation='utf8_general_ci', db_column='CreatedBy', max_length=50)),
                ('updatedby', models.CharField(blank=True, db_collation='utf8_general_ci', db_column='UpdatedBy', max_length=50, null=True)),
                ('deletedby', models.CharField(blank=True, db_collation='utf8_general_ci', db_column='DeletedBy', max_length=50, null=True)),
                ('departamentid', models.ForeignKey(db_column='DepartamentId', on_delete=django.db.models.deletion.DO_NOTHING, to='ReservApp.departaments')),
            ],
            options={
                'db_table': 'postalcodes',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Resources',
            fields=[
                ('resourceid', models.AutoField(db_column='ResourceId', primary_key=True, serialize=False)),
                ('hiredate', models.DateTimeField(blank=True, db_column='HireDate', null=True)),
                ('isactive', models.SmallIntegerField(db_column='IsActive')),
                ('createdat', models.DateTimeField(db_column='CreatedAt')),
                ('updatedat', models.DateTimeField(blank=True, db_column='UpdatedAt', null=True)),
                ('deletedat', models.DateTimeField(blank=True, db_column='DeletedAt', null=True)),
                ('createdby', models.CharField(db_collation='utf8_general_ci', db_column='CreatedBy', max_length=50)),
                ('updatedby', models.CharField(blank=True, db_collation='utf8_general_ci', db_column='UpdatedBy', max_length=50, null=True)),
                ('deletedby', models.CharField(blank=True, db_collation='utf8_general_ci', db_column='DeletedBy', max_length=50, null=True)),
                ('contactid', models.ForeignKey(db_column='ContactId', on_delete=django.db.models.deletion.DO_NOTHING, to='ReservApp.contacts')),
            ],
            options={
                'db_table': 'resources',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='States',
            fields=[
                ('stateid', models.IntegerField(db_column='StateId', primary_key=True, serialize=False)),
                ('description', models.CharField(db_collation='utf8_general_ci', db_column='Description', max_length=100)),
                ('iso_3166_numeric_1', models.CharField(db_collation='utf8_general_ci', db_column='Iso_3166_numeric_1', max_length=3, unique=True)),
                ('iso_3166_alpha_2', models.CharField(db_collation='utf8_general_ci', db_column='Iso_3166_alpha_2', max_length=3, unique=True)),
                ('iso_3166_alpha_3', models.CharField(db_collation='utf8_general_ci', db_column='Iso_3166_alpha_3', max_length=5, unique=True)),
                ('statesimage', models.CharField(blank=True, db_collation='utf8_general_ci', db_column='StatesImage', max_length=100, null=True)),
                ('isactive', models.SmallIntegerField(db_column='IsActive')),
                ('createdat', models.DateTimeField(db_column='CreatedAt')),
                ('updatedat', models.DateTimeField(blank=True, db_column='UpdatedAt', null=True)),
                ('deletedat', models.DateTimeField(blank=True, db_column='DeletedAt', null=True)),
                ('createdby', models.CharField(db_collation='utf8_general_ci', db_column='CreatedBy', max_length=50)),
                ('updatedby', models.CharField(blank=True, db_collation='utf8_general_ci', db_column='UpdatedBy', max_length=50, null=True)),
                ('deletedby', models.CharField(blank=True, db_collation='utf8_general_ci', db_column='DeletedBy', max_length=50, null=True)),
                ('countryid', models.ForeignKey(db_column='CountryId', on_delete=django.db.models.deletion.DO_NOTHING, to='ReservApp.countries')),
            ],
            options={
                'db_table': 'states',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='cities',
            name='stateid',
            field=models.ForeignKey(db_column='StateId', on_delete=django.db.models.deletion.DO_NOTHING, to='ReservApp.states'),
        ),
        migrations.CreateModel(
            name='Addresses',
            fields=[
                ('addressid', models.AutoField(db_column='AddressId', primary_key=True, serialize=False)),
                ('entitytype', models.CharField(blank=True, db_collation='utf8_general_ci', db_column='EntityType', max_length=100, null=True)),
                ('rowid', models.BigIntegerField(db_column='RowId')),
                ('isdefault', models.SmallIntegerField(db_column='IsDefault')),
                ('ischecked', models.SmallIntegerField(db_column='IsChecked')),
                ('street', models.CharField(db_collation='utf8_general_ci', db_column='Street', max_length=100)),
                ('number', models.BigIntegerField(db_column='Number')),
                ('floor', models.BigIntegerField(db_column='Floor')),
                ('departament', models.CharField(blank=True, db_collation='utf8_general_ci', db_column='Departament', max_length=10, null=True)),
                ('postalcode', models.CharField(blank=True, db_collation='utf8_general_ci', db_column='PostalCode', max_length=10, null=True)),
                ('section', models.CharField(blank=True, db_collation='utf8_general_ci', db_column='Section', max_length=10, null=True)),
                ('betweenstreet1', models.CharField(blank=True, db_collation='utf8_general_ci', db_column='BetweenStreet1', max_length=100, null=True)),
                ('betweenstreet2', models.CharField(blank=True, db_collation='utf8_general_ci', db_column='BetweenStreet2', max_length=100, null=True)),
                ('betweenstreet3', models.CharField(blank=True, db_collation='utf8_general_ci', db_column='BetweenStreet3', max_length=100, null=True)),
                ('betweenstreet4', models.CharField(blank=True, db_collation='utf8_general_ci', db_column='BetweenStreet4', max_length=100, null=True)),
                ('betweenstreet1number', models.BigIntegerField(blank=True, db_column='BetweenStreet1Number', null=True)),
                ('betweenstreet2number', models.BigIntegerField(blank=True, db_column='BetweenStreet2Number', null=True)),
                ('betweenstreet3number', models.BigIntegerField(blank=True, db_column='BetweenStreet3Number', null=True)),
                ('betweenstreet4number', models.BigIntegerField(blank=True, db_column='BetweenStreet4Number', null=True)),
                ('latitude', models.FloatField(blank=True, db_column='Latitude', null=True)),
                ('longitude', models.FloatField(blank=True, db_column='Longitude', null=True)),
                ('observations', models.CharField(db_collation='utf8_general_ci', db_column='Observations', max_length=100)),
                ('isactive', models.SmallIntegerField(db_column='IsActive')),
                ('createdat', models.DateTimeField(db_column='CreatedAt')),
                ('updatedat', models.DateTimeField(blank=True, db_column='UpdatedAt', null=True)),
                ('deletedat', models.DateTimeField(blank=True, db_column='DeletedAt', null=True)),
                ('createdby', models.CharField(db_collation='utf8_general_ci', db_column='CreatedBy', max_length=50)),
                ('updatedby', models.CharField(blank=True, db_collation='utf8_general_ci', db_column='UpdatedBy', max_length=50, null=True)),
                ('deletedby', models.CharField(blank=True, db_collation='utf8_general_ci', db_column='DeletedBy', max_length=50, null=True)),
                ('cityid', models.ForeignKey(db_column='CityId', on_delete=django.db.models.deletion.DO_NOTHING, to='ReservApp.cities')),
                ('companyid', models.ForeignKey(db_column='CompanyId', on_delete=django.db.models.deletion.DO_NOTHING, to='ReservApp.companies')),
                ('countryid', models.ForeignKey(db_column='CountryId', on_delete=django.db.models.deletion.DO_NOTHING, to='ReservApp.countries')),
                ('departamentid', models.ForeignKey(db_column='DepartamentId', on_delete=django.db.models.deletion.DO_NOTHING, to='ReservApp.departaments')),
                ('stateid', models.ForeignKey(db_column='StateId', on_delete=django.db.models.deletion.DO_NOTHING, to='ReservApp.states')),
            ],
            options={
                'db_table': 'addresses',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Suppliers',
            fields=[
                ('supplierid', models.AutoField(db_column='SupplierId', primary_key=True, serialize=False)),
                ('isactive', models.SmallIntegerField(db_column='IsActive')),
                ('createdat', models.DateTimeField(db_column='CreatedAt')),
                ('updatedat', models.DateTimeField(blank=True, db_column='UpdatedAt', null=True)),
                ('deletedat', models.DateTimeField(blank=True, db_column='DeletedAt', null=True)),
                ('createdby', models.CharField(db_collation='utf8_general_ci', db_column='CreatedBy', max_length=50)),
                ('updatedby', models.CharField(blank=True, db_collation='utf8_general_ci', db_column='UpdatedBy', max_length=50, null=True)),
                ('deletedby', models.CharField(blank=True, db_collation='utf8_general_ci', db_column='DeletedBy', max_length=50, null=True)),
                ('contactid', models.ForeignKey(db_column='ContactId', on_delete=django.db.models.deletion.DO_NOTHING, to='ReservApp.contacts')),
            ],
            options={
                'db_table': 'suppliers',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Supplierplans',
            fields=[
                ('supplierplanid', models.AutoField(db_column='SupplierPlanId', primary_key=True, serialize=False)),
                ('description', models.CharField(db_collation='utf8_general_ci', db_column='Description', max_length=100)),
                ('order', models.SmallIntegerField(db_column='Order')),
                ('isdefault', models.IntegerField(db_column='IsDefault')),
                ('isactive', models.SmallIntegerField(db_column='IsActive')),
                ('createdat', models.DateTimeField(db_column='CreatedAt')),
                ('updatedat', models.DateTimeField(blank=True, db_column='UpdatedAt', null=True)),
                ('deletedat', models.DateTimeField(blank=True, db_column='DeletedAt', null=True)),
                ('createdby', models.CharField(db_collation='utf8_general_ci', db_column='CreatedBy', max_length=50)),
                ('updatedby', models.CharField(blank=True, db_collation='utf8_general_ci', db_column='UpdatedBy', max_length=50, null=True)),
                ('deletedby', models.CharField(blank=True, db_collation='utf8_general_ci', db_column='DeletedBy', max_length=50, null=True)),
                ('supplierid', models.ForeignKey(db_column='SupplierId', on_delete=django.db.models.deletion.DO_NOTHING, to='ReservApp.suppliers')),
            ],
            options={
                'db_table': 'supplierplans',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Supplieritems',
            fields=[
                ('supplieritemid', models.AutoField(db_column='SupplierItemId', primary_key=True, serialize=False)),
                ('isactive', models.SmallIntegerField(db_column='IsActive')),
                ('createdat', models.DateTimeField(db_column='CreatedAt')),
                ('updatedat', models.DateTimeField(blank=True, db_column='UpdatedAt', null=True)),
                ('deletedat', models.DateTimeField(blank=True, db_column='DeletedAt', null=True)),
                ('createdby', models.CharField(db_collation='utf8_general_ci', db_column='CreatedBy', max_length=50)),
                ('updatedby', models.CharField(blank=True, db_collation='utf8_general_ci', db_column='UpdatedBy', max_length=50, null=True)),
                ('deletedby', models.CharField(blank=True, db_collation='utf8_general_ci', db_column='DeletedBy', max_length=50, null=True)),
                ('itemid', models.ForeignKey(db_column='ItemId', on_delete=django.db.models.deletion.DO_NOTHING, to='ReservApp.items')),
                ('supplierid', models.ForeignKey(db_column='SupplierId', on_delete=django.db.models.deletion.DO_NOTHING, to='ReservApp.suppliers')),
            ],
            options={
                'db_table': 'supplieritems',
                'managed': True,
                'unique_together': {('supplierid', 'itemid')},
            },
        ),
        migrations.CreateModel(
            name='Supplierplanitems',
            fields=[
                ('supplierplanitemid', models.AutoField(db_column='SupplierPlanItemId', primary_key=True, serialize=False)),
                ('description', models.CharField(db_collation='utf8_general_ci', db_column='Description', max_length=100)),
                ('order', models.SmallIntegerField(db_column='Order')),
                ('percentagecovered', models.DecimalField(db_column='PercentageCovered', decimal_places=2, max_digits=4)),
                ('amountcovered', models.DecimalField(db_column='AmountCovered', decimal_places=2, max_digits=18)),
                ('isactive', models.SmallIntegerField(db_column='IsActive')),
                ('createdat', models.DateTimeField(db_column='CreatedAt')),
                ('updatedat', models.DateTimeField(blank=True, db_column='UpdatedAt', null=True)),
                ('deletedat', models.DateTimeField(blank=True, db_column='DeletedAt', null=True)),
                ('createdby', models.CharField(db_collation='utf8_general_ci', db_column='CreatedBy', max_length=50)),
                ('updatedby', models.CharField(blank=True, db_collation='utf8_general_ci', db_column='UpdatedBy', max_length=50, null=True)),
                ('deletedby', models.CharField(blank=True, db_collation='utf8_general_ci', db_column='DeletedBy', max_length=50, null=True)),
                ('supplieritemid', models.ForeignKey(db_column='SupplierItemId', on_delete=django.db.models.deletion.DO_NOTHING, to='ReservApp.supplieritems')),
                ('supplierplanid', models.ForeignKey(db_column='SupplierPlanId', on_delete=django.db.models.deletion.DO_NOTHING, to='ReservApp.supplierplans')),
            ],
            options={
                'db_table': 'supplierplanitems',
                'managed': True,
                'unique_together': {('supplierplanid', 'supplieritemid')},
            },
        ),
    ]
