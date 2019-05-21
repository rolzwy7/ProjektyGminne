from django.contrib import admin


class ProjektyGminneAdminSite(admin.AdminSite):
    site_header = "Projekty Gminne - Warszawa"
    index_template = "admin/base/index.html"
    login_template = "admin/base/login.html"


admin_site = ProjektyGminneAdminSite(name="projekty-gminne-admin-site")
