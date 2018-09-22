from peewee import *

database = SqliteDatabase('code/data/better_breakfasts_complete.db', **{})

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class Listing(BaseModel):
    availability_365 = TextField(null=True)
    calculated_host_listings_count = TextField(null=True)
    host = TextField(column_name='host_id', null=True)
    host_name = TextField(null=True)
    id = TextField(null=True)
    last_review = TextField(null=True)
    latitude = TextField(null=True)
    longitude = TextField(null=True)
    minimum_nights = TextField(null=True)
    name = TextField(null=True)
    neighbourhood = TextField(null=True)
    number_of_reviews = TextField(null=True)
    price = TextField(null=True)
    reviews_per_month = TextField(null=True)
    room_type = TextField(null=True)

    class Meta:
        table_name = 'listing'
        primary_key = False

class Reviews(BaseModel):
    comments = TextField(null=True)
    date = TextField(null=True)
    id = TextField(null=True)
    listing = TextField(column_name='listing_id', null=True)
    reviewer = TextField(column_name='reviewer_id', null=True)
    reviewer_name = TextField(null=True)

    class Meta:
        table_name = 'reviews'
        primary_key = False

class Venue(BaseModel):
    fid = CharField()
    latitude = DecimalField()
    longitude = DecimalField()
    name = CharField()
    price = IntegerField(null=True)
    rating = FloatField(null=True)
    ratingsignals = IntegerField(column_name='ratingSignals', null=True)
    url = CharField(null=True)

    class Meta:
        table_name = 'venue'

class Vicinity(BaseModel):
    listing = ForeignKeyField(column_name='listing_id', field='id', model=Listing)
    venue = ForeignKeyField(column_name='venue_id', field='id', model=Venue)

    class Meta:
        table_name = 'vicinity'

