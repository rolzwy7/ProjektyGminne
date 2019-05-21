from django.contrib import admin


class ProjektyGminneAdminSite(admin.AdminSite):
    site_header = "Projekty Gminne - Administrator"
    index_template = "admin/index_custom.html"
    login_template = "admin/login_custom.html"


admin_site = ProjektyGminneAdminSite(name="projekty-gminne-admin-site")
