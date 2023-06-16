{
    'name': 'snippets kodershop',
    'author': 'Kodershop',
    'website': 'https://kodershop.com/',
    'category': 'Website',
    'license': 'OPL-1',
    'version': '16.0.1.0',
    'depends': [
        'base',
        'website',
        'project',
    ],
    'data': [
        'views/website_form.xml',
        # 'views/project_views.xml',
        # 'views/timesheet_submit_template.xml',
    ],
    'assets': {
        'website.assets_wysiwyg': [
            'snippet_kodershop/static/src/js/task_form.js',
        ],
    },

    'installable': True,
    'application': True,
}