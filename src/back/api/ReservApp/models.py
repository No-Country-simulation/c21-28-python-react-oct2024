# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Addresses(models.Model):
    addressid = models.AutoField(db_column='AddressId', primary_key=True)  # Field name made lowercase.
    companyid = models.ForeignKey('Companies', models.DO_NOTHING, db_column='CompanyId')  # Field name made lowercase.
    entitytype = models.CharField(db_column='EntityType', max_length=100, db_collation='und-x-icu', blank=True, null=True)  # Field name made lowercase.
    rowid = models.BigIntegerField(db_column='RowId')  # Field name made lowercase.
    countryid = models.ForeignKey('Countries', models.DO_NOTHING, db_column='CountryId')  # Field name made lowercase.
    stateid = models.ForeignKey('States', models.DO_NOTHING, db_column='StateId')  # Field name made lowercase.
    cityid = models.ForeignKey('Cities', models.DO_NOTHING, db_column='CityId')  # Field name made lowercase.
    departamentid = models.ForeignKey('Departaments', models.DO_NOTHING, db_column='DepartamentId')  # Field name made lowercase.
    isdefault = models.SmallIntegerField(db_column='IsDefault')  # Field name made lowercase.
    ischecked = models.SmallIntegerField(db_column='IsChecked')  # Field name made lowercase.
    street = models.CharField(db_column='Street', max_length=100, db_collation='und-x-icu')  # Field name made lowercase.
    number = models.BigIntegerField(db_column='Number')  # Field name made lowercase.
    floor = models.BigIntegerField(db_column='Floor')  # Field name made lowercase.
    departament = models.CharField(db_column='Departament', max_length=10, db_collation='und-x-icu', blank=True, null=True)  # Field name made lowercase.
    postalcode = models.CharField(db_column='PostalCode', max_length=10, db_collation='und-x-icu', blank=True, null=True)  # Field name made lowercase.
    section = models.CharField(db_column='Section', max_length=10, db_collation='und-x-icu', blank=True, null=True)  # Field name made lowercase.
    betweenstreet1 = models.CharField(db_column='BetweenStreet1', max_length=100, db_collation='und-x-icu', blank=True, null=True)  # Field name made lowercase.
    betweenstreet2 = models.CharField(db_column='BetweenStreet2', max_length=100, db_collation='und-x-icu', blank=True, null=True)  # Field name made lowercase.
    betweenstreet3 = models.CharField(db_column='BetweenStreet3', max_length=100, db_collation='und-x-icu', blank=True, null=True)  # Field name made lowercase.
    betweenstreet4 = models.CharField(db_column='BetweenStreet4', max_length=100, db_collation='und-x-icu', blank=True, null=True)  # Field name made lowercase.
    betweenstreet1number = models.BigIntegerField(db_column='BetweenStreet1Number', blank=True, null=True)  # Field name made lowercase.
    betweenstreet2number = models.BigIntegerField(db_column='BetweenStreet2Number', blank=True, null=True)  # Field name made lowercase.
    betweenstreet3number = models.BigIntegerField(db_column='BetweenStreet3Number', blank=True, null=True)  # Field name made lowercase.
    betweenstreet4number = models.BigIntegerField(db_column='BetweenStreet4Number', blank=True, null=True)  # Field name made lowercase.
    latitude = models.FloatField(db_column='Latitude', blank=True, null=True)  # Field name made lowercase.
    longitude = models.FloatField(db_column='Longitude', blank=True, null=True)  # Field name made lowercase.
    observations = models.CharField(db_column='Observations', max_length=100, db_collation='und-x-icu')  # Field name made lowercase.
    isactive = models.SmallIntegerField(db_column='IsActive')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=50, db_collation='und-x-icu')  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=50, db_collation='und-x-icu', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=50, db_collation='und-x-icu', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'addresses'


class Cities(models.Model):
    cityid = models.IntegerField(db_column='CityId', primary_key=True)  # Field name made lowercase.
    stateid = models.ForeignKey('States', models.DO_NOTHING, db_column='StateId')  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=100, db_collation='und-x-icu')  # Field name made lowercase.
    isactive = models.SmallIntegerField(db_column='IsActive')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=50, db_collation='und-x-icu')  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=50, db_collation='und-x-icu', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=50, db_collation='und-x-icu', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'cities'


class Companies(models.Model):
    companyid = models.IntegerField(db_column='CompanyId', primary_key=True)  # Field name made lowercase.
    denomination = models.CharField(db_column='Denomination', max_length=100, db_collation='und-x-icu')  # Field name made lowercase.
    isactive = models.SmallIntegerField(db_column='IsActive')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=50, db_collation='und-x-icu')  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=50, db_collation='und-x-icu', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=50, db_collation='und-x-icu', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'companies'


class Contacts(models.Model):
    contactid = models.BigAutoField(db_column='ContactId', primary_key=True)  # Field name made lowercase.
    companyid = models.ForeignKey(Companies, models.DO_NOTHING, db_column='CompanyId')  # Field name made lowercase.
    genderid = models.ForeignKey('Genders', models.DO_NOTHING, db_column='GenderId')  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=100, db_collation='und-x-icu')  # Field name made lowercase.
    middlename = models.CharField(db_column='MiddleName', max_length=100, db_collation='und-x-icu')  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=100, db_collation='und-x-icu')  # Field name made lowercase.
    birthdate = models.DateTimeField(db_column='BirthDate', blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=100, db_collation='und-x-icu')  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=100, db_collation='und-x-icu')  # Field name made lowercase.
    note = models.CharField(db_column='Note', max_length=2000, db_collation='und-x-icu')  # Field name made lowercase.
    imgpath = models.CharField(db_column='ImgPath', max_length=250, db_collation='und-x-icu', blank=True, null=True)  # Field name made lowercase.
    ischecked = models.SmallIntegerField(db_column='IsChecked')  # Field name made lowercase.
    isactive = models.SmallIntegerField(db_column='IsActive')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=50, db_collation='und-x-icu')  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=50, db_collation='und-x-icu', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=50, db_collation='und-x-icu', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'contacts'
        unique_together = (('companyid', 'firstname', 'middlename', 'lastname', 'birthdate'),)


class Countries(models.Model):
    countryid = models.IntegerField(db_column='CountryId', primary_key=True)  # Field name made lowercase.
    currencyid = models.ForeignKey('Currencies', models.DO_NOTHING, db_column='CurrencyId')  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=100, db_collation='und-x-icu')  # Field name made lowercase.
    phoneareacode = models.CharField(db_column='PhoneAreaCode', unique=True, max_length=3, db_collation='und-x-icu')  # Field name made lowercase.
    iso_3166_numeric_1 = models.CharField(db_column='Iso_3166_numeric_1', unique=True, max_length=3, db_collation='und-x-icu')  # Field name made lowercase.
    iso_3166_alpha_2 = models.CharField(db_column='Iso_3166_alpha_2', unique=True, max_length=2, db_collation='und-x-icu')  # Field name made lowercase.
    iso_3166_alpha_3 = models.CharField(db_column='Iso_3166_alpha_3', unique=True, max_length=3, db_collation='und-x-icu')  # Field name made lowercase.
    identityindividual = models.CharField(db_column='IdentityIndividual', unique=True, max_length=20, db_collation='und-x-icu')  # Field name made lowercase.
    identitylegal = models.CharField(db_column='IdentityLegal', unique=True, max_length=20, db_collation='und-x-icu')  # Field name made lowercase.
    identityother = models.CharField(db_column='IdentityOther', unique=True, max_length=20, db_collation='und-x-icu')  # Field name made lowercase.
    identitycode = models.SmallIntegerField(db_column='IdentityCode', unique=True)  # Field name made lowercase.
    countriesimage = models.CharField(db_column='CountriesImage', max_length=100, db_collation='und-x-icu', blank=True, null=True)  # Field name made lowercase.
    isactive = models.SmallIntegerField(db_column='IsActive')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=50, db_collation='und-x-icu')  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=50, db_collation='und-x-icu', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=50, db_collation='und-x-icu', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'countries'


class Currencies(models.Model):
    currencyid = models.AutoField(db_column='CurrencyId', primary_key=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=100, db_collation='und-x-icu')  # Field name made lowercase.
    code = models.CharField(db_column='Code', unique=True, max_length=100, db_collation='und-x-icu')  # Field name made lowercase.
    symbol = models.CharField(db_column='Symbol', unique=True, max_length=100, db_collation='und-x-icu')  # Field name made lowercase.
    currenciesimage = models.CharField(db_column='CurrenciesImage', max_length=100, db_collation='und-x-icu', blank=True, null=True)  # Field name made lowercase.
    isactive = models.SmallIntegerField(db_column='IsActive')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=50, db_collation='und-x-icu')  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=50, db_collation='und-x-icu', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=50, db_collation='und-x-icu', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'currencies'


class Departaments(models.Model):
    departamentid = models.IntegerField(db_column='DepartamentId', primary_key=True)  # Field name made lowercase.
    cityid = models.ForeignKey(Cities, models.DO_NOTHING, db_column='CityId')  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=100, db_collation='und-x-icu')  # Field name made lowercase.
    isactive = models.SmallIntegerField(db_column='IsActive')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=50, db_collation='und-x-icu')  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=50, db_collation='und-x-icu', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=50, db_collation='und-x-icu', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'departaments'


class Genders(models.Model):
    genderid = models.IntegerField(db_column='GenderId', primary_key=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=100, db_collation='und-x-icu')  # Field name made lowercase.
    isactive = models.SmallIntegerField(db_column='IsActive')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=50, db_collation='und-x-icu')  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=50, db_collation='und-x-icu', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=50, db_collation='und-x-icu', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'genders'


class Items(models.Model):
    itemid = models.AutoField(db_column='ItemId', primary_key=True)  # Field name made lowercase.
    companyid = models.ForeignKey(Companies, models.DO_NOTHING, db_column='CompanyId', blank=True, null=True)  # Field name made lowercase.
    parentid = models.ForeignKey('self', models.DO_NOTHING, db_column='ParentId', blank=True, null=True)  # Field name made lowercase.
    itemtypeid = models.ForeignKey('Itemtypes', models.DO_NOTHING, db_column='ItemTypeId', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=100, db_collation='und-x-icu')  # Field name made lowercase.
    isactive = models.SmallIntegerField(db_column='IsActive')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=50, db_collation='und-x-icu')  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=50, db_collation='und-x-icu', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=50, db_collation='und-x-icu', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'items'


class Itemtypes(models.Model):
    itemtypeid = models.IntegerField(db_column='ItemTypeId', primary_key=True)  # Field name made lowercase.
    companyid = models.ForeignKey(Companies, models.DO_NOTHING, db_column='CompanyId')  # Field name made lowercase.
    parentid = models.ForeignKey('self', models.DO_NOTHING, db_column='ParentId', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=100, db_collation='und-x-icu')  # Field name made lowercase.
    isactive = models.SmallIntegerField(db_column='IsActive')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=50, db_collation='und-x-icu')  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=50, db_collation='und-x-icu', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=50, db_collation='und-x-icu', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'itemtypes'


class Locations(models.Model):
    locationid = models.AutoField(db_column='LocationId', primary_key=True)  # Field name made lowercase.
    companyid = models.ForeignKey(Companies, models.DO_NOTHING, db_column='CompanyId')  # Field name made lowercase.
    parentid = models.ForeignKey('self', models.DO_NOTHING, db_column='ParentId', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=100, db_collation='und-x-icu')  # Field name made lowercase.
    ccode = models.CharField(db_column='CCode', unique=True, max_length=5, db_collation='und-x-icu')  # Field name made lowercase.
    ncode = models.SmallIntegerField(db_column='NCode', unique=True)  # Field name made lowercase.
    isroot = models.SmallIntegerField(db_column='IsRoot')  # Field name made lowercase.
    isactive = models.SmallIntegerField(db_column='IsActive')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=50, db_collation='und-x-icu')  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=50, db_collation='und-x-icu', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=50, db_collation='und-x-icu', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'locations'


class Notes(models.Model):
    noteid = models.AutoField(db_column='NoteId', primary_key=True)  # Field name made lowercase.
    companyid = models.ForeignKey(Companies, models.DO_NOTHING, db_column='CompanyId')  # Field name made lowercase.
    entitytype = models.CharField(db_column='EntityType', max_length=100, db_collation='und-x-icu', blank=True, null=True)  # Field name made lowercase.
    rowid = models.BigIntegerField(db_column='RowId')  # Field name made lowercase.
    text = models.CharField(db_column='Text', max_length=2000, db_collation='und-x-icu')  # Field name made lowercase.
    isactive = models.SmallIntegerField(db_column='IsActive')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=50, db_collation='und-x-icu')  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=50, db_collation='und-x-icu', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=50, db_collation='und-x-icu', blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=100, db_collation='und-x-icu')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'notes'


class Partners(models.Model):
    partnerid = models.AutoField(db_column='PartnerId', primary_key=True)  # Field name made lowercase.
    contactid = models.ForeignKey(Contacts, models.DO_NOTHING, db_column='ContactId')  # Field name made lowercase.
    isactive = models.SmallIntegerField(db_column='IsActive')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=50, db_collation='und-x-icu')  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=50, db_collation='und-x-icu', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=50, db_collation='und-x-icu', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'partners'


class Postalcodes(models.Model):
    postalcodeid = models.IntegerField(db_column='PostalCodeId', primary_key=True)  # Field name made lowercase.
    departamentid = models.ForeignKey(Departaments, models.DO_NOTHING, db_column='DepartamentId')  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=10, db_collation='und-x-icu')  # Field name made lowercase.
    isactive = models.SmallIntegerField(db_column='IsActive')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=50, db_collation='und-x-icu')  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=50, db_collation='und-x-icu', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=50, db_collation='und-x-icu', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'postalcodes'


class Resources(models.Model):
    resourceid = models.AutoField(db_column='ResourceId', primary_key=True)  # Field name made lowercase.
    contactid = models.ForeignKey(Contacts, models.DO_NOTHING, db_column='ContactId')  # Field name made lowercase.
    hiredate = models.DateTimeField(db_column='HireDate', blank=True, null=True)  # Field name made lowercase.
    isactive = models.SmallIntegerField(db_column='IsActive')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=50, db_collation='und-x-icu')  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=50, db_collation='und-x-icu', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=50, db_collation='und-x-icu', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'resources'


class States(models.Model):
    stateid = models.IntegerField(db_column='StateId', primary_key=True)  # Field name made lowercase.
    countryid = models.ForeignKey(Countries, models.DO_NOTHING, db_column='CountryId')  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=100, db_collation='und-x-icu')  # Field name made lowercase.
    iso_3166_numeric_1 = models.CharField(db_column='Iso_3166_numeric_1', unique=True, max_length=3, db_collation='und-x-icu')  # Field name made lowercase.
    iso_3166_alpha_2 = models.CharField(db_column='Iso_3166_alpha_2', unique=True, max_length=3, db_collation='und-x-icu')  # Field name made lowercase.
    iso_3166_alpha_3 = models.CharField(db_column='Iso_3166_alpha_3', unique=True, max_length=5, db_collation='und-x-icu')  # Field name made lowercase.
    statesimage = models.CharField(db_column='StatesImage', max_length=100, db_collation='und-x-icu', blank=True, null=True)  # Field name made lowercase.
    isactive = models.SmallIntegerField(db_column='IsActive')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=50, db_collation='und-x-icu')  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=50, db_collation='und-x-icu', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=50, db_collation='und-x-icu', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'states'


class Supplieritems(models.Model):
    supplieritemid = models.AutoField(db_column='SupplierItemId', primary_key=True)  # Field name made lowercase.
    supplierid = models.ForeignKey('Suppliers', models.DO_NOTHING, db_column='SupplierId')  # Field name made lowercase.
    itemid = models.ForeignKey(Items, models.DO_NOTHING, db_column='ItemId')  # Field name made lowercase.
    isactive = models.SmallIntegerField(db_column='IsActive')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=50, db_collation='und-x-icu')  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=50, db_collation='und-x-icu', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=50, db_collation='und-x-icu', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'supplieritems'
        unique_together = (('supplierid', 'itemid'),)


class Supplierplanitems(models.Model):
    supplierplanitemid = models.AutoField(db_column='SupplierPlanItemId', primary_key=True)  # Field name made lowercase.
    supplierplanid = models.ForeignKey('Supplierplans', models.DO_NOTHING, db_column='SupplierPlanId')  # Field name made lowercase.
    supplieritemid = models.ForeignKey(Supplieritems, models.DO_NOTHING, db_column='SupplierItemId')  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=100, db_collation='und-x-icu')  # Field name made lowercase.
    order = models.SmallIntegerField(db_column='Order')  # Field name made lowercase.
    percentagecovered = models.DecimalField(db_column='PercentageCovered', max_digits=4, decimal_places=2)  # Field name made lowercase.
    amountcovered = models.DecimalField(db_column='AmountCovered', max_digits=18, decimal_places=2)  # Field name made lowercase.
    isactive = models.SmallIntegerField(db_column='IsActive')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=50, db_collation='und-x-icu')  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=50, db_collation='und-x-icu', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=50, db_collation='und-x-icu', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'supplierplanitems'
        unique_together = (('supplierplanid', 'supplieritemid'),)


class Supplierplans(models.Model):
    supplierplanid = models.AutoField(db_column='SupplierPlanId', primary_key=True)  # Field name made lowercase.
    supplierid = models.ForeignKey('Suppliers', models.DO_NOTHING, db_column='SupplierId')  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=100, db_collation='und-x-icu')  # Field name made lowercase.
    order = models.SmallIntegerField(db_column='Order')  # Field name made lowercase.
    isdefault = models.IntegerField(db_column='IsDefault')  # Field name made lowercase.
    isactive = models.SmallIntegerField(db_column='IsActive')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=50, db_collation='und-x-icu')  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=50, db_collation='und-x-icu', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=50, db_collation='und-x-icu', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'supplierplans'


class Suppliers(models.Model):
    supplierid = models.AutoField(db_column='SupplierId', primary_key=True)  # Field name made lowercase.
    contactid = models.ForeignKey(Contacts, models.DO_NOTHING, db_column='ContactId')  # Field name made lowercase.
    isactive = models.SmallIntegerField(db_column='IsActive')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=50, db_collation='und-x-icu')  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=50, db_collation='und-x-icu', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=50, db_collation='und-x-icu', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'suppliers'
