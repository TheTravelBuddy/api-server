from neomodel import (
    ArrayProperty,
    BooleanProperty,
    DateProperty,
    DateTimeProperty,
    FloatProperty,
    IntegerProperty,
    RegexProperty,
    RelationshipFrom,
    RelationshipTo,
    StringProperty,
    StructuredNode,
    UniqueIdProperty,
    cardinality,
)

from ...helpers.conversion import str_enum_to_choices
from ...helpers.validation import (
    BusinessTypeEnum,
    GenderEnum,
    HotelAmenitiesEnum,
    MoodEnum,
    PackageAmenitiesEnum,
    ServicesEnum,
    TopicsEnum,
)
from .relations import (
    BookedRel,
    CommentedOnRel,
    LikesRel,
    OwnsRel,
    PackageDayRel,
    ReviewedRel,
    StayedAtRel,
    TaggedRel,
    VisitedRel,
)

GENDERS = str_enum_to_choices(GenderEnum)
MOODS = str_enum_to_choices(MoodEnum)
TOPICS = str_enum_to_choices(TopicsEnum)
SERVICES = str_enum_to_choices(ServicesEnum)
PACKAGE_AMENITIES = str_enum_to_choices(PackageAmenitiesEnum)
HOTEL_AMENITIES = str_enum_to_choices(HotelAmenitiesEnum)
BUSINESS_TYPE = str_enum_to_choices(BusinessTypeEnum)


class User(StructuredNode):
    uid = UniqueIdProperty()
    firebase_id = StringProperty()
    name = StringProperty(max_length=120, required=True)
    phone = RegexProperty(expression=r"^\+(\d){12}$", required=True)
    profile_picture = StringProperty(
        default="https://picsum.photos/201"  # TODO: get proper asset for new user
    )


class Traveller(User):
    gender = StringProperty(choices=GENDERS, required=True)
    dob = DateProperty(required=True)
    mood = StringProperty(choices=MOODS, default="M")

    likes_hotel = RelationshipTo("Hotel", "LIKES_HOTEL", model=LikesRel)
    likes_package = RelationshipTo("Package", "LIKES_PACKAGE", model=LikesRel)
    likes_city = RelationshipTo("City", "LIKES_CITY", model=LikesRel)
    likes_shop = RelationshipTo("Shop", "LIKES_SHOP", model=LikesRel)
    likes_attraction = RelationshipTo("Attraction", "LIKES_ATTRACTION", model=LikesRel)
    likes_blog = RelationshipTo("Blog", "LIKES_BLOG", model=LikesRel)

    has_hotel_booking = RelationshipTo("HotelBooking", "HAS_BOOKING", model=OwnsRel)
    has_package_booking = RelationshipTo("PackageBooking", "HAS_BOOKING", model=OwnsRel)

    reviewed_hotel = RelationshipTo("Hotel", "REVIEWED_HOTEL", model=ReviewedRel)
    reviewed_package = RelationshipTo("Package", "REVIEWED_PACKAGE", model=ReviewedRel)
    reviewed_city = RelationshipTo("City", "REVIEWED_CITY", model=ReviewedRel)
    reviewed_shop = RelationshipTo("Shop", "REVIEWED_SHOP", model=ReviewedRel)
    reviewed_attraction = RelationshipTo(
        "Attraction", "REVIEWED_ATTRACTION", model=ReviewedRel
    )

    visited_hotel = RelationshipTo("Hotel", "VISITED_HOTEL", model=VisitedRel)
    taken_package = RelationshipTo("Package", "TAKEN_PACKAGE", model=VisitedRel)
    visited_city = RelationshipTo("City", "VISITED_CITY", model=VisitedRel)
    visited_shop = RelationshipTo("Shop", "VISITED_SHOP", model=VisitedRel)
    visited_attraction = RelationshipTo(
        "Attraction", "VISITED_ATTRACTIONS", model=VisitedRel
    )

    read_blog = RelationshipTo("Blog", "READ_BLOG", model=VisitedRel)

    stayed_at_city = RelationshipTo("City", "STAYED_AT_CITY", model=StayedAtRel)
    stayed_at_hotel = RelationshipTo("Hotel", "STAYED_AT_HOTEL", model=StayedAtRel)

    author_of = RelationshipTo("Blog", "AUTHOR_OF", model=OwnsRel)

    commented_on = RelationshipTo("Blog", "COMMENTED_ON", model=CommentedOnRel)


class Business(User):
    business_type = StringProperty(choices=BUSINESS_TYPE)
    is_verified = BooleanProperty(default=False)
    address = StringProperty(max_length=512)
    latitude = FloatProperty()
    longitude = FloatProperty()


class Agency(Business):
    description = StringProperty()
    business_type = StringProperty(choices=BUSINESS_TYPE, default="TRAVEL_AGENCY")
    offers_package = RelationshipTo("Package", "OFFERS_PACKAGE", model=OwnsRel)


class ShopOwner(Business):
    business_type = StringProperty(choices=BUSINESS_TYPE, default="SHOP_OWNER")
    owns_shop = RelationshipTo("Shop", "OWNS_SHOP", model=OwnsRel)


class HotelOwner(Business):
    business_type = StringProperty(choices=BUSINESS_TYPE, default="HOTEL_OWNER")
    owns_hotel = RelationshipTo("Hotel", "OWNS_HOTEL", model=OwnsRel)


class Location(StructuredNode):
    uid = UniqueIdProperty()
    name = StringProperty(max_length=120, required=True)
    description = StringProperty(max_length=4096, required=True)
    latitude = FloatProperty(required=True)
    longitude = FloatProperty(required=True)
    photos = ArrayProperty(base_property=StringProperty(), default=[])
    is_in = RelationshipFrom("Blog", "IS_IN", model=TaggedRel)

    tagged_in_blog = RelationshipFrom("Blog", "TAGGED_LOCATION", model=TaggedRel)


class City(Location):
    liked_by = RelationshipFrom("Traveller", "LIKES_CITY", model=LikesRel)
    reviewed_by = RelationshipFrom("Traveller", "REVIEWED_CITY", model=ReviewedRel)

    stayed_by = RelationshipFrom("Traveller", "STAYED_AT_CITY", model=StayedAtRel)

    has_hotels = RelationshipFrom("Hotel", "LOCATED_IN", model=OwnsRel)
    has_packages = RelationshipFrom("PackageDay", "VISITS_CITY", model=OwnsRel)


class Attraction(Location):
    liked_by = RelationshipFrom("Traveller", "LIKES_ATTRACTION", model=LikesRel)
    reviewed_by = RelationshipFrom(
        "Traveller", "REVIEWED_ATTRACTION", model=ReviewedRel
    )

    visited_by = RelationshipFrom("Traveller", "VISITED_ATTRACTION", model=VisitedRel)


class Shop(Location):
    liked_by = RelationshipFrom("Traveller", "LIKES_SHOP", model=LikesRel)
    reviewed_by = RelationshipFrom("Traveller", "REVIEWED_SHOP", model=ReviewedRel)
    owned_by = RelationshipFrom("ShopOwner", "OWNS_SHOP", model=OwnsRel)

    visited_by = RelationshipFrom("Traveller", "VISITED_SHOP", model=VisitedRel)


class Blog(StructuredNode):
    uid = UniqueIdProperty()
    title = StringProperty(max_length=512, required=True)
    content = StringProperty(max_length=4096, required=True)
    published_on = DateTimeProperty(default_now=True)
    photos = ArrayProperty(base_property=StringProperty())

    authored_by = RelationshipFrom("Traveller", "AUTHOR_OF", model=OwnsRel)

    read_by = RelationshipFrom("Traveller", "READ_BLOG", model=VisitedRel)
    liked_by = RelationshipFrom("Traveller", "LIKES_BLOG", model=LikesRel)
    commented_by = RelationshipFrom("Traveller", "COMMENTED_ON", model=CommentedOnRel)

    tagged_topic = RelationshipTo("Topic", "TAGGED_TOPIC", model=TaggedRel)
    tagged_location = RelationshipTo("Location", "TAGGED_LOCATION", model=TaggedRel)


class Hotel(StructuredNode):
    uid = UniqueIdProperty()
    name = StringProperty(max_length=120, required=True)
    price = IntegerProperty(required=True)
    description = StringProperty(max_length=4096, required=True)
    photos = ArrayProperty(required=True, base_property=StringProperty())
    address = StringProperty(max_length=512, required=True)
    locality = StringProperty(required=True)
    postal_code = IntegerProperty(required=True)
    latitude = FloatProperty(required=True)
    longitude = FloatProperty(required=True)
    phone = RegexProperty(expression=r"^\+(\d){12}$", required=True)
    amenities = ArrayProperty(base_property=StringProperty(choices=HOTEL_AMENITIES))

    located_in = RelationshipTo(
        "City", "LOCATED_IN", model=OwnsRel, cardinality=cardinality.One
    )

    owned_by = RelationshipFrom("HotelOwner", "OWNS_HOTEL", model=OwnsRel)

    liked_by = RelationshipFrom("Traveller", "LIKES_HOTEL", model=LikesRel)

    has_booking = RelationshipFrom("HotelBooking", "FOR_HOTEL", model=OwnsRel)
    reviewed_by = RelationshipFrom("Traveller", "REVIEWED_HOTEL", model=ReviewedRel)

    stayed_by = RelationshipFrom("Traveller", "STAYED_AT_HOTEL", model=StayedAtRel)


class Package(StructuredNode):
    uid = UniqueIdProperty()
    name = StringProperty(max_length=512, required=True)
    price = IntegerProperty(required=True)
    description = StringProperty(max_length=4096, required=True)
    photos = ArrayProperty(base_property=StringProperty())
    amenities = ArrayProperty(base_property=StringProperty(choices=PACKAGE_AMENITIES))

    has_day = RelationshipTo("PackageDay", "HAS_DAY", model=PackageDayRel)

    offered_by = RelationshipFrom("Agency", "OFFERS_PACKAGE", model=OwnsRel)
    has_booking = RelationshipFrom("PackageBooking", "FOR_HOTEL", model=OwnsRel)

    liked_by = RelationshipFrom("Traveller", "LIKES_PACKAGE", model=LikesRel)
    booked_by = RelationshipFrom("Traveller", "BOOKED_PACKAGE", model=BookedRel)
    reviewed_by = RelationshipFrom("Traveller", "REVIEWED_PACKAGE", model=ReviewedRel)


class PackageDay(StructuredNode):
    uid = UniqueIdProperty()
    title = StringProperty(required=True)
    description = StringProperty()

    visits_city = RelationshipTo("City", "VISITS_CITY", model=OwnsRel)
    of_package = RelationshipFrom("Package", "HAS_DAY", model=PackageDayRel)


class Topic(StructuredNode):
    uid = UniqueIdProperty()
    name = StringProperty(max_length=120, required=True)

    tagged_in_blog = RelationshipFrom("Blog", "TAGGED_TOPIC", model=TaggedRel)


class HotelBooking(StructuredNode):
    uid = UniqueIdProperty()
    booked_at = DateTimeProperty(default_now=True)
    booking_date = DateProperty(required=True)
    days = IntegerProperty(required=True)
    adults = IntegerProperty(required=True)
    children = IntegerProperty(required=True)
    rooms = IntegerProperty(required=True)

    by_user = RelationshipFrom("Traveller", "HAS_BOOKING", model=OwnsRel)
    for_hotel = RelationshipTo("Hotel", "FOR_HOTEL", model=OwnsRel)


class PackageBooking(StructuredNode):
    uid = UniqueIdProperty()
    booked_at = DateTimeProperty(default_now=True)
    booking_date = DateProperty(required=True)
    people = IntegerProperty(required=True)

    by_user = RelationshipFrom("Traveller", "HAS_BOOKING", model=OwnsRel)
    for_package = RelationshipTo("Package", "FOR_PACKAGE", model=OwnsRel)
