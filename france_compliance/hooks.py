from . import __version__ as app_version

app_name = "france_compliance"
app_title = "France Compliance"
app_publisher = "Frappe Technologies Private Limited"
app_description = "App to include regional settings for France"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "diksha@frappe.io"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/france_compliance/css/france_compliance.css"
# app_include_js = "/assets/france_compliance/js/france_compliance.js"

# include js, css files in header of web template
# web_include_css = "/assets/france_compliance/css/france_compliance.css"
# web_include_js = "/assets/france_compliance/js/france_compliance.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "france_compliance/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "france_compliance.utils.jinja_methods",
# 	"filters": "france_compliance.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "france_compliance.install.before_install"
after_install = "france_compliance.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "france_compliance.uninstall.before_uninstall"
# after_uninstall = "france_compliance.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "france_compliance.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

doc_events = {
	"Sales Invoice": {
		"on_trash": "france_compliance.check_deletion_permission",
		"on_submit": "france_compliance.create_transaction_log"
	},
	"Payment Entry": {
		"on_trash": "france_compliance.check_deletion_permission",
		"on_submit": "france_compliance.create_transaction_log"
	},
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"france_compliance.tasks.all"
# 	],
# 	"daily": [
# 		"france_compliance.tasks.daily"
# 	],
# 	"hourly": [
# 		"france_compliance.tasks.hourly"
# 	],
# 	"weekly": [
# 		"france_compliance.tasks.weekly"
# 	],
# 	"monthly": [
# 		"france_compliance.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "france_compliance.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "france_compliance.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "france_compliance.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"france_compliance.auth.validate"
# ]

regional_overrides = {
	'France': {
		'erpnext.tests.test_regional.test_method': 'france_compliance.install.test_method'
	},
}