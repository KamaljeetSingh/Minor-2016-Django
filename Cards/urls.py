from django.conf.urls import url, include
from . import views
app_name = 'cards'
urlpatterns = [


    url(r"^$", views.CardsProjects_All , name='CardsProjects_All'),

    url(r"^showcard/$", views.Show_Card , name='show_card'),

    # home/showcard/2/delete/
    url(r"^showcard/(?P<pk>[0-9]+)/delete/$", views.DeleteCard.as_view() , name='delete_card'),
    url(r"^store-desc/$", views.Desc_post , name='desc_post'),
    url(r"^showcard/itemadd/$", views.add_item , name='add_item'),
    url(r"^store-post/$", views.Store_post, name='store_post'),
]
