import flet as ft
import json
from typing import List, Dict
from pages import *
from diagnosis_engine import DiagnosisEngine

# ========================================
# MAIN APP
# ========================================
def main(page: ft.Page):
    # Page configuration
    page.title = "WaterWise - Water-borne Disease Detection"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 0
    page.scroll = None
    
    # Load disease data
    diseases_data = load_diseases_data()
    diagnosis_engine = DiagnosisEngine(diseases_data)
    
    # App state
    app_state = {
        'selected_symptoms': [],
        'diagnosis_result': None
    }
    
    # Navigation function
    def navigate_to(route):
        page.controls.clear()
        
        if route == "home":
            page.add(create_welcome_page(page, navigate_to))
        elif route == "symptoms":
            page.add(create_symptom_input_page(page, navigate_to, app_state))
        elif route == "result":
            page.add(create_result_page(page, navigate_to, app_state, diagnosis_engine))
        elif route == "learn":
            page.add(create_learn_page(page, navigate_to))
        elif route == "about":
            page.add(create_about_page(page, navigate_to))
        
        page.update()
    
    # Start with home page
    navigate_to("home")

if __name__ == "__main__":
    ft.app(target=main)
