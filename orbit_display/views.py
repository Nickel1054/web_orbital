from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from orbit_display.models import CelestialBody
from orbit_display.forms import CelestialBodiesChecked

# Create your views here.


# class OrbitVisPage(TemplateView):
#     template_name = 'orbit_home.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data()
#         context['planets'] = CelestialBody.objects.order_by('a')
#         return context
#
#
# def calculate_orbits(request):
#     if request.method == 'POST':
#         print()


class CheckedBodiesView(FormView):
    template_name = 'orbit_home.html'
    form_class = CelestialBodiesChecked
    success_url = '/plot/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['planets'] = CelestialBody.objects.order_by('a')
        return context

    def form_valid(self, form):
        form.show_checked()
        return super(CheckedBodiesView, self).form_valid(form)


class PlotView(TemplateView):
    template_name = 'orbit_plot.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['bodies'] = self.kwargs['objects']


def plot_orbits(request, objects):
    res = request.POST.getlist['check']
    return render(request, 'orbit_plot.html', {'result': res})

