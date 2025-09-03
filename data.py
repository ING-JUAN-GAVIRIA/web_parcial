from datetime import date

events = [
    {
        "id": 1,
        "title": "Conferencia de Python",
        "slug": "conferencia-python",
        "description": "desarrollo web con Flask.",
        "date": "2025-09-15",
        "time": "14:00",
        "location": "Auditorio Principal",
        "category": "Tecnología",
        "max_attendees": 50,
        "attendees": [
            {"name": "Juan Gaviria", "email": "juan@gmail.com"}
        ],
        "featured": True
    },
    {
        "id": 2,
        "title": "Partido Futbol",
        "slug": "partido-interfacultades",
        "description": "Torneo deportivo amistoso entre facultades.",
        "date": "2025-09-10",
        "time": "10:00",
        "location": "Cancha Central",
        "category": "Deportivo",
        "max_attendees": 30,
        "attendees": [],
        "featured": False
    },
]

categories = ["Tecnología", "Académico", "Cultural", "Deportivo", "Social"]

def next_id():
    if not events:
        return 1
    return max(e["id"] for e in events) + 1
