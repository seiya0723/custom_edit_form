from django.shortcuts import render,redirect

from django.views import View
from .models import Topic
from .forms import TopicForm

class BbsView(View):

    def get(self, request, *args, **kwargs):

        topics  = Topic.objects.all()
        context = { "topics":topics }

        return render(request,"bbs/index.html",context)

    def post(self, request, *args, **kwargs):

        formset     = TopicForm(request.POST)

        if formset.is_valid():
            print("バリデーションOK")
            formset.save()
        else:
            print("バリデーションNG")

        return redirect("bbs:index")

index   = BbsView.as_view()

class BbsEditView(View):

    def get(self, request, pk, *args, **kwargs):

        return redirect("bbs:index")

    def post(self, request, pk, *args, **kwargs):

        instance    = Topic.objects.filter(id=pk).first()
        formset     = TopicForm(request.POST, instance=instance)

        if formset.is_valid():
            print("バリデーションOK")
            formset.save()
        else:
            print("バリデーションNG")

        return redirect("bbs:index")

edit   = BbsEditView.as_view()

