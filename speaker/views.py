from django.shortcuts import render

# Create your views here.
speakers = [
    {
        "id": 1,
        "name": "John Smith",
        "topic": "Artificial Intelligence",
        "experience": "5 years",
        "rating": 4.8,
        "contact": "john.smith@example.com"
    },
    {
        "id": 2,
        "name": "Emily Johnson",
        "topic": "Data Science",
        "experience": "3 years",
        "rating": 4.5,
        "contact": "emily.johnson@example.com"
    },
    {
        "id": 3,
        "name": "Michael Davis",
        "topic": "Blockchain",
        "experience": "2 years",
        "rating": 4.2,
        "contact": "michael.davis@example.com"
    },
    {
        "id": 4,
        "name": "Sarah Wilson",
        "topic": "Web Development",
        "experience": "4 years",
        "rating": 4.9,
        "contact": "sarah.wilson@example.com"
    },
    {
        "id": 5,
        "name": "Jennifer Lee",
        "topic": "Mobile App Development",
        "experience": "6 years",
        "rating": 4.7,
        "contact": "jennifer.lee@example.com"
    },
    {
        "id": 6,
        "name": "Robert Thompson",
        "topic": "Cloud Computing",
        "experience": "3 years",
        "rating": 4.4,
        "contact": "robert.thompson@example.com"
    }
]

def speaker_list(request):
    return render(request, 'speakers.html', {'speakers': speakers})

def speaker_details(request, id):
    speaker = list(filter(lambda speaker: speaker['id'] == id, speakers))[0]
    if not speaker:
        return render(request, 'Not such Speaker')
    return render(request, 'speaker_details.html', {'speaker': speaker})

def delete_speaker(request, id):
    speaker = list(filter(lambda s: s['id'] == id, speakers))[0]
    speakers.remove(speaker)
    return render(request, 'speakers.html', {'speakers': speakers})

    