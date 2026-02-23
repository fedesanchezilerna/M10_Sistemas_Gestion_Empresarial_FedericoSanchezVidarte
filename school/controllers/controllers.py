# -*- coding: utf-8 -*-

import os
from odoo import http
from odoo.http import request


class SchoolController(http.Controller):

    @http.route('/school/events/', auth='public', type='http')
    def list_events(self, **kw):
        """Returns an HTML page with all school events using name_get"""
        # Get events data
        events = request.env['school.event'].sudo().search([])
        event_names = events.name_get()
        
        # Build events HTML
        if event_names:
            events_html = ""
            for event_id, name in event_names:
                events_html += f"""
                    <div class="event-item">
                        <span class="event-text">{name}</span>
                    </div>
                """
        else:
            events_html = """
                <div class="no-events">
                    <p>📭 No events registered yet</p>
                </div>
            """
        
        # Read HTML template
        template_path = os.path.join(os.path.dirname(__file__), '..', 'static', 'events.html')
        with open(template_path, 'r', encoding='utf-8') as f:
            html = f.read()
        
        # Replace placeholders
        html = html.replace('{EVENT_COUNT}', str(len(event_names)))
        html = html.replace('{EVENTS_HTML}', events_html)
        
        return html

