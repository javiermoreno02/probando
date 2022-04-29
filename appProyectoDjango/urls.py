from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('departamentos/<int:departamento_id>/', views.show_departamento, name='detail'),
    path('departamentos/<int:departamento_id>/empleados', views.index_empleados, name='empleados'),
    path('empleados/<int:empleado_id>', views.show_empleado, name='empleado'),
    path('habilidades/<int:habilidad_id>', views.show_habilidad, name='habilidad'),


]

<<<<<<< HEAD
# probando 3# 

=======
# probando 3# 
>>>>>>> b1bb7f1f1f501ad72cf0381cf6c72c8b708ae818
