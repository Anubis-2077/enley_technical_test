from typing import Any

from .models import Contracts, RecurrentContracts
from django.views.generic import ListView
from django.core.paginator import Paginator
from django.db.models import Subquery



class ContractListView(ListView):
    """La vista ContractListView se encarga de listar contratos que cumplen con los siguientes criterios:
        -Tienen una fecha de inicio en el año 2020.
        -El nombre del usuario contiene "Jho".
        -No están en la tabla de contratos recurrentes (RecurrentContracts).
    Además, la vista implementa paginación, mostrando 25 contratos por página. 
    Utiliza select_related para mejorar la eficiencia de las consultas al incluir datos relacionados de la tabla User."""
    
    model = Contracts
    template_name = 'technical_test/contract_list.html'
    context_object_name = 'contracts'
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)

        page_size = 25  
        page_number = self.request.GET.get('page', 1)

        # Filtrar contratos no recurrentes ANTES de paginar
        non_recurrent_contracts = Contracts.objects.filter(
            start_date__year=2020, user__name='Jho'
        ).exclude(
            id__in=Subquery(RecurrentContracts.objects.values('contract_id'))
        ).select_related('user').order_by('start_date')

        paginator = Paginator(non_recurrent_contracts, page_size)  # Paginar los contratos ya filtrados
        page_obj = paginator.get_page(page_number)

        context['contracts'] = page_obj.object_list
        context['page_obj'] = page_obj
        return context
        
        
        
        
        
        


