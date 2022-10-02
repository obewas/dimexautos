from django.shortcuts import render, get_object_or_404
from .models import *
from .forms import *
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, DetailView

# Create your views here.


class CarListView(ListView):

    model = Car
    template_name = 'car/carList.html'


class CarCreateView(CreateView):

	model = Car
	fields = '__all__'
	template_name = 'car/createCar.html'

	success_url ="/"

class CarUpdateView(UpdateView):

	model = Car
	fields = '__all__'
	template_name = 'car/updateCar.html'
	
	success_url ="/"

class CarDeleteView(DeleteView):

	model = Car
	template_name = 'car/deleteCar.html'

	success_url ="/"


class CarDetailView(DetailView):
	
	model = Car
	template_name = 'car/detailCar.html'

################################################################################################################

class CarCostView(CreateView):

	model = Cost
	fields = '__all__'
	template_name = 'car/carCost.html'

class CostListView(ListView):

    model = Cost
    template_name = 'car/costList.html'
    

class CostUpdateView(UpdateView):

	model = Cost
	fields = '__all__'
	template_name = 'car/updateCost.html'
	
	success_url ="/"

class CostDetailView(DetailView):
	
	model = Cost
	template_name = 'car/detailCost.html'

class CostDeleteView(DeleteView):

	model = Cost
	template_name = 'car/deleteCost.html'

	success_url ="/"

##############################################################################################################

class CarProfitView(CreateView):

	model = Profit
	fields = '__all__'
	template_name = 'car/carProfit.html'

	success_url ="/"


	def get_context_data(self,pk, *args, **kwargs):
		context = super().get_context_data(*args, **kwargs)
		pk = self.kwargs['pk']
		profit = get_object_or_404(Profit, pk=pk)
		context['profit'] = profit
		return context


