# from django.http import HttpResponse
#
# from django.shortcuts import render, redirect
#
# def index(request):
#     return HttpResponse("Home Page")
#
# def students(request):
#     students = Talaba.objects.all()
#     if request.method == "POST":
#         form = TalabaForm(request.POST)
#         if form.is_valid():
#             Talaba.objects.creat(
#                 ism=form.cleaned_data.get('ism'),
#                 guruh=form.cleaned_data.get('guruh'),
#                 kurs=form.cleaned_data.get('kurs'),
#                 kitob_soni=form.cleaned_data.get('kitob_soni'),
#             )
#         return redirect('/students/')
#     context = {
#         'students': students,
#         'form':
#     }
#     return render(request, 'students.html', context)
#
# def talaba_tahrirlash(request, pk):
#     talaba = Talaba.objects.get(id=pk)
#     if request.method == 'POST':
#         form = TalabaForm(request.POST, instance=talaba)
#         if form.is_valid():
#             form.save()
#         return redirect('/students/')
#     context = {
#         'talaba': talaba,
#         'form': TalabaForm(instance=talaba)
#     }
#     return render(request, 'talaba_tahrirlash.html', context)
