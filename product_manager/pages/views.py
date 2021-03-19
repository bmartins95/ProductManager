from django.shortcuts import render

def contact_view(request, *args, **kwargs):
    context = {
        'my_name': "Bruno Martins",
        'my_email': "bmartins.eng@gmail.com",
        'my_phone_ddd': 48,
        'my_phone_number': 996435380
    }
    return render(request, "contact.html", context)
