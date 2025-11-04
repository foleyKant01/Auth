# # app.py
# import os, math, re, time
# from typing import List, Dict, Any, Optional
# from flask import Flask, request, jsonify
# import requests

# app = Flask(__name__)

# # ---------- Config ----------
# OVERPASS_URL = "https://overpass-api.de/api/interpreter"
# NOMINATIM_UA = "YourAppName/1.0 (contact@email)"
# # Active le fallback IA si OPENAI_API_KEY est présent dans l'env
# OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
# OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")  # remplace si besoin

# # ---------- Utils ----------
# def haversine(lat1, lon1, lat2, lon2):
#     R = 6371.0
#     dlat = math.radians(lat2 - lat1)
#     dlon = math.radians(lon2 - lon1)
#     a = math.sin(dlat/2)**2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon/2)**2
#     return R * 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))

# def safe_str(s: Optional[str]) -> str:
#     return s.strip() if isinstance(s, str) else ""

# def sanitize_query(q: str) -> str:
#     # supprime guillemets pour éviter de casser la requête Overpass/regex
#     return re.sub(r'["\']+', "", q).strip()

# # ---------- Mapping FR -> OSM tags (extrait, tu peux étendre) ----------
# TAG_MAPPING = {
#     # Santé
#     "pharmacie": "pharmacy", "pharmacies": "pharmacy", "clinique": "clinic",
#     "hôpital": "hospital", "hopital": "hospital", "laboratoire": "laboratory",

#     # Alimentation
#     "restaurant": "restaurant", "resto": "restaurant", "fast-food": "fast_food",
#     "supermarché": "supermarket", "supérette": "supermarket",
#     "boulangerie": "bakery", "café": "cafe", "bar": "bar", "glacier": "ice_cream",

#     # Transports
#     "station service": "fuel", "station essence": "fuel", "parking": "parking",
#     "taxi": "taxi", "garage": "garage", "arrêt de bus": "bus_stop",

#     # Éducation
#     "école": "school", "collège": "school", "college": "school",
#     "lycée": "school", "université": "university",

#     # Finance / Poste
#     "banque": "bank", "guichet": "atm", "bureau de poste": "post_office",

#     # Tourisme / culte / loisirs
#     "hôtel": "hotel", "hotel": "hotel", "auberge": "hostel",
#     "église": "place_of_worship", "mosquée": "place_of_worship", "temple": "place_of_worship",
#     "cinéma": "cinema", "parc": "park", "musée": "museum", "centre sportif": "sports_centre",

#     # Administration
#     "mairie": "townhall", "préfecture": "public_building",
# }

# # ---------- Overpass ----------
# def build_overpass_query(user_input: str, area_name: str, limit: int = 80) -> str:
#     """
#     Stratégie hybride :
#       - si mot-clé FR mappé => filtre par tag (amenity/shop/etc.)
#       - sinon => regex sur name
#     """
#     q = sanitize_query(user_input.lower())
#     tag = TAG_MAPPING.get(q)
#     # On cible la commune (admin_level=8) quand possible pour réduire le bruit
#     if tag:
#         return f"""
#         [out:json][timeout:60];
#         area["name"="{area_name}"]["admin_level"="8"]->.a;
#         (
#           node["amenity"="{tag}"](area.a);
#           node["shop"="{tag}"](area.a);
#           node["tourism"="{tag}"](area.a);
#           node["leisure"="{tag}"](area.a);
#           node["office"="{tag}"](area.a);
#         );
#         out center {limit};
#         """
#     else:
#         # recherche libre par nom (insensible à la casse)
#         return f"""
#         [out:json][timeout:60];
#         area["name"="{area_name}"]["admin_level"="8"]->.a;
#         node["name"~"{q}", i](area.a);
#         out center {limit};
#         """

# def fetch_overpass(query: str) -> Dict[str, Any]:
#     resp = requests.get(OVERPASS_URL, params={"data": query}, timeout=60,
#                         headers={"User-Agent": NOMINATIM_UA})
#     if resp.status_code != 200:
#         raise RuntimeError(f"Overpass error {resp.status_code}")
#     try:
#         return resp.json()
#     except Exception:
#         # Parfois Overpass renvoie du HTML d'erreur → gérer proprement
#         raise RuntimeError("Overpass returned non-JSON")

# def to_osm_results(osm_json: Dict[str, Any],
#                    user_lat: float, user_lon: float) -> List[Dict[str, Any]]:
#     results = []
#     for el in osm_json.get("elements", []):
#         if "lat" not in el or "lon" not in el:
#             # pour certains ways/relations, il faudrait 'center', ici on skip
#             continue
#         tags = el.get("tags", {}) or {}
#         name = tags.get("name", "Inconnu")
#         city = tags.get("addr:city") or tags.get("addr:town") or tags.get("addr:village")
#         suburb = tags.get("addr:suburb") or tags.get("addr:neighbourhood")
#         street = tags.get("addr:street")
#         lat, lon = el["lat"], el["lon"]
#         dist = haversine(user_lat, user_lon, lat, lon)

#         # Description courte auto (si rien d’autre)
#         desc_parts = []
#         # type
#         for k in ("amenity", "shop", "tourism", "leisure", "office"):
#             if tags.get(k):
#                 desc_parts.append(tags[k])
#                 break
#         # horaires / phone
#         if tags.get("opening_hours"):
#             desc_parts.append(f"Ouvert: {tags['opening_hours']}")
#         if tags.get("phone"):
#             desc_parts.append(f"Tel: {tags['phone']}")
#         base_desc = ", ".join(desc_parts) if desc_parts else None

#         results.append({
#             "bu_uid": None,
#             "bu_name": name,
#             "bu_categorie": tags.get("amenity") or tags.get("shop") or tags.get("tourism") or tags.get("leisure") or tags.get("office"),
#             "bu_city": city,
#             "bu_address": street or suburb,
#             "latitude": lat,
#             "longitude": lon,
#             "source": "osm",
#             "distance_km": round(dist, 2),
#             "raw_tags": tags,          # utile pour debug ou enrichissement
#             "base_description": base_desc,  # fallback minimal
#             "description": None,       # sera enrichi ensuite
#         })
#     return results

# # ---------- Wikipedia ----------
# def wikipedia_summary_fr(title: str) -> Optional[str]:
#     # API REST Summary (FR). Remplace espaces par _
#     url = f"https://fr.wikipedia.org/api/rest_v1/page/summary/{title.replace(' ', '_')}"
#     r = requests.get(url, timeout=15, headers={"User-Agent": NOMINATIM_UA})
#     if r.status_code == 200:
#         j = r.json()
#         # 'extract' = résumé court
#         if isinstance(j, dict) and j.get("extract"):
#             return j["extract"].strip()
#     return None

# def find_best_wiki_description(name: str) -> Optional[str]:
#     """
#     Essaye :
#       - titre exact
#       - titre sans mots communs (ex: Direction Technique de la Mairie de Bingerville -> Mairie de Bingerville)
#     """
#     name = safe_str(name)
#     if not name:
#         return None

#     # 1) titre exact
#     desc = wikipedia_summary_fr(name)
#     if desc:
#         return desc

#     # 2) heuristique légère : garder les 3 derniers mots si phrase longue
#     parts = [p for p in re.split(r"\s+", name) if p]
#     if len(parts) >= 3:
#         guess = " ".join(parts[-3:])
#         desc = wikipedia_summary_fr(guess)
#         if desc:
#             return desc

#     # 3) Retirer termes administratifs fréquents
#     reduced = re.sub(r"\b(Direction|Technique|de|la|du|des|de la|de l'|Mairie|Service|Commune|Ville)\b", "", name, flags=re.I)
#     reduced = re.sub(r"\s{2,}", " ", reduced).strip()
#     if reduced and reduced.lower() != name.lower():
#         desc = wikipedia_summary_fr(reduced)
#         if desc:
#             return desc

#     return None

# # ---------- Fallback IA (optionnel) ----------
# def ai_generate_short_description(name: str, tags: Dict[str, Any]) -> Optional[str]:
#     """
#     Utilise OpenAI si clé dispo. Sinon retourne None.
#     """
#     if not OPENAI_API_KEY:
#         return None

#     # Construit un prompt contextuel très court
#     context_bits = []
#     for k in ("amenity", "shop", "tourism", "leisure", "office"):
#         if tags.get(k):
#             context_bits.append(f"type: {k}={tags[k]}")
#             break
#     for k in ("addr:city", "addr:town", "addr:village", "addr:suburb"):
#         if tags.get(k):
#             context_bits.append(f"{k}: {tags[k]}")
#             break

#     prompt = (
#         f"Écris une description factuelle, neutre et concise (1 phrase) de \"{name}\" "
#         f"en Côte d'Ivoire si pertinent. Utilise uniquement des infos plausibles pour une fiche d'annuaire. "
#         f"Évite les superlatifs et le marketing. Contexte brut: {', '.join(context_bits) or 'aucun'}."
#     )

#     # Appel HTTP direct à l’API Chat Completions (sans SDK)
#     try:
#         r = requests.post(
#             "https://api.openai.com/v1/chat/completions",
#             headers={"Authorization": f"Bearer {OPENAI_API_KEY}", "Content-Type": "application/json"},
#             json={
#                 "model": OPENAI_MODEL,
#                 "messages": [
#                     {"role": "system", "content": "Tu es un assistant qui rédige des descriptions courtes et précises pour un annuaire local."},
#                     {"role": "user", "content": prompt}
#                 ],
#                 "temperature": 0.2,
#                 "max_tokens": 80
#             },
#             timeout=25
#         )
#         if r.status_code == 200:
#             j = r.json()
#             text = j["choices"][0]["message"]["content"].strip()
#             return text
#     except Exception:
#         return None
#     return None

# # ---------- Enrichissement description ----------
# def enrich_descriptions(items: List[Dict[str, Any]]) -> None:
#     """
#     Modifie la liste in-place :
#       - tente Wikipedia par nom exact et variantes
#       - si rien trouvé, utilise base_description (tags)
#       - si activé, fallback IA
#     """
#     for it in items:
#         name = it.get("bu_name") or ""
#         # 1) Wikipedia
#         desc = find_best_wiki_description(name)
#         if not desc:
#             # 2) fallback base_description (tags)
#             desc = it.get("base_description")
#         if not desc:
#             # 3) IA optionnelle
#             desc = ai_generate_short_description(name, it.get("raw_tags") or {}) or None

#         it["description"] = desc
#         # Nettoie le payload si tu ne veux pas exposer ces champs
#         it.pop("raw_tags", None)
#         it.pop("base_description", None)


# # ---------- Endpoint combiné ----------
# def combined_search():
#     headers = {"User-Agent": NOMINATIM_UA}

#     """
#     Body JSON:
#     {
#       "textSearch": "pharmacie", 
#       "commune": "Yopougon",
#       "latitude": 5.33,
#       "longitude": -4.04,
#       "page": 1,
#       "per_page": 10
#     }
#     """
#     try:
#         data = request.get_json(force=True)
#         text = sanitize_query(data.get("textSearch", ""))
#         commune = data.get("commune", "Yopougon")
#         user_lat = float(data.get("latitude"))
#         user_lon = float(data.get("longitude"))
#         page = int(data.get("page", 1))
#         per_page = int(data.get("per_page", 10))

#         if not text:
#             return jsonify({"status":"error", "error_description":"textSearch is required"}), 400

#         # --- 1) OSM via Overpass
#         q = build_overpass_query(text, commune, limit=120)
#         osm_json = fetch_overpass(q)
#         osm_items = to_osm_results(osm_json, user_lat, user_lon)

#         # TODO (optionnel) : ajouter ici tes résultats internes DB si tu veux fusionner
#         # internal_items = ...
#         # combined = internal_items + osm_items
#         combined = osm_items

#         # Tri par distance
#         combined.sort(key=lambda x: x["distance_km"])

#         # Enrichir description (wiki -> base -> IA)
#         enrich_descriptions(combined)

#         # Pagination
#         total = len(combined)
#         start = (page - 1) * per_page
#         end = start + per_page
#         paginated = combined[start:end]

#         return jsonify({
#             "status": "success",
#             "results": paginated,
#             "total": total,
#             "pages": (total + per_page - 1) // per_page,
#             "current_page": page
#         })
#     except Exception as e:
#         return jsonify({"status":"error", "error_description": str(e)}), 500


