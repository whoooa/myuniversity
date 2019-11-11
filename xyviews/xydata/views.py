from django.shortcuts import render, HttpResponseRedirect, Http404, reverse
from xyviews.xydata.models import University
from xyapps.utils.common_b import get_p_data


def index(request):
    page = request.GET.get("page") or "1"
    universitys = University.objects.all()
    ptotal, p_list = get_p_data(universitys, page)
    context = {"universitys": p_list, "ptotal":ptotal, "page": page}
    return render(request, "myuniversity/index.html", context)

def uni_list(request):
    page = request.GET.get("page") or "1"
    universitys = University.objects.order_by("id")
    key = request.GET.get("key")
    if key:
        key = key.strip()
        universitys = universitys.filter(name__icontains=key)
    ptotal, p_list = get_p_data(universitys, page)
    context = {"universitys": p_list, "ptotal": ptotal, "page": page}
    return render(request, "myuniversity/uni_list.html", context)

def uni_detail(request, name):
    if not name:
        return Http404
    university = University.objects.get(name=name)
    context = {"university": university}
    return render(request, "myuniversity/uni_detail.html", context)

def link(request, url):
    if url:
        return HttpResponseRedirect(url)
    return Http404

def aboutus(request, uid):
    university = University.objects.get(uid=uid)
    context = {"university": university}
    return render(request, "myuniversity/aboutus.html", context)