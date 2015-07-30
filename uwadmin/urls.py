from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView

from django.contrib import admin

from .views import (
    api_contact,
    ContactList,
    ContactCreate,
    ContactDetail,
    ContactUpdate,
    OpenBibleStoryListView,
    OpenBibleStoryCreateView,
    OpenBibleStoryDetailView,
    OpenBibleStoryUpdateView,
    PublishRequestCreateView,
    PublishRequestUpdateView,
    PublishRequestDeleteView,
)


urlpatterns = patterns(
    "",
    url(r"^$", TemplateView.as_view(template_name="homepage.html"), name="home"),
    url(r"^admin/", include(admin.site.urls)),
    url(r"^account/", include("account.urls")),
    url(r"^api/contacts/", api_contact, name="api_contacts"),
    url(r"^contacts/$", ContactList.as_view(), name="contact_list"),
    url(r"^contacts/create/$", ContactCreate.as_view(), name="contact_create"),
    url(r"^contacts/(?P<pk>\d+)/$", ContactDetail.as_view(), name="contact_detail"),
    url(r"^contacts/(?P<pk>\d+)/update/$", ContactUpdate.as_view(), name="contact_update"),
    url(r"^obs/$", OpenBibleStoryListView.as_view(), name="obs_list"),
    url(r"^obs/create/$", OpenBibleStoryCreateView.as_view(), name="obs_create"),
    url(r"^obs/(?P<pk>\d+)/$", OpenBibleStoryDetailView.as_view(), name="obs_detail"),
    url(r"^obs/(?P<code>[\w-]+)/update/$", OpenBibleStoryUpdateView.as_view(), name="obs_update"),
    url(r"^publish/request/$", PublishRequestCreateView.as_view(), name="publish_request"),
    url(r"^publish/request/(?P<pk>\d+)", PublishRequestUpdateView.as_view(), name="publish_request_update"),
    url(r"^publish/request-reject/(?P<pk>\d+)", PublishRequestDeleteView.as_view(), name="publish_request_delete"),
    url(r"^ac/langnames/", "uwadmin.views.languages_autocomplete", name="names_autocomplete"),
    url(r"^ac/src-langnames/", "uwadmin.views.source_languages_autocomplete", name="source_names_autocomplete"),
    url(r"^ajax/langversion/", "uwadmin.views.ajax_language_version", name="ajax_language_version")
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
