from ..models.database import Hotel, Package


def seed_hotel():
    return dict(
        hotel1=Hotel(
            name="Hoe Hotel",
            price=100,
            description="Best Hotel to visit at night",
            photos=[],
            address="7,Race Course Road,Delhi",
            latitude=72.2222,
            longitude=18.2222,
        ).save(),
        hotel2=Hotel(
            name="Moe Hotel",
            price=1000,
            description="Cutest Hotel",
            photos=[],
            address="7,Face Course Road,Delhi",
            latitude=72.2220,
            longitude=18.2220,
        ).save(),
        hotel3=Hotel(
            name="Joe Hotel",
            price=200,
            description="Best Hotel which does not waste food",
            photos=[],
            address="7,Pizza Course Road,Mumbai",
            latitude=72.2211,
            longitude=18.2211,
        ).save(),
        hotel5=Hotel(
            name="Bae Hotel",
            price=4000,
            description="Best Hotel with Music",
            photos=[],
            address="7,Race Music Road,Mumbai",
            latitude=72.1222,
            longitude=18.1222,
        ).save(),
        hotel6=Hotel(
            name="Koi Hotel",
            price=1000,
            description="Best Underrated Hotel",
            photos=[],
            address="7,Race base Road,Pune",
            latitude=72.7222,
            longitude=18.7222,
        ).save(),
        hotel7=Hotel(
            name="Voi Hotel",
            price=700,
            description="Best Hotel Famous",
            photos=[],
            address="7,Race Case Road,Jaipur",
            latitude=72.8222,
            longitude=18.8222,
        ).save(),
        hotel8=Hotel(
            name="Toi Hotel",
            price=800,
            description="Could have been Best Hotel",
            photos=[],
            address="7,Race Maze Road,Pune",
            latitude=72.5222,
            longitude=18.5222,
        ).save(),
        hotel9=Hotel(
            name="Suzy Hotel",
            price=300,
            description="Famous Hotel Which suzy lived in",
            photos=[],
            address="7,Race suzy Road,Pune",
            latitude=72.1222,
            longitude=18.2222,
        ).save(),
        hotel10=Hotel(
            name="Shu Shan Hotel",
            price=7000,
            description="Hotel Based on Shu Shan Era",
            photos=[],
            address="7,Source Course Road,Mumbai",
            latitude=72.9222,
            longitude=18.2222,
        ).save(),
        hotel11=Hotel(
            name="Harichandra Hotel",
            price=7000,
            description="Best Hotel lived by Hari",
            photos=[],
            address="7,Morse Course Road,Delhi",
            latitude=72.2222,
            longitude=18.9222,
        ).save(),
        hotel12=Hotel(
            name="Vikas Hotel",
            price=2000,
            description="Best Hotel by Vikas Kanna",
            photos=[],
            address="7,Dorse Course Road,Delhi",
            latitude=72.6222,
            longitude=18.6222,
        ).save(),
        hotel13=Hotel(
            name="Sanjiv Hotel",
            price=100,
            description="Best Hotel by Sanjiv Kapur",
            photos=[],
            address="7,Khana Kazana Road,Mumbai",
            latitude=72.0222,
            longitude=18.0222,
        ).save(),
        hotel14=Hotel(
            name="Ranveer Hotel",
            price=100,
            description="Best Hotel by Ranveer",
            photos=[],
            address="7,Race Taste Road,Delhi",
            latitude=72.55222,
            longitude=18.992222,
        ).save(),
        hotel15=Hotel(
            name="Brar Hotel",
            price=100,
            description="Best Hotel by Ranveer",
            photos=[],
            address="7,Taste Course Road,Delhi",
            latitude=72.888,
            longitude=18.888,
        ).save(),
        hotel16=Hotel(
            name="Bae Hotel",
            price=1000,
            description="Best Couple Friendly Hotel",
            photos=[],
            address="7,Race Face Road,Mumbai",
            latitude=72.2223,
            longitude=18.2223,
        ).save(),
    )


def seed_package():
    return dict(
        package1=Package(
            name="monsoon mumbai",
            price=110,
            description="Enjoy monsoon of mumbai at your pleasure",
            photos=[
                "https://picsum.photos/1000",
                "https://picsum.photos/1002",
                "https://picsum.photos/1003",
                "https://picsum.photos/1004",
            ],
            itinerary={},
        ).save(),
        package2=Package(
            name="majistic mumbai",
            price=15,
            description="The glory and majisticism of mumbai",
            photos=[
                "https://picsum.photos/1005",
                "https://picsum.photos/1006",
                "https://picsum.photos/1007",
                "https://picsum.photos/1008",
            ],
            itinerary={},
        ).save(),
        package3=Package(
            name="aamchi mumbai",
            price=110,
            description="Enjoy your mumbai",
            photos=[
                "https://picsum.photos/1009",
                "https://picsum.photos/1010",
                "https://picsum.photos/1011",
                "https://picsum.photos/1012",
            ],
            itinerary={},
        ).save(),
        package4=Package(
            name="Royalty of Jaipur",
            price=200,
            description="Experincy the royalty and plushiness of jaipur",
            photos=[
                "https://picsum.photos/1013",
                "https://picsum.photos/1014",
                "https://picsum.photos/1015",
                "https://picsum.photos/1016",
            ],
            itinerary={},
        ).save(),
        package5=Package(
            name="Dil se Dilli dekho",
            price=500,
            description="See the dehli for what it is, its heart",
            photos=[
                "https://picsum.photos/1017",
                "https://picsum.photos/1018",
                "https://picsum.photos/1019",
                "https://picsum.photos/1020",
            ],
            itinerary={},
        ).save(),
        package6=Package(
            name="Have Pleasure in Pune",
            price=100,
            description="Have pleasure of reliving the marathas of pune",
            photos=[
                "https://picsum.photos/1021",
                "https://picsum.photos/1022",
                "https://picsum.photos/1023",
                "https://picsum.photos/1024",
            ],
            itinerary={},
        ).save(),
    )
