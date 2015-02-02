from django.conf.urls import *
from . import views
from django.views.generic import TemplateView

urlpatterns = patterns('cvrf.views',
	(r'^hello', TemplateView.as_view(template_name='cvrf_hello.html')),
	#url(r'^rawxml/([mM][sS]\d{2}-\d{3})', views.rawxml),
	url(r'^([\w]+)/$',  views.vendor_index),
	url(r'^([\w]+)/catalog', views.vendor_index),
	url(r'^([mM][sS])/rawxml/([mM][sS]\d{2}-\d{3})', views.rawxml),
	url(r'^([rR][eE][dD][hH][aA][tT])/rawxml/(cvrf-rhsa-\d{4}-\d{4})', views.rawxml),
	url(r'^([cC][iI][sS][cC][oO])/rawxml/(cisco-s[aArR]-\d{8}-.*_cvrf)', views.rawxml),
	url(r'^([oO][rR][aA][cC][lL][eE])/rawxml/(\d{7})', views.rawxml),
	url(r'^([mM][sS])/prettyxml/([mM][sS]\d{2}-\d{3})', views.prettyxml),
	url(r'^([rR][eE][dD][hH][aA][tT])/prettyxml/(cvrf-rhsa-\d{4}-\d{4})', views.prettyxml),
	url(r'^([cC][iI][sS][cC][oO])/prettyxml/(cisco-s[aArR]-\d{8}-.*_cvrf)', views.prettyxml),
	url(r'^([oO][rR][aA][cC][lL][eE])/prettyxml/(\d{7})', views.prettyxml),
	url(r'^([mM][sS])/xml/([mM][sS]\d{2}-\d{3})', views.cvrfxml),
	url(r'^([rR][eE][dD][hH][aA][tT])/xml/(cvrf-rhsa-\d{4}-\d{4})', views.cvrfxml),
	url(r'^([cC][iI][sS][cC][oO])/xml/(cisco-s[aArR]-\d{8}-.*_cvrf)', views.cvrfxml),
	url(r'^([oO][rR][aA][cC][lL][eE])/xml/(\d{7})', views.cvrfxml),
	url(r'^[mM][sS]/import', views.import_msrc_cvrf),
	url(r'^[rR][eE][dD][hH][aA][tT]/import', views.import_redhat_cvrf),
	url(r'^[oO][rR][aA][cC][lL][eE]/import', views.import_oracle_cvrf),
	url(r'^[cC][iI][sS][cC][oO]/import', views.import_cisco_cvrf),
	url(r'^catalog', TemplateView.as_view(template_name='cvrf_catalog.html')),
	url(r'.*', TemplateView.as_view(template_name='cvrf_catalog.html')),
	#url(r'^pretty/([mM][sS])/([mM][sS]\d{2}-\d{3})', views.prettyxmltest),
	#url(r'^pretty/([rR][eE][dD][hH][aA][tT])/(cvrf-rhsa-\d{4}-\d{4})', views.prettyxmltest),
)
