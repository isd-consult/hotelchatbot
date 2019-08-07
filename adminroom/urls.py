from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^service/$', views.select_room, name='adminchatroom'),
    url(r'^service/livechatrooms/$', views.livechatrooms, name='livechatrooms'),
    url(r'^service/(?P<pk>\d+)/chatroom/$', views.selectedroom, name='selectedroom'),
    url(r'^service/(?P<pk>\d+)/sendmessage/$', views.sendmessage, name='sendmessage'),
    url(r'^service/(?P<pk>\d+)/messageclear/$', views.messageclear, name='messageclear'),
    url(r'^service/(?P<pk>\d+)/messages/$', views.messages, name='messages'),
    url(r'^service/exitroom/$', views.exitroom, name='exitroom'),
    url(r'^service/(?P<customer>\w+)/offerchat/$', views.offerchat, name='offerchat'),
    url(r'^service/translate/$', views.reqtranslate, name='reqtranslate'),
    url(r'^service/changetheme/$', views.changetheme, name='changetheme'),
    url(r'^service/controlpanel/$', views.controlpanel, name='controlpanel'),
    url(r'^service/addtobot/$', views.addtobot, name='addtobot'),
    url(r'^service/deletefrombot/$', views.deletefrombot, name='deletefrombot'),
    url(r'^service/getbotdata/$', views.getbotdata, name='getbotdata'),
    url(r'^service/botlearn/$', views.botlearn, name='botlearn'),
    url(r'^service/changeroomname/$', views.changeroomname, name='changeroomname'),
    url(r'^service/(?P<pk>\d+)/customerinfo/$', views.customerinfo, name='customerinfo'),
    url(r'^service/broadcastmessage/$', views.broadcastmessage, name='broadcastmessage'),
]