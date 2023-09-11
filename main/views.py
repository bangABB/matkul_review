from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Kelas SDA',
        'class': 'Kelas A ganteng',
        'jumlah':'101',
        'deskripsi':'matkul paling susah sejagat raya, tungguin abis uts deh',
        'difficulty':'halooo cuma 11/10 kok',
        'nilai' : 'B-'
    }

    return render(request, "main.html", context)
# Create your views here.
