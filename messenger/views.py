from django.views.generic import TemplateView, ListView, DetailView

from messenger.models import Message


# --------------------------Home view-----------------------------
class HomeView(TemplateView):
    template_name = "messenger/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["num_messages"] = Message.objects.count()

        return context


# --------------------------List View =================================
class MessageListView(ListView):
    model = Message


# --------------------------Detail View ================================
class MessageDetailView(DetailView):
    model = Message
