import json
from typing import List, Dict

# ========================================
# COLOR THEME CONSTANTS
# ========================================
class AppTheme:
    # Primary Colors - More vibrant and modern
    PRIMARY_TEAL = "#0891B2"  # Cyan-600
    PRIMARY_TEAL_DARK = "#0E7490"  # Cyan-700
    PRIMARY_TEAL_LIGHT = "#06B6D4"  # Cyan-500
    DEEP_BLUE = "#0C4A6E"  # Sky-900
    LIGHT_AQUA = "#ECFEFF"  # Cyan-50
    CYAN_HIGHLIGHT = "#22D3EE"  # Cyan-400
    ACCENT_BLUE = "#3B82F6"  # Blue-500
    
    # Urgency Colors - More vibrant
    URGENCY_HIGH = "#EF4444"  # Red-500
    URGENCY_MEDIUM = "#F59E0B"  # Amber-500
    URGENCY_LOW = "#10B981"  # Emerald-500
    
    # Background Colors
    WHITE = "#FFFFFF"
    OFF_WHITE = "#F8FAFC"  # Slate-50
    LIGHT_GREEN = "#ECFDF5"  # Emerald-50
    SOFT_GRAY = "#F1F5F9"  # Slate-100
    
    # Text Colors
    TEXT_PRIMARY = "#0F172A"  # Slate-900
    TEXT_SECONDARY = "#475569"  # Slate-600
    TEXT_MUTED = "#94A3B8"  # Slate-400
    
    # Shadow
    SHADOW_COLOR = "#00000015"
    SHADOW_MEDIUM = "#00000025"
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
            return AppTheme.URGENCY_HIGH
        elif urgency_lower == "high":
            return AppTheme.URGENCY_MEDIUM
        else:
            return AppTheme.URGENCY_LOW


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
