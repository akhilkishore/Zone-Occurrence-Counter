from app.main import bp
from app.main.views import ZoneOccurrence

# add URL routing here
bp.add_url_rule(
    '/count-zone-occurrence', 
    view_func=ZoneOccurrence.as_view('zone-occurrence'))
