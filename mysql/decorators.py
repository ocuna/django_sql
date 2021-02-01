from django.contrib.auth.decorators import user_passes_test

def group_required(*group_names):
    """Requires user membership in at least one of the groups passed in."""
    def in_groups(u):
        # assert False, u.is_authenticated
        # assert False, u.groups.filter(name__in=group_names)
        if u.is_authenticated:
            if bool(u.groups.filter(name__in=group_names)) | u.is_superuser:
                return True
        return False

    # I'm currenlty using the url package: 
    # https://stackoverflow.com/questions/36177769/django-groups-and-permissions
    # https://stackoverflow.com/questions/29673549/method-decorator-with-login-required-and-permission-required
    return user_passes_test(in_groups, login_url='/accounts/403')