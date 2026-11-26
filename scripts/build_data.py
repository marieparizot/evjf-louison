#!/usr/bin/env python3
"""Génère data/evjf.json et data/embedded_data.js (fonctionnement hors-ligne).

Toutes les adresses et téléphones ont été relevés en novembre 2026 sur les sites
officiels ou des annuaires (Michelin, offices de tourisme, Gîtes de France...).
Lancer : python3 scripts/build_data.py
"""
import json, pathlib

W = "https://thumb.wikimedia.org/wikipedia/commons/thumb/"

def wm(path, credit):
    return {"photo": W + path, "credit": "Photo Wikimedia Commons · " + credit}

CHEF_NOTE = ("Take a Chef : chefs notés, menu sur devis gratuit. Indicatif 2026 pour 7 à 12 convives : "
             "≈ 55 à 130 €/pers selon le menu (courses et service compris, boissons en plus).")

DATA = {
  "version": 1,
  "updated": "2026-11-26",
  "title": "EVJF de Louison",
  "dates": [
    {"id": "we1", "label": "WE du 3-4 avril 2027", "fri": "2027-04-02", "sat": "2027-04-03", "sun": "2027-04-04"},
    {"id": "we2", "label": "WE du 10-11 avril 2027", "fri": "2027-04-09", "sat": "2027-04-10", "sun": "2027-04-11"}
  ],
  "ticker": [
    "💍 FLASH INFO : Louise a dit oui. On ne sait toujours pas qui a été le plus surpris.",
    "📸 Les photos de Louise ont été choisies avec amour et une totale absence de pitié.",
    "🧖‍♀️ Le spa sert à réparer la soirée de la veille. Ou à préparer celle du soir. Les deux, en fait.",
    "👩‍🍳 Le chef à domicile a été prévenu : pas de cuisine moléculaire, on veut du fromage.",
    "🪩 Code vestimentaire du samedi soir : paillettes obligatoires, dignité facultative.",
    "🚄 Rappel : le dernier train du dimanche ne nous attendra pas, même si on lui fait des yeux doux.",
    "🔊 Le karaoké n'est pas au programme. On sait tous comment ça va finir quand même.",
    "📵 Aucune photo de cet EVJF ne fuitera. Sauf les meilleures. Et les pires surtout."
  ],
  "likeToasts": [
    "Excellent goût. Presque aussi bon que celui de Louise en matière de frange.",
    "Like enregistré. Ton trophée de témoin de l'année est en cours de gravure.",
    "Validé ! Le comité d'organisation (toi) approuve.",
    "Noté. On mettra ça sur la liste « choses qu'on regrettera dimanche ».",
    "Tu as cliqué avec ton cœur. Ton banquier, lui, a cliqué sur « annuler ».",
    "❤️ Merci ! Ce vote compte double si tu ramènes des chips."
  ],
  "unlikeToasts": [
    "Like retiré. On respecte, mais on juge un peu.",
    "Changement d'avis ? Typique d'une veille de mariage.",
    "OK, on fait comme si on n'avait rien vu."
  ],
  "group": {"adults": 7, "note": "7 participants : viser au moins 4 chambres."},
  "tiers": {
    "1": {"label": "€", "name": "Malin", "joke": "on garde des sous pour le cadeau (et les shots)", "budget": "≈ 150 à 230 €/pers le week-end (1 nuit, hors train)"},
    "2": {"label": "€€", "name": "Confort", "joke": "raisonnable, donc personne ne le choisira", "budget": "≈ 250 à 400 €/pers le week-end (1 nuit, hors train)"},
    "3": {"label": "€€€", "name": "Waouh", "joke": "on vend un rein, mais un rein bien hydraté", "budget": "≈ 450 €/pers et plus le week-end (1 nuit, hors train)"}
  },
  "types": {
    "logement": {"label": "Logements", "emoji": "🏡"},
    "spa": {"label": "Spa de la journée", "emoji": "🧖‍♀️"},
    "activite": {"label": "Activité", "emoji": "🥂"},
    "chef": {"label": "Chef à domicile", "emoji": "👩‍🍳"},
    "soiree": {"label": "Sortir le soir", "emoji": "🪩"}
  },
  "cities": [
    # ------------------------------------------------------------------ REIMS
    {
      "joke": "Le seul endroit où boire du champagne au petit-déjeuner s'appelle « découvrir le patrimoine local ».", "id": "reims", "name": "Reims & la Champagne", "emoji": "🥂",
      "trip": "45 min en TGV (Paris-Est → Reims)",
      "vibe": "Champagne à volonté, caves, vignes et spas nordiques. Soirées plus calmes : bars à cocktails et à champagne autour de la place d'Erlon.",
      "scores": {"spa": 5, "soiree": 3, "budget": 4},
      **wm("8/8b/Cathedral_of_Reims_%2817%29.jpg/960px-Cathedral_of_Reims_%2817%29.jpg", "Cathédrale de Reims, CC BY-SA 4.0"),
      "search": "Reims, France",
      "items": [
        {"id": "reims-ospa", "type": "logement", "tier": 2, "name": "Ô Spa Champenois",
         "desc": "Maison d'hôtes 450 m² avec espace spa, 10 personnes, 3 chambres. Au cœur des vignes de la Montagne de Reims.",
         "address": "Écueil, 51500 (15 min de Reims)", "url": "https://www.gites-de-france.com/fr/grand-est/marne/o-spa-champenois-51g51218",
         "ref": "Gîtes de France n° 51G51218",
         **wm("6/6a/Hautvillers%2C_wineyards-1.JPG/960px-Hautvillers%2C_wineyards-1.JPG", "vignes de Champagne (photo d'ambiance), CC BY 4.0")},
        {"id": "reims-prelude", "type": "logement", "tier": 2, "name": "Prélude Hautvillers",
         "desc": "Grande maison de 12 personnes, 4 chambres, au centre du village d'Hautvillers, berceau du champagne (Dom Pérignon).",
         "address": "Hautvillers, 51160 (25 min de Reims)", "url": "https://www.gites-de-france.com/fr/grand-est/marne/prelude-hautvillers-12-pers-51g723",
         "ref": "Gîtes de France n° 51G723",
         **wm("3/3d/Mo%C3%ABt_Chandon_Vineyards_Hautvillers.jpg/960px-Mo%C3%ABt_Chandon_Vineyards_Hautvillers.jpg", "Hautvillers, CC BY-SA 3.0")},
        {"id": "reims-mellifera", "type": "logement", "tier": 1, "name": "La Villa Mellifera",
         "desc": "Villa 215 m² pour 12 personnes, 6 chambres : presque une chambre chacun. Aux portes de Reims, pratique pour sortir en VTC.",
         "address": "Cernay-lès-Reims, 51420 (10 min de Reims)", "url": "https://www.gites-de-france.com/fr/grand-est/marne/la-villa-mellifera-51g774",
         "ref": "Gîtes de France n° 51G774",
         **wm("2/24/Mairie_de_Cernay_162.jpg/960px-Mairie_de_Cernay_162.jpg", "Cernay-lès-Reims (photo du village), CC BY-SA")},
        {"id": "reims-chanzy", "type": "spa", "tier": 2, "name": "Spa Deep Nature – La Caserne Chanzy",
         "desc": "Spa de l'hôtel 5★ en plein centre de Reims : piscine, hammam, sauna, soins. Ouvert aux personnes extérieures sur réservation.",
         "address": "18 rue Tronsson-Ducoudray, 51100 Reims", "phone": "+33 3 26 83 18 18",
         "url": "https://www.marriott.com/hotels/travel/rheak/",
         **wm("2/21/Reims_-_place_Drouet-d%27Erlon_-_2023-06-04_-_01.jpg/960px-Reims_-_place_Drouet-d%27Erlon_-_2023-06-04_-_01.jpg", "centre de Reims, CC BY-SA 4.0")},
        {"id": "reims-sacy", "type": "spa", "tier": 3, "name": "Château de Sacy – spa nordique",
         "desc": "Château-hôtel dans les vignes : sauna, bains nordiques en tonneau avec vue sur les coteaux, soins. Brunch ou déjeuner possible sur place.",
         "address": "Rue des Croisettes, 51500 Sacy", "phone": "+33 3 26 07 60 38",
         "url": "https://chateaudesacy-reims.fr/",
         "photo": "https://chateaudesacy-reims.fr/wp-content/uploads/2026/08/2.jpg", "credit": "Photo : Château de Sacy"},
        {"id": "reims-royal", "type": "spa", "tier": 3, "name": "Royal Champagne Hôtel & Spa",
         "desc": "Le palace des vignes (5★) : spa de 1 500 m², piscines intérieure et extérieure face aux coteaux. Ouvert de mars à décembre.",
         "address": "9 rue de la République, 51160 Champillon", "phone": "+33 3 26 52 41 14",
         "url": "https://royalchampagne.com/",
         **wm("d/d7/Champillon_01790.JPG/960px-Champillon_01790.JPG", "Champillon, CC BY-SA 3.0")},
        {"id": "reims-pommery", "type": "activite", "tier": 1, "name": "Visite des caves Pommery",
         "desc": "Caves crayères classées UNESCO, 18 km de galeries, dégustation. Dès ≈ 30 €/pers. Réserver à l'avance, les créneaux partent vite.",
         "address": "5 place du Général Gouraud, 51100 Reims", "url": "https://www.champagnepommery.com/",
         **wm("a/a1/Maison_Vrancken_-_Domaine_Pommery_-_Reims.jpg/960px-Maison_Vrancken_-_Domaine_Pommery_-_Reims.jpg", "Domaine Pommery, CC BY-SA 4.0")},
        {"id": "reims-chef", "type": "chef", "tier": 2, "name": "Chef à domicile à Reims (Take a Chef)",
         "desc": "Une vingtaine de chefs à domicile autour de Reims. On décrit la soirée, plusieurs chefs envoient un menu. " + CHEF_NOTE,
         "address": "Reims et alentours", "url": "https://www.takeachef.com/fr-fr/chef-a-domicile/reims",
         "photo": "https://d1zzxdyvtq79bu.cloudfront.net/context/frontend/images/open-graph/chef_privado_take_a_chef.jpg", "credit": "Photo : Take a Chef"},
        {"id": "reims-bootlegger", "type": "soiree", "tier": 2, "name": "Bootlegger",
         "desc": "Bar à cocktails façon speakeasy, cosy et réservable pour un groupe.",
         "address": "4 rue Gaston Boyer, 51100 Reims", "url": "https://www.privateaser.com/lieu/51307-bootlegger",
         "photo": "https://privateaser-media.s3.eu-west-1.amazonaws.com/etab_photos/51307/750x375/459393.jpg", "credit": "Photo : Privateaser"},
        {"id": "reims-lapaix", "type": "soiree", "tier": 2, "name": "Bar La Paix",
         "desc": "Bar à cocktails et à champagne de l'hôtel de la Paix, à deux pas de la place d'Erlon.",
         "address": "9 rue Buirette, 51100 Reims", "url": "https://www.privateaser.com/lieu/64638-bar-la-paix",
         "photo": "https://privateaser-media.s3.eu-west-1.amazonaws.com/etab_photos/64638/750x375/617705.jpg", "credit": "Photo : Privateaser"},
        {"id": "reims-apostrophe", "type": "soiree", "tier": 1, "name": "L'Apostrophe",
         "desc": "Bar-brasserie avec terrasse sur la place d'Erlon, la rue la plus animée de Reims le soir. Cocktails.",
         "address": "59 place Drouet-d'Erlon, 51100 Reims", "url": "https://www.arrivalguides.com/en/Travelguide/REIMS/barsandnightlife/l-apostrophe-17249",
         "photo": "https://image.arrivalguides.com/1200x630/09/aa24401274ee9f1d4ce248717b1031e0.jpg", "credit": "Photo : ArrivalGuides"}
      ]
    },
    # -------------------------------------------------------------- DEAUVILLE
    {
      "joke": "Ambiance Planches, casino et brushing. Mettez une veste : la mer du Nord ne fait pas de cadeau aux EVJF en avril.", "id": "deauville", "name": "Deauville & Trouville", "emoji": "🌊",
      "trip": "2 h en train (Paris-Saint-Lazare → Trouville-Deauville) ou 2 h en voiture (A13)",
      "vibe": "Bord de mer chic, les Planches, casino et boîte de nuit le samedi. Spas marins haut de gamme. Gîtes à colombages dans le Pays d'Auge.",
      "scores": {"spa": 5, "soiree": 4, "budget": 3},
      **wm("0/01/Deauville-planches.jpg/960px-Deauville-planches.jpg", "Les Planches de Deauville, CC BY-SA 3.0"),
      "search": "Deauville, France",
      "items": [
        {"id": "deau-manette", "type": "logement", "tier": 2, "name": "La Manette",
         "desc": "Gîte haut de gamme pour 8 personnes, 4 chambres, jardin de 1 800 m² et spa privatif (5 places, ouvert d'avril à octobre : à confirmer pour début avril).",
         "address": "Gonneville-sur-Honfleur, 14600 (20 min de Deauville)", "url": "https://www.gites-de-france.com/fr/normandie/calvados/la-manette-14g3069",
         "ref": "Gîtes de France n° 14G3069",
         **wm("2/24/Beuvron-en-Auge_-_Vue_de_la_Grande_Rue_en_direction_de_l%27%C3%A9glise_Saint-Martin.jpg/960px-Beuvron-en-Auge_-_Vue_de_la_Grande_Rue_en_direction_de_l%27%C3%A9glise_Saint-Martin.jpg", "Pays d'Auge (photo d'ambiance), CC BY-SA 4.0")},
        {"id": "deau-mimosas", "type": "logement", "tier": 2, "name": "Gîte des Mimosas",
         "desc": "Maison de 190 m² pour 8 personnes, 4 chambres, avec jacuzzi (un avis signale une panne : demander confirmation).",
         "address": "Formentin, 14340 (25 min de Deauville)", "url": "https://www.gites-de-france.com/fr/normandie/calvados/gite-des-mimosas-14g2231",
         "ref": "Gîtes de France n° 14G2231",
         **wm("8/81/%C3%89glise_Saint-Martin_et_monument_aux_morts_de_Formentin.jpg/960px-%C3%89glise_Saint-Martin_et_monument_aux_morts_de_Formentin.jpg", "Formentin (photo du village), CC BY-SA")},
        {"id": "deau-bonheur", "type": "logement", "tier": 3, "name": "Le Bonheur en Auge",
         "desc": "Grand gîte 10 personnes avec spa ET sauna privés, entre Deauville et Honfleur.",
         "address": "Les Authieux-sur-Calonne, 14130 (20 min de Deauville)", "url": "https://www.gites-de-france.com/fr/normandie/calvados/le-bonheur-en-auge-14g3584",
         "ref": "Gîtes de France n° 14G3584",
         **wm("9/92/Les_Authieux-sur-Calonne_Mairie.JPG/960px-Les_Authieux-sur-Calonne_Mairie.JPG", "Les Authieux-sur-Calonne (photo du village), CC BY-SA")},
        {"id": "deau-angerville", "type": "logement", "tier": 2, "name": "Les Deux Gîtes du Bel Angerville",
         "desc": "Deux gîtes réunis jusqu'à 14 personnes, avec bain nordique. Idéal si on veut de la place pour tout le monde.",
         "address": "Pays d'Auge (25 min de Deauville)", "url": "https://www.vrbo.com/2682027a",
         "photo": "https://media.vrbo.com/lodging/131000000/130850000/130841700/130841694/43230640.jpg?impolicy=resizecrop&rw=575&rh=575&ra=fill", "credit": "Photo : annonce Vrbo/Abritel"},
        {"id": "deau-cures", "type": "spa", "tier": 2, "name": "Les Cures Marines – Trouville (MGallery 5★)",
         "desc": "Thalasso face à la mer : piscine d'eau de mer intérieure, bain bouillonnant, hammam, sauna. Formules demi-journée spa + déjeuner (aussi sur Staycation).",
         "address": "Boulevard de la Cahotte, 14360 Trouville-sur-Mer", "phone": "+33 2 31 14 26 00",
         "url": "https://www.lescuresmarines.com/",
         **wm("1/14/Beach_of_Trouville-sur-mer.jpg/960px-Beach_of_Trouville-sur-mer.jpg", "plage de Trouville, CC BY-SA 4.0")},
        {"id": "deau-guerlain", "type": "spa", "tier": 3, "name": "Spa Guerlain – Hôtel Barrière Le Normandy",
         "desc": "Le spa du mythique Normandy (piscine, sauna, hammam, soins Guerlain), ouvert aux personnes extérieures à l'hôtel.",
         "address": "38 rue Jean Mermoz, 14800 Deauville",
         "url": "https://www.hotelsbarriere.com/fr/deauville/le-normandy/experiences/spa",
         "photo": "https://a.storyblok.com/f/287000/2000x1335/f1fcc0cda0/entree-du-spa-guerlain-du-normandy.jpg/m/960x640/filters:format(webp):quality(80)", "credit": "Photo : Hôtels Barrière"},
        {"id": "deau-chef", "type": "chef", "tier": 2, "name": "Chef à domicile à Deauville (Take a Chef)",
         "desc": "Une quarantaine de chefs sur Deauville-Trouville ; menus réservés en moyenne ≈ 83 €/pers. " + CHEF_NOTE,
         "address": "Deauville, Trouville, Pays d'Auge", "url": "https://www.takeachef.com/fr-fr/chef-prive/deauville",
         "photo": "https://d1zzxdyvtq79bu.cloudfront.net/context/frontend/images/open-graph/chef_privado_take_a_chef.jpg", "credit": "Photo : Take a Chef"},
        {"id": "deau-casino", "type": "soiree", "tier": 2, "name": "Casino Barrière de Deauville",
         "desc": "Le Grand Casino de 1912 : bars (O2 Sofa Bar), jeux, et club le samedi soir. Pièce d'identité obligatoire.",
         "address": "2 rue Edmond Blanc, 14800 Deauville", "phone": "+33 2 31 14 31 14",
         "url": "https://www.hotelsbarriere.com/fr/deauville/experiences/casinos",
         **wm("c/cc/France-000638_-_Grand_Casino_%2814974258481%29.jpg/960px-France-000638_-_Grand_Casino_%2814974258481%29.jpg", "Grand Casino de Deauville, CC BY-SA")},
        {"id": "deau-barnormandy", "type": "soiree", "tier": 3, "name": "Le Bar du Normandy",
         "desc": "Boiseries, cheminée et cocktails signature au calvados : l'apéritif chic avant le casino.",
         "address": "38 rue Jean Mermoz, 14800 Deauville",
         "url": "https://www.hotelsbarriere.com/fr/deauville/le-normandy/restaurants-et-bars/le-bar-du-normandy",
         "photo": "https://a.storyblok.com/f/287000/2000x1335/b45c7486b5/deauville-hotel-le-normandy-bar-du-normandy-cheminee-1.jpg/m/960x640/filters:format(webp):quality(80)", "credit": "Photo : Hôtels Barrière"}
      ]
    },
    # ------------------------------------------------------------------ LILLE
    {
      "joke": "On y vient pour le spa, on y reste pour la welsh. Les régimes d'avant-mariage ne passent pas la gare Lille-Flandres.", "id": "lille", "name": "Lille", "emoji": "🍻",
      "trip": "1 h en TGV (Paris-Nord → Lille-Flandres)",
      "vibe": "Très festive et abordable : bars du Vieux-Lille, rue de la Barre, estaminets. Gîtes avec spa à 15 min dans la campagne.",
      "scores": {"spa": 4, "soiree": 5, "budget": 5},
      **wm("f/f8/Lille_gd_place_arc_en_ciel.jpg/960px-Lille_gd_place_arc_en_ciel.jpg", "Grand-Place de Lille, CC BY-SA 4.0"),
      "search": "Lille, France",
      "items": [
        {"id": "lille-frene", "type": "logement", "tier": 2, "name": "Le Frêne",
         "desc": "Gîte 8 personnes avec sauna/spa, noté 4,9/5 (34 avis). À 15 km de Lille.",
         "address": "Avelin, 59710 (20 min de Lille)", "url": "https://www.gites-de-france.com/fr/hauts-de-france/nord/le-frene-59g20480",
         "ref": "Gîtes de France n° 59G20480",
         **wm("c/c8/France%2C_Nord%2C_Avelin_%2801%29%2C_centre.jpg/960px-France%2C_Nord%2C_Avelin_%2801%29%2C_centre.jpg", "Avelin (photo du village), CC BY-SA 4.0")},
        {"id": "lille-aurore", "type": "logement", "tier": 2, "name": "Gîte de l'Aurore",
         "desc": "10 personnes, 5 chambres, espace bien-être en option (≈ 50 € les 2 h pour 2, +30 €/pers. supplémentaire : à confirmer).",
         "address": "Avelin, 59710 (20 min de Lille)", "url": "https://www.gites-de-france.com/fr/hauts-de-france/nord/gite-de-laurore-59g204510",
         "ref": "Gîtes de France n° 59G204510",
         **wm("7/74/Avelin.-_Antroeuilles_chemin_de_la_Botte_d%27Or_%282%29.jpg/960px-Avelin.-_Antroeuilles_chemin_de_la_Botte_d%27Or_%282%29.jpg", "campagne d'Avelin, CC BY-SA 4.0")},
        {"id": "lille-grenier", "type": "logement", "tier": 1, "name": "Le Grenier à Grain",
         "desc": "Grande maison de 215 m² pour 12 personnes : beaucoup de place pour un petit prix par personne. Spa à faire en ville.",
         "address": "Sainghin-en-Weppes, 59184 (25 min de Lille)", "url": "https://www.gites-de-france.com/fr/hauts-de-france/nord/le-grenier-grain-59g2642",
         "ref": "Gîtes de France n° 59G2642",
         **wm("3/3b/Lille_Collage.jpg/960px-Lille_Collage.jpg", "Lille, CC BY-SA")},
        {"id": "lille-labna", "type": "spa", "tier": 2, "name": "Labna Spa",
         "desc": "Hammam oriental dans une cave voûtée du XVIIIe siècle, en plein Vieux-Lille. Sauna, hammam et jacuzzi privatisables pour un groupe.",
         "address": "45 rue de la Barre, 59000 Lille", "url": "https://www.planity.com/labna-59000-lille",
         "photo": "https://mms.cdn.global.prodsharedsvc.planityapp.com/planity/image/upload/c_crop,w_1640,h_861,x_0,y_32/q_auto,w_1200,h_630,f_auto/teebkfwbnsjxuyp1rhgb", "credit": "Photo : Planity"},
        {"id": "lille-hermitage", "type": "spa", "tier": 3, "name": "Spa by Hermitage Gantois",
         "desc": "Spa de l'hôtel 5★ (ancien hospice du XVe) : piscine chauffée, hammam, soins haut de gamme. Entre Grand'Place et Hôtel de Ville.",
         "address": "224 rue Pierre-Mauroy, 59000 Lille", "phone": "+33 3 20 85 30 30",
         "url": "https://en.lilletourism.com/get-out/the-best-addresses/entertainment/spa-by-hermitage-gantois-lille-en-4697156/",
         "photo": "https://api.cloudly.space/resize/crop/1200/627/75/aHR0cHM6Ly9oYXV0c2RlZnJhbmNlLm1lZGlhLnRvdXJpbnNvZnQuZXUvdXBsb2FkL3NwYS1oZXJtaXRhZ2UtZ2FudG9pcy1taW4uanBn/image.webp", "credit": "Photo : Office de tourisme de Lille"},
        {"id": "lille-chef", "type": "chef", "tier": 2, "name": "Chef à domicile à Lille (Take a Chef)",
         "desc": "Nombreux chefs sur la métropole lilloise, ils se déplacent aussi dans les gîtes de la campagne. " + CHEF_NOTE,
         "address": "Lille et métropole", "url": "https://www.takeachef.com/fr-fr/chef-a-domicile/lille",
         "photo": "https://d1zzxdyvtq79bu.cloudfront.net/context/frontend/images/open-graph/chef_privado_take_a_chef.jpg", "credit": "Photo : Take a Chef"},
        {"id": "lille-vespero", "type": "soiree", "tier": 2, "name": "Vespero",
         "desc": "Bar à cocktails rétro rue de Gand, pensé pour les soirées de groupe et privatisations.",
         "address": "11 rue de Gand, 59800 Lille", "url": "https://www.privateaser.com/lieu/45747-vespero",
         "photo": "https://privateaser-media.s3.eu-west-1.amazonaws.com/etab_photos/45747/750x375/471385.jpg", "credit": "Photo : Privateaser"},
        {"id": "lille-labarre", "type": "soiree", "tier": 3, "name": "La Barre – Hôtel Clarance",
         "desc": "Bar chic de l'hôtel 5★ Clarance, noté 4,9/5. Ouvert tous les jours de 17h30 à minuit.",
         "address": "Rue de la Barre, 59800 Lille (Hôtel Clarance)", "url": "https://www.privateaser.com/lieu/64453-la-barre",
         "photo": "https://privateaser-media.s3.eu-west-1.amazonaws.com/etab_photos/64453/750x375/614999.jpg", "credit": "Photo : Privateaser"},
        {"id": "lille-vieuxlille", "type": "soiree", "tier": 1, "name": "Tournée du Vieux-Lille",
         "desc": "Rue de la Barre (Maloot HiFi Bar au n° 3, No Stress au n° 13 – rhum), rue de Gand, place Louise-de-Bettignies (JoKeR). Tout se fait à pied.",
         "address": "Rue de la Barre, 59800 Lille", "url": "https://www.lebonbon.fr/lille/les-tops-food-et-drink/bar-a-cocktail-lille/",
         **wm("0/03/La_Maison_Haute_place_de_Gand_%C3%A0_Lille..jpg/960px-La_Maison_Haute_place_de_Gand_%C3%A0_Lille..jpg", "Vieux-Lille, CC BY 4.0")}
      ]
    },
    # -------------------------------------------------------------- BRUXELLES
    {
      "joke": "2 000 bières au Delirium : on ne les goûtera pas toutes. Enfin, en théorie.", "id": "bruxelles", "name": "Bruxelles", "emoji": "🇧🇪",
      "trip": "1 h 25 en train (Paris-Nord → Bruxelles-Midi). Carte d'identité obligatoire.",
      "vibe": "La plus festive : bières, clubs mythiques (Fuse), quartier Saint-Géry. Très bon rapport qualité-prix. Logement plutôt en ville.",
      "scores": {"spa": 3, "soiree": 5, "budget": 4},
      **wm("2/26/Grand-Place%2C_Brussels_-_panorama%2C_June_2018.jpg/960px-Grand-Place%2C_Brussels_-_panorama%2C_June_2018.jpg", "Grand-Place de Bruxelles, CC BY-SA 4.0"),
      "search": "Bruxelles, Belgique",
      "items": [
        {"id": "bxl-airbnb", "type": "logement", "tier": 2, "name": "Maisons de ville à Ixelles / Saint-Gilles",
         "desc": "À Bruxelles, les grandes maisons de ville se louent surtout sur Airbnb/Abritel. Les liens « Chercher un logement » plus bas sont déjà réglés (7 personnes, 4 chambres, vos dates).",
         "address": "Ixelles et Saint-Gilles, quartiers animés au sud du centre", "url": "https://www.airbnb.fr/s/Ixelles--Belgique/homes?adults=7&min_bedrooms=4",
         **wm("c/c6/Place_Saint-G%C3%A9ry_%C3%A0_Bruxelles.jpg/960px-Place_Saint-G%C3%A9ry_%C3%A0_Bruxelles.jpg", "Bruxelles, CC BY-SA 4.0")},
        {"id": "bxl-thehotel", "type": "spa", "tier": 2, "name": "The Hotel Brussels – spa panoramique",
         "desc": "Spa au 23e étage avec vue sur tout Bruxelles ; formules journée spa + sauna guidé (aussi sur Staycation).",
         "address": "Boulevard de Waterloo 38, 1000 Bruxelles", "phone": "+32 2 504 11 11",
         "url": "https://www.thehotel-brussels.be/",
         **wm("7/7b/Grand-Place_Flower_Carpet_2018_%2818mm%29.jpg/960px-Grand-Place_Flower_Carpet_2018_%2818mm%29.jpg", "Bruxelles, CC BY 4.0")},
        {"id": "bxl-aspria", "type": "spa", "tier": 3, "name": "Aspria Royal La Rasante (David Lloyd)",
         "desc": "Grand club bien-être : piscines, saunas, hammam. Les soins du spa sont ouverts aux non-membres.",
         "address": "Rue Sombre 56, 1200 Woluwe-Saint-Lambert",
         "url": "https://www.davidlloyd.be/en/clubs/brussels-royal-la-rasante/club-facilities/spa-and-wellbeing/",
         **wm("e/e0/Royal_Palace_in_Brussels.JPG/960px-Royal_Palace_in_Brussels.JPG", "Bruxelles, CC BY-SA 3.0")},
        {"id": "bxl-chef", "type": "chef", "tier": 2, "name": "Chef à domicile à Bruxelles (Take a Chef)",
         "desc": "Take a Chef fonctionne aussi en Belgique. " + CHEF_NOTE,
         "address": "Bruxelles", "url": "https://www.takeachef.com/fr-be/chef-a-domicile/bruxelles",
         "photo": "https://d1zzxdyvtq79bu.cloudfront.net/context/frontend/images/open-graph/chef_privado_take_a_chef.jpg", "credit": "Photo : Take a Chef"},
        {"id": "bxl-delirium", "type": "soiree", "tier": 1, "name": "Delirium Café",
         "desc": "Le temple de la bière (plus de 2 000 références), sur plusieurs étages, à 200 m de la Grand-Place.",
         "address": "Impasse de la Fidélité 4, 1000 Bruxelles", "url": "https://www.privateaser.com/lieu/46572-delirium-cafe",
         **wm("4/4c/Delirium_Cafe_-_16251053439.jpg/960px-Delirium_Cafe_-_16251053439.jpg", "Delirium Café, CC0")},
        {"id": "bxl-sgery", "type": "soiree", "tier": 1, "name": "Quartier Saint-Géry",
         "desc": "Les bars en terrasse autour des halles Saint-Géry : parfait pour commencer la soirée.",
         "address": "Place Saint-Géry, 1000 Bruxelles", "url": "https://visit.brussels/fr/visiteurs/",
         **wm("1/1f/Caf%C3%A9s_Bruxelles-Saint_G%C3%A9ry%C2%A9Marie-Fran%C3%A7oise_Plissart.jpg/960px-Caf%C3%A9s_Bruxelles-Saint_G%C3%A9ry%C2%A9Marie-Fran%C3%A7oise_Plissart.jpg", "Saint-Géry, CC BY-SA 4.0")},
        {"id": "bxl-fuse", "type": "soiree", "tier": 2, "name": "Fuse",
         "desc": "Club mythique de Bruxelles (depuis 1994), le samedi jusqu'au matin. Pour ceux qui veulent danser.",
         "address": "208 rue Blaes, 1000 Bruxelles", "url": "https://www.fuse.be/",
         **wm("2/26/Grand-Place%2C_Brussels_-_panorama%2C_June_2018.jpg/960px-Grand-Place%2C_Brussels_-_panorama%2C_June_2018.jpg", "Bruxelles, CC BY-SA 4.0")}
      ]
    },
    # --------------------------------------------------------------- BORDEAUX
    {
      "joke": "Spa de vinothérapie : on se baigne dans le raisin, on finit en buvant le reste. C'est du soin.", "id": "bordeaux", "name": "Bordeaux", "emoji": "🍷",
      "trip": "2 h 05 en TGV (Paris-Montparnasse → Bordeaux-Saint-Jean)",
      "vibe": "Élégante et festive : quais, bars de Saint-Pierre, péniche I.Boat. Le spa de vinothérapie des Sources de Caudalie, au milieu des vignes.",
      "scores": {"spa": 5, "soiree": 4, "budget": 3},
      **wm("d/d3/Miroir_d%27eau_Bordeaux_3.jpg/960px-Miroir_d%27eau_Bordeaux_3.jpg", "Miroir d'eau de Bordeaux, CC BY 3.0"),
      "search": "Bordeaux, France",
      "items": [
        {"id": "bdx-moulin", "type": "logement", "tier": 1, "name": "Gîte de Moulin",
         "desc": "Grand gîte de 256 m² pour 12 personnes, 5 chambres, dans les vignes du Bourgeais.",
         "address": "Cubnezais, 33620 (35 min de Bordeaux)", "url": "https://www.gites-de-france.com/fr/nouvelle-aquitaine/gironde/gite-de-moulin-33g4428",
         "ref": "Gîtes de France n° 33G4428",
         **wm("0/0d/Ch%C3%A2teau_Smith-Haut-Lafitte.jpg/960px-Ch%C3%A2teau_Smith-Haut-Lafitte.jpg", "vignoble bordelais (photo d'ambiance), CC BY-SA")},
        {"id": "bdx-gites-spa", "type": "logement", "tier": 2, "name": "Gîtes avec spa privatif en Gironde",
         "desc": "Sélection de gîtes avec spa en Gironde (ex. villa 10 personnes avec spa privatif à Soussans, près de Margaux).",
         "address": "Gironde (20 à 40 min de Bordeaux)", "url": "https://www.gites.fr/spa_gironde_d33.html",
         **wm("c/c6/%C3%89coquartier_Darwin_Bordeaux_2024.jpg/960px-%C3%89coquartier_Darwin_Bordeaux_2024.jpg", "Bordeaux, CC BY-SA 4.0")},
        {"id": "bdx-hammam", "type": "spa", "tier": 1, "name": "Grand Hammam de Bordeaux",
         "desc": "Hammam traditionnel réservé aux femmes, gommage et massages. Parfait pour un EVJF à petit prix.",
         "address": "45 rue des Menuts, 33000 Bordeaux", "url": "https://www.guide-piscine.fr/thermes-de-france/gironde/grand-hammam-de-bordeaux-a-bordeaux-500_T",
         **wm("9/97/Miroir_d%27eau_%28Bordeaux%29.jpg/960px-Miroir_d%27eau_%28Bordeaux%29.jpg", "Bordeaux, CC BY-SA 4.0")},
        {"id": "bdx-saunham", "type": "spa", "tier": 1, "name": "Saun'ham Hugo",
         "desc": "Sauna et hammam en centre-ville, cours Victor-Hugo.",
         "address": "9 rue de l'Observance, 33000 Bordeaux", "phone": "+33 5 56 31 50 01",
         "url": "https://www.koifaire.com/aquitaine/saun,ham,hugo-34404.html",
         **wm("b/b0/Sous_le_miroir_d%27eau_de_Bordeaux.jpg/960px-Sous_le_miroir_d%27eau_de_Bordeaux.jpg", "Bordeaux, CC0")},
        {"id": "bdx-caudalie", "type": "spa", "tier": 3, "name": "Les Sources de Caudalie – Spa Vinothérapie",
         "desc": "Le spa mythique au milieu des vignes de Smith Haut Lafitte. Rituels demi-journée 290 à 455 € (brochure 2025) ; le week-end, minimum 3 soins réservés.",
         "address": "Chemin de Smith Haut-Lafitte, 33650 Martillac (20 min de Bordeaux)", "phone": "+33 5 57 83 83 83",
         "url": "https://www.sources-hotels.com/bordeaux/",
         "photo": "https://www.sources-hotels.com/bordeaux/wp-content/uploads/sites/3/2024/12/SOURCE_2-1-1260x1000.jpg", "credit": "Photo : Les Sources de Caudalie"},
        {"id": "bdx-chef", "type": "chef", "tier": 2, "name": "Chef à domicile à Bordeaux (Take a Chef)",
         "desc": "Beaucoup de chefs sur Bordeaux et les vignobles ; on peut demander un accord mets-vins. " + CHEF_NOTE,
         "address": "Bordeaux et Gironde", "url": "https://www.takeachef.com/fr-fr/chef-a-domicile/bordeaux",
         "photo": "https://d1zzxdyvtq79bu.cloudfront.net/context/frontend/images/open-graph/chef_privado_take_a_chef.jpg", "credit": "Photo : Take a Chef"},
        {"id": "bdx-iboat", "type": "soiree", "tier": 2, "name": "I.Boat",
         "desc": "Ancien ferry transformé en club et salle de concert, aux Bassins à flot. Tram B, arrêt Bassins à flot.",
         "address": "Bassin à flot n° 1, quai Armand-Lalande, 33300 Bordeaux", "phone": "+33 5 56 10 48 35",
         "url": "https://www.privateaser.com/lieu/57908-iboat",
         **wm("c/cb/Bassins_%C3%A0_flot_de_Bordeaux.jpg/960px-Bassins_%C3%A0_flot_de_Bordeaux.jpg", "Bassins à flot, CC BY-SA")},
        {"id": "bdx-darwin", "type": "soiree", "tier": 1, "name": "Darwin – Magasin Général",
         "desc": "Friche branchée rive droite : bar-restaurant Magasin Général, bar extérieur le week-end, concerts.",
         "address": "87 quai des Queyries, 33100 Bordeaux", "url": "https://www.bordeaux-tourism.co.uk/cultural-heritage/darwin-caserne-niel.html",
         **wm("1/15/Bordeaux-Quartier_Darwin_%287%29.jpg/960px-Bordeaux-Quartier_Darwin_%287%29.jpg", "Darwin, CC BY-SA 4.0")}
      ]
    },
    # ------------------------------------------------------------------- LYON
    {
      "joke": "Capitale de la gastronomie : le chef à domicile va devoir assurer, sinon on le dénonce à Paul Bocuse.", "id": "lyon", "name": "Lyon", "emoji": "🦁",
      "trip": "2 h en TGV (Paris-Gare de Lyon → Lyon Part-Dieu)",
      "vibe": "Capitale de la gastronomie, Vieux Lyon, rooftop-club Le Sucre. Spas variés de 35 € à très chic. Gîtes avec spa en périphérie et dans le Beaujolais.",
      "scores": {"spa": 4, "soiree": 5, "budget": 4},
      **wm("4/4b/Vieuxlyon_saintjean_toits.jpg/960px-Vieuxlyon_saintjean_toits.jpg", "Vieux Lyon, CC BY-SA 3.0"),
      "search": "Lyon, France",
      "items": [
        {"id": "lyon-faubourg", "type": "logement", "tier": 2, "name": "Lyon Faubourg",
         "desc": "Maison 8 personnes, 4 chambres, avec piscine, sauna ET jacuzzi, jardin. À quelques km de Lyon.",
         "address": "Saint-Priest, 69800 (20 min de Lyon)", "url": "https://www.gites-de-france.com/fr/auvergne-rhone-alpes/rhone/lyon-faubourg-69g1966",
         "ref": "Gîtes de France n° 69G1966",
         **wm("8/8b/Ch%C3%A2teau_de_Saint-Priest_Face_Ouest_2.JPG/960px-Ch%C3%A2teau_de_Saint-Priest_Face_Ouest_2.JPG", "Saint-Priest (photo de la ville), CC BY-SA 3.0")},
        {"id": "lyon-ifs", "type": "logement", "tier": 2, "name": "Gîte des Ifs",
         "desc": "Maison de 200 m², 8 personnes, 4 chambres, sauna/spa, dans le village de pierres dorées d'Oingt (Beaujolais).",
         "address": "Val d'Oingt, 69620 (40 min de Lyon)", "url": "https://www.gites-de-france.com/fr/auvergne-rhone-alpes/rhone/gite-des-ifs-69g10015",
         "ref": "Gîtes de France n° 69G10015",
         **wm("9/96/Oingt_int%C3%A9rieur_du_village_69.jpg/960px-Oingt_int%C3%A9rieur_du_village_69.jpg", "Oingt, CC BY-SA 4.0")},
        {"id": "lyon-balicina", "type": "spa", "tier": 1, "name": "Balicina",
         "desc": "Grand centre balnéo : bassins chauds, jets, saunas, hammam, fontaine de glace. 35 € le week-end, sur réservation. Réservé aux adultes.",
         "address": "64 avenue Rockefeller, 69008 Lyon", "phone": "+33 4 28 38 27 00",
         "url": "https://www.balicina.fr/",
         "photo": "https://media.lyon-france.com/1280x852/6333127/42531579.jpg", "credit": "Photo : Office du tourisme de Lyon"},
        {"id": "lyon-canuts", "type": "spa", "tier": 2, "name": "Spa des Canuts",
         "desc": "Hammam traditionnel et soins à la Croix-Rousse, séances de 2 h, formules groupes.",
         "address": "51 rue Deleuvre, 69004 Lyon", "phone": "+33 4 78 39 57 72",
         "url": "https://www.planity.com/spa-des-canuts-69004-lyon",
         "photo": "https://mms.cdn.global.prodsharedsvc.planityapp.com/planity/image/upload/c_crop,w_1080,h_643,x_0,y_39/q_auto,w_1200,h_630,f_auto/ju2g6zfwhszlyt5dab3d", "credit": "Photo : Planity"},
        {"id": "lyon-carlton", "type": "spa", "tier": 3, "name": "Spa du Carlton Lyon (MGallery)",
         "desc": "Spa chic de l'hôtel Carlton, près de Bellecour : hammam sur demande, soins. Accès avec un soin réservé.",
         "address": "4 rue Jussieu, 69002 Lyon", "phone": "+33 4 78 42 56 51",
         "url": "https://www.visiterlyon.com/sortir/culture-et-loisirs/activites-loisirs-et-bien-etre/bien-etre/spa-carlton-m-gallery",
         "photo": "https://media.lyon-france.com/1280x853/426966/12948176.jpg", "credit": "Photo : Office du tourisme de Lyon"},
        {"id": "lyon-chef", "type": "chef", "tier": 2, "name": "Chef à domicile à Lyon (Take a Chef)",
         "desc": "Le plus grand choix de chefs hors Paris, cuisine lyonnaise ou gastronomique. " + CHEF_NOTE,
         "address": "Lyon et alentours", "url": "https://www.takeachef.com/fr-fr/chef-a-domicile/lyon",
         "photo": "https://d1zzxdyvtq79bu.cloudfront.net/context/frontend/images/open-graph/chef_privado_take_a_chef.jpg", "credit": "Photo : Take a Chef"},
        {"id": "lyon-sucre", "type": "soiree", "tier": 2, "name": "Le Sucre",
         "desc": "Club-rooftop sur le toit de la Sucrière, au bord de la Saône. LA soirée lyonnaise.",
         "address": "50 quai Rambaud, 69002 Lyon", "url": "https://www.le-sucre.eu/",
         **wm("9/94/La_Sucri%C3%A8re_%28Lyon%29_01.jpg/960px-La_Sucri%C3%A8re_%28Lyon%29_01.jpg", "La Sucrière, CC BY-SA 4.0")},
        {"id": "lyon-vieuxlyon", "type": "soiree", "tier": 1, "name": "Vieux Lyon & quais",
         "desc": "Apéro dans les bars du Vieux Lyon et de la presqu'île, puis péniches des quais du Rhône.",
         "address": "Quartier Saint-Jean, 69005 Lyon", "url": "https://www.visiterlyon.com/sortir/nocturne",
         **wm("0/05/La_Sa%C3%B4ne_dans_le_vieux_Lyon_%C3%A0_la_Renaissance.jpg/960px-La_Sa%C3%B4ne_dans_le_vieux_Lyon_%C3%A0_la_Renaissance.jpg", "Vieux Lyon, domaine public")}
      ]
    }
  ],
  "sources": [
    "Gîtes de France (gites-de-france.com), fiches consultées en novembre 2026",
    "Guide Michelin, Gault&Millau, Marriott, Hôtels Barrière, Accor : adresses des hôtels-spas",
    "Offices de tourisme de Lille, Lyon, Bordeaux ; visit.brussels",
    "Take a Chef : tarifs moyens 2026",
    "Brochure spa Les Sources de Caudalie 2025",
    "Photos : sites officiels des lieux ou Wikimedia Commons (licences libres, auteurs sur commons.wikimedia.org)"
  ]
}

root = pathlib.Path(__file__).resolve().parent.parent
(root / "data").mkdir(exist_ok=True)
# Photos de Louise : toutes les images déposées dans assets/louise/
POS = {"01-metro-selfie": "66% 40%", "02-parc-trio": "47% 32%", "03-dos-a-dos": "72% 28%", "04-cuisine": "38% 36%",
       "05-frange": "55% 32%", "06-profil": "36% 36%", "07-bac": "48% 28%", "08-metro": "76% 38%",
       "09-photomaton": "50% 12%", "10-floue": "62% 45%"}
DATA["louise"] = [{"src": "assets/louise/" + f.name, "pos": POS.get(f.stem, "50% 35%")}
                  for f in sorted((root / "assets" / "louise").glob("*"))
                  if f.suffix.lower() in (".jpg", ".jpeg", ".png", ".webp")]
txt = json.dumps(DATA, ensure_ascii=False, indent=1)
(root / "data" / "evjf.json").write_text(txt, encoding="utf-8")
(root / "data" / "embedded_data.js").write_text("window.EVJF_DATA = " + txt + ";\n", encoding="utf-8")
n = sum(len(c["items"]) for c in DATA["cities"])
print(f"OK : {len(DATA['cities'])} villes, {n} propositions, {len(DATA['louise'])} photos de Louise")
