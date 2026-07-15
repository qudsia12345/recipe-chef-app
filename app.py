import streamlit as st
import os
import time
from dotenv import load_dotenv
from groq import Groq

# Load environment state profiles
load_dotenv()

# --- ENTERPRISE CONFIGURATION ENGINE ---
st.set_page_config(
    page_title="AI Recipe Chef & Wellness Tracker",
    page_icon="🍳",
    layout="wide"  # Spacious high-end editorial layout
)

# --- MASTER ADVANCED EUCALYPTUS & CASHMERE CSS ENGINE ---
st.markdown("""
    <style>
        /* Base Background: Luxurious Cashmere Cream Texture */
        .stApp {
            background-image: radial-gradient(circle at 10% 20%, rgb(240, 249, 245) 0%, rgb(247, 252, 247) 90%);
            color: #1F2937 !important;
        }
        
        /* Layout structure customization */
        .block-container {
            padding-top: 3rem !important;
            padding-bottom: 5rem !important;
        }
        
        /* Advanced Editorial Full-Width Header Container */
        .header-container {
            width: 100%;
            background: #FFFFFF;
            border-bottom: 5px solid #0D9488;
            border-radius: 20px 20px 0 0;
            padding: 40px;
            margin-bottom: 40px;
            box-shadow: 0 10px 40px rgba(13, 148, 136, 0.05);
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        
        h1 {
            color: #0F172A !important;
            font-family: 'Inter', sans-serif;
            font-weight: 900 !important;
            letter-spacing: -2px;
            margin: 0 !important;
            font-size: 3rem;
        }
        
        h3, h4 {
            font-family: 'Inter', sans-serif;
            color: #115E59 !important;
            font-weight: 600 !important;
        }
        
        /* --- STRENGTHENED INPUT FIELDS FIX LAYER --- */
        div[data-baseweb="input"] {
            background-color: #FFFFFF !important;
            border: 2px solid #E2E8F0 !important;
            border-radius: 12px !important;
            transition: all 0.3s ease-in-out;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.03) !important;
        }
        
        div[data-baseweb="input"]:focus-within {
            border: 2px solid #14B8A6 !important;
            box-shadow: 0 0 20px rgba(20, 184, 166, 0.2) !important;
        }
        
        /* FORCED BLACK TEXT OVERRIDE FOR INPUT FIELDS */
        input {
            color: #0F172A !important;
            -webkit-text-fill-color: #0F172A !important;
            font-size: 16px !important;
        }
        
        .stTextInput input, .stTextArea textarea {
            color: #0F172A !important;
            -webkit-text-fill-color: #0F172A !important;
            background-color: #FFFFFF !important;
        }
        
        input::placeholder {
            color: #94A3B8 !important;
            -webkit-text-fill-color: #94A3B8 !important;
        }
        
        /* --- ULTRA STRICT SELECTBOX DROPDOWN OVERRIDES --- */
        div[data-baseweb="select"], 
        div[data-baseweb="select"] > div,
        .stSelectbox > div {
            background-color: #FFFFFF !important;
            border-radius: 12px !important;
        }
        
        div[data-baseweb="select"] {
            border: 2px solid #E2E8F0 !important;
        }
        
        div[data-baseweb="select"] div,
        div[data-baseweb="select"] span,
        div[data-baseweb="select"] p,
        .stSelectbox p,
        .stSelectbox span,
        .stSelectbox div {
            color: #0F172A !important;
            -webkit-text-fill-color: #0F172A !important;
        }
        
        ul[role="listbox"], ul[role="listbox"] li {
            background-color: #FFFFFF !important;
            color: #0F172A !important;
        }
        
        /* Luxury Solid State Button Style */
        .stButton>button {
            background: #0D9488 !important;
            color: #FFFFFF !important;
            border: none !important;
            border-radius: 12px !important;
            padding: 14px 28px !important;
            font-weight: 700 !important;
            width: 100%;
            transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
            box-shadow: 0 6px 18px rgba(13, 148, 136, 0.25);
            text-transform: uppercase;
            letter-spacing: 1px;
            font-size: 14px;
        }
        
        .stButton>button:hover {
            transform: translateY(-2px);
            background: #115E59 !important;
            box-shadow: 0 10px 25px rgba(13, 148, 136, 0.35);
        }
        
        /* High-End Frosted Display Cards */
        .recipe-box {
            background: #FFFFFF;
            border: 1px solid #E2E8F0;
            border-left: 6px solid #14B8A6;
            border-radius: 18px;
            padding: 30px;
            margin-top: 25px;
            box-shadow: 0 15px 45px rgba(0, 0, 0, 0.06);
            color: #374151 !important;
            font-size: 16px;
            line-height: 1.7;
        }
        
        label, [data-testid="stWidgetLabel"] p {
            color: #374151 !important;
            -webkit-text-fill-color: #374151 !important;
            font-weight: 600 !important;
            font-size: 14px !important;
        }
    </style>
""", unsafe_allow_html=True)

# --- TITLE HEADER ARCHITECTURE ---
st.markdown("""
    <div class="header-container">
        <div>
            <p style="color: #0D9488; font-weight: 700; letter-spacing: 2.5px; margin: 0 0 6px 0; font-size: 11px; text-transform: uppercase;">⚡ DESI WELLNESS SCHEMATIC</p>
            <h1>Pakistani Recipe Chef & Wellness Tracker</h1>
            <p style="color: #6B7280; margin: 12px 0 0 0; font-size: 15px; line-height: 1.6; max-width: 600px;">
                Input your current pantry assets to generate real-time traditional Pakistani culinary formulas with advanced macro and caloric breakdown analytics.
            </p>
        </div>
        <div style="font-size: 5rem; color: #CCFBF1; opacity: 0.8; padding-right: 20px;">🍲</div>
    </div>
""", unsafe_allow_html=True)

# --- INSTANTIATE API CLIENT CORE ---
api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key) if api_key else None

# --- CORE USER INTERFACE CONTROL LAYER ---
st.write("### 🛒 Pantry Input Node")

col1, col2, col3 = st.columns([2, 1, 1])

with col1:
    ingredients = st.text_input("Ingredients Available", placeholder="e.g., Chicken, Rice, Whole wheat flour, Tomatoes, Garlic...")
    
with col2:
    # ADDED "Weight Loss" AND "Weight Gain" OPTIONS HERE
    diet_type = st.selectbox("Dietary Goal", ["No Restrictions", "Weight Loss", "Weight Gain", "High Fiber", "Low Carb", "High Protein", "Keto", "Vegetarian"])

with col3:
    recipe_style = st.selectbox("Recipe Category", ["Gravy", "Rice", "Chapati", "Salad", "Puree", "Soups"])

st.markdown("<br>", unsafe_allow_html=True)
generate_btn = st.button("Initialize Pakistani Culinary Process 🍳")

# --- EXECUTION LOGIC MATRIX ---
if generate_btn:
    if not ingredients:
        st.error("Validation Core Failure: Ingredients matrix cannot be null.")
    elif not client:
        st.error("Infrastructure Error: API Key engine activation failed or node unreachable.")
    else:
        system_prompt = f"""
        You are an Elite AI Culinary Chef specializing in traditional Pakistani Cuisine and a Wellness Nutritionist. 
        Your goal is to synthesize a high-quality, authentic, and realistic Pakistani recipe using primarily the specific ingredients provided by the user.
        
        Strict Style Constraints:
        - The recipe MUST be format-optimized as a Pakistani **{recipe_style}** dish. 
        - You must strictly adhere to the specified Dietary Goal: {diet_type} while keeping the recipe completely Pakistani in taste and style.
          * If 'Weight Loss' is selected, make the recipe low-calorie, nutrient-dense, and control oil/fat usage strictly.
          * If 'Weight Gain' is selected, include healthy high-calorie Pakistani options (like using healthy nuts, full-fat dairy, or proper portion enhancements).
        - Your response must include an estimated Calorie and Macronutrient breakdown profile (Protein, Carbs, Fats, Fiber) at the very end.
        
        Strict Presentation Guidelines:
        1. Format your response with an introductory sentence and the traditional Pakistani recipe title in **bold**.
        2. Give a clear section for "**Ingredients Grid**" (including typical Pakistani spices needed).
        3. Give a clear section for "**Procedural Synthesis Steps**" (Desi cooking style aligned with the category {recipe_style}).
        4. Give a clear section for "**Nutritional Analysis Profile**" (Clearly state Total Calories and whether it matches the goal: {diet_type}).
        5. The overall tone must be highly professional, structured, and easy to read.
        """
        
        user_prompt = f"Pakistani ingredients available: {ingredients}. Specified Dietary Goal: {diet_type}. Category requested: {recipe_style}."
        
        with st.spinner("Synthesizing Pakistani culinary formulas and analytics..."):
            try:
                time.sleep(1.2)
                completion = client.chat.completions.create(
                    model="llama-3.1-8b-instant",
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": user_prompt}
                    ],
                    temperature=0.3
                )
                
                ai_response = completion.choices[0].message.content
                
                st.markdown("<br>", unsafe_allow_html=True)
                st.write("### 📜 Traditional Desi Culinary Formula")
                st.markdown(f'<div class="recipe-box">{ai_response}</div>', unsafe_allow_html=True)
                
            except Exception as e:
                st.error(f"Inference Engine Failure: {str(e)}")
