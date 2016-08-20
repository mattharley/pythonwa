from django.shortcuts import render_to_response


def home_page(request):
    return render_to_response(
        'home-jobs.html',
        {
        },

        # context_instance=RequestContext(request)
    )
