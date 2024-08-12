from talon import Context, Module, ui

ctx = Context()
ctx.matches = r"""
app: calendar
"""

mod = Module()

def get_week_calendar_area_group():
    app = ui.active_app()
    window = app.active_window
    week_calendar_area = window.children.find_one(
            AXDescription="Week Calendar Area"
        )
    return week_calendar_area

def click_button_with_description(description):
    week_calendar_area = get_week_calendar_area_group()
    button = week_calendar_area.children.find_one(
            AXRole="AXButton", AXDescription=description
        )
    button.perform("AXPress")


@mod.action_class
class Actions:
    def click_today():
        """Clicks Today Button"""
        click_button_with_description("Today")

    def click_next_week():
        """Clicks Next Week Button"""
        click_button_with_description("next week")

    def click_last_week():
        """Clicks Next Week Button"""
        click_button_with_description("previous week")