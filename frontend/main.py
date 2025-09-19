from nicegui import ui
from app.config import settings
from frontend.pages import dashboard, data_input, reports, chatbot

# NiceGUI 단일 통합
def create_app():
    with ui.header().classes('items-center justify-between'):
        ui.label('ESG Reporting Service').classes('text-h6')
        with ui.row():
            ui.link('Dashboard', '/').classes('text-white')
            ui.link('Data Input', '/data').classes('text-white')  
            ui.link('Reports', '/reports').classes('text-white')
            ui.link('Chatbot', '/chat').classes('text-white')

    dashboard.create_dashboard_page()
    data_input.create_data_input_page()
    reports.create_reports_page()
    chatbot.create_chatbot_page()
    
    return ui

if __name__ == "__main__":
    ui.run(host=settings.APP_HOST, port=settings.APP_PORT)  # 단일 8080 포트
