from django.shortcuts import render
from .models import kategori_db, diziler_db

dizi_kategori=["Bilim kurgu","Macera", "Dram", "Aksiyon"]
dizi_listesi=[
    {
        "id": 1,
        "dizi_adi": "Dizi 1",
        "dizi_aciklama": "Dizi 1 Açıklama",
        "dizi_konusu": "Dizi 1 Konusu",
        "dizi_imbd": "7.6",
        "dizi_gorsel": "indir.jpeg",
        "anasayfa": True
    },
    {
        "id": 2,
        "dizi_adi": "Dizi 2",
        "dizi_aciklama": "Dizi 2 Açıklama",
        "dizi_konusu": "Dizi 2 Konusu",
        "dizi_imbd": "3.6",
        "dizi_gorsel": "indir2.jpeg",
        "anasayfa": True
    },
    {   
        "id": 3,
        "dizi_adi": "Dizi 3",
        "dizi_aciklama": "Dizi 3 Açıklama",
        "dizi_konusu": "Dizi 3 Konusu",
        "dizi_imbd": "6.2",
        "dizi_gorsel": "indir3.jpeg",
        "anasayfa": False
    },
    {   
        "id": 4,
        "dizi_adi": "Dizi 4",
        "dizi_aciklama": "Dizi 4 Açıklama",
        "dizi_konusu": "Dizi 4 Konusu",
        "dizi_imbd": "9.6",
        "dizi_gorsel": "indir4.jpeg",
        "anasayfa": False
    },
]

def index(requests):
    data={
        "kategoriler": kategori_db.objects.all(),
        "dizi_listesi": diziler_db.objects.all(),
    };
    return render(requests, "index.html", data)

def diziler(requests):
    data={
        "kategoriler": kategori_db.objects.all(),
        "dizi_listesi": diziler_db.objects.all(),
    };
    return render(requests, "diziler.html", data)

def dizi_detay(requests, id):
    data={
        "dizim": diziler_db.objects.get(id=id)
    };
    return render(requests, "dizi_detay.html",data)

def kategoriler(requests, id):
    data={
        "diziler": diziler_db.objects.get(id=id)
    };
    return render(requests, "kategoriler.html", data)