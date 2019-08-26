from django.shortcuts import render


def home_page(request):
    return render(
        request,
        'home-jobs.html',
        {
        },

        # context_instance=RequestContext(request)
    )
