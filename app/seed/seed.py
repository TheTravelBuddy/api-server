from neomodel import db, install_all_labels, remove_all_labels

from .seed_blog_relation import (
    seed_blog_comment_relation,
    seed_blog_location_relation,
    seed_blog_relations,
    seed_blog_topic_relation,
)
from .seed_blogs import seed_blog
from .seed_bookings import seed_hotel, seed_package, seed_package_day
from .seed_locations import seed_attraction, seed_city
from .seed_relations import (
    seed_city_review_relation,
    seed_hotel_city_relations,
    seed_hotel_like_relation,
    seed_hotel_review_relation,
    seed_package_agency,
    seed_package_review_relation,
)
from .seed_topic import seed_topic
from .seed_users import seed_agency, seed_hotel_owner, seed_shop_owner, seed_traveller


def seed_db():
    print("Seeding DB...")
    db.cypher_query("MATCH (n) DETACH DELETE n")

    remove_all_labels()
    print("Installing Labels...")
    install_all_labels()

    with db.transaction:
        print("Seeding Nodes...")
        hotels = seed_hotel()
        packages = seed_package()
        seed_attraction()
        cities = seed_city()
        agencies = seed_agency()
        seed_hotel_owner()
        seed_shop_owner()
        travellers = seed_traveller()
        blogs = seed_blog()
        topics = seed_topic()
        seed_package_day(packages, cities)

        print("Seeding Relations...")
        seed_hotel_city_relations(hotels, cities)
        seed_blog_relations(travellers, blogs)
        seed_package_review_relation(travellers, packages)
        seed_city_review_relation(travellers, cities)
        seed_hotel_review_relation(travellers, hotels)
        seed_blog_topic_relation(topics, blogs)
        seed_blog_location_relation(
            cities, blogs
        )  # EXTRA: locations=cities+attractions
        seed_blog_comment_relation(travellers, blogs)
        seed_hotel_like_relation(travellers, hotels)
        seed_package_agency(packages, agencies)
        print("Done.")
