from django.urls import path
from . import views

#Degining path to own app project in benefecial and "" represents the root app link that comes from main urls.
#If we want to create second link then we cann addd here and it should work like a charm.
urlpatterns = [
    path("",views.receipes, name="receipes"),
    #The <id> is used inorder to make it dynamic.
    path("delete_receipes/<id>", views.delete_receipe, name="delete_receipes")
]
