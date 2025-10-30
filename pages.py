import flet as ft
from flet import Icons
from diagnosis_engine import AppTheme, COMMON_SYMPTOMS, load_diseases_data, SymptomExtractor

# ========================================
# PAGE 1: WELCOME SCREEN
# ========================================
def create_welcome_page(page: ft.Page, navigate_to):
    """Create the welcome/home page with modern design"""
    
    return ft.Container(
        content=ft.Column(
            controls=[
                # Spacer
                ft.Container(height=40),
                
                # Hero section with logo
                ft.Container(
                    content=ft.Column([
                        # Animated icon container
                        ft.Container(
                            content=ft.Icon(
                                name=Icons.WATER_DROP,
                                size=100,
                                color=AppTheme.WHITE
                            ),
                            width=140,
                            height=140,
                            bgcolor=AppTheme.PRIMARY_TEAL,
                            border_radius=70,
                            shadow=ft.BoxShadow(
                                spread_radius=8,
                                blur_radius=25,
                                color=AppTheme.PRIMARY_TEAL + "40",
                                offset=ft.Offset(0, 8)
                            ),
                            alignment=ft.alignment.center
                        ),
                        ft.Container(height=20),
                        ft.Text(
                            "WaterWise",
                            size=48,
                            weight=ft.FontWeight.BOLD,
                            color=AppTheme.TEXT_PRIMARY,
                            text_align=ft.TextAlign.CENTER,
                        ),
                        ft.Container(height=5),
                        ft.Text(
                            "Early Detection of Water-Borne Diseases",
                            size=17,
                            color=AppTheme.TEXT_SECONDARY,
                            text_align=ft.TextAlign.CENTER,
                            weight=ft.FontWeight.W_500
                        ),
                        ft.Container(height=5),
                        ft.Text(
                            "AI-powered symptom analysis for your health",
                            size=14,
                            color=AppTheme.TEXT_MUTED,
                            text_align=ft.TextAlign.CENTER,
                        ),
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=0
                    ),
                    padding=ft.padding.only(bottom=40),
                ),
                
                # Main CTA Buttons with cards
                ft.Container(
                    content=ft.Column([
                        # Primary CTA
                        ft.Container(
                            content=ft.ElevatedButton(
                                content=ft.Row([
                                    ft.Icon(Icons.MEDICAL_SERVICES_ROUNDED, size=28, color=AppTheme.WHITE),
                                    ft.Text("Start Diagnosis", size=19, weight=ft.FontWeight.BOLD)
                                ],
                                alignment=ft.MainAxisAlignment.CENTER,
                                spacing=12
                                ),
                                width=320,
                                height=65,
                                bgcolor=AppTheme.PRIMARY_TEAL,
                                color=AppTheme.WHITE,
                                elevation=8,
                                on_click=lambda _: navigate_to("symptoms"),
                                style=ft.ButtonStyle(
                                    shape=ft.RoundedRectangleBorder(radius=16),
                                    overlay_color=AppTheme.PRIMARY_TEAL_DARK
                                )
                            ),
                            shadow=ft.BoxShadow(
                                spread_radius=1,
                                blur_radius=20,
                                color=AppTheme.PRIMARY_TEAL + "35",
                                offset=ft.Offset(0, 8)
                            )
                        ),
                        
                        # Secondary CTA
                        ft.Container(
                            content=ft.Container(
                                content=ft.TextButton(
                                    content=ft.Row([
                                        ft.Icon(Icons.LIGHTBULB_ROUNDED, size=24, color=AppTheme.PRIMARY_TEAL),
                                        ft.Text("Learn Prevention Tips", size=17, weight=ft.FontWeight.W_600, color=AppTheme.PRIMARY_TEAL)
                                    ],
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    spacing=10
                                    ),
                                    width=320,
                                    height=60,
                                    on_click=lambda _: navigate_to("learn"),
                                    style=ft.ButtonStyle(
                                        shape=ft.RoundedRectangleBorder(radius=16),
                                        bgcolor=AppTheme.SOFT_GRAY,
                                        overlay_color=AppTheme.LIGHT_AQUA
                                    )
                                ),
                                border_radius=16,
                            )
                        ),
                        
                        # Tertiary link
                        ft.Container(
                            content=ft.TextButton(
                                content=ft.Row([
                                    ft.Icon(Icons.INFO_ROUNDED, size=20, color=AppTheme.TEXT_SECONDARY),
                                    ft.Text("About WaterWise", size=15, color=AppTheme.TEXT_SECONDARY)
                                ],
                                alignment=ft.MainAxisAlignment.CENTER,
                                spacing=8
                                ),
                                on_click=lambda _: navigate_to("about"),
                                style=ft.ButtonStyle(
                                    overlay_color=AppTheme.LIGHT_AQUA
                                )
                            ),
                            padding=ft.padding.only(top=5)
                        ),
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=18
                    ),
                    padding=20
                ),
                
                # Spacer
                ft.Container(expand=True),
                
                # Footer
                ft.Container(
                    content=ft.Column([
                        ft.Container(
                            content=ft.Row([
                                ft.Icon(Icons.VERIFIED_ROUNDED, size=16, color=AppTheme.TEXT_MUTED),
                                ft.Text(
                                    "Built for Hackathon 2025",
                                    size=13,
                                    color=AppTheme.TEXT_MUTED,
                                    weight=ft.FontWeight.W_500
                                )
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            spacing=6
                            )
                        ),
                        ft.Text(
                            "Version 1.0",
                            size=11,
                            color=AppTheme.TEXT_MUTED,
                            text_align=ft.TextAlign.CENTER,
                        )
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=4
                    ),
                    padding=ft.padding.only(bottom=25)
                )
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=0
        ),
        gradient=ft.LinearGradient(
            begin=ft.alignment.top_left,
            end=ft.alignment.bottom_right,
            colors=[AppTheme.LIGHT_AQUA, AppTheme.WHITE, AppTheme.SOFT_GRAY]
        ),
        expand=True,
        padding=20
    )


# ========================================
# PAGE 2: AI-POWERED SYMPTOM INPUT PAGE
# ========================================
def create_symptom_input_page(page: ft.Page, navigate_to, app_state):
    """Create AI-powered symptom input page with natural language processing"""
    
    symptom_extractor = SymptomExtractor()
    extracted_symptoms = []
    
    # Text input field
    symptom_input = ft.TextField(
        label="Describe your symptoms",
        hint_text="E.g., 'I have watery diarrhea, vomiting, and feeling very weak'",
        multiline=True,
        min_lines=4,
        max_lines=6,
        border_color=AppTheme.PRIMARY_TEAL,
        focused_border_color=AppTheme.PRIMARY_TEAL_DARK,
        text_size=16,
        bgcolor=AppTheme.WHITE,
        border_radius=12,
    )
    
    # Detected symptoms display
    detected_symptoms_column = ft.Column(
        controls=[],
        spacing=8
    )
    
    ai_status_text = ft.Text(
        "AI will analyze your text and extract symptoms automatically",
        size=13,
        color=AppTheme.TEXT_MUTED,
        italic=True
    )
    
    def analyze_symptoms(e):
        """Use AI to extract symptoms from text"""
        text = symptom_input.value
        if not text or not text.strip():
            page.snack_bar = ft.SnackBar(
                content=ft.Text("Please describe your symptoms"),
                bgcolor=AppTheme.URGENCY_MEDIUM
            )
            page.snack_bar.open = True
            page.update()
            return
        
        # Extract symptoms using rule-based AI
        extracted_symptoms.clear()
        extracted_symptoms.extend(symptom_extractor.extract_symptoms(text))
        
        if not extracted_symptoms:
            ai_status_text.value = "❌ No symptoms detected. Try being more specific (e.g., 'fever', 'diarrhea', 'vomiting')"
            ai_status_text.color = AppTheme.URGENCY_HIGH
            detected_symptoms_column.controls.clear()
        else:
            ai_status_text.value = f"✅ AI detected {len(extracted_symptoms)} symptom(s)"
            ai_status_text.color = AppTheme.URGENCY_LOW
            
            # Display detected symptoms
            detected_symptoms_column.controls.clear()
            for symptom in extracted_symptoms:
                detected_symptoms_column.controls.append(
                    ft.Container(
                        content=ft.Row([
                            ft.Icon(Icons.CHECK_CIRCLE_ROUNDED, size=20, color=AppTheme.URGENCY_LOW),
                            ft.Text(
                                symptom,
                                size=15,
                                weight=ft.FontWeight.W_500,
                                color=AppTheme.TEXT_PRIMARY
                            )
                        ],
                        spacing=10
                        ),
                        bgcolor=AppTheme.LIGHT_GREEN,
                        padding=12,
                        border_radius=10,
                        border=ft.border.all(1, AppTheme.URGENCY_LOW + "40")
                    )
                )
        
        page.update()
    
    def on_detect_click(e):
        """Proceed to diagnosis"""
        if not extracted_symptoms:
            page.snack_bar = ft.SnackBar(
                content=ft.Text("Please analyze your symptoms first using the AI button"),
                bgcolor=AppTheme.URGENCY_HIGH
            )
            page.snack_bar.open = True
            page.update()
            return
        
        app_state['selected_symptoms'] = extracted_symptoms.copy()
        app_state['symptom_text'] = symptom_input.value
        navigate_to("result")
    
    return ft.Container(
        content=ft.Column([
            # Modern Header
            ft.Container(
                content=ft.Row([
                    ft.IconButton(
                        icon=Icons.ARROW_BACK_ROUNDED,
                        icon_color=AppTheme.WHITE,
                        icon_size=28,
                        on_click=lambda _: navigate_to("home"),
                        style=ft.ButtonStyle(
                            overlay_color=AppTheme.PRIMARY_TEAL_DARK
                        )
                    ),
                    ft.Text(
                        "Describe Your Symptoms",
                        size=22,
                        weight=ft.FontWeight.BOLD,
                        color=AppTheme.WHITE
                    )
                ],
                spacing=8
                ),
                bgcolor=AppTheme.PRIMARY_TEAL,
                padding=18,
                shadow=ft.BoxShadow(
                    spread_radius=0,
                    blur_radius=12,
                    color=AppTheme.SHADOW_MEDIUM,
                    offset=ft.Offset(0, 3)
                )
            ),
            
            # Main content area
            ft.Container(
                content=ft.Column([
                    # AI Badge
                    ft.Container(
                        content=ft.Row([
                            ft.Icon(Icons.PSYCHOLOGY_ROUNDED, size=24, color=AppTheme.ACCENT_BLUE),
                            ft.Text(
                                "Rule-Based AI Symptom Analyzer",
                                size=16,
                                weight=ft.FontWeight.BOLD,
                                color=AppTheme.TEXT_PRIMARY
                            )
                        ],
                        spacing=10
                        ),
                        bgcolor=AppTheme.LIGHT_AQUA,
                        padding=15,
                        border_radius=12,
                        border=ft.border.all(2, AppTheme.ACCENT_BLUE + "40")
                    ),
                    
                    ft.Container(height=20),
                    
                    # Instructions
                    ft.Container(
                        content=ft.Column([
                            ft.Text(
                                "💬 Tell us how you're feeling",
                                size=17,
                                weight=ft.FontWeight.BOLD,
                                color=AppTheme.TEXT_PRIMARY
                            ),
                            ft.Container(height=5),
                            ft.Text(
                                "Type in natural language and our AI will identify the symptoms automatically.",
                                size=14,
                                color=AppTheme.TEXT_SECONDARY
                            )
                        ])
                    ),
                    
                    ft.Container(height=15),
                    
                    # Text input
                    symptom_input,
                    
                    ft.Container(height=15),
                    
                    # Analyze button
                    ft.Container(
                        content=ft.ElevatedButton(
                            content=ft.Row([
                                ft.Icon(Icons.AUTO_FIX_HIGH_ROUNDED, size=24, color=AppTheme.WHITE),
                                ft.Text("Analyze with AI", size=17, weight=ft.FontWeight.BOLD)
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            spacing=10
                            ),
                            width=340,
                            height=56,
                            bgcolor=AppTheme.ACCENT_BLUE,
                            color=AppTheme.WHITE,
                            elevation=6,
                            on_click=analyze_symptoms,
                            style=ft.ButtonStyle(
                                shape=ft.RoundedRectangleBorder(radius=14),
                            )
                        ),
                        shadow=ft.BoxShadow(
                            spread_radius=0,
                            blur_radius=15,
                            color=AppTheme.ACCENT_BLUE + "35",
                            offset=ft.Offset(0, 5)
                        )
                    ),
                    
                    ft.Container(height=15),
                    
                    # Status text
                    ai_status_text,
                    
                    ft.Container(height=10),
                    
                    # Detected symptoms area
                    ft.Container(
                        content=detected_symptoms_column,
                        padding=5
                    ),
                    
                ],
                scroll=ft.ScrollMode.AUTO
                ),
                expand=True,
                padding=20,
                bgcolor=AppTheme.OFF_WHITE
            ),
            
            # Diagnosis button at bottom
            ft.Container(
                content=ft.Container(
                    content=ft.ElevatedButton(
                        content=ft.Row([
                            ft.Icon(Icons.BIOTECH_ROUNDED, size=26, color=AppTheme.WHITE),
                            ft.Text("Get Diagnosis", size=18, weight=ft.FontWeight.BOLD)
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=12
                        ),
                        width=360,
                        height=62,
                        bgcolor=AppTheme.PRIMARY_TEAL,
                        color=AppTheme.WHITE,
                        elevation=8,
                        on_click=on_detect_click,
                        style=ft.ButtonStyle(
                            shape=ft.RoundedRectangleBorder(radius=16),
                            overlay_color=AppTheme.PRIMARY_TEAL_DARK
                        )
                    ),
                    shadow=ft.BoxShadow(
                        spread_radius=1,
                        blur_radius=20,
                        color=AppTheme.PRIMARY_TEAL + "35",
                        offset=ft.Offset(0, 6)
                    )
                ),
                padding=18,
                bgcolor=AppTheme.WHITE
            )
        ],
        spacing=0,
        expand=True
        ),
        expand=True
    )


# ========================================
# PAGE 3: DIAGNOSIS RESULT PAGE
# ========================================
def create_result_page(page: ft.Page, navigate_to, app_state, diagnosis_engine):
    """Create diagnosis result page"""
    
    selected_symptoms = app_state.get('selected_symptoms', [])
    results = diagnosis_engine.match_symptoms(selected_symptoms)
    
    if not results:
        # No match found
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
                    bgcolor=AppTheme.PRIMARY_TEAL,
                    padding=15
                ),
                ft.Container(
                    content=ft.Column([
                        ft.Icon(Icons.INFO_OUTLINE, size=80, color=AppTheme.DEEP_BLUE),
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
                            bgcolor=AppTheme.PRIMARY_TEAL,
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
    
    # Get top result
    top_result = results[0]
    disease = top_result['disease']
    confidence = top_result['confidence']
    matched_symptoms = top_result['matched_symptoms']
    
    # Get urgency info
    consult_info = disease.get('consultDoctor', {})
    urgency = consult_info.get('urgency', 'medium')
    urgency_color = diagnosis_engine.get_urgency_color(urgency)
    
    # Urgency badge
    if urgency.lower() == "immediate" or urgency.lower() == "critical":
        urgency_text = "🟥 URGENT - Immediate Doctor Visit Required"
    elif urgency.lower() == "high":
        urgency_text = "🟧 HIGH - Consult Doctor Soon"
    else:
        urgency_text = "🟩 MODERATE - Monitor Symptoms"
    
    # Create result content
    result_content = [
        # Modern Header
        ft.Container(
            content=ft.Row([
                ft.IconButton(
                    icon=Icons.ARROW_BACK_ROUNDED,
                    icon_color=AppTheme.WHITE,
                    icon_size=28,
                    on_click=lambda _: navigate_to("symptoms"),
                    style=ft.ButtonStyle(
                        overlay_color=AppTheme.PRIMARY_TEAL_DARK
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
            bgcolor=AppTheme.PRIMARY_TEAL,
            padding=18,
            shadow=ft.BoxShadow(
                spread_radius=0,
                blur_radius=12,
                color=AppTheme.SHADOW_MEDIUM,
                offset=ft.Offset(0, 3)
            )
        ),
        
        # Scrollable content
        ft.Container(
            content=ft.Column([
                # Disease card - Modern design
                ft.Container(
                    content=ft.Column([
                        ft.Row([
                            ft.Icon(
                                Icons.CORONAVIRUS_ROUNDED,
                                size=40,
                                color=AppTheme.PRIMARY_TEAL
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
                                    color=AppTheme.TEXT_MUTED,
                                    weight=ft.FontWeight.W_500
                                )
                            ],
                            spacing=2,
                            expand=True
                            )
                        ],
                        spacing=12
                        ),
                        ft.Container(height=15),
                        # Confidence indicator
                        ft.Container(
                            content=ft.Column([
                                ft.Row([
                                    ft.Text(
                                        "Match Confidence",
                                        size=14,
                                        color=AppTheme.TEXT_SECONDARY,
                                        weight=ft.FontWeight.W_500
                                    ),
                                    ft.Text(
                                        f"{confidence}%",
                                        size=18,
                                        weight=ft.FontWeight.BOLD,
                                        color=AppTheme.PRIMARY_TEAL
                                    )
                                ],
                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                                ),
                                ft.Container(height=8),
                                ft.ProgressBar(
                                    value=confidence / 100,
                                    color=AppTheme.PRIMARY_TEAL,
                                    bgcolor=AppTheme.SOFT_GRAY,
                                    height=8,
                                    border_radius=4
                                )
                            ]),
                            bgcolor=AppTheme.LIGHT_AQUA,
                            padding=15,
                            border_radius=12
                        ),
                        ft.Container(height=12),
                        # Urgency badge - Modern
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
                    padding=24,
                    border_radius=16,
                    border=ft.border.all(1, AppTheme.SOFT_GRAY),
                    shadow=ft.BoxShadow(
                        spread_radius=0,
                        blur_radius=15,
                        color=AppTheme.SHADOW_MEDIUM,
                        offset=ft.Offset(0, 4)
                    )
                ),
                
                # Matched Symptoms - Modern card
                ft.Container(
                    content=ft.Column([
                        ft.Row([
                            ft.Icon(Icons.CHECK_CIRCLE_ROUNDED, size=24, color=AppTheme.URGENCY_LOW),
                            ft.Text(
                                "Matched Symptoms",
                                size=18,
                                weight=ft.FontWeight.BOLD,
                                color=AppTheme.TEXT_PRIMARY
                            )
                        ],
                        spacing=10
                        ),
                        ft.Container(height=12),
                        ft.Column([
                            ft.Container(
                                content=ft.Row([
                                    ft.Icon(Icons.CIRCLE, size=8, color=AppTheme.PRIMARY_TEAL),
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
                    border=ft.border.all(1, AppTheme.SOFT_GRAY),
                    shadow=ft.BoxShadow(
                        spread_radius=0,
                        blur_radius=10,
                        color=AppTheme.SHADOW_COLOR,
                        offset=ft.Offset(0, 3)
                    )
                ),
                
                # Home Remedies
                ft.Container(
                    content=ft.Column([
                        ft.Text(
                            "🏠 Home Remedies",
                            size=18,
                            weight=ft.FontWeight.BOLD,
                            color=AppTheme.DEEP_BLUE
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
                                        color=AppTheme.DEEP_BLUE
                                    )
                                ]),
                                border=ft.border.only(
                                    left=ft.BorderSide(3, AppTheme.CYAN_HIGHLIGHT)
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
                        color=AppTheme.SHADOW_COLOR
                    )
                ),
                
                # Doctor consultation
                ft.Container(
                    content=ft.Column([
                        ft.Text(
                            "👨‍⚕️ When to See a Doctor",
                            size=18,
                            weight=ft.FontWeight.BOLD,
                            color=AppTheme.DEEP_BLUE
                        ),
                        ft.Text(
                            consult_info.get('reason', 'Consult a doctor if symptoms persist.'),
                            size=14
                        ),
                        ft.Text(
                            consult_info.get('condition', ''),
                            size=13,
                            italic=True,
                            color=AppTheme.DEEP_BLUE
                        ) if consult_info.get('condition') else ft.Container()
                    ]),
                    bgcolor=AppTheme.WHITE,
                    padding=15,
                    border_radius=10,
                    shadow=ft.BoxShadow(
                        spread_radius=2,
                        blur_radius=5,
                        color=AppTheme.SHADOW_COLOR
                    )
                ),
                
                # Action buttons
                ft.Container(
                    content=ft.Column([
                        ft.ElevatedButton(
                            content=ft.Row([
                                ft.Icon(Icons.REFRESH, size=20),
                                ft.Text("Restart Diagnosis", size=16)
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            spacing=10
                            ),
                            width=300,
                            height=50,
                            bgcolor=AppTheme.PRIMARY_TEAL,
                            color=AppTheme.WHITE,
                            on_click=lambda _: navigate_to("home")
                        ),
                        ft.OutlinedButton(
                            content=ft.Row([
                                ft.Icon(Icons.LIGHTBULB_OUTLINE, size=20),
                                ft.Text("Learn Prevention Tips", size=16)
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            spacing=10
                            ),
                            width=300,
                            height=50,
                            on_click=lambda _: navigate_to("learn")
                        )
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=15
                    ),
                    padding=ft.padding.only(top=20, bottom=20)
                )
            ],
            spacing=15,
            scroll=ft.ScrollMode.AUTO
            ),
            expand=True,
            padding=15,
            bgcolor=AppTheme.OFF_WHITE
        )
    ]
    
    return ft.Column(
        controls=result_content,
        spacing=0,
        expand=True
    )


# ========================================
# PAGE 4: LEARN & PREVENTION PAGE
# ========================================
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
            # Header
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
                bgcolor=AppTheme.PRIMARY_TEAL,
                padding=15
            ),
            
            # Content
            ft.Container(
                content=ft.Column([
                    # Intro
                    ft.Container(
                        content=ft.Column([
                            ft.Icon(
                                Icons.HEALTH_AND_SAFETY,
                                size=60,
                                color=AppTheme.PRIMARY_TEAL
                            ),
                            ft.Text(
                                "Why Water Safety Matters",
                                size=22,
                                weight=ft.FontWeight.BOLD,
                                color=AppTheme.DEEP_BLUE,
                                text_align=ft.TextAlign.CENTER
                            ),
                            ft.Text(
                                "Water-borne diseases affect millions globally each year. Simple prevention steps can save lives.",
                                size=14,
                                text_align=ft.TextAlign.CENTER,
                                color=AppTheme.DEEP_BLUE
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
                            color=AppTheme.SHADOW_COLOR
                        )
                    ),
                    
                    # Tips section
                    ft.Text(
                        "💧 Prevention Guidelines",
                        size=20,
                        weight=ft.FontWeight.BOLD,
                        color=AppTheme.DEEP_BLUE
                    ),
                    
                    # Tips cards
                    ft.Column([
                        ft.Container(
                            content=ft.Row([
                                ft.Icon(
                                    tip['icon'],
                                    size=30,
                                    color=AppTheme.PRIMARY_TEAL
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
                            border=ft.border.all(2, AppTheme.CYAN_HIGHLIGHT),
                            shadow=ft.BoxShadow(
                                spread_radius=1,
                                blur_radius=3,
                                color=AppTheme.SHADOW_COLOR
                            )
                        )
                        for tip in prevention_tips
                    ],
                    spacing=10
                    ),
                    
                    # Quick facts
                    ft.Container(
                        content=ft.Column([
                            ft.Text(
                                "📊 Quick Facts",
                                size=18,
                                weight=ft.FontWeight.BOLD,
                                color=AppTheme.DEEP_BLUE
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
                        bgcolor=AppTheme.LIGHT_GREEN,
                        padding=15,
                        border_radius=10,
                        border=ft.border.all(2, AppTheme.URGENCY_LOW)
                    ),
                    
                    # Action buttons
                    ft.Container(
                        content=ft.Column([
                            ft.ElevatedButton(
                                content=ft.Text("Start Diagnosis", size=16, weight=ft.FontWeight.BOLD),
                                width=280,
                                height=50,
                                bgcolor=AppTheme.PRIMARY_TEAL,
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
                bgcolor=AppTheme.OFF_WHITE
            )
        ],
        spacing=0,
        expand=True
        ),
        expand=True,
        gradient=ft.LinearGradient(
            begin=ft.alignment.top_center,
            end=ft.alignment.bottom_center,
            colors=[AppTheme.LIGHT_GREEN, AppTheme.WHITE]
        )
    )


# ========================================
# PAGE 5: ABOUT PAGE
# ========================================
def create_about_page(page: ft.Page, navigate_to):
    """Create about/settings page"""
    
    return ft.Container(
        content=ft.Column([
            # Header
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
                bgcolor=AppTheme.PRIMARY_TEAL,
                padding=15
            ),
            
            # Content
            ft.Container(
                content=ft.Column([
                    # Logo
                    ft.Container(
                        content=ft.Column([
                            ft.Icon(
                                Icons.WATER_DROP,
                                size=100,
                                color=AppTheme.PRIMARY_TEAL
                            ),
                            ft.Text(
                                "WaterWise",
                                size=32,
                                weight=ft.FontWeight.BOLD,
                                color=AppTheme.PRIMARY_TEAL
                            ),
                            ft.Text(
                                "Version 1.0",
                                size=14,
                                color=AppTheme.DEEP_BLUE,
                                italic=True
                            )
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=10
                        ),
                        padding=30
                    ),
                    
                    # About section
                    ft.Container(
                        content=ft.Column([
                            ft.Text(
                                "About This App",
                                size=20,
                                weight=ft.FontWeight.BOLD,
                                color=AppTheme.DEEP_BLUE
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
                            color=AppTheme.SHADOW_COLOR
                        )
                    ),
                    
                    # Features
                    ft.Container(
                        content=ft.Column([
                            ft.Text(
                                "✨ Features",
                                size=18,
                                weight=ft.FontWeight.BOLD,
                                color=AppTheme.DEEP_BLUE
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
                            color=AppTheme.SHADOW_COLOR
                        )
                    ),
                    
                    # Disclaimer
                    ft.Container(
                        content=ft.Column([
                            ft.Icon(Icons.WARNING_AMBER, size=40, color=AppTheme.URGENCY_MEDIUM),
                            ft.Text(
                                "Important Disclaimer",
                                size=16,
                                weight=ft.FontWeight.BOLD,
                                color=AppTheme.DEEP_BLUE,
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
                        bgcolor=AppTheme.OFF_WHITE,
                        padding=20,
                        border_radius=10,
                        border=ft.border.all(2, AppTheme.URGENCY_MEDIUM)
                    ),
                    
                    # Credits
                    ft.Container(
                        content=ft.Column([
                            ft.Text(
                                "Credits",
                                size=16,
                                weight=ft.FontWeight.BOLD,
                                color=AppTheme.DEEP_BLUE
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
                            bgcolor=AppTheme.PRIMARY_TEAL,
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
                bgcolor=AppTheme.OFF_WHITE
            )
        ],
        spacing=0,
        expand=True
        ),
        expand=True
    )
