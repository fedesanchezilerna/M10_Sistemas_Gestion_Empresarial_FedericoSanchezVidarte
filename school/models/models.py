# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import date
from dateutil.relativedelta import relativedelta


class SchoolStudent(models.Model):
    """Model for managing students"""
    _name = 'school.student'
    _description = 'School Student'

    name = fields.Char(string='Name', required=True)
    last_name = fields.Char(string='Last Name', required=True)
    birth_date = fields.Date(string='Birth Date')
    id_number = fields.Char(string='ID Number', required=True)
    active = fields.Boolean(string='Active', default=True)
    age = fields.Integer(string='Age', compute='_compute_age', store=True)
    class_id = fields.Many2one('school.class', string='Class')

    _sql_constraints = [
        ('id_number_unique', 'UNIQUE(id_number)', 'The ID number must be unique')
    ]

    @api.depends('birth_date')
    def _compute_age(self):
        """Calculates the age of the student based on their birth date"""
        for record in self:
            if record.birth_date:
                today = date.today()
                record.age = relativedelta(today, record.birth_date).years
            else:
                record.age = 0


class SchoolClass(models.Model):
    """Model for managing school classes"""
    _name = 'school.class'
    _description = 'School Class'

    name = fields.Char(string='Class Name', required=True)
    grade = fields.Selection([
        ('first', 'First'),
        ('second', 'Second'),
        ('third', 'Third'),
        ('fourth', 'Fourth')
    ], string='Grade')
    date_begin = fields.Date(string='Start Date')
    date_end = fields.Date(string='End Date')
    tutor_id = fields.Many2one('hr.employee', string='Tutor')
    student_ids = fields.One2many('school.student', 'class_id', string='Students')
    student_number = fields.Integer(string='Number of Students', compute='_compute_student_number', store=True)
    description = fields.Text(string='Description')

    @api.depends('student_ids')
    def _compute_student_number(self):
        """Calculates the number of students in the class"""
        for record in self:
            record.student_number = len(record.student_ids)


class SchoolEvent(models.Model):
    """Model for managing school events"""
    _name = 'school.event'
    _description = 'School Event'
    _order = 'date desc'

    name = fields.Char(string='Event Name', required=True)
    date = fields.Datetime(string='Date', default=fields.Datetime.now)
    students_ids = fields.Many2many('school.student', string='Students')
    type = fields.Selection([
        ('absence', 'Absence'),
        ('delay', 'Delay'),
        ('congratulations', 'Congratulations'),
        ('behavior', 'Behavior')
    ], string='Event Type')
    description = fields.Text(string='Description')


