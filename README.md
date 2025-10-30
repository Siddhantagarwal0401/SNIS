# 💧 WaterWise - Water-borne Disease Detection App

A rule-based AI application for early detection of water-borne diseases through symptom analysis.

## Features

### 🤖 **Rule-Based AI Symptom Analyzer**
- **Natural Language Processing**: Type your symptoms in plain English (e.g., "I have fever, diarrhea, and feeling weak")
- **Intelligent Keyword Extraction**: AI automatically identifies and extracts symptoms from your description
- **Multi-keyword Recognition**: Understands variations like "vomiting", "throwing up", "puking"
- **Context-Aware Parsing**: Recognizes phrases like "I have", "I'm experiencing", "suffering from"
- **Real-time Feedback**: Instant visual confirmation of detected symptoms

### 💊 **Smart Diagnosis Engine**
- **Symptom-based Matching**: Advanced rule-based algorithm matches extracted symptoms against disease database
- **Confidence Scoring**: Percentage-based confidence levels for accurate predictions
- **Multi-disease Detection**: Ranks all possible matches by confidence score
- **Urgency Indicators**: Color-coded urgency levels (Critical, High, Medium)

### 🏥 **Comprehensive Health Information**
- **Home Remedies**: Detailed remedy suggestions with instructions and frequency
- **Doctor Consultation Guidelines**: Clear urgency indicators for when to seek medical help
- **Prevention Education**: Evidence-based water safety and hygiene tips
- **Disease Categories**: Bacterial, viral, and parasitic disease classification

### 🎨 **Modern User Experience**
- **Beautiful UI**: Professional gradient backgrounds, card-based layouts, smooth shadows
- **Mobile-First Design**: Responsive layout optimized for all screen sizes
- **Intuitive Navigation**: Multi-page flow with clear visual hierarchy
- **Accessibility**: High contrast colors and readable typography

## Tech Stack

- **Framework**: Flet (Python)
- **Architecture**: Rule-based matching engine
- **Data Format**: JSON
- **Design**: Material Design with custom color theme

## Installation

1. **Install Python 3.8+** (if not already installed)

2. **Install dependencies**:
```bash
pip install -r requirements.txt
```

## Running the App

```bash
python waterwise_app.py
```

The app will open in a new window. You can also run it in web mode:

```bash
flet run waterwise_app.py --web
```

## Project Structure

```
.
├── waterwise_app.py       # Main application entry point
├── pages.py               # All page components (Welcome, Symptoms, Result, Learn, About)
├── diagnosis_engine.py    # Rule engine and disease matching logic
├── diseases.json          # Disease database with symptoms and remedies
├── requirements.txt       # Python dependencies
└── README.md             # This file
```

## How It Works

### 1. **Welcome Page**
- Introduction to the app
- Options to start diagnosis or learn prevention tips

### 2. **Symptom Input Page**
- Select from 20+ common symptoms
- Validates at least one symptom is selected
- Stores selections for diagnosis

### 3. **Diagnosis Result Page**
- Displays most likely disease based on symptom matching
- Shows confidence percentage
- Lists matched symptoms
- Provides home remedies with detailed instructions
- Indicates when to see a doctor with urgency level

### 4. **Learn & Prevention Page**
- Water safety guidelines
- Prevention tips with icons
- Quick facts about water-borne diseases

### 5. **About Page**
- App information and version
- Features list
- Important medical disclaimer
- Credits

## Rule-Based AI Architecture

### Symptom Extraction Engine

The AI uses a sophisticated rule-based approach with multiple layers:

**Layer 1: Keyword Database**
- 20+ symptom categories with 5-7 keyword variations each
- Examples: "diarrhea" → ["diarrhea", "loose stool", "watery stool", "runny stool"]
- Covers medical terms, colloquial language, and common misspellings

**Layer 2: Direct Keyword Matching**
- Normalizes user input (lowercase, trim whitespace)
- Scans text for exact keyword matches
- Prevents duplicate symptom detection

**Layer 3: Context-Aware Phrase Recognition**
- Identifies common symptom descriptions: "I have", "experiencing", "feeling"
- Extracts symptom context from surrounding words
- Handles sentence structure variations

**Layer 4: Confidence Scoring**
- Calculates symptom relevance based on keyword frequency
- Returns normalized 0-1 confidence scores

### Diagnosis Matching Engine

**Step 1: Symptom Extraction**
```
User Input: "I have fever, diarrhea, and vomiting"
AI Output: ["Fever", "Diarrhea", "Vomiting"]
```

**Step 2: Disease Matching**
- Compares extracted symptoms against 5 disease profiles
- Each disease has 4-7 documented symptoms

**Step 3: Confidence Calculation**
```
Confidence = (Matched Symptoms / Total Disease Symptoms) × 100
```

**Step 4: Ranking & Display**
- Sorts diseases by confidence score (highest first)
- Returns top match with full details
- Includes urgency mapping for medical guidance

## Disease Database

Currently includes 5 major water-borne diseases:

1. **Cholera** (Bacterial, Critical)
2. **Typhoid** (Bacterial, High)
3. **Giardiasis** (Parasitic, Medium)
4. **Amoebiasis** (Parasitic, High)
5. **Hepatitis A** (Viral, High)

Each disease entry includes:
- Unique ID
- Category and severity level
- Symptoms with individual severity ratings
- Home remedies with instructions and frequency
- Doctor consultation guidelines

## Color Theme

- **Primary Teal**: `#009688` - Main brand color
- **Deep Blue**: `#004D40` - Text and accents
- **Light Aqua**: `#E0F7FA` - Backgrounds
- **Urgency High**: `#E53935` (Red)
- **Urgency Medium**: `#FB8C00` (Orange)
- **Urgency Low**: `#43A047` (Green)

## Customization

### Adding New Diseases

Edit `diseases.json` and add a new disease object following this structure:

```json
{
  "id": "disease_006",
  "name": "Disease Name",
  "category": "bacterial|viral|parasitic",
  "severity": "critical|high|medium|low",
  "transmission": "waterborne",
  "symptoms": [
    {
      "symptom": "Symptom description",
      "severity": "critical|high|medium|low"
    }
  ],
  "homeRemedies": [
    {
      "remedy": "Remedy name",
      "instructions": "How to use it",
      "frequency": "How often"
    }
  ],
  "consultDoctor": {
    "required": true,
    "urgency": "immediate|high|medium",
    "reason": "Explanation"
  }
}
```

### Adding New Symptoms

Edit `COMMON_SYMPTOMS` list in `diagnosis_engine.py`

## Disclaimer

**This app is for informational and educational purposes only.**

It does not provide medical advice, diagnosis, or treatment. Always seek the advice of your physician or other qualified health provider with any questions you may have regarding a medical condition. Never disregard professional medical advice or delay in seeking it because of something you have read in this app.

## Future Enhancements

- Symptom severity sliders
- Multi-disease suggestions (top 2-3 matches)
- Local language support (Hindi, regional languages)
- Dark mode
- Offline persistence
- Export/share diagnosis results

## Built For

Hackathon 2025 | Version 1.0

## License

MIT License - Built for educational purposes
