from odoo import http
from odoo.http import request
from odoo.exceptions import ValidationError


class ProjectWebsiteController(http.Controller):
    @http.route('/timesheet', type='http', auth='public', website=True)
    def timesheet_form(self, **kwargs):
        return request.render('snippet_kodershop.timesheet_form_template', {})

    @http.route('/timesheet/submit', type='http', auth='public', methods=['POST'], website=True)
    def timesheet_submit(self, **post):
        project_name = post.get('project_id')
        project = request.env['project.project'].sudo().search([('name', '=', project_name)], limit=1)
        project_task = post.get('task_id')
        task = request.env['project.task'].sudo().search([('name', '=', project_task)], limit=1)

        if not project:
            project = request.env['project.project'].sudo().create({'name': project_name})
        if not task:
            task = request.env['project.task'].sudo().create({'name': project_task})

        analytic_account = project.analytic_account_id

        if not analytic_account.active:
            raise ValidationError("The associated analytic account is not active.")

        timesheet_form = request.env['account.analytic.line']
        timesheet_form.create({
            'project_id': project.id,
            'task_id': task.id,
            'name': post.get('name'),
            'unit_amount': float(post.get('unit_amount')),
        })
        return request.render('snippet_kodershop.timesheet_form_template', {})
