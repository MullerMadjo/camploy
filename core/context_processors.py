from cv.models import CV

def user_cv(request):
    if request.user.is_authenticated:
        try:
            return {'user_cv': CV.objects.filter(user=request.user).first()}
        except Exception:
            return {'user_cv': None}
    return {'user_cv': None}
