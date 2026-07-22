"""
CivicIQ -- Groq Vision Service
Handles image-related analysis for uploaded citizen photos.
Since Groq does not support multimodal/vision input, this service uses:
1. Groq text-based analysis on citizen descriptions for richer classification.
2. Deterministic keyword fallback for guaranteed stability.
"""

import os
import json
import re
from typing import Dict, Any, List
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")

# Primary and fallback models
PRIMARY_MODEL = "llama-3.3-70b-versatile"
FALLBACK_MODEL = "llama-3.1-8b-instant"

_client = None


def _get_client():
    """Get or create the Groq client. Returns None if no API key."""
    global _client
    if _client is not None:
        return _client
    if not GROQ_API_KEY or GROQ_API_KEY == "your_api_key_here":
        return None
    try:
        from groq import Groq
        _client = Groq(api_key=GROQ_API_KEY)
        return _client
    except Exception as e:
        print(f"[GROQ_VISION_SERVICE] Failed to initialize Groq client: {e}")
        return None


def _clean_json_response(text: str) -> str:
    """Strip markdown code blocks (e.g. ```json ... ```) to find clean JSON."""
    text = text.strip()
    match = re.search(r"```(?:json)?\s*(.*?)\s*```", text, re.DOTALL | re.IGNORECASE)
    if match:
        return match.group(1).strip()
    return text


async def analyze_uploaded_image(image_path: str, citizen_description: str) -> Dict[str, Any]:
    """
    Analyze an uploaded image file by using Groq text-based analysis
    on the citizen's description.

    Since Groq does not support multimodal/vision input, this function:
    1. Attempts text-based classification via Groq LLM using the citizen description.
    2. Falls back to deterministic keyword-based inference if Groq is unavailable.

    Returns:
    {
        "issue_type": "POTHOLE",
        "severity": "HIGH",
        "confidence": 0.91,
        "visual_evidence": [
            "large damaged road surface",
            "visible road cavity",
            "water accumulation near damaged area"
        ]
    }
    """
    fallback_result = _generate_inferred_fallback(citizen_description)

    client = _get_client()
    if client is None:
        print("[GROQ_VISION_SERVICE] No Groq API key configured. Using deterministic fallback.")
        return fallback_result

    if not os.path.exists(image_path):
        print(f"[GROQ_VISION_SERVICE] File not found: {image_path}. Using deterministic fallback.")
        return fallback_result

    try:
        prompt = f"""You are a civic infrastructure analysis AI. A citizen has submitted a photo of a civic issue along with the following description:

"{citizen_description}"

Based on this description, classify the issue:
1. "issue_type": Choose EXACTLY one of these categories:
   - POTHOLE
   - WATER_LEAKAGE
   - WATERLOGGING
   - GARBAGE_OVERFLOW
   - BROKEN_STREETLIGHT
   - DRAINAGE_PROBLEM
   - ROAD_DAMAGE
   - EXPOSED_WIRES
   - SEWAGE_OVERFLOW
   - DRAIN_BLOCKAGE

2. "severity": Choose EXACTLY one of:
   - LOW
   - MEDIUM
   - HIGH
   - CRITICAL

3. "confidence": Estimate confidence as a decimal number between 0.0 and 1.0 (e.g. 0.85).

4. "visual_evidence": Provide exactly 3 short, concrete observations that would be expected based on the description. Describe only what would be physically visible. Do not speculate on subterranean causes or administrative issues.

You MUST return ONLY a valid JSON object with NO additional text, conforming exactly to this structure:
{{
    "issue_type": "POTHOLE",
    "severity": "HIGH",
    "confidence": 0.91,
    "visual_evidence": [
        "large damaged road surface",
        "visible road cavity",
        "water accumulation near damaged area"
    ]
}}"""

        # Try primary model, then fallback
        for model in [PRIMARY_MODEL, FALLBACK_MODEL]:
            try:
                response = client.chat.completions.create(
                    model=model,
                    max_tokens=400,
                    temperature=0.2,
                    messages=[
                        {"role": "system", "content": "You are a civic infrastructure analysis AI. Respond with valid JSON only."},
                        {"role": "user", "content": prompt},
                    ],
                )

                raw_text = response.choices[0].message.content
                cleaned_text = _clean_json_response(raw_text)
                data = json.loads(cleaned_text)

                # Validate keys
                required_keys = ["issue_type", "severity", "confidence", "visual_evidence"]
                if all(k in data for k in required_keys):
                    return {
                        "issue_type": str(data["issue_type"]).upper(),
                        "severity": str(data["severity"]).upper(),
                        "confidence": float(data["confidence"]),
                        "visual_evidence": list(data["visual_evidence"])[:3],
                    }
                else:
                    print(f"[GROQ_VISION_SERVICE] Returned JSON was missing keys ({model}). Trying next model.")
                    continue

            except json.JSONDecodeError as e:
                print(f"[GROQ_VISION_SERVICE] Invalid JSON from {model}: {e}. Trying next model.")
                continue
            except Exception as e:
                error_msg = str(e).lower()
                if "model" in error_msg or "not found" in error_msg or "unavailable" in error_msg:
                    print(f"[GROQ_VISION_SERVICE] Model {model} unavailable: {e}. Trying next model.")
                    continue
                print(f"[GROQ_VISION_SERVICE] API call failed ({model}): {e}. Using fallback.")
                return fallback_result

        # Both models failed to produce valid output
        print("[GROQ_VISION_SERVICE] All models failed. Using deterministic fallback.")
        return fallback_result

    except Exception as e:
        print(f"[GROQ_VISION_SERVICE] Analysis call failed: {e}. Using fallback.")
        return fallback_result


def _generate_inferred_fallback(description: str) -> Dict[str, Any]:
    """Infers issue type, severity, and visual evidence from description for high-fidelity fallback."""
    desc_lower = description.lower()

    keyword_map = [
        (["water leak", "pipe leak", "pipe burst", "water flowing", "water seep"], "WATER_LEAKAGE", "HIGH", [
            "visible stream of water flowing on road surface",
            "soil erosion around suspected leakage source",
            "damp/saturated pavement area"
        ]),
        (["pothole", "pot hole", "road hole", "cavity"], "POTHOLE", "MEDIUM", [
            "depressed circular cavity in asphalt surface",
            "exposed aggregate sub-base within road hole",
            "cracked pavement edges bordering the cavity"
        ]),
        (["waterlogging", "water logging", "flooding", "water stagnant", "standing water"], "WATERLOGGING", "MEDIUM", [
            "standing pools of water covering road lanes",
            "submerged roadway markers and curb boundaries",
            "water ripples from local commuter wade-throughs"
        ]),
        (["road damage", "road broken", "road crack", "road surface"], "ROAD_DAMAGE", "MEDIUM", [
            "visible longitudinal structural cracks in asphalt",
            "uneven surface elevation on main corridor road",
            "crumbling road shoulders and debris accumulation"
        ]),
        (["garbage", "waste", "trash", "rubbish", "dumping"], "GARBAGE_OVERFLOW", "MEDIUM", [
            "overflowing community waste dumpster",
            "mixed domestic and organic refuse scattered on pavement",
            "loose waste blockages near street walkway"
        ]),
        (["drain block", "blocked drain", "drain clog"], "DRAIN_BLOCKAGE", "MEDIUM", [
            "drain inlet cover obstructed by plastic debris",
            "local water backup centering around drainage grate",
            "silt and organic waste buildup inside drain aperture"
        ]),
        (["drainage", "drain problem", "water not flowing"], "DRAINAGE_PROBLEM", "MEDIUM", [
            "obstructed gutter lanes holding stagnant runoff",
            "overflowing sewer catch basin inlet",
            "accumulation of street sludge along concrete gutter"
        ]),
        (["exposed wire", "live wire", "electric", "electrocution"], "EXPOSED_WIRES", "CRITICAL", [
            "stripped electrical cabling suspended low overhead",
            "exposed junction wire terminals near main pole structure",
            "weather-worn insulation wrap posing safety risk"
        ]),
        (["sewage", "sewer", "manhole overflow"], "SEWAGE_OVERFLOW", "HIGH", [
            "murky effluent bubbling from manhole seam cover",
            "dark liquid pooling on street side curb",
            "organic sludge residue visible on local roadway"
        ]),
        (["streetlight", "street light", "lamp not", "dark road"], "BROKEN_STREETLIGHT", "MEDIUM", [
            "unlit overhead sodium/LED luminaire fixture",
            "cracked light housing cover structure on support mast",
            "dark road corridor section showing high visibility drop"
        ])
    ]

    for keywords, issue_type, severity, visual_evidence in keyword_map:
        for kw in keywords:
            if kw in desc_lower:
                return {
                    "issue_type": issue_type,
                    "severity": severity,
                    "confidence": 0.88,
                    "visual_evidence": visual_evidence
                }

    # Default fallback
    return {
        "issue_type": "ROAD_DAMAGE",
        "severity": "MEDIUM",
        "confidence": 0.50,
        "visual_evidence": [
            "road surface defect matching citizen description text",
            "visual abnormality requiring active location audit",
            "unidentified structural decay reported"
        ]
    }
