from django.urls import path

from core import settings
from erp.views import cria_funcionario, lista_funcionarios, busca_funcionario_por_id, atualiza_funcionario, \
    HomeView, ProdutoCreateView, ProdutoListView, ProdutoUpdateView, ProdutoDetailView, ProdutoDeleteView, \
    VendaCreateView, VendaListView, VendaDetailView, VendaUpdateView, VendaDeleteView, ErpLoginView, DashboardView, \
    ErpLogoutView
from django.conf.urls.static import static

app_name = 'erp'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),

    # Login
    path('login/', ErpLoginView.as_view(), name='login'),

    # Logout
    path('logout/', ErpLogoutView.as_view(), name='logout'),

    path('dashboard/', DashboardView.as_view(), name='dashboard'),

    # Funcionario
    path('funcionarios/', lista_funcionarios, name='lista_funcionarios'),
    path('funcionarios/novo', cria_funcionario, name='cria_funcionario'),
    path('funcionarios/detalhe/<pk>', busca_funcionario_por_id, name='busca_funcionario_por_id'),
    path('funcionarios/atualiza/<pk>', atualiza_funcionario, name='atualiza_funcionario'),

    # Produtos
    path('produtos/', ProdutoListView.as_view(), name='lista_produto'),
    path('produtos/novo', ProdutoCreateView.as_view(), name='cria_produto'),
    path('produtos/detalhe/<pk>', ProdutoDetailView.as_view(), name='detalhes_produto'),
    path('produtos/atualiza/<slug>', ProdutoUpdateView.as_view(), name='atualiza_produto'),
    path('produtos/deleta/<slug>', ProdutoDeleteView.as_view(), name='deleta_produto'),

    # Vendas
    path('vendas/', VendaListView.as_view(), name='lista_venda'),
    path('vendas/novo', VendaCreateView.as_view(), name='cria_venda'),
    path('vendas/detalhe/<pk>', VendaDetailView.as_view(), name='detalhes_venda'),
    path('vendas/atualiza/<pk>', VendaUpdateView.as_view(), name='atualiza_venda'),
    path('vendas/deleta/<pk>', VendaDeleteView.as_view(), name='deleta_venda'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

