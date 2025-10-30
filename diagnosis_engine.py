import json
from typing import List, Dict


class AppTheme:
    
    PRIMARY = "#2563EB"  
    PRIMARY_DARK = "#1E40AF"
    PRIMARY_LIGHT = "#3B82F6"
    PRIMARY_GRADIENT_START = "#2563EB"
    PRIMARY_GRADIENT_END = "#7C3AED"
    
    
    ACCENT = "#8B5CF6"  
    ACCENT_TEAL = "#14B8A6"  
    ACCENT_EMERALD = "#10B981"
    STATUS_CRITICAL = "#DC2626"
    STATUS_WARNING = "#F59E0B"
    STATUS_SUCCESS = "#10B981"
    STATUS_INFO = "#3B82F6"
    

    WHITE = "#FFFFFF"
    BACKGROUND = "#F8FAFC" 
    SURFACE = "#F1F5F9" 
    CARD = "#FFFFFF"
    
    TEXT_PRIMARY = "#0F172A"  
    TEXT_SECONDARY = "#475569" 
    TEXT_TERTIARY = "#94A3B8" 
    TEXT_DISABLED = "#CBD5E1" 
    
  
    BORDER = "#E2E8F0" 
    BORDER_FOCUS = "#2563EB"
    DIVIDER = "#F1F5F9"
    
    
    SHADOW_SM = "#0000000A"
    SHADOW_MD = "#00000012"
    SHADOW_LG = "#0000001A"
    SHADOW_XL = "#00000025"
    SHADOW_STRONG = "#00000035"




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
            
            disease_symptoms = [s['symptom'].lower() for s in disease['symptoms']]
            
            
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





SYMPTOM_DATABASE = {
    "Diarrhea": ["diarrhea", "loose stool", "watery stool", "frequent stool", "runny stool", "upset stomach"],
    "Vomiting": ["vomit", "vomiting", "throwing up", "puke", "puking", "nausea and vomiting"],
    "Nausea": ["nausea", "nauseous", "queasy", "sick feeling", "feel sick"],
    "Fever": ["fever", "high temperature", "hot", "burning up", "temperature", "febrile"],
    "Dehydration": [
        "dehydration", "dehydrated", "thirsty", "dry mouth", "dizzy",
        "dizziness", "lightheaded", "light-headed", "light headed",
        "dry lips", "sunken eyes"
    ],
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

COMMON_SYMPTOMS = list(SYMPTOM_DATABASE.keys())


class SymptomExtractor:
    """Intelligent rule-based extractor with severity and negation awareness"""
    
    def __init__(self):
        self.symptom_db = SYMPTOM_DATABASE
        

        self.mild_modifiers = [
            "mild", "slight", "slightly", "minor", "low-grade", "low grade",
            "little bit", "a bit", "bit of", "somewhat", "occasionally", "little"
        ]
        self.severe_modifiers = [
            "severe", "intense", "extreme", "very bad", "terrible", "awful",
            "serious", "constant", "persistent", "chronic", "unbearable", "excruciating"
        ]
        
        self.negations = ["no ", "not ", "without ", "denies ", "deny ", "never ", "lack of "]
    
    def extract_symptoms(self, text: str) -> List[str]:
        """
        Extract symptoms with severity & negation filtering.
        Filters out clearly mild or negated symptom mentions.
        """
        if not text:
            return []
        
        text_lower = text.lower().strip()
        matched_symptoms: List[str] = []
        
        segments: List[str] = []
        tmp = text_lower.replace(";", ",")
        tmp = tmp.replace(" and ", ",")
        for part in tmp.split(","):
            p = part.strip()
            if p:
                segments.append(p)
        if not segments:
            segments = [text_lower]
        
        for segment in segments:
            for symptom, keywords in self.symptom_db.items():
                for keyword in keywords:
                    if keyword in segment:
                        if self._is_negated(segment, keyword):
                            continue
                        if self._is_mild_symptom(segment, keyword):
                            continue
                        if symptom not in matched_symptoms:
                            matched_symptoms.append(symptom)
                        break
        
        return matched_symptoms
    
    def _is_negated(self, text: str, symptom_keyword: str) -> bool:
        """Return True if a negation appears near the symptom mention."""
        pos = text.find(symptom_keyword)
        if pos == -1:
            return False
        window = text[max(0, pos - 25):pos + len(symptom_keyword)]
        return any(n in window for n in self.negations)
    
    def _is_mild_symptom(self, text: str, symptom_keyword: str) -> bool:
        """Return True if the symptom appears with a mild-intensity modifier nearby."""
        pos = text.find(symptom_keyword)
        if pos == -1:
            return False
        start = max(0, pos - 32)
        end = min(len(text), pos + len(symptom_keyword) + 32)
        context = text[start:end]
        
        for mild in self.mild_modifiers:
            if mild in context:
                mpos = context.find(mild)
                kpos = context.find(symptom_keyword)
                if abs(mpos - kpos) < 22:
                    return True
        
        for sev in self.severe_modifiers:
            if sev in context:
                return False
        
        return False
    
    def get_symptom_confidence(self, text: str, symptom: str) -> float:
        """
        Calculate confidence score for a matched symptom
        Higher score = more explicit mention
        """
        text_lower = text.lower()
        keywords = self.symptom_db.get(symptom, [])
        
        count = sum(1 for keyword in keywords if keyword in text_lower)
        
        return min(count / len(keywords), 1.0) if keywords else 0.0
