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
  "updated": "2026-11-27",
  "title": "Louison la reine et ses 6 gueux",
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
    "Offices de tourisme de Madrid (esmadrid.com), Rome (turismoroma.it), Amsterdam (iamsterdam.com) ; Time Out ; Funbooker, Winedering, Privateaser",
    "Photos : sites officiels des lieux ou Wikimedia Commons (licences libres, auteurs sur commons.wikimedia.org)"
  ]
}


# ---------------------------------------------------------------- RETOUCHES
# 1) On retire les propositions bas de gamme (demande de Marie, 27/11/2026)
REMOVE = {"reims-mellifera", "reims-apostrophe", "lille-grenier", "lille-vieuxlille",
          "bxl-delirium", "bxl-sgery", "bdx-moulin", "bdx-hammam", "bdx-saunham",
          "bdx-darwin", "bdx-gites-spa", "lyon-balicina", "lyon-vieuxlyon"}
del DATA["tiers"]["1"]
DATA["types"] = {
  "logement": {"label": "Logements", "emoji": "🏡"},
  "spa": {"label": "Spa de la journée", "emoji": "🧖‍♀️"},
  "fun": {"label": "Activités marrantes", "emoji": "🎉"},
  "activite": {"label": "Visite", "emoji": "🥂"},
  "chef": {"label": "Chef à domicile", "emoji": "👩‍🍳"},
  "soiree": {"label": "Sortir le soir", "emoji": "🪩"},
}
FUN = {
 "reims": [
  {"id": "reims-sabrage", "type": "fun", "tier": 2, "name": "Cours de sabrage – Champagne Caroline Dufour",
   "desc": "Ouvrir une bouteille de champagne au sabre, comme des hussards. Puis on la boit, évidemment. Dès 50 €/pers. (Grande Réserve), jusqu'à 25 personnes.",
   "address": "10 rue Noël, 51100 Reims", "url": "https://www.winedering.com/fr/introduction-to-sabrage-at-champagne-caroline-dufour-in-reims_d5577_travel",
   "photo": "https://cdn.winedering.com/uploads/travels/5577/big/img1286.jpg.webp?hash=8e30a659c31b53017073692309ab0da1", "credit": "Photo : Winedering"}],
 "deauville": [
  {"id": "deau-cheval", "type": "fun", "tier": 2, "name": "Balade à cheval spéciale EVJF",
   "desc": "Randonnée « spéciale EVG/EVJF » d'1 h avec une monitrice diplômée d'État, à 15 min de Deauville. 75 €/pers., par groupes de 4 cavaliers (on fait 2 tours).",
   "address": "197 chemin du Calvaire, 14950 Glanville", "url": "https://www.funbooker.com/fr/annonce/balade-a-cheval-proche-de-deauville/voir",
   "photo": "https://res.cloudinary.com/funbooker/image/upload/ar_1:1,f_auto,q_auto,t_lr-medium,w_400/v1/marketplace-listing/xgugnnw8aci4enhwxvlh", "credit": "Photo : Funbooker"}],
 "lille": [
  {"id": "lille-karafun", "type": "fun", "tier": 2, "name": "KaraFun Lille – karaoké en salle privée",
   "desc": "Salles de karaoké et de quiz privatisées, rien que pour nous. Personne ne saura qui a chanté du Lara Fabian. Sauf tout le monde.",
   "address": "8 rue Ratisbonne, 59000 Lille", "url": "https://www.privateaser.com/lieu/5628-karafun-bar-lille",
   "photo": "https://privateaser-media.s3.eu-west-1.amazonaws.com/etab_photos/5628/750x375/404245.jpg", "credit": "Photo : Privateaser"}],
 "bruxelles": [
  {"id": "bxl-gerbaud", "type": "fun", "tier": 2, "name": "Chocolaterie Laurent Gerbaud",
   "desc": "Atelier vitré où l'on voit fabriquer les chocolats, puis salon de dégustation près du Mont des Arts. Pour se donner bonne conscience avant les bières.",
   "address": "Rue Ravenstein 2D, 1000 Bruxelles", "url": "https://www.visit.brussels/fr/visiteurs/boire-et-manger/ou-acheter-du-chocolat-a-bruxelles",
   "photo": "https://www.visit.brussels/content/dam/visitbrussels/images/b2c/where-to-eat/specialites-culinaires/Chocolat_8660x5773.jpg/_jcr_content/renditions/facebook.jpeg", "credit": "Photo : visit.brussels"},
  {"id": "bxl-bbp", "type": "fun", "tier": 2, "name": "Brussels Beer Project – taproom Dansaert",
   "desc": "Brasserie artisanale culte : dégustation des bières maison en plein centre. Plus classe que le Delirium, on peut le dire à nos parents.",
   "address": "Rue Antoine Dansaert 188, 1000 Bruxelles", "url": "https://www.beerproject.be/fr/pages/dansaert-taproom",
   "photo": "https://beerproject.be/cdn/shop/files/ALL_STARS_9534e47e-18d5-4992-8cf8-6ba37ce749b8_1200x1200.jpg?v=1625556565", "credit": "Photo : Brussels Beer Project"}],
 "bordeaux": [
  {"id": "bdx-creevin", "type": "fun", "tier": 2, "name": "Atelier « Créez votre propre vin »",
   "desc": "On assemble sa propre cuvée avec un œnologue, puis visite du Musée du Vin et du Négoce. 75 €/pers., privatisable. Nom de la cuvée suggéré : « Château Louison 2027 ».",
   "address": "41 rue Borie, 33000 Bordeaux", "url": "https://www.funbooker.com/fr/annonce/decouvrez-et-creez-votre-vin-lors-dune-visite-a-bordeaux-33/voir",
   "photo": "https://res.cloudinary.com/funbooker/image/upload/ar_1:1,f_auto,q_auto,t_lr-medium,w_400/v1/marketplace-listing/ea5nigp7ciuwblb6dpvi", "credit": "Photo : Funbooker"},
  {"id": "bdx-citeduvin", "type": "activite", "tier": 2, "name": "La Cité du Vin",
   "desc": "Le musée du vin XXL au bord de la Garonne, avec dégustation au belvédère tout en haut. Culturel ET alcoolisé.",
   "address": "134 quai de Bacalan, 33300 Bordeaux", "url": "https://www.laciteduvin.com/fr",
   "photo": "https://thumb.wikimedia.org/wikipedia/commons/thumb/f/fa/Cit%C3%A9_du_Vin_Bordeaux_31.jpg/960px-Cit%C3%A9_du_Vin_Bordeaux_31.jpg", "credit": "Photo Wikimedia Commons · La Cité du Vin"}],
 "lyon": [
  {"id": "lyon-karaoke", "type": "fun", "tier": 2, "name": "Karaoké Box Guillotière",
   "desc": "Box de karaoké privée pour 7 à 18 personnes, 2 h de micro. Noté 4,8/5. Le chef à domicile n'est pas invité à chanter.",
   "address": "8 place Raspail, 69007 Lyon", "url": "https://www.funbooker.com/fr/annonce/karaoke-box-a-lyon-69/voir",
   "photo": "https://res.cloudinary.com/funbooker/image/upload/ar_1:1,f_auto,q_auto,t_lr-medium,w_400/v1/marketplace-listing/p4rbl6ezuxry0vn3oi26", "credit": "Photo : Funbooker"},
  {"id": "lyon-quizroom", "type": "fun", "tier": 2, "name": "Quiz Room – plateau télé",
   "desc": "Jeu télé grandeur nature avec de vrais buzzers. Dès 50 €/pers. Idéal pour savoir enfin qui connaît le mieux Louise.",
   "address": "51 rue Denuzière, 69002 Lyon", "url": "https://www.quizroom.fr/",
   "photo": "https://cdn.prod.website-files.com/5cc01dcb6a3b686cd53e9e64/62610a33307149a27d9c153f_Buzzez%20pour%20de%20vrai%20comme%20sur%20un%20plateau%20TV.png", "credit": "Photo : Quiz Room"}],
}
VILLAS = {
 "bordeaux": {"id": "bdx-villas", "type": "logement", "tier": 2, "name": "Villas avec spa autour de Bordeaux",
   "desc": "Sélection Airbnb déjà filtrée : maisons entières, 7 voyageurs, au moins 4 chambres, avec jacuzzi. Vers Martillac et Léognan, au milieu des vignes et à 20 min des quais.",
   "address": "Martillac, 33650 (20 min de Bordeaux)", "url": "https://www.airbnb.fr/s/Martillac--France/homes?adults=7&min_bedrooms=4&amenities%5B%5D=25&room_types%5B%5D=Entire%20home%2Fapt",
   **wm("0/0d/Ch%C3%A2teau_Smith-Haut-Lafitte.jpg/960px-Ch%C3%A2teau_Smith-Haut-Lafitte.jpg", "vignes de Martillac, CC BY-SA")}
}
for c in DATA["cities"]:
    c["items"] = [i for i in c["items"] if i["id"] not in REMOVE]
    for i in c["items"]:
        if i["id"] == "reims-pommery": i["tier"] = 2
        if i["id"] == "bxl-airbnb":
            i["name"] = "Maisons de maître à Ixelles / Uccle"
            i["desc"] = "Sélection Airbnb déjà filtrée : maisons entières pour 7, au moins 4 chambres, dans les beaux quartiers au sud du centre. Assez de place pour le chef et pour la piste de danse."
            i["url"] = "https://www.airbnb.fr/s/Ixelles--Belgique/homes?adults=7&min_bedrooms=4&room_types%5B%5D=Entire%20home%2Fapt"
    if c["id"] in VILLAS: c["items"].insert(0, VILLAS[c["id"]])
    c["items"] += FUN.get(c["id"], [])


# ---------------------------------------------------------------- VILLES EN AVION (27/11/2026)
WC = "https://thumb.wikimedia.org/wikipedia/commons/thumb/"
TAC = "https://d1zzxdyvtq79bu.cloudfront.net/context/frontend/images/open-graph/chef_privado_take_a_chef.jpg"
def airbnb(q, extra=""):
    return f"https://www.airbnb.fr/s/{q}/homes?adults=7&min_bedrooms=4&room_types%5B%5D=Entire%20home%2Fapt{extra}"
def chef(cid, city, url):
    return {"id": cid, "type": "chef", "tier": 2, "name": f"Chef à domicile à {city} (Take a Chef)",
            "desc": "Take a Chef fonctionne aussi ici : on décrit la soirée, plusieurs chefs proposent un menu. Prix souvent un peu plus doux qu'en France. " + CHEF_NOTE,
            "address": city, "url": url, "photo": TAC, "credit": "Photo : Take a Chef"}
for c in DATA["cities"]: c.setdefault("mode", "train")
DATA["cities"] += [
 {"id": "barcelone", "mode": "avion", "name": "Barcelone", "emoji": "🇪🇸",
  "trip": "✈️ 1 h 45 de vol (Paris → Barcelone-El Prat)",
  "vibe": "Plage, tapas, cava et soirées qui commencent à minuit. Spa dans des bains romains à la bougie, catamaran au coucher du soleil.",
  "joke": "À Barcelone on dîne à 22 h et on sort à 1 h. Le chef à domicile fera donc le petit-déjeuner.",
  "scores": {"spa": 5, "soiree": 5, "budget": 3}, "photo": WC + "7/77/Beach%2C_Barcelona_%28P1170713%29.jpg/960px-Beach%2C_Barcelona_%28P1170713%29.jpg",
  "credit": "Photo Wikimedia Commons · plage de Barcelone, CC BY-SA 4.0", "search": "Barcelone, Espagne",
  "items": [
   {"id": "bcn-villas", "type": "logement", "tier": 2, "name": "Maisons avec piscine autour de Barcelone",
    "desc": "Sélection Airbnb déjà filtrée : maisons entières pour 7, au moins 4 chambres, avec piscine. Côté Sitges ou Castelldefels, à 30 min du centre et à 10 min de la plage.",
    "address": "Sitges / Castelldefels (30 min de Barcelone)", "url": airbnb("Sitges--Espagne", "&amenities%5B%5D=7"),
    "photo": WC + "7/7c/Boats%2C_Barcelona_%28P1170705%29.jpg/960px-Boats%2C_Barcelona_%28P1170705%29.jpg", "credit": "Photo Wikimedia Commons · CC BY-SA 4.0"},
   {"id": "bcn-aire", "type": "spa", "tier": 3, "name": "AIRE Ancient Baths",
    "desc": "Bains thermaux à la romaine dans une ancienne bâtisse du Born : bassins chaud, froid, salé, à la lueur des bougies. Massages possibles.",
    "address": "Passeig de Picasso 22, 08003 Barcelone", "url": "https://beaire.com/en/aire-ancient-baths-barcelona",
    "photo": WC + "e/e2/Porto_deportivo_en_Barcelona_B19.jpg/960px-Porto_deportivo_en_Barcelona_B19.jpg", "credit": "Photo Wikimedia Commons · Barcelone, CC BY-SA 4.0"},
   chef("bcn-chef", "Barcelone", "https://www.takeachef.com/en-es/private-chef/barcelona"),
   {"id": "bcn-cata", "type": "fun", "tier": 2, "name": "Catamaran privé au coucher du soleil",
    "desc": "2 h en mer rien que pour nous, skipper inclus, départ du Port Olímpic environ 2 h avant le coucher du soleil. Cava, musique, et photos de groupe qui feront des jalouses.",
    "address": "Port Olímpic, 08005 Barcelone", "url": "https://www.nautal.com/uk/activities/barcelona/sunset-catamaran-experience-in-barcelona-30306",
    "photo": WC + "7/7c/Boats%2C_Barcelona_%28P1170705%29.jpg/960px-Boats%2C_Barcelona_%28P1170705%29.jpg", "credit": "Photo Wikimedia Commons · CC BY-SA 4.0"},
   {"id": "bcn-opium", "type": "soiree", "tier": 3, "name": "Opium Barcelona",
    "desc": "Club sur la plage, à côté du Port Olímpic : on danse les pieds presque dans le sable.",
    "address": "Passeig Marítim de la Barceloneta 34, 08003 Barcelone", "url": "https://www.timeout.com/barcelona/clubs/opium-mar",
    "photo": WC + "7/77/Beach%2C_Barcelona_%28P1170713%29.jpg/960px-Beach%2C_Barcelona_%28P1170713%29.jpg", "credit": "Photo Wikimedia Commons · CC BY-SA 4.0"}]},
 {"id": "madrid", "mode": "avion", "name": "Madrid", "emoji": "💃",
  "trip": "✈️ 2 h de vol (Paris → Madrid-Barajas)",
  "vibe": "Tapas, flamenco, terrasses et clubs sur 7 étages. Hammam arabe en plein centre. Ville qui ne dort jamais, nous non plus.",
  "joke": "Madrid, où « on rentre tôt » veut dire 6 h du matin. Prévoir des lunettes de soleil pour le brunch.",
  "scores": {"spa": 4, "soiree": 5, "budget": 4}, "photo": WC + "f/f3/Gran_Via%2C_Madrid%2C_at_night_II.jpg/960px-Gran_Via%2C_Madrid%2C_at_night_II.jpg",
  "credit": "Photo Wikimedia Commons · Gran Vía, CC BY 2.0", "search": "Madrid, Espagne",
  "items": [
   {"id": "mad-maisons", "type": "logement", "tier": 2, "name": "Grandes maisons à Madrid",
    "desc": "Sélection Airbnb déjà filtrée : logements entiers pour 7, au moins 4 chambres, avec jacuzzi. Viser les quartiers Salamanca, Chamberí ou La Latina pour tout faire à pied.",
    "address": "Madrid (Salamanca, Chamberí, La Latina)", "url": airbnb("Madrid--Espagne", "&amenities%5B%5D=25"),
    "photo": WC + "5/58/Plaza_Mayor_de_Madrid_-_01.jpg/960px-Plaza_Mayor_de_Madrid_-_01.jpg", "credit": "Photo Wikimedia Commons · Plaza Mayor, CC BY-SA 3.0"},
   {"id": "mad-hammam", "type": "spa", "tier": 2, "name": "Hammam Al Ándalus",
    "desc": "Bains arabes à la lumière tamisée : bassins chaud, tiède, froid, hammam et massages, à deux pas de la Puerta del Sol.",
    "address": "Calle de Atocha 14, 28012 Madrid", "url": "https://www.esmadrid.com/mcb/en/venue-service/hammam-al-andalus-madrid",
    "photo": WC + "0/04/Ba%C3%B1os_%C3%A1rabes_Hammam_al_%C3%81ndalus%2C_M%C3%A1laga%2C_Espa%C3%B1a%2C_2023-05-20%2C_DD_133.jpg/960px-Ba%C3%B1os_%C3%A1rabes_Hammam_al_%C3%81ndalus%2C_M%C3%A1laga%2C_Espa%C3%B1a%2C_2023-05-20%2C_DD_133.jpg", "credit": "Photo Wikimedia Commons · Hammam Al Ándalus (Málaga), CC BY-SA 4.0"},
   chef("mad-chef", "Madrid", "https://www.takeachef.com/en-es/private-chef/madrid"),
   {"id": "mad-corral", "type": "fun", "tier": 3, "name": "Flamenco au Corral de la Morería",
    "desc": "Le tablao flamenco le plus célèbre du monde (depuis 1956). Spectacle avec dîner ou boisson. Défi : Louise doit apprendre un pas avant la fin du week-end.",
    "address": "Calle de la Morería 17, 28005 Madrid", "url": "https://www.esmadrid.com/en/nightlife/corral-moreria",
    "photo": "https://www.esmadrid.com/sites/default/files/styles/content_type_full/public/recursosturisticos/noche/2024884750_117201212926_adj.jpg?itok=r-L33uTt", "credit": "Photo : esmadrid.com"},
   {"id": "mad-kapital", "type": "soiree", "tier": 2, "name": "Teatro Kapital",
    "desc": "Club géant sur 7 étages, une ambiance par étage. On se perd, on se retrouve au rooftop.",
    "address": "Calle de Atocha 125, 28012 Madrid", "url": "https://teatrokapital.com/",
    "photo": WC + "b/b8/Teatro_Kapital_Madrid.jpg/960px-Teatro_Kapital_Madrid.jpg", "credit": "Photo Wikimedia Commons · CC BY-SA 4.0"}]},
 {"id": "budapest", "mode": "avion", "name": "Budapest", "emoji": "🇭🇺",
  "trip": "✈️ 2 h 15 de vol (Paris → Budapest)",
  "vibe": "La capitale des bains thermaux et des « ruin bars ». Très bon rapport qualité-prix, et une fête dans les bains le samedi soir.",
  "joke": "Budapest : le seul endroit où on peut faire la fête en maillot de bain en avril sans finir en hypothermie.",
  "scores": {"spa": 5, "soiree": 5, "budget": 5}, "photo": WC + "f/fd/Sz%C3%A9chenyi_Chain_Bridge_in_Budapest_at_night.jpg/960px-Sz%C3%A9chenyi_Chain_Bridge_in_Budapest_at_night.jpg",
  "credit": "Photo Wikimedia Commons · Pont des Chaînes, CC0", "search": "Budapest, Hongrie",
  "items": [
   {"id": "bud-appart", "type": "logement", "tier": 2, "name": "Grands appartements de standing à Budapest",
    "desc": "Sélection Airbnb déjà filtrée : logements entiers pour 7, au moins 4 chambres. Les beaux appartements haussmanniens du centre (districts V, VI, VII) sont très abordables.",
    "address": "Budapest, districts V-VI-VII", "url": airbnb("Budapest--Hongrie"),
    "photo": WC + "b/bc/BP_parliament_at_night_B%C3%85n.JPG/960px-BP_parliament_at_night_B%C3%85n.JPG", "credit": "Photo Wikimedia Commons · Parlement, CC BY 2.5"},
   {"id": "bud-szechenyi", "type": "spa", "tier": 2, "name": "Bains Széchenyi",
    "desc": "Les bains thermaux mythiques : 18 bassins dont des extérieurs à 38 °C, saunas, massages. Une journée entière pour quelques dizaines d'euros.",
    "address": "Állatkerti körút 9-11, 1146 Budapest", "url": "https://szechenyibath.hu/",
    "photo": WC + "7/71/Budapest_Sz%C3%A9chenyi_Baths_R01.jpg/960px-Budapest_Sz%C3%A9chenyi_Baths_R01.jpg", "credit": "Photo Wikimedia Commons · CC BY 3.0"},
   chef("bud-chef", "Budapest", "https://www.takeachef.com/en-hu/private-chef/budapest"),
   {"id": "bud-sparty", "type": "fun", "tier": 2, "name": "Sparty – la fête dans les bains Széchenyi",
    "desc": "Le samedi soir : DJ, lasers et danseurs dans les bassins à 34-38 °C. Dès ≈ 30 €/pers. Le spa et la soirée en un seul ticket. Réservé aux majeurs.",
    "address": "Állatkerti körút 9-11, 1146 Budapest", "url": "https://www.headout.com/sparty-budapest-c-802",
    "photo": WC + "6/65/Budapest_Sz%C3%A9chenyi_Baths_R04.jpg/960px-Budapest_Sz%C3%A9chenyi_Baths_R04.jpg", "credit": "Photo Wikimedia Commons · CC BY 3.0"},
   {"id": "bud-szimpla", "type": "soiree", "tier": 2, "name": "Szimpla Kert",
    "desc": "Le premier et le plus célèbre des « ruin bars » : un immeuble en ruine rempli de bric-à-brac, de bars et de musique. Ouvert jusqu'à 4 h.",
    "address": "Kazinczy utca 14, 1075 Budapest", "url": "https://www.timeout.com/budapest/bars-and-pubs/szimpla-kert",
    "photo": "https://media.timeout.com/images/106021449/image.jpg", "credit": "Photo : Time Out"}]},
 {"id": "rome", "mode": "avion", "name": "Rome", "emoji": "🇮🇹",
  "trip": "✈️ 2 h 05 de vol (Paris → Rome-Fiumicino)",
  "vibe": "Dolce vita : apéritivo à Trastevere, pâtes fraîches, hammam au cœur du Ghetto. Plus romantique que déchaînée, mais quel décor.",
  "joke": "À Rome, on fera comme les Romains : apéritivo à 18 h, re-apéritivo à 19 h, et « juste un dernier » à 2 h.",
  "scores": {"spa": 4, "soiree": 4, "budget": 3}, "photo": WC + "d/d8/Colosseum_in_Rome-April_2007-1-_copie_2B.jpg/960px-Colosseum_in_Rome-April_2007-1-_copie_2B.jpg",
  "credit": "Photo Wikimedia Commons · Colisée, CC BY-SA 2.5", "search": "Rome, Italie",
  "items": [
   {"id": "rom-villas", "type": "logement", "tier": 2, "name": "Villas et grands appartements à Rome",
    "desc": "Sélection Airbnb déjà filtrée : logements entiers pour 7, au moins 4 chambres, avec jacuzzi. Trastevere ou Monti pour sortir à pied.",
    "address": "Rome (Trastevere, Monti)", "url": airbnb("Rome--Italie", "&amenities%5B%5D=25"),
    "photo": WC + "9/98/Santa_Maria_in_Trastevere_church_in_Rome_%2812%29.jpg/960px-Santa_Maria_in_Trastevere_church_in_Rome_%2812%29.jpg", "credit": "Photo Wikimedia Commons · Trastevere, CC BY-SA 4.0"},
   {"id": "rom-acqua", "type": "spa", "tier": 3, "name": "AcquaMadre Hammam",
    "desc": "Hammam élégant dans le Ghetto, près de Piazza Argentina : bains chaud, tiède, froid, gommage. Réservation nécessaire.",
    "address": "Via di Sant'Ambrogio 17, 00186 Rome", "url": "https://www.wantedinrome.com/yellowpage/acquamadre-hammam.html",
    "photo": WC + "7/7e/Santa_Maria_in_Trastevere_church_in_Rome_%2813%29.jpg/960px-Santa_Maria_in_Trastevere_church_in_Rome_%2813%29.jpg", "credit": "Photo Wikimedia Commons · Rome, CC BY-SA 4.0"},
   chef("rom-chef", "Rome", "https://www.takeachef.com/en-it/private-chef/rome"),
   {"id": "rom-pasta", "type": "fun", "tier": 2, "name": "Cours de pâtes fraîches à la maison",
    "desc": "On demande au chef à domicile de commencer par un cours de pâtes : chacun fait ses tagliatelles, puis on les mange. Celui qui rate ses pâtes paie le limoncello.",
    "address": "Dans la maison louée", "url": "https://www.takeachef.com/en-it/private-chef/rome",
    "photo": WC + "d/d8/Colosseum_in_Rome-April_2007-1-_copie_2B.jpg/960px-Colosseum_in_Rome-April_2007-1-_copie_2B.jpg", "credit": "Photo Wikimedia Commons · CC BY-SA 2.5"},
   {"id": "rom-freni", "type": "soiree", "tier": 2, "name": "Freni e Frizioni",
    "desc": "Bar à cocktails culte de Trastevere (classé parmi les meilleurs du monde), apéritivo et foule sur la placette jusqu'à tard.",
    "address": "Via del Politeama 4, 00153 Rome", "phone": "+39 06 4549 7499", "url": "https://www.timeout.com/rome/bars-and-pubs/freni-e-frizioni",
    "photo": "https://media.timeout.com/images/106111178/image.jpg", "credit": "Photo : Time Out"}]},
 {"id": "amsterdam", "mode": "avion", "name": "Amsterdam", "emoji": "🇳🇱",
  "trip": "✈️ 1 h 20 de vol, ou 3 h 20 de train direct (Paris-Nord → Amsterdam)",
  "vibe": "Canaux, vélos, bières et clubs mythiques. Grand spa urbain avec 8 saunas. Facile d'accès, même en train.",
  "joke": "Amsterdam : on ira voir les tulipes. Enfin, c'est ce qu'on dira aux parents.",
  "scores": {"spa": 5, "soiree": 5, "budget": 3}, "photo": WC + "d/d3/Water_reflection_of_canal_houses_at_blue_hour_in_Damrak_Amsterdam_the_Netherlands.jpg/960px-Water_reflection_of_canal_houses_at_blue_hour_in_Damrak_Amsterdam_the_Netherlands.jpg",
  "credit": "Photo Wikimedia Commons · Damrak, CC BY-SA 4.0", "search": "Amsterdam, Pays-Bas",
  "items": [
   {"id": "ams-maisons", "type": "logement", "tier": 3, "name": "Maisons de canal à Amsterdam",
    "desc": "Sélection Airbnb déjà filtrée : logements entiers pour 7, au moins 4 chambres. Les maisons de canal sont chères mais magiques. Plan B moins cher : une péniche-logement.",
    "address": "Amsterdam (Jordaan, De Pijp)", "url": airbnb("Amsterdam--Pays-Bas"),
    "photo": WC + "e/ef/Colorful_canal_houses_at_golden_hour_in_Damrak_avenue_Amsterdam_the_Netherlands.jpg/960px-Colorful_canal_houses_at_golden_hour_in_Damrak_avenue_Amsterdam_the_Netherlands.jpg", "credit": "Photo Wikimedia Commons · CC BY-SA 4.0"},
   {"id": "ams-zuiver", "type": "spa", "tier": 2, "name": "Spa Zuiver",
    "desc": "Grand spa dans les bois d'Amsterdam : 8 saunas, bains, salles de repos et piscine de 40 m en partie couverte.",
    "address": "Koenenkade 8, 1081 KH Amsterdam", "phone": "+31 20 301 0700", "url": "https://www.inyourpocket.com/Amsterdam/Spa-Amsterdam-Zuiver_96928v",
    "photo": "https://s.inyourpocket.com/gallery/31809.jpg", "credit": "Photo : In Your Pocket"},
   chef("ams-chef", "Amsterdam", "https://www.takeachef.com/en-nl/private-chef/amsterdam"),
   {"id": "ams-heineken", "type": "fun", "tier": 2, "name": "Heineken Experience",
    "desc": "Visite interactive de l'ancienne brasserie, avec dégustation et rooftop en option. Espaces privatisables pour les groupes. Pédagogique, on vous jure.",
    "address": "Stadhouderskade 78, 1072 AE Amsterdam", "url": "https://www.heinekenexperience.com/en/about-the-experience",
    "photo": WC + "d/d4/Heineken_Museum_Experience_%2C_Amsterdam_-_Ank_Kumar_01.jpg/960px-Heineken_Museum_Experience_%2C_Amsterdam_-_Ank_Kumar_01.jpg", "credit": "Photo Wikimedia Commons · CC0"},
   {"id": "ams-bateau", "type": "fun", "tier": 2, "name": "Bateau privé sur les canaux",
    "desc": "Petit bateau privatisé pour 7 avec skipper, boissons à bord, 1 à 2 h sur les canaux. Plusieurs compagnies partent du centre : comparer sur le site officiel de la ville.",
    "address": "Canaux du centre d'Amsterdam", "url": "https://www.iamsterdam.com/en/see-and-do/things-to-do",
    "photo": WC + "5/52/Canal_boats_in_Amsterdam_04.jpg/960px-Canal_boats_in_Amsterdam_04.jpg", "credit": "Photo Wikimedia Commons · CC BY 4.0"},
   {"id": "ams-paradiso", "type": "soiree", "tier": 2, "name": "Paradiso",
    "desc": "Ancienne église devenue salle de concert et club mythique. Soirées jusqu'au bout de la nuit.",
    "address": "Weteringschans 6-8, 1017 SG Amsterdam", "url": "https://www.paradiso.nl/",
    "photo": WC + "0/00/Paradiso%2C_Amsterdam_7239.jpg/960px-Paradiso%2C_Amsterdam_7239.jpg", "credit": "Photo Wikimedia Commons · CC BY-SA 4.0"}]},
]

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
