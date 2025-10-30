import flet as ft
from flet import Icons
from diagnosis_engine import AppTheme, COMMON_SYMPTOMS, load_diseases_data, SymptomExtractor
from hospital_finder import HospitalFinder


def create_welcome_page(page: ft.Page, navigate_to):
    """Professional medical-grade welcome page"""
    
    screen_width = page.width if page.width else 420
    
    return ft.Container(
        content=ft.Column(
            controls=[
                ft.Container(height=60),
                
            
                ft.Container(
                    content=ft.Column([
                        # Minimalist icon
                        ft.Container(
                            content=ft.Icon(
                                name=Icons.WATER_DROP_ROUNDED,
                                size=72,
                                color=AppTheme.WHITE
                            ),
                            width=120,
                            height=120,
                            bgcolor=AppTheme.PRIMARY,
                            border_radius=28,
                            shadow=ft.BoxShadow(
                                spread_radius=0,
                                blur_radius=40,
                                color=AppTheme.SHADOW_XL,
                                offset=ft.Offset(0, 12)
                            ),
                            alignment=ft.alignment.center
                        ),
                        ft.Container(height=28),
                        ft.Text(
                            "WaterWise",
                            size=38,
                            weight=ft.FontWeight.BOLD,
                            color=AppTheme.TEXT_PRIMARY,
                            text_align=ft.TextAlign.CENTER,
                        ),
                        ft.Container(height=10),
                        ft.Container(
                            content=ft.Text(
                                "Advanced water-borne disease detection and nearby medical facility finder",
                                size=14,
                                color=AppTheme.TEXT_SECONDARY,
                                text_align=ft.TextAlign.CENTER,
                                weight=ft.FontWeight.W_500
                            ),
                            padding=ft.padding.symmetric(horizontal=40)
                        ),
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=0
                    ),
                    padding=ft.padding.only(bottom=45),
                ),
                
                # Professional action cards
                ft.Container(
                    content=ft.Column([
                        # Primary action
                        ft.Container(
                            content=ft.ElevatedButton(
                                content=ft.Row([
                                    ft.Icon(Icons.BLOODTYPE_ROUNDED, size=24, color=AppTheme.WHITE),
                                    ft.Text("Start Diagnosis", size=17, weight=ft.FontWeight.W_600)
                                ],
                                alignment=ft.MainAxisAlignment.CENTER,
                                spacing=12
                                ),
                                width=min(screen_width - 48, 380),
                                height=60,
                                bgcolor=AppTheme.PRIMARY,
                                color=AppTheme.WHITE,
                                elevation=0,
                                on_click=lambda _: navigate_to("symptoms"),
                                style=ft.ButtonStyle(
                                    shape=ft.RoundedRectangleBorder(radius=16)
                                )
                            ),
                            shadow=ft.BoxShadow(
                                spread_radius=0,
                                blur_radius=30,
                                color=AppTheme.SHADOW_LG,
                                offset=ft.Offset(0, 8)
                            )
                        ),
                        
                        ft.Container(height=16),
                        
                        # Secondary actions
                        ft.Row([
                            ft.Container(
                                content=ft.TextButton(
                                    content=ft.Column([
                                        ft.Container(
                                            content=ft.Icon(Icons.HEALTH_AND_SAFETY_ROUNDED, size=32, color=AppTheme.PRIMARY),
                                            width=56,
                                            height=56,
                                            bgcolor=AppTheme.PRIMARY + "15",
                                            border_radius=14,
                                            alignment=ft.alignment.center
                                        ),
                                        ft.Container(height=10),
                                        ft.Text("Prevention", size=13, weight=ft.FontWeight.W_600, color=AppTheme.TEXT_PRIMARY)
                                    ],
                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                    spacing=0
                                    ),
                                    on_click=lambda _: navigate_to("learn"),
                                    style=ft.ButtonStyle(
                                        shape=ft.RoundedRectangleBorder(radius=18),
                                        bgcolor=AppTheme.CARD,
                                        padding=ft.padding.all(18)
                                    )
                                ),
                                shadow=ft.BoxShadow(
                                    spread_radius=0,
                                    blur_radius=20,
                                    color=AppTheme.SHADOW_MD,
                                    offset=ft.Offset(0, 4)
                                ),
                                border_radius=18,
                                expand=True
                            ),
                            
                            ft.Container(width=14),
                            
                            ft.Container(
                                content=ft.TextButton(
                                    content=ft.Column([
                                        ft.Container(
                                            content=ft.Icon(Icons.INFO_ROUNDED, size=32, color=AppTheme.ACCENT),
                                            width=56,
                                            height=56,
                                            bgcolor=AppTheme.ACCENT + "15",
                                            border_radius=14,
                                            alignment=ft.alignment.center
                                        ),
                                        ft.Container(height=10),
                                        ft.Text("About", size=13, weight=ft.FontWeight.W_600, color=AppTheme.TEXT_PRIMARY)
                                    ],
                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                    spacing=0
                                    ),
                                    on_click=lambda _: navigate_to("about"),
                                    style=ft.ButtonStyle(
                                        shape=ft.RoundedRectangleBorder(radius=18),
                                        bgcolor=AppTheme.CARD,
                                        padding=ft.padding.all(18)
                                    )
                                ),
                                shadow=ft.BoxShadow(
                                    spread_radius=0,
                                    blur_radius=20,
                                    color=AppTheme.SHADOW_MD,
                                    offset=ft.Offset(0, 4)
                                ),
                                border_radius=18,
                                expand=True
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER
                        ),
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=0
                    ),
                    padding=ft.padding.symmetric(horizontal=24)
                ),
                
                ft.Container(expand=True),
                
                # Minimal footer
                
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=0
        ),
        bgcolor=AppTheme.BACKGROUND,
        expand=True,
        padding=0
    )



def create_symptom_input_page(page: ft.Page, navigate_to, app_state):
    """Create AI-powered symptom input page with professional mobile UX"""
    
    symptom_extractor = SymptomExtractor()
    extracted_symptoms = []
    
    screen_width = page.width if page.width else 420
    
    symptom_input = ft.TextField(
        hint_text="E.g., 'I have watery diarrhea, vomiting, and feeling very weak'",
        multiline=True,
        min_lines=6,
        max_lines=9,
        border_color=AppTheme.BORDER,
        focused_border_color=AppTheme.PRIMARY,
        text_size=14,
        bgcolor=AppTheme.CARD,
        border_radius=12,
        border_width=1.5,
        content_padding=16,
        cursor_color=AppTheme.PRIMARY,
        text_style=ft.TextStyle(
            weight=ft.FontWeight.W_400,
            color=AppTheme.TEXT_PRIMARY
        )
    )
    
    detected_symptoms_column = ft.Column(
        controls=[],
        spacing=8
    )
    
    ai_status_text = ft.Text(
        "Analysis will extract symptoms from your description",
        size=12,
        color=AppTheme.TEXT_TERTIARY,
        italic=True
    )
    
    def analyze_symptoms(e):
        """Use AI to extract symptoms from text"""
        text = symptom_input.value
        if not text or not text.strip():
            page.snack_bar = ft.SnackBar(
                content=ft.Text("Please describe your symptoms"),
                bgcolor=AppTheme.STATUS_WARNING
            )
            page.snack_bar.open = True
            page.update()
            return
        
        extracted_symptoms.clear()
        extracted_symptoms.extend(symptom_extractor.extract_symptoms(text))
        
        if not extracted_symptoms:
            ai_status_text.value = "No symptoms detected. Try being more specific (e.g., 'fever', 'diarrhea', 'vomiting')"
            ai_status_text.color = AppTheme.STATUS_WARNING
            detected_symptoms_column.controls.clear()
        else:
            ai_status_text.value = f"Found {len(extracted_symptoms)} symptom(s) from your description"
            ai_status_text.color = AppTheme.STATUS_SUCCESS
            
            detected_symptoms_column.controls.clear()
            for idx, symptom in enumerate(extracted_symptoms):
                detected_symptoms_column.controls.append(
                    ft.Container(
                        content=ft.Row([
                            ft.Container(
                                content=ft.Text(
                                    str(idx + 1),
                                    size=12,
                                    weight=ft.FontWeight.BOLD,
                                    color=AppTheme.WHITE
                                ),
                                width=26,
                                height=26,
                                bgcolor=AppTheme.STATUS_SUCCESS,
                                border_radius=13,
                                alignment=ft.alignment.center
                            ),
                            ft.Text(
                                symptom,
                                size=15,
                                weight=ft.FontWeight.W_600,
                                color=AppTheme.TEXT_PRIMARY,
                                expand=True
                            ),
                            ft.Icon(Icons.CHECK_CIRCLE, size=20, color=AppTheme.STATUS_SUCCESS),
                        ],
                        spacing=12,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER
                        ),
                        bgcolor=AppTheme.CARD,
                        padding=12,
                        border_radius=10,
                        border=ft.border.all(1, AppTheme.BORDER),
                        shadow=ft.BoxShadow(
                            spread_radius=0,
                            blur_radius=12,
                            color=AppTheme.SHADOW_SM,
                            offset=ft.Offset(0, 2)
                        )
                    )
                )
        
        page.update()
    
    def on_detect_click(e):
        """Proceed to diagnosis"""
        if not extracted_symptoms:
            page.snack_bar = ft.SnackBar(
                content=ft.Text("Please analyze your symptoms first using the AI button"),
                bgcolor=AppTheme.STATUS_CRITICAL
            )
            page.snack_bar.open = True
            page.update()
            return
        
        app_state['selected_symptoms'] = extracted_symptoms.copy()
        app_state['symptom_text'] = symptom_input.value
        navigate_to("result")
    
    return ft.Container(
        content=ft.Column([
            ft.Container(
                content=ft.Row([
                    ft.IconButton(
                        icon=Icons.ARROW_BACK_ROUNDED,
                        icon_color=AppTheme.WHITE,
                        icon_size=26,
                        on_click=lambda _: navigate_to("home")
                    ),
                    ft.Text(
                        "Symptom Assessment",
                        size=20,
                        weight=ft.FontWeight.W_600,
                        color=AppTheme.WHITE
                    )
                ],
                spacing=4
                ),
                bgcolor=AppTheme.PRIMARY,
                padding=ft.padding.symmetric(horizontal=16, vertical=14),
                shadow=ft.BoxShadow(
                    spread_radius=0,
                    blur_radius=20,
                    color=AppTheme.SHADOW_MD,
                    offset=ft.Offset(0, 4)
                )
            ),
            
            ft.Container(
                content=ft.Column([
                    ft.Container(
                        content=ft.Column([
                            ft.Text(
                                "Describe your symptoms",
                                size=18,
                                weight=ft.FontWeight.W_600,
                                color=AppTheme.TEXT_PRIMARY
                            ),
                            ft.Container(height=6),
                            ft.Text(
                                "Provide a detailed description of how you're feeling. Be specific about severity, duration, and any relevant details.",
                                size=13,
                                color=AppTheme.TEXT_SECONDARY,
                                weight=ft.FontWeight.W_500
                            )
                        ]),
                        padding=ft.padding.only(bottom=4)
                    ),
                    
                    ft.Container(height=16),
                    
                    ft.Container(
                        content=symptom_input,
                        shadow=ft.BoxShadow(
                            spread_radius=0,
                            blur_radius=12,
                            color=AppTheme.SHADOW_SM,
                            offset=ft.Offset(0, 3)
                        ),
                        border_radius=14
                    ),
                    
                    ft.Container(height=18),
                    
                    ft.Container(
                        content=ft.ElevatedButton(
                            content=ft.Row([
                                ft.Icon(Icons.ANALYTICS_ROUNDED, size=22, color=AppTheme.WHITE),
                                ft.Text("Analyze Symptoms", size=16, weight=ft.FontWeight.W_600)
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            spacing=10
                            ),
                            width=min(screen_width - 40, 400),
                            height=54,
                            bgcolor=AppTheme.ACCENT,
                            color=AppTheme.WHITE,
                            elevation=0,
                            on_click=analyze_symptoms,
                            style=ft.ButtonStyle(
                                shape=ft.RoundedRectangleBorder(radius=14)
                            )
                        ),
                        shadow=ft.BoxShadow(
                            spread_radius=0,
                            blur_radius=24,
                            color=AppTheme.SHADOW_LG,
                            offset=ft.Offset(0, 6)
                        )
                    ),
                    
                    ft.Container(height=20),
                    
                    ft.Container(
                        content=ft.Row([
                            ft.Icon(Icons.INFO_OUTLINE, size=16, color=AppTheme.TEXT_TERTIARY),
                            ai_status_text
                        ], spacing=8),
                        padding=ft.padding.symmetric(horizontal=4, vertical=8),
                        bgcolor=AppTheme.SURFACE,
                        border_radius=10
                    ),
                    
                    ft.Container(height=20),
                    
                    ft.Container(
                        content=ft.Column([
                            ft.Row([
                                ft.Icon(Icons.CHECKLIST_RTL_ROUNDED, size=20, color=AppTheme.PRIMARY),
                                ft.Text(
                                    "Detected Symptoms",
                                    size=16,
                                    weight=ft.FontWeight.BOLD,
                                    color=AppTheme.TEXT_PRIMARY
                                )
                            ], spacing=8) if extracted_symptoms else ft.Container(height=0),
                            ft.Container(height=12) if extracted_symptoms else ft.Container(height=0),
                            detected_symptoms_column
                        ],
                        spacing=12
                        ),
                        padding=ft.padding.only(top=4)
                    ),
                    
                    
                    ft.Container(height=24),
                    
                    ft.Container(
                        content=ft.ElevatedButton(
                            content=ft.Row([
                                ft.Icon(Icons.MEDICAL_SERVICES_ROUNDED, size=24, color=AppTheme.WHITE),
                                ft.Text("Get Diagnosis", size=17, weight=ft.FontWeight.BOLD)
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            spacing=12
                            ),
                            width=min(screen_width - 40, 400),
                            height=58,
                            bgcolor=AppTheme.PRIMARY,
                            color=AppTheme.WHITE,
                            elevation=0,
                            on_click=on_detect_click,
                            style=ft.ButtonStyle(
                                shape=ft.RoundedRectangleBorder(radius=16)
                            )
                        ),
                        shadow=ft.BoxShadow(
                            spread_radius=0,
                            blur_radius=28,
                            color=AppTheme.SHADOW_LG,
                            offset=ft.Offset(0, 8)
                        ),
                        padding=ft.padding.only(bottom=28)
                    )
                ],
                scroll=ft.ScrollMode.AUTO
                ),
                expand=True,
                padding=20,
                bgcolor=AppTheme.BACKGROUND
            )
        ],
        spacing=0,
        expand=True
        ),
        expand=True
    )


def create_result_page(page: ft.Page, navigate_to, app_state, diagnosis_engine):
    """Create diagnosis result page"""
    
    selected_symptoms = app_state.get('selected_symptoms', [])
    results = diagnosis_engine.match_symptoms(selected_symptoms)
    
    if not results:
        return ft.Container(
            content=ft.Column([
                ft.Container(
                    content=ft.Row([
                        ft.IconButton(
                            icon=Icons.ARROW_BACK,
                            icon_color=AppTheme.WHITE,
                            on_click=lambda _: navigate_to("symptoms")
                        ),
                        ft.Text(
                            "Diagnosis Result",
                            size=24,
                            weight=ft.FontWeight.BOLD,
                            color=AppTheme.WHITE
                        )
                    ]),
                    bgcolor=AppTheme.PRIMARY,
                    padding=15
                ),
                ft.Container(
                    content=ft.Column([
                        ft.Icon(Icons.INFO_OUTLINE, size=80, color=AppTheme.PRIMARY_DARK),
                        ft.Text(
                            "No Match Found",
                            size=24,
                            weight=ft.FontWeight.BOLD,
                            text_align=ft.TextAlign.CENTER
                        ),
                        ft.Text(
                            "We couldn't match your symptoms to our database. Please consult a doctor for proper diagnosis.",
                            size=16,
                            text_align=ft.TextAlign.CENTER
                        ),
                        ft.ElevatedButton(
                            "Try Again",
                            bgcolor=AppTheme.PRIMARY,
                            color=AppTheme.WHITE,
                            on_click=lambda _: navigate_to("symptoms")
                        )
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=20
                    ),
                    expand=True,
                    padding=40,
                    alignment=ft.alignment.center
                )
            ]),
            expand=True
        )
    
    top_result = results[0]
    disease = top_result['disease']
    confidence = top_result['confidence']
    matched_symptoms = top_result['matched_symptoms']
    
    consult_info = disease.get('consultDoctor', {})
    urgency = consult_info.get('urgency', 'medium')
    urgency_color = diagnosis_engine.get_urgency_color(urgency)
    
    if urgency.lower() == "immediate" or urgency.lower() == "critical":
        urgency_text = "🟥 URGENT - Immediate Doctor Visit Required"
    elif urgency.lower() == "high":
        urgency_text = "🟧 HIGH - Consult Doctor Soon"
    else:
        urgency_text = "🟩 MODERATE - Monitor Symptoms"
    
    result_content = [
        ft.Container(
            content=ft.Row([
                ft.IconButton(
                    icon=Icons.ARROW_BACK_ROUNDED,
                    icon_color=AppTheme.WHITE,
                    icon_size=28,
                    on_click=lambda _: navigate_to("symptoms"),
                    style=ft.ButtonStyle(
                        overlay_color=AppTheme.PRIMARY_DARK
                    )
                ),
                ft.Text(
                    "Diagnosis Result",
                    size=22,
                    weight=ft.FontWeight.BOLD,
                    color=AppTheme.WHITE
                )
            ],
            spacing=8
            ),
            bgcolor=AppTheme.PRIMARY,
            padding=18,
            shadow=ft.BoxShadow(
                spread_radius=0,
                blur_radius=12,
                color=AppTheme.SHADOW_MD,
                offset=ft.Offset(0, 3)
            )
        ),
        
        ft.Container(
            content=ft.Column([
                ft.Container(
                    content=ft.Column([
                        ft.Row([
                            ft.Icon(
                                Icons.CORONAVIRUS_ROUNDED,
                                size=40,
                                color=AppTheme.PRIMARY
                            ),
                            ft.Column([
                                ft.Text(
                                    disease['name'],
                                    size=26,
                                    weight=ft.FontWeight.BOLD,
                                    color=AppTheme.TEXT_PRIMARY
                                ),
                                ft.Text(
                                    f"{disease.get('category', 'Disease').capitalize()} | {disease.get('severity', 'Unknown').capitalize()}",
                                    size=13,
                                    color=AppTheme.TEXT_TERTIARY,
                                    weight=ft.FontWeight.W_500
                                )
                            ],
                            spacing=2,
                            expand=True
                            )
                        ],
                        spacing=12
                        ),
                        ft.Container(height=20),
                        ft.Container(
                            content=ft.Row([
                                ft.Icon(
                                    Icons.WARNING_ROUNDED if urgency.lower() in ["immediate", "critical", "high"] else Icons.INFO_ROUNDED,
                                    size=22,
                                    color=AppTheme.WHITE
                                ),
                                ft.Text(
                                    urgency_text,
                                    size=14,
                                    weight=ft.FontWeight.BOLD,
                                    color=AppTheme.WHITE
                                )
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            spacing=10
                            ),
                            bgcolor=urgency_color,
                            padding=14,
                            border_radius=12,
                            shadow=ft.BoxShadow(
                                spread_radius=0,
                                blur_radius=10,
                                color=urgency_color + "40",
                                offset=ft.Offset(0, 4)
                            )
                        )
                    ]),
                    bgcolor=AppTheme.WHITE,
                    padding=26,
                    border_radius=18,
                    border=ft.border.all(1, AppTheme.BORDER),
                    shadow=ft.BoxShadow(
                        spread_radius=0,
                        blur_radius=20,
                        color=AppTheme.SHADOW_MD,
                        offset=ft.Offset(0, 6)
                    )
                ),
                
                ft.Container(height=18),
                
                ft.Container(
                    content=ft.Column([
                        ft.Row([
                            ft.Icon(Icons.CHECK_CIRCLE_ROUNDED, size=26, color=AppTheme.STATUS_SUCCESS),
                            ft.Text(
                                "Matched Symptoms",
                                size=19,
                                weight=ft.FontWeight.BOLD,
                                color=AppTheme.TEXT_PRIMARY
                            )
                        ],
                        spacing=12
                        ),
                        ft.Container(height=16),
                        ft.Column([
                            ft.Container(
                                content=ft.Row([
                                    ft.Icon(Icons.CIRCLE, size=8, color=AppTheme.PRIMARY),
                                    ft.Text(
                                        s['symptom'],
                                        size=15,
                                        color=AppTheme.TEXT_PRIMARY,
                                        weight=ft.FontWeight.W_500
                                    )
                                ],
                                spacing=12
                                ),
                                padding=ft.padding.only(left=5, top=6, bottom=6)
                            )
                            for s in matched_symptoms
                        ],
                        spacing=4
                        )
                    ]),
                    bgcolor=AppTheme.WHITE,
                    padding=20,
                    border_radius=14,
                    border=ft.border.all(1, AppTheme.BORDER),
                    shadow=ft.BoxShadow(
                        spread_radius=0,
                        blur_radius=10,
                        color=AppTheme.SHADOW_SM,
                        offset=ft.Offset(0, 3)
                    )
                ),
                
                ft.Container(
                    content=ft.Column([
                        ft.Text(
                            "🏠 Home Remedies",
                            size=18,
                            weight=ft.FontWeight.BOLD,
                            color=AppTheme.PRIMARY_DARK
                        ),
                        ft.Column([
                            ft.Container(
                                content=ft.Column([
                                    ft.Text(
                                        remedy['remedy'],
                                        size=15,
                                        weight=ft.FontWeight.BOLD
                                    ),
                                    ft.Text(
                                        remedy['instructions'],
                                        size=13
                                    ),
                                    ft.Text(
                                        f"Frequency: {remedy['frequency']}",
                                        size=12,
                                        italic=True,
                                        color=AppTheme.PRIMARY_DARK
                                    )
                                ]),
                                border=ft.border.only(
                                    left=ft.BorderSide(3, AppTheme.ACCENT_TEAL)
                                ),
                                padding=ft.padding.only(left=10, top=5, bottom=5)
                            )
                            for remedy in disease.get('homeRemedies', [])
                        ])
                    ]),
                    bgcolor=AppTheme.WHITE,
                    padding=15,
                    border_radius=10,
                    shadow=ft.BoxShadow(
                        spread_radius=2,
                        blur_radius=5,
                        color=AppTheme.SHADOW_SM
                    )
                ),
                
                ft.Container(
                    content=ft.Column([
                        ft.Text(
                            "👨‍⚕️ When to See a Doctor",
                            size=18,
                            weight=ft.FontWeight.BOLD,
                            color=AppTheme.PRIMARY_DARK
                        ),
                        ft.Text(
                            consult_info.get('reason', 'Consult a doctor if symptoms persist.'),
                            size=14
                        ),
                        ft.Text(
                            consult_info.get('condition', ''),
                            size=13,
                            italic=True,
                            color=AppTheme.PRIMARY_DARK
                        ) if consult_info.get('condition') else ft.Container()
                    ]),
                    bgcolor=AppTheme.WHITE,
                    padding=15,
                    border_radius=10,
                    shadow=ft.BoxShadow(
                        spread_radius=2,
                        blur_radius=5,
                        color=AppTheme.SHADOW_SM
                    )
                ),
                
                ft.Container(
                    content=ft.Column([
                        ft.Container(
                            content=ft.ElevatedButton(
                                content=ft.Row([
                                    ft.Icon(Icons.LOCAL_HOSPITAL_ROUNDED, size=24, color=AppTheme.WHITE),
                                    ft.Text("Find Nearby Hospitals", size=17, weight=ft.FontWeight.BOLD)
                                ],
                                alignment=ft.MainAxisAlignment.CENTER,
                                spacing=12
                                ),
                                width=340,
                                height=60,
                                bgcolor=AppTheme.STATUS_CRITICAL,
                                color=AppTheme.WHITE,
                                elevation=0,
                                on_click=lambda _: (
                                    app_state.update({'detected_disease': disease['name']}),
                                    navigate_to("hospitals")
                                ),
                                style=ft.ButtonStyle(
                                    shape=ft.RoundedRectangleBorder(radius=16)
                                )
                            ),
                            shadow=ft.BoxShadow(
                                spread_radius=0,
                                blur_radius=24,
                                color=AppTheme.SHADOW_LG,
                                offset=ft.Offset(0, 6)
                            )
                        ),
                        
                        ft.Container(height=16),
                        
                        ft.Row([
                            ft.Container(
                                content=ft.ElevatedButton(
                                    content=ft.Row([
                                        ft.Icon(Icons.REFRESH_ROUNDED, size=22, color=AppTheme.WHITE),
                                        ft.Text("Restart", size=15, weight=ft.FontWeight.W_600)
                                    ],
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    spacing=8
                                    ),
                                    height=52,
                                    bgcolor=AppTheme.PRIMARY,
                                    color=AppTheme.WHITE,
                                    elevation=0,
                                    on_click=lambda _: navigate_to("home"),
                                    style=ft.ButtonStyle(
                                        shape=ft.RoundedRectangleBorder(radius=14)
                                    )
                                ),
                                expand=True,
                                shadow=ft.BoxShadow(
                                    spread_radius=0,
                                    blur_radius=16,
                                    color=AppTheme.SHADOW_SM,
                                    offset=ft.Offset(0, 4)
                                )
                            ),
                            
                            ft.Container(width=12),
                            
                            ft.Container(
                                content=ft.OutlinedButton(
                                    content=ft.Row([
                                        ft.Icon(Icons.LIGHTBULB_ROUNDED, size=22, color=AppTheme.PRIMARY),
                                        ft.Text("Prevention", size=15, weight=ft.FontWeight.W_600, color=AppTheme.PRIMARY)
                                    ],
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    spacing=8
                                    ),
                                    height=52,
                                    on_click=lambda _: navigate_to("learn"),
                                    style=ft.ButtonStyle(
                                        shape=ft.RoundedRectangleBorder(radius=14),
                                        side=ft.BorderSide(2, AppTheme.PRIMARY),
                                        bgcolor=AppTheme.WHITE
                                    )
                                ),
                                expand=True
                            )
                        ],
                        alignment=ft.MainAxisAlignment.CENTER
                        )
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=0
                    ),
                    padding=ft.padding.only(top=24, bottom=24)
                )
            ],
            spacing=15,
            scroll=ft.ScrollMode.AUTO
            ),
            expand=True,
            padding=15,
            bgcolor=AppTheme.BACKGROUND
        )
    ]
    
    return ft.Column(
        controls=result_content,
        spacing=0,
        expand=True
    )


def create_learn_page(page: ft.Page, navigate_to):
    """Create prevention and education page"""
    
    prevention_tips = [
        {"icon": Icons.WATER_DROP, "tip": "Always boil or filter water before drinking"},
        {"icon": Icons.WASH, "tip": "Wash hands with soap before eating and after using the toilet"},
        {"icon": Icons.RESTAURANT, "tip": "Avoid raw food washed with unsafe water"},
        {"icon": Icons.PLUMBING, "tip": "Clean water tanks regularly"},
        {"icon": Icons.INVENTORY_2, "tip": "Store water in closed containers"},
        {"icon": Icons.SANITIZER, "tip": "Use hand sanitizer when soap is unavailable"},
        {"icon": Icons.LOCAL_HOSPITAL, "tip": "Seek medical help immediately for severe symptoms"},
    ]
    
    return ft.Container(
        content=ft.Column([
            ft.Container(
                content=ft.Row([
                    ft.IconButton(
                        icon=Icons.ARROW_BACK,
                        icon_color=AppTheme.WHITE,
                        on_click=lambda _: navigate_to("home")
                    ),
                    ft.Text(
                        "Prevention Tips",
                        size=24,
                        weight=ft.FontWeight.BOLD,
                        color=AppTheme.WHITE
                    )
                ]),
                bgcolor=AppTheme.PRIMARY,
                padding=15
            ),
            
            ft.Container(
                content=ft.Column([
                    ft.Container(
                        content=ft.Column([
                            ft.Icon(
                                Icons.HEALTH_AND_SAFETY,
                                size=60,
                                color=AppTheme.PRIMARY
                            ),
                            ft.Text(
                                "Why Water Safety Matters",
                                size=22,
                                weight=ft.FontWeight.BOLD,
                                color=AppTheme.PRIMARY_DARK,
                                text_align=ft.TextAlign.CENTER
                            ),
                            ft.Text(
                                "Water-borne diseases affect millions globally each year. Simple prevention steps can save lives.",
                                size=14,
                                text_align=ft.TextAlign.CENTER,
                                color=AppTheme.PRIMARY_DARK
                            )
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=10
                        ),
                        bgcolor=AppTheme.WHITE,
                        padding=20,
                        border_radius=10,
                        shadow=ft.BoxShadow(
                            spread_radius=2,
                            blur_radius=5,
                            color=AppTheme.SHADOW_SM
                        )
                    ),
                    
                    ft.Text(
                        "💧 Prevention Guidelines",
                        size=20,
                        weight=ft.FontWeight.BOLD,
                        color=AppTheme.PRIMARY_DARK
                    ),
                    
                    ft.Column([
                        ft.Container(
                            content=ft.Row([
                                ft.Icon(
                                    tip['icon'],
                                    size=30,
                                    color=AppTheme.PRIMARY
                                ),
                                ft.Text(
                                    tip['tip'],
                                    size=14,
                                    expand=True
                                )
                            ],
                            spacing=15
                            ),
                            bgcolor=AppTheme.WHITE,
                            padding=15,
                            border_radius=8,
                            border=ft.border.all(2, AppTheme.ACCENT_TEAL),
                            shadow=ft.BoxShadow(
                                spread_radius=1,
                                blur_radius=3,
                                color=AppTheme.SHADOW_SM
                            )
                        )
                        for tip in prevention_tips
                    ],
                    spacing=10
                    ),
                    
                    ft.Container(
                        content=ft.Column([
                            ft.Text(
                                "📊 Quick Facts",
                                size=18,
                                weight=ft.FontWeight.BOLD,
                                color=AppTheme.PRIMARY_DARK
                            ),
                            ft.Text(
                                "• Over 2 billion people lack access to safe drinking water",
                                size=13
                            ),
                            ft.Text(
                                "• Water-borne diseases cause ~2 million deaths annually",
                                size=13
                            ),
                            ft.Text(
                                "• Simple hygiene can prevent 50% of infections",
                                size=13
                            ),
                            ft.Text(
                                "• Children under 5 are most vulnerable",
                                size=13
                            )
                        ]),
                        bgcolor=AppTheme.SURFACE,
                        padding=15,
                        border_radius=10,
                        border=ft.border.all(2, AppTheme.STATUS_SUCCESS)
                    ),
                    
                    ft.Container(
                        content=ft.Column([
                            ft.ElevatedButton(
                                content=ft.Text("Start Diagnosis", size=16, weight=ft.FontWeight.BOLD),
                                width=280,
                                height=50,
                                bgcolor=AppTheme.PRIMARY,
                                color=AppTheme.WHITE,
                                on_click=lambda _: navigate_to("symptoms")
                            ),
                            ft.TextButton(
                                content=ft.Text("Back to Home", size=14),
                                on_click=lambda _: navigate_to("home")
                            )
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=10
                        ),
                        padding=ft.padding.only(top=20, bottom=20)
                    )
                ],
                spacing=15,
                scroll=ft.ScrollMode.AUTO
                ),
                expand=True,
                padding=15,
                bgcolor=AppTheme.BACKGROUND
            )
        ],
        spacing=0,
        expand=True
        ),
        expand=True,
        gradient=ft.LinearGradient(
            begin=ft.alignment.top_center,
            end=ft.alignment.bottom_center,
            colors=[AppTheme.SURFACE, AppTheme.WHITE]
        )
    )


def create_about_page(page: ft.Page, navigate_to):
    """Create about/settings page"""
    
    return ft.Container(
        content=ft.Column([
            ft.Container(
                content=ft.Row([
                    ft.IconButton(
                        icon=Icons.ARROW_BACK,
                        icon_color=AppTheme.WHITE,
                        on_click=lambda _: navigate_to("home")
                    ),
                    ft.Text(
                        "About WaterWise",
                        size=24,
                        weight=ft.FontWeight.BOLD,
                        color=AppTheme.WHITE
                    )
                ]),
                bgcolor=AppTheme.PRIMARY,
                padding=15
            ),
            
            ft.Container(
                content=ft.Column([
                    ft.Container(
                        content=ft.Column([
                            ft.Icon(
                                Icons.WATER_DROP,
                                size=100,
                                color=AppTheme.PRIMARY
                            ),
                            ft.Text(
                                "WaterWise",
                                size=32,
                                weight=ft.FontWeight.BOLD,
                                color=AppTheme.PRIMARY
                            ),
                            ft.Text(
                                "Version 1.0",
                                size=14,
                                color=AppTheme.PRIMARY_DARK,
                                italic=True
                            )
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=10
                        ),
                        padding=30
                    ),
                    
                    ft.Container(
                        content=ft.Column([
                            ft.Text(
                                "About This App",
                                size=20,
                                weight=ft.FontWeight.BOLD,
                                color=AppTheme.PRIMARY_DARK
                            ),
                            ft.Text(
                                "WaterWise is a rule-based AI application designed for early detection "
                                "of water-borne diseases through symptom analysis. Our mission is to "
                                "provide accessible health information and promote water safety awareness.",
                                size=14,
                                text_align=ft.TextAlign.JUSTIFY
                            )
                        ]),
                        bgcolor=AppTheme.WHITE,
                        padding=20,
                        border_radius=10,
                        shadow=ft.BoxShadow(
                            spread_radius=2,
                            blur_radius=5,
                            color=AppTheme.SHADOW_SM
                        )
                    ),
                    
                    ft.Container(
                        content=ft.Column([
                            ft.Text(
                                "✨ Features",
                                size=18,
                                weight=ft.FontWeight.BOLD,
                                color=AppTheme.PRIMARY_DARK
                            ),
                            ft.Text("• Symptom-based disease detection", size=14),
                            ft.Text("• Home remedy suggestions", size=14),
                            ft.Text("• Urgency level indicators", size=14),
                            ft.Text("• Prevention education", size=14),
                            ft.Text("• Mobile-first responsive design", size=14)
                        ]),
                        bgcolor=AppTheme.WHITE,
                        padding=20,
                        border_radius=10,
                        shadow=ft.BoxShadow(
                            spread_radius=2,
                            blur_radius=5,
                            color=AppTheme.SHADOW_SM
                        )
                    ),
                    
                    ft.Container(
                        content=ft.Column([
                            ft.Icon(Icons.WARNING_AMBER, size=40, color=AppTheme.STATUS_WARNING),
                            ft.Text(
                                "Important Disclaimer",
                                size=16,
                                weight=ft.FontWeight.BOLD,
                                color=AppTheme.PRIMARY_DARK,
                                text_align=ft.TextAlign.CENTER
                            ),
                            ft.Text(
                                "This app is for informational purposes only and does not replace professional medical advice. "
                                "Always consult with a qualified healthcare provider for diagnosis and treatment.",
                                size=13,
                                text_align=ft.TextAlign.CENTER,
                                italic=True
                            )
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=10
                        ),
                        bgcolor=AppTheme.BACKGROUND,
                        padding=20,
                        border_radius=10,
                        border=ft.border.all(2, AppTheme.STATUS_WARNING)
                    ),
                    
                    ft.Container(
                        content=ft.Column([
                            ft.Text(
                                "Credits",
                                size=16,
                                weight=ft.FontWeight.BOLD,
                                color=AppTheme.PRIMARY_DARK
                            ),
                            ft.Text(
                                "Developed for Hackathon 2025",
                                size=13,
                                italic=True
                            ),
                            ft.Text(
                                "Built with Flet Framework",
                                size=12
                            )
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=5
                        ),
                        padding=20
                    ),
                    
                    # Back button
                    ft.Container(
                        content=ft.ElevatedButton(
                            content=ft.Text("Back to Home", size=16, weight=ft.FontWeight.BOLD),
                            width=250,
                            height=50,
                            bgcolor=AppTheme.PRIMARY,
                            color=AppTheme.WHITE,
                            on_click=lambda _: navigate_to("home")
                        ),
                        alignment=ft.alignment.center,
                        padding=ft.padding.only(bottom=20)
                    )
                ],
                spacing=20,
                scroll=ft.ScrollMode.AUTO
                ),
                expand=True,
                padding=15,
                bgcolor=AppTheme.BACKGROUND
            )
        ],
        spacing=0,
        expand=True
        ),
        expand=True
    )


def create_hospital_finder_page(page: ft.Page, navigate_to, app_state):
    """Create hospital finder page with location-based search"""
    
    hospital_finder = HospitalFinder()
    screen_width = page.width if page.width else 420
    
    disease_name = app_state.get('detected_disease', 'General')
    
    user_location = None
    user_city = None
    location_data = hospital_finder.get_user_location()
    if location_data:
        user_location = (location_data[0], location_data[1])
        user_city = location_data[2]
    
    cities = hospital_finder.get_cities_list()
    city_dropdown = ft.Dropdown(
        label="Select City",
        options=[ft.dropdown.Option(city) for city in cities],
        value=user_city if user_city in cities else (cities[0] if cities else None),
        width=min(screen_width - 40, 360),
        border_color=AppTheme.PRIMARY,
        text_size=14,
        border_radius=12
    )
    

    sort_dropdown = ft.Dropdown(
        label="Sort By",
        options=[
            ft.dropdown.Option("distance", "Distance"),
            ft.dropdown.Option("rating", "Rating")
        ],
        value="distance" if user_location else "rating",
        width=min((screen_width - 60) / 2, 170),
        text_size=13,
        border_radius=10
    )
    
    hospitals_column = ft.Column(controls=[], spacing=12, scroll=ft.ScrollMode.AUTO)
    
    status_text = ft.Text("", size=13, color=AppTheme.TEXT_TERTIARY, italic=True)
    
    def create_hospital_card(hospital: dict):
        """Create a professional hospital card with enhanced layout"""
        distance = hospital.get('distance_km')
        travel_time = hospital.get('travel_time')
        
        return ft.Container(
            content=ft.Column([
                ft.Row([
                    ft.Container(
                        content=ft.Icon(Icons.LOCAL_HOSPITAL_ROUNDED, size=28, color=AppTheme.WHITE),
                        width=52, height=52, bgcolor=AppTheme.PRIMARY,
                        border_radius=14, alignment=ft.alignment.center,
                        shadow=ft.BoxShadow(
                            spread_radius=0,
                            blur_radius=12,
                            color=AppTheme.SHADOW_SM,
                            offset=ft.Offset(0, 2)
                        )
                    ),
                    ft.Column([
                        ft.Text(hospital['name'], size=17, weight=ft.FontWeight.BOLD, color=AppTheme.TEXT_PRIMARY),
                        ft.Text(hospital.get('type', 'Hospital'), size=13, color=AppTheme.TEXT_TERTIARY, weight=ft.FontWeight.W_500)
                    ], spacing=3, expand=True)
                ], spacing=14),
                
                ft.Container(height=14),
                
                ft.Row([
                    ft.Container(
                        content=ft.Row([
                            ft.Icon(Icons.STAR_ROUNDED, size=17, color=AppTheme.STATUS_WARNING),
                            ft.Text(f"{hospital.get('rating', 'N/A')}/5.0", size=13, weight=ft.FontWeight.W_600)
                        ], spacing=5),
                        bgcolor=AppTheme.SURFACE,
                        padding=ft.padding.symmetric(horizontal=10, vertical=6),
                        border_radius=8
                    ),
                    ft.Container(
                        content=ft.Row([
                            ft.Icon(Icons.LOCATION_ON, size=17, color=AppTheme.STATUS_CRITICAL),
                            ft.Text(f"{distance:.1f} km" if distance else "N/A", size=13, weight=ft.FontWeight.W_600)
                        ], spacing=5),
                        bgcolor=AppTheme.SURFACE,
                        padding=ft.padding.symmetric(horizontal=10, vertical=6),
                        border_radius=8
                    ),
                    ft.Container(
                        content=ft.Row([
                            ft.Icon(Icons.ACCESS_TIME, size=17, color=AppTheme.ACCENT),
                            ft.Text(travel_time if travel_time else "N/A", size=13, weight=ft.FontWeight.W_600, color=AppTheme.ACCENT)
                        ], spacing=5),
                        bgcolor=AppTheme.SURFACE,
                        padding=ft.padding.symmetric(horizontal=10, vertical=6),
                        border_radius=8
                    )
                ], spacing=8, wrap=True),
                
                ft.Container(height=10),
                ft.Row([
                    ft.Icon(Icons.PLACE_ROUNDED, size=14, color=AppTheme.TEXT_TERTIARY),
                    ft.Text(hospital.get('address', ''), size=12, color=AppTheme.TEXT_SECONDARY, expand=True)
                ], spacing=6),
                ft.Container(
                    content=ft.Row([
                        ft.Icon(Icons.MEDICAL_SERVICES, size=15, color=AppTheme.ACCENT),
                        ft.Text(", ".join(hospital.get('specializations', [])[:2]), size=12,
                               color=AppTheme.ACCENT, weight=ft.FontWeight.W_600, expand=True)
                    ], spacing=7),
                    bgcolor=AppTheme.SURFACE, padding=10, border_radius=10, margin=ft.margin.only(top=10)
                ),
                
                ft.Container(height=14),
                
                ft.Row([
                    ft.ElevatedButton(
                        content=ft.Row([
                            ft.Icon(Icons.CALL, size=20, color=AppTheme.WHITE),
                            ft.Text("Call", size=14, weight=ft.FontWeight.BOLD)
                        ], spacing=7, alignment=ft.MainAxisAlignment.CENTER),
                        bgcolor=AppTheme.STATUS_SUCCESS, color=AppTheme.WHITE, height=44, expand=True,
                        elevation=0,
                        on_click=lambda _,h=hospital: page.launch_url(hospital_finder.get_call_url(h.get('phone', ''))),
                        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=12))
                    ),
                    ft.ElevatedButton(
                        content=ft.Row([
                            ft.Icon(Icons.DIRECTIONS, size=20, color=AppTheme.WHITE),
                            ft.Text("Directions", size=14, weight=ft.FontWeight.BOLD)
                        ], spacing=7, alignment=ft.MainAxisAlignment.CENTER),
                        bgcolor=AppTheme.ACCENT, color=AppTheme.WHITE, height=44, expand=True,
                        elevation=0,
                        on_click=lambda _,h=hospital: page.launch_url(hospital_finder.get_directions_url(h, user_location)),
                        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=12))
                    )
                ], spacing=12)
            ]),
            bgcolor=AppTheme.WHITE, padding=20, border_radius=16,
            border=ft.border.all(1, AppTheme.BORDER),
            shadow=ft.BoxShadow(spread_radius=0, blur_radius=16, color=AppTheme.SHADOW_MD, offset=ft.Offset(0, 4))
        )
    
    def search_hospitals(e=None):
        """Search for hospitals based on filters"""
        selected_city = city_dropdown.value
        sort_by = sort_dropdown.value
        
        results = hospital_finder.find_nearby_hospitals(
            disease_name=disease_name, user_coords=user_location,
            city=selected_city, max_distance=50.0, sort_by=sort_by
        )
        
        hospitals_column.controls.clear()
        
        if results:
            status_text.value = f"Found {len(results)} hospital(s) for {disease_name}"
            status_text.color = AppTheme.STATUS_SUCCESS
            for hospital in results[:10]:
                hospitals_column.controls.append(create_hospital_card(hospital))
        else:
            status_text.value = f"No hospitals found in {selected_city}"
            status_text.color = AppTheme.STATUS_CRITICAL
            hospitals_column.controls.append(
                ft.Container(
                    content=ft.Column([
                        ft.Icon(Icons.SEARCH_OFF, size=60, color=AppTheme.TEXT_TERTIARY),
                        ft.Text("No Results", size=20, weight=ft.FontWeight.BOLD, color=AppTheme.TEXT_PRIMARY),
                        ft.Text("Try selecting a different city", size=14, color=AppTheme.TEXT_SECONDARY)
                    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=10),
                    padding=40, alignment=ft.alignment.center
                )
            )
        page.update()
    
    search_hospitals()
    
    return ft.Container(
        content=ft.Column([
            ft.Container(
                content=ft.Row([
                    ft.IconButton(icon=Icons.ARROW_BACK_ROUNDED, icon_color=AppTheme.WHITE, icon_size=28,
                                 on_click=lambda _: navigate_to("result"),
                                 style=ft.ButtonStyle(overlay_color=AppTheme.PRIMARY_DARK)),
                    ft.Column([
                        ft.Text("Nearby Hospitals", size=20, weight=ft.FontWeight.BOLD, color=AppTheme.WHITE),
                        ft.Text(f"For {disease_name}", size=12, color=AppTheme.WHITE + "CC")
                    ], spacing=2)
                ], spacing=8),
                bgcolor=AppTheme.PRIMARY, padding=18,
                shadow=ft.BoxShadow(spread_radius=0, blur_radius=12, color=AppTheme.SHADOW_MD, offset=ft.Offset(0, 3))
            ),
            
            ft.Container(
                content=ft.Column([
                    ft.Container(
                        content=ft.Row([
                            ft.Icon(Icons.MY_LOCATION_ROUNDED, size=20, color=AppTheme.PRIMARY),
                            ft.Text(f"Location: {user_city if user_city else 'Select city below'}",
                                   size=14, weight=ft.FontWeight.W_600, color=AppTheme.TEXT_PRIMARY)
                        ], spacing=10),
                        bgcolor=AppTheme.SURFACE, padding=12, border_radius=10
                    ),
                    ft.Container(height=12),
                    ft.Row([city_dropdown]),
                    ft.Row([
                        sort_dropdown,
                        ft.ElevatedButton(
                            content=ft.Row([ft.Icon(Icons.SEARCH_ROUNDED, size=20, color=AppTheme.WHITE),
                                           ft.Text("Search", size=14, weight=ft.FontWeight.BOLD)],
                                          alignment=ft.MainAxisAlignment.CENTER, spacing=8),
                            bgcolor=AppTheme.PRIMARY, color=AppTheme.WHITE, height=50, expand=True,
                            on_click=search_hospitals,
                            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=12))
                        )
                    ], spacing=10),
                    ft.Container(height=8),
                    ft.Row([ft.Icon(Icons.INFO_OUTLINE, size=16, color=AppTheme.TEXT_TERTIARY), status_text], spacing=6)
                ]),
                bgcolor=AppTheme.WHITE, padding=16,
                border=ft.border.only(bottom=ft.BorderSide(1, AppTheme.BORDER))
            ),
            
            ft.Container(content=hospitals_column, expand=True, padding=16, bgcolor=AppTheme.BACKGROUND)
        ], spacing=0, expand=True),
        expand=True
    )
