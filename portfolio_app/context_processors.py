from .models import Profile

def sidebar_context(request):
    profile = Profile.objects.first()  # İlk profili çekiyoruz (Singleton)
    return {'profile': profile}
