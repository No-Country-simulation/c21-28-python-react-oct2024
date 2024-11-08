# Generated by Django 5.1.2 on 2024-10-28 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ReservApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addresses',
            name='betweenstreet1',
            field=models.CharField(blank=True, db_collation='und-x-icu', db_column='BetweenStreet1', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='addresses',
            name='betweenstreet2',
            field=models.CharField(blank=True, db_collation='und-x-icu', db_column='BetweenStreet2', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='addresses',
            name='betweenstreet3',
            field=models.CharField(blank=True, db_collation='und-x-icu', db_column='BetweenStreet3', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='addresses',
            name='betweenstreet4',
            field=models.CharField(blank=True, db_collation='und-x-icu', db_column='BetweenStreet4', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='addresses',
            name='createdby',
            field=models.CharField(db_collation='und-x-icu', db_column='CreatedBy', max_length=50),
        ),
        migrations.AlterField(
            model_name='addresses',
            name='deletedby',
            field=models.CharField(blank=True, db_collation='und-x-icu', db_column='DeletedBy', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='addresses',
            name='departament',
            field=models.CharField(blank=True, db_collation='und-x-icu', db_column='Departament', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='addresses',
            name='entitytype',
            field=models.CharField(blank=True, db_collation='und-x-icu', db_column='EntityType', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='addresses',
            name='observations',
            field=models.CharField(db_collation='und-x-icu', db_column='Observations', max_length=100),
        ),
        migrations.AlterField(
            model_name='addresses',
            name='postalcode',
            field=models.CharField(blank=True, db_collation='und-x-icu', db_column='PostalCode', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='addresses',
            name='section',
            field=models.CharField(blank=True, db_collation='und-x-icu', db_column='Section', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='addresses',
            name='street',
            field=models.CharField(db_collation='und-x-icu', db_column='Street', max_length=100),
        ),
        migrations.AlterField(
            model_name='addresses',
            name='updatedby',
            field=models.CharField(blank=True, db_collation='und-x-icu', db_column='UpdatedBy', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='cities',
            name='createdby',
            field=models.CharField(db_collation='und-x-icu', db_column='CreatedBy', max_length=50),
        ),
        migrations.AlterField(
            model_name='cities',
            name='deletedby',
            field=models.CharField(blank=True, db_collation='und-x-icu', db_column='DeletedBy', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='cities',
            name='description',
            field=models.CharField(db_collation='und-x-icu', db_column='Description', max_length=100),
        ),
        migrations.AlterField(
            model_name='cities',
            name='updatedby',
            field=models.CharField(blank=True, db_collation='und-x-icu', db_column='UpdatedBy', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='companies',
            name='createdby',
            field=models.CharField(db_collation='und-x-icu', db_column='CreatedBy', max_length=50),
        ),
        migrations.AlterField(
            model_name='companies',
            name='deletedby',
            field=models.CharField(blank=True, db_collation='und-x-icu', db_column='DeletedBy', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='companies',
            name='denomination',
            field=models.CharField(db_collation='und-x-icu', db_column='Denomination', max_length=100),
        ),
        migrations.AlterField(
            model_name='companies',
            name='updatedby',
            field=models.CharField(blank=True, db_collation='und-x-icu', db_column='UpdatedBy', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='createdby',
            field=models.CharField(db_collation='und-x-icu', db_column='CreatedBy', max_length=50),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='deletedby',
            field=models.CharField(blank=True, db_collation='und-x-icu', db_column='DeletedBy', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='email',
            field=models.CharField(db_collation='und-x-icu', db_column='Email', max_length=100),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='firstname',
            field=models.CharField(db_collation='und-x-icu', db_column='FirstName', max_length=100),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='imgpath',
            field=models.CharField(blank=True, db_collation='und-x-icu', db_column='ImgPath', max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='lastname',
            field=models.CharField(db_collation='und-x-icu', db_column='LastName', max_length=100),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='middlename',
            field=models.CharField(db_collation='und-x-icu', db_column='MiddleName', max_length=100),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='note',
            field=models.CharField(db_collation='und-x-icu', db_column='Note', max_length=2000),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='phone',
            field=models.CharField(db_collation='und-x-icu', db_column='Phone', max_length=100),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='updatedby',
            field=models.CharField(blank=True, db_collation='und-x-icu', db_column='UpdatedBy', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='countries',
            name='countriesimage',
            field=models.CharField(blank=True, db_collation='und-x-icu', db_column='CountriesImage', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='countries',
            name='createdby',
            field=models.CharField(db_collation='und-x-icu', db_column='CreatedBy', max_length=50),
        ),
        migrations.AlterField(
            model_name='countries',
            name='deletedby',
            field=models.CharField(blank=True, db_collation='und-x-icu', db_column='DeletedBy', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='countries',
            name='description',
            field=models.CharField(db_collation='und-x-icu', db_column='Description', max_length=100),
        ),
        migrations.AlterField(
            model_name='countries',
            name='identityindividual',
            field=models.CharField(db_collation='und-x-icu', db_column='IdentityIndividual', max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='countries',
            name='identitylegal',
            field=models.CharField(db_collation='und-x-icu', db_column='IdentityLegal', max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='countries',
            name='identityother',
            field=models.CharField(db_collation='und-x-icu', db_column='IdentityOther', max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='countries',
            name='iso_3166_alpha_2',
            field=models.CharField(db_collation='und-x-icu', db_column='Iso_3166_alpha_2', max_length=2, unique=True),
        ),
        migrations.AlterField(
            model_name='countries',
            name='iso_3166_alpha_3',
            field=models.CharField(db_collation='und-x-icu', db_column='Iso_3166_alpha_3', max_length=3, unique=True),
        ),
        migrations.AlterField(
            model_name='countries',
            name='iso_3166_numeric_1',
            field=models.CharField(db_collation='und-x-icu', db_column='Iso_3166_numeric_1', max_length=3, unique=True),
        ),
        migrations.AlterField(
            model_name='countries',
            name='phoneareacode',
            field=models.CharField(db_collation='und-x-icu', db_column='PhoneAreaCode', max_length=3, unique=True),
        ),
        migrations.AlterField(
            model_name='countries',
            name='updatedby',
            field=models.CharField(blank=True, db_collation='und-x-icu', db_column='UpdatedBy', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='currencies',
            name='code',
            field=models.CharField(db_collation='und-x-icu', db_column='Code', max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='currencies',
            name='createdby',
            field=models.CharField(db_collation='und-x-icu', db_column='CreatedBy', max_length=50),
        ),
        migrations.AlterField(
            model_name='currencies',
            name='currenciesimage',
            field=models.CharField(blank=True, db_collation='und-x-icu', db_column='CurrenciesImage', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='currencies',
            name='deletedby',
            field=models.CharField(blank=True, db_collation='und-x-icu', db_column='DeletedBy', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='currencies',
            name='description',
            field=models.CharField(db_collation='und-x-icu', db_column='Description', max_length=100),
        ),
        migrations.AlterField(
            model_name='currencies',
            name='symbol',
            field=models.CharField(db_collation='und-x-icu', db_column='Symbol', max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='currencies',
            name='updatedby',
            field=models.CharField(blank=True, db_collation='und-x-icu', db_column='UpdatedBy', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='departaments',
            name='createdby',
            field=models.CharField(db_collation='und-x-icu', db_column='CreatedBy', max_length=50),
        ),
        migrations.AlterField(
            model_name='departaments',
            name='deletedby',
            field=models.CharField(blank=True, db_collation='und-x-icu', db_column='DeletedBy', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='departaments',
            name='description',
            field=models.CharField(db_collation='und-x-icu', db_column='Description', max_length=100),
        ),
        migrations.AlterField(
            model_name='departaments',
            name='updatedby',
            field=models.CharField(blank=True, db_collation='und-x-icu', db_column='UpdatedBy', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='genders',
            name='createdby',
            field=models.CharField(db_collation='und-x-icu', db_column='CreatedBy', max_length=50),
        ),
        migrations.AlterField(
            model_name='genders',
            name='deletedby',
            field=models.CharField(blank=True, db_collation='und-x-icu', db_column='DeletedBy', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='genders',
            name='description',
            field=models.CharField(db_collation='und-x-icu', db_column='Description', max_length=100),
        ),
        migrations.AlterField(
            model_name='genders',
            name='updatedby',
            field=models.CharField(blank=True, db_collation='und-x-icu', db_column='UpdatedBy', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='items',
            name='createdby',
            field=models.CharField(db_collation='und-x-icu', db_column='CreatedBy', max_length=50),
        ),
        migrations.AlterField(
            model_name='items',
            name='deletedby',
            field=models.CharField(blank=True, db_collation='und-x-icu', db_column='DeletedBy', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='items',
            name='description',
            field=models.CharField(db_collation='und-x-icu', db_column='Description', max_length=100),
        ),
        migrations.AlterField(
            model_name='items',
            name='updatedby',
            field=models.CharField(blank=True, db_collation='und-x-icu', db_column='UpdatedBy', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='itemtypes',
            name='createdby',
            field=models.CharField(db_collation='und-x-icu', db_column='CreatedBy', max_length=50),
        ),
        migrations.AlterField(
            model_name='itemtypes',
            name='deletedby',
            field=models.CharField(blank=True, db_collation='und-x-icu', db_column='DeletedBy', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='itemtypes',
            name='description',
            field=models.CharField(db_collation='und-x-icu', db_column='Description', max_length=100),
        ),
        migrations.AlterField(
            model_name='itemtypes',
            name='updatedby',
            field=models.CharField(blank=True, db_collation='und-x-icu', db_column='UpdatedBy', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='locations',
            name='ccode',
            field=models.CharField(db_collation='und-x-icu', db_column='CCode', max_length=5, unique=True),
        ),
        migrations.AlterField(
            model_name='locations',
            name='createdby',
            field=models.CharField(db_collation='und-x-icu', db_column='CreatedBy', max_length=50),
        ),
        migrations.AlterField(
            model_name='locations',
            name='deletedby',
            field=models.CharField(blank=True, db_collation='und-x-icu', db_column='DeletedBy', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='locations',
            name='description',
            field=models.CharField(db_collation='und-x-icu', db_column='Description', max_length=100),
        ),
        migrations.AlterField(
            model_name='locations',
            name='updatedby',
            field=models.CharField(blank=True, db_collation='und-x-icu', db_column='UpdatedBy', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='notes',
            name='createdby',
            field=models.CharField(db_collation='und-x-icu', db_column='CreatedBy', max_length=50),
        ),
        migrations.AlterField(
            model_name='notes',
            name='deletedby',
            field=models.CharField(blank=True, db_collation='und-x-icu', db_column='DeletedBy', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='notes',
            name='entitytype',
            field=models.CharField(blank=True, db_collation='und-x-icu', db_column='EntityType', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='notes',
            name='text',
            field=models.CharField(db_collation='und-x-icu', db_column='Text', max_length=2000),
        ),
        migrations.AlterField(
            model_name='notes',
            name='title',
            field=models.CharField(db_collation='und-x-icu', db_column='Title', max_length=100),
        ),
        migrations.AlterField(
            model_name='notes',
            name='updatedby',
            field=models.CharField(blank=True, db_collation='und-x-icu', db_column='UpdatedBy', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='partners',
            name='createdby',
            field=models.CharField(db_collation='und-x-icu', db_column='CreatedBy', max_length=50),
        ),
        migrations.AlterField(
            model_name='partners',
            name='deletedby',
            field=models.CharField(blank=True, db_collation='und-x-icu', db_column='DeletedBy', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='partners',
            name='updatedby',
            field=models.CharField(blank=True, db_collation='und-x-icu', db_column='UpdatedBy', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='postalcodes',
            name='code',
            field=models.CharField(db_collation='und-x-icu', db_column='Code', max_length=10),
        ),
        migrations.AlterField(
            model_name='postalcodes',
            name='createdby',
            field=models.CharField(db_collation='und-x-icu', db_column='CreatedBy', max_length=50),
        ),
        migrations.AlterField(
            model_name='postalcodes',
            name='deletedby',
            field=models.CharField(blank=True, db_collation='und-x-icu', db_column='DeletedBy', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='postalcodes',
            name='updatedby',
            field=models.CharField(blank=True, db_collation='und-x-icu', db_column='UpdatedBy', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='resources',
            name='createdby',
            field=models.CharField(db_collation='und-x-icu', db_column='CreatedBy', max_length=50),
        ),
        migrations.AlterField(
            model_name='resources',
            name='deletedby',
            field=models.CharField(blank=True, db_collation='und-x-icu', db_column='DeletedBy', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='resources',
            name='updatedby',
            field=models.CharField(blank=True, db_collation='und-x-icu', db_column='UpdatedBy', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='states',
            name='createdby',
            field=models.CharField(db_collation='und-x-icu', db_column='CreatedBy', max_length=50),
        ),
        migrations.AlterField(
            model_name='states',
            name='deletedby',
            field=models.CharField(blank=True, db_collation='und-x-icu', db_column='DeletedBy', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='states',
            name='description',
            field=models.CharField(db_collation='und-x-icu', db_column='Description', max_length=100),
        ),
        migrations.AlterField(
            model_name='states',
            name='iso_3166_alpha_2',
            field=models.CharField(db_collation='und-x-icu', db_column='Iso_3166_alpha_2', max_length=3, unique=True),
        ),
        migrations.AlterField(
            model_name='states',
            name='iso_3166_alpha_3',
            field=models.CharField(db_collation='und-x-icu', db_column='Iso_3166_alpha_3', max_length=5, unique=True),
        ),
        migrations.AlterField(
            model_name='states',
            name='iso_3166_numeric_1',
            field=models.CharField(db_collation='und-x-icu', db_column='Iso_3166_numeric_1', max_length=3, unique=True),
        ),
        migrations.AlterField(
            model_name='states',
            name='statesimage',
            field=models.CharField(blank=True, db_collation='und-x-icu', db_column='StatesImage', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='states',
            name='updatedby',
            field=models.CharField(blank=True, db_collation='und-x-icu', db_column='UpdatedBy', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='supplieritems',
            name='createdby',
            field=models.CharField(db_collation='und-x-icu', db_column='CreatedBy', max_length=50),
        ),
        migrations.AlterField(
            model_name='supplieritems',
            name='deletedby',
            field=models.CharField(blank=True, db_collation='und-x-icu', db_column='DeletedBy', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='supplieritems',
            name='updatedby',
            field=models.CharField(blank=True, db_collation='und-x-icu', db_column='UpdatedBy', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='supplierplanitems',
            name='createdby',
            field=models.CharField(db_collation='und-x-icu', db_column='CreatedBy', max_length=50),
        ),
        migrations.AlterField(
            model_name='supplierplanitems',
            name='deletedby',
            field=models.CharField(blank=True, db_collation='und-x-icu', db_column='DeletedBy', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='supplierplanitems',
            name='description',
            field=models.CharField(db_collation='und-x-icu', db_column='Description', max_length=100),
        ),
        migrations.AlterField(
            model_name='supplierplanitems',
            name='updatedby',
            field=models.CharField(blank=True, db_collation='und-x-icu', db_column='UpdatedBy', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='supplierplans',
            name='createdby',
            field=models.CharField(db_collation='und-x-icu', db_column='CreatedBy', max_length=50),
        ),
        migrations.AlterField(
            model_name='supplierplans',
            name='deletedby',
            field=models.CharField(blank=True, db_collation='und-x-icu', db_column='DeletedBy', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='supplierplans',
            name='description',
            field=models.CharField(db_collation='und-x-icu', db_column='Description', max_length=100),
        ),
        migrations.AlterField(
            model_name='supplierplans',
            name='updatedby',
            field=models.CharField(blank=True, db_collation='und-x-icu', db_column='UpdatedBy', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='suppliers',
            name='createdby',
            field=models.CharField(db_collation='und-x-icu', db_column='CreatedBy', max_length=50),
        ),
        migrations.AlterField(
            model_name='suppliers',
            name='deletedby',
            field=models.CharField(blank=True, db_collation='und-x-icu', db_column='DeletedBy', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='suppliers',
            name='updatedby',
            field=models.CharField(blank=True, db_collation='und-x-icu', db_column='UpdatedBy', max_length=50, null=True),
        ),
    ]
