from django.contrib.admin.apps import AdminConfig


class ProjektyGminneAdminConfig(AdminConfig):
    default_site = 'ProjektyGminne.admin.ProjektyGminneAdminSite'
