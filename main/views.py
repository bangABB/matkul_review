from django.shortcuts import render
def show_main(request):
    
    context = [
        {
            'name': 'SDA',
            'class': 'A',
            'amount': '101',
            'deskripsi': 'matkul paling susah sejagat raya, tungguin abis uts deh',
            'nilai': 'B-',
        },
        {
            'name': 'Statprob',
            'class': 'B',
            'amount': '70',
            'deskripsi': 'statprob keren',
            'nilai': 'C',
        },
    ]

    user_data = {
        'nama_user': 'Masabil Arraya Muhammad',
        'kelas_user': 'PBP A',
        'NPM' : "2206082101"
    }

    apllication_data = {
        'nama_aplikasi':'REVIEW MATKUL',
        'tanggal_dibuat':'13/09/2023'
    }

    return render(request, "main.html", {"view": context, "user_data": user_data, "application_data":apllication_data})