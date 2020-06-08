# Copyright 2020 Jesus Ramoneda <jesus.ramoneda@qubiq.es>
# License AGPL-3.0 or later (https: //www.gnu.org/licenses/agpl).

{
    "name": "Event Survey",
    "summary": "Manage Survey thought Events",
    "version": "13.0.1.0.0",
    "category": "Pro",
    "website": "https://www.qubiq.es",
    "author": "QubiQ, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        'event',
        'survey'
    ],
    "data": [
        "views/survey_survey.xml",
        "views/event_event.xml",
    ],
}
