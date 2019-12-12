from django.shortcuts import *
from main.models import Asutus
from main.models import Tootaja

# Create your views here.
def home(request):
    args = {'page_url': request.get_full_path()}
    return render(request, 'main/index.html', args)
    

def vaatatootaja(request):
    tootajad = Tootaja.objects.all()
    args = {'tootajad': tootajad,
            'page_url': request.get_full_path()}
    return render(request, 'main/vaatatootaja.html', args)

def vaata_asutusi(request):
    asutused = Asutus.objects.all()
    args = {'asutused': asutused,
            'page_url': request.get_full_path()}
    return render(request, 'main/vaata_asutusi.html', args)
    

def lisatootaja(request):
    if request.method == "POST":
      asutus = request.POST.get('asutus', '')
      eesNimi = request.POST.get('eesNimi', '')
      perekonnaNimi = request.POST.get('perekonnaNimi', '')
      asutus = Asutus.objects.only('id').get(pk=asutus)
      Tootaja.objects.create(asutus=asutus, eesNimi=eesNimi, perekonnaNimi=perekonnaNimi)
    
    args = {'asutused' : Asutus.objects.all(),
            'page_url': request.get_full_path()}
    return render(request, 'main/lisatootaja.html', args)


def kustutatootaja(request):
  tootaja_id = request.GET.get('id', '')
  tootaja = Tootaja.objects.get(id=tootaja_id)
  tootaja.delete()

  return HttpResponseRedirect('/vaatatootaja')

def lisaasutus(request):
    if request.method == "POST":
      nimi = request.POST.get('nimi', '')
      avamise_kellaaeg = request.POST.get('poe_avamise_aeg', '')
      sulgemise_kellaaeg = request.POST.get('poe_sulgemise_aeg', '')
      Asutus.objects.create(nimi=nimi, avamise_kellaaeg=avamise_kellaaeg, sulgemise_kellaaeg=sulgemise_kellaaeg)

    args = {'page_url': request.get_full_path()}
    return render(request, 'main/lisaasutus.html', args)