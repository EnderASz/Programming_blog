from split_settings.tools import include

include(
    'project_settings/base.py',
    'project_settings/my_apps.py',
    'project_settings/static.py',
    'project_settings/sass_compressor.py',
    'project_settings/database.py',
)
