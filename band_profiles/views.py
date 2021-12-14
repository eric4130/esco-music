from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import BandProfile
from .forms import *

# Create your views here.

def index(request):
    return render(request, 'band_profiles/index.html')


def profiles(request):
    profiles = BandProfile.objects.order_by('bandName')
    context = {'profiles': profiles}
    return render(request, 'band_profiles/profiles.html', context)


def profile(request, profile_id):
    profile = BandProfile.objects.get(id=profile_id)
    context = {'profile': profile}
    return render(request, 'band_profiles/profile.html', context)

@login_required
def new_profile(request):
    if request.method !='POST':
        #no data, blank form
        form = ProfileForm()
    else:
        #data submitted, process data
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            new_profile = form.save(commit=False)
            new_profile.owner = request.user
            new_profile.save()
            return redirect('band_profiles:profiles')
    #display a blank or invalid form
    context = {'form': form}
    return render(request, 'band_profiles/new_profile.html', context)


@login_required
def edit_profile(request, profile_id):
    #edit an existing profile
    profile = BandProfile.objects.get(id=profile_id)
    name = profile.bandName
    summary = profile.bandSummary
    image = profile.bandImage
    if profile.owner != request.user:
        raise Http404

    if request.method != 'POST':
        #initial request, pre-fill with current profile
        form = ProfileForm(instance=profile)
    else:
        #POST data submitted, process data
        form=ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('band_profiles:profile', profile_id=profile.id)
    context = {'profile': profile, 'name': name, 'summary': summary, 'image': image, 'form': form}
    return render(request, 'band_profiles/edit_profile.html', context)

