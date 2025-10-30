import flet as ft
import json
from typing import List, Dict
from pages import *
from diagnosis_engine import DiagnosisEngine

def main(page: ft.Page):
    page.title = "WaterWise - Water-borne Disease Detection"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 0
    page.scroll = None
    page.window_width = 420
    page.window_height = 800
    page.window_resizable = True
    page.fonts = {
        "Inter": "https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap"
    }
    page.theme = ft.Theme(font_family="Inter")
    
    diseases_data = load_diseases_data()
    diagnosis_engine = DiagnosisEngine(diseases_data)
    
    app_state = {
        'selected_symptoms': [],
        'diagnosis_result': None
    }
    
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
        elif route == "hospitals":
            page.add(create_hospital_finder_page(page, navigate_to, app_state))
        
        page.update()
    
    navigate_to("home")

if __name__ == "__main__":
    ft.app(target=main)
