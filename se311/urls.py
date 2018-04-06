from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from account.views import deleteMember, displayAllMembers, login, login_request, logout_request, register, home, logout1, display_profile, userEdit
from file.views import index, hello, about, faq, contact, addNewCategory, allContent, deleteFile, search, list_all_posts,display_post
from core.views import upload

#from account import login.views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name='home'),
    url(r'^home/$', home),
    url(r'^about/$', about),
    url(r'^faq/$', faq),
    url(r'^contact/$', contact),
    url(r'^addNewCategory/$', addNewCategory),
    url(r'^allContent/$', list_all_posts),
    url(r'^deleteFile/$', deleteFile),
    url(r'^deleteMember/$', deleteMember),
    url(r'^search/$', search),
    url(r'^displayAllMembers/$', displayAllMembers),
    url(r'^login_request/', login_request, name='login_request'),
    url(r'^login/$', login),
    url(r'^logout_request/$', logout_request, name='logout'),
    url(r'^logout/$', logout1),
    url(r'^register/$', register, name='register'),
    url(r'^show_post/(?P<id>\w+)/$', display_post),
    url(r'^show_profile/(?P<id>\w+)/$', display_profile),
    url(r'^show_userEdit/(?P<id>\w+)/$', userEdit, name='user_edit'),
    url(r'^hello/', hello),




] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

