import json
from typing import List, Dict

# ========================================
# PROFESSIONAL COLOR THEME
# ========================================
class AppTheme:
    # Primary - Medical Blue Palette
    PRIMARY = "#2563EB"  # Professional Blue
    PRIMARY_DARK = "#1E40AF"
    PRIMARY_LIGHT = "#3B82F6"
    PRIMARY_GRADIENT_START = "#2563EB"
    PRIMARY_GRADIENT_END = "#7C3AED"
    
    # Accent Colors
    ACCENT = "#8B5CF6"  # Purple accent
    ACCENT_TEAL = "#14B8A6"  # Teal
    ACCENT_EMERALD = "#10B981"
    
    # Medical Status Colors
    STATUS_CRITICAL = "#DC2626"
    STATUS_WARNING = "#F59E0B"
    STATUS_SUCCESS = "#10B981"
    STATUS_INFO = "#3B82F6"
    
    # Neutral Palette
    WHITE = "#FFFFFF"
    BACKGROUND = "#F8FAFC"  # Slate-50
    SURFACE = "#F1F5F9"  # Slate-100
    CARD = "#FFFFFF"
    
    # Text Hierarchy
    TEXT_PRIMARY = "#0F172A"  # Slate-900
    TEXT_SECONDARY = "#475569"  # Slate-600
    TEXT_TERTIARY = "#94A3B8"  # Slate-400
    TEXT_DISABLED = "#CBD5E1"  # Slate-300
    
    # Borders & Dividers
    BORDER = "#E2E8F0"  # Slate-200
    BORDER_FOCUS = "#2563EB"
    DIVIDER = "#F1F5F9"
    
    # Shadows (premium depth)
    SHADOW_SM = "#0000000A"
    SHADOW_MD = "#00000012"
    SHADOW_LG = "#0000001A"
    SHADOW_XL = "#00000025"
    SHADOW_STRONG = "#00000035"


# ========================================
# DATA LOADER
# ========================================
def load_diseases_data():
    """Load diseases data from JSON file"""
    try:
        with open('diseases.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {
            "metadata": {"version": "1.0", "totalDiseases": 0},
            "diseases": []
        }


# ========================================
# DIAGNOSIS ENGINE
# ========================================
class DiagnosisEngine:
    def __init__(self, diseases_data):
        self.diseases_data = diseases_data
        self.diseases = diseases_data.get('diseases', [])
    
    def match_symptoms(self, selected_symptoms: List[str]) -> List[Dict]:
        """
        Match selected symptoms against disease database
        Returns list of matches with confidence scores
        """
        results = []
        
        for disease in self.diseases:
            # Extract disease symptoms
            disease_symptoms = [s['symptom'].lower() for s in disease['symptoms']]
            
            # Calculate match score
            matched = []
            for selected in selected_symptoms:
                for disease_symptom in disease['symptoms']:
                    if selected.lower() in disease_symptom['symptom'].lower():
                        matched.append(disease_symptom)
                        break
            
            if matched:
                match_count = len(matched)
                total_disease_symptoms = len(disease['symptoms'])
                confidence = (match_count / total_disease_symptoms) * 100
                
                results.append({
                    'disease': disease,
                    'matched_symptoms': matched,
                    'confidence': round(confidence, 1),
                    'match_count': match_count
                })
        
        # Sort by confidence (highest first)
        results.sort(key=lambda x: x['confidence'], reverse=True)
        return results
    
    def get_urgency_color(self, urgency: str) -> str:
        """Return color based on urgency level"""
        urgency_lower = urgency.lower()
        if urgency_lower == "immediate" or urgency_lower == "critical":
            return AppTheme.STATUS_CRITICAL
        elif urgency_lower == "high":
            return AppTheme.STATUS_WARNING
        else:
            return AppTheme.STATUS_SUCCESS


# ========================================
# RULE-BASED AI - SYMPTOM EXTRACTION
# ========================================

# Master symptom database with variations and keywords
SYMPTOM_DATABASE = {
    "Diarrhea": ["diarrhea", "loose stool", "watery stool", "frequent stool", "runny stool", "upset stomach"],
    "Vomiting": ["vomit", "vomiting", "throwing up", "puke", "puking", "nausea and vomiting"],
    "Nausea": ["nausea", "nauseous", "queasy", "sick feeling", "feel sick"],
    "Fever": ["fever", "high temperature", "hot", "burning up", "temperature", "febrile"],
    "Dehydration": ["dehydration", "dehydrated", "thirsty", "dry mouth", "dizzy"],
    "Stomach cramps": ["stomach cramp", "stomach pain", "belly pain", "abdominal cramp", "tummy ache"],
    "Abdominal pain": ["abdominal pain", "stomach ache", "belly ache", "gut pain"],
    "Bloating": ["bloat", "bloating", "swollen belly", "gas", "gassy", "distended"],
    "Headache": ["headache", "head pain", "head hurts", "migraine"],
    "Fatigue": ["fatigue", "tired", "exhausted", "weak", "weakness", "no energy", "lethargy"],
    "Body pain": ["body pain", "body ache", "muscle pain", "joint pain", "aching"],
    "Leg cramps": ["leg cramp", "leg pain", "calf pain"],
    "Jaundice": ["jaundice", "yellow eyes", "yellow skin", "yellowish", "yellowing"],
    "Dark urine": ["dark urine", "brown urine", "tea colored urine", "dark pee"],
    "Loss of appetite": ["no appetite", "loss of appetite", "don't want to eat", "not hungry"],
    "Rash": ["rash", "skin rash", "red spots", "skin irritation"],
    "Rapid dehydration": ["rapid dehydration", "severe dehydration", "very dehydrated"],
    "Greasy stools": ["greasy stool", "oily stool", "fatty stool"],
    "Loose stools": ["loose stool", "soft stool"],
    "Whitish tongue coating": ["white tongue", "coated tongue", "whitish tongue"]
}

# Common symptoms list for reference
COMMON_SYMPTOMS = list(SYMPTOM_DATABASE.keys())


class SymptomExtractor:
    """Rule-based AI for extracting symptoms from natural language text"""
    
    def __init__(self):
        self.symptom_db = SYMPTOM_DATABASE
    
    def extract_symptoms(self, text: str) -> List[str]:
        """
        Extract symptoms from user input text using rule-based matching
        Returns list of matched symptom names
        """
        if not text:
            return []
        
        # Normalize input
        text_lower = text.lower().strip()
        matched_symptoms = []
        
        # Rule 1: Direct keyword matching
        for symptom, keywords in self.symptom_db.items():
            for keyword in keywords:
                if keyword in text_lower:
                    if symptom not in matched_symptoms:
                        matched_symptoms.append(symptom)
                    break
        
        # Rule 2: Handle common phrases
        # "I have X" or "I'm experiencing X"
        phrases = [
            "i have", "i've got", "i am experiencing", "i'm experiencing",
            "suffering from", "feeling", "i feel", "having"
        ]
        
        for phrase in phrases:
            if phrase in text_lower:
                # Additional context-based extraction
                parts = text_lower.split(phrase)
                if len(parts) > 1:
                    symptom_part = parts[1].split('.')[0].split(',')[0].strip()
                    # Check this part against keywords
                    for symptom, keywords in self.symptom_db.items():
                        for keyword in keywords:
                            if keyword in symptom_part:
                                if symptom not in matched_symptoms:
                                    matched_symptoms.append(symptom)
                                break
        
        return matched_symptoms
    
    def get_symptom_confidence(self, text: str, symptom: str) -> float:
        """
        Calculate confidence score for a matched symptom
        Higher score = more explicit mention
        """
        text_lower = text.lower()
        keywords = self.symptom_db.get(symptom, [])
        
        # Count keyword occurrences
        count = sum(1 for keyword in keywords if keyword in text_lower)
        
        # Normalize to 0-1 score
        return min(count / len(keywords), 1.0) if keywords else 0.0
