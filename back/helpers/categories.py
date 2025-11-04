from flask import request
import uuid
from config.db import db
from model.tt import *


def InsertAllCategories():
    categories_data = [
        {
            "ca_name": "Agroalimentaire",
            "ca_description": "Industrie spécialisée dans la transformation, la production et la distribution de produits alimentaires issus de l’agriculture et de l’élevage."
        },
        {
            "ca_name": "BTP (Bâtiment et Travaux Publics)",
            "ca_description": "Secteur dédié à la construction, la rénovation et la maintenance d’infrastructures publiques ou privées telles que les bâtiments, routes et ponts."
        },
        {
            "ca_name": "Fabrication de biens de consommation",
            "ca_description": "Industrie produisant des produits destinés à une utilisation directe par les consommateurs, comme les meubles, les ustensiles ou les jouets."
        },
        {
            "ca_name": "Industrie pharmaceutique",
            "ca_description": "Secteur engagé dans la recherche, la fabrication et la distribution de médicaments et produits de santé destinés à la médecine humaine ou vétérinaire."
        },
        {
            "ca_name": "Industrie chimique",
            "ca_description": "Industrie produisant des substances chimiques utilisées dans divers domaines comme l’agriculture, la pharmacie, les cosmétiques ou l’industrie lourde."
        },
        {
            "ca_name": "Industrie textile",
            "ca_description": "Secteur impliqué dans la fabrication de tissus, vêtements et autres produits à base de fibres naturelles ou synthétiques."
        },
        {
            "ca_name": "Électronique / Électroménager",
            "ca_description": "Industrie dédiée à la conception, fabrication et vente d’appareils électroniques et électroménagers pour les ménages ou les entreprises."
        },
        {
            "ca_name": "Automobile et pièces détachées",
            "ca_description": "Secteur couvrant la fabrication, l’assemblage, la vente et la réparation de véhicules ainsi que de pièces détachées pour automobiles."
        },
        {
            "ca_name": "Transformation du bois",
            "ca_description": "Activité industrielle consistant à transformer le bois brut en produits finis ou semi-finis comme le mobilier, les planches ou les panneaux."
        },
        {
            "ca_name": "Transformation du plastique",
            "ca_description": "Secteur impliqué dans la fabrication de produits en plastique à usage industriel ou domestique, à partir de matières premières pétrochimiques."
        },
        {
            "ca_name": "Métallurgie / Sidérurgie",
            "ca_description": "Industrie travaillant l’extraction, la transformation et le traitement des métaux, notamment le fer et l’acier, pour divers usages industriels."
        },
        {
            "ca_name": "Énergie et énergies renouvelables",
            "ca_description": "Secteur produisant et distribuant de l’énergie, incluant les sources fossiles (pétrole, gaz) et renouvelables (solaire, éolienne, hydraulique)."
        },
        {
            "ca_name": "Production d’eau potable",
            "ca_description": "Activité consistant à capter, traiter et distribuer de l’eau propre et potable pour la consommation domestique, industrielle ou agricole."
        },
        {
            "ca_name": "Commerce de détail (boutique, magasin, supérette)",
            "ca_description": "Activité de vente directe de produits aux consommateurs finaux dans des points de vente physiques comme des boutiques, magasins ou supérettes."
        },
        {
            "ca_name": "Supermarché / Hypermarché",
            "ca_description": "Grande surface de distribution proposant un large éventail de produits alimentaires et non alimentaires en libre-service, souvent à prix compétitifs."
        },
        {
            "ca_name": "Import / Export",
            "ca_description": "Commerce international consistant à importer des produits depuis l’étranger ou à exporter des biens locaux vers d'autres pays."
        },
        {
            "ca_name": "Vente en gros",
            "ca_description": "Activité commerciale destinée à la revente en grande quantité à des professionnels, revendeurs ou détaillants, plutôt qu'aux consommateurs finaux."
        },
        {
            "ca_name": "E-commerce",
            "ca_description": "Vente de biens ou services via des plateformes en ligne ou des sites web, avec gestion de paiements numériques et de livraison."
        },
        {
            "ca_name": "Vente de matériaux de construction",
            "ca_description": "Commerce spécialisé dans la distribution de matériaux et équipements destinés à la construction et à la rénovation de bâtiments."
        },
        {
            "ca_name": "Vente d’articles électroménagers",
            "ca_description": "Commerce de vente d’appareils électriques destinés à un usage domestique, comme les réfrigérateurs, machines à laver ou micro-ondes."
        },
        {
            "ca_name": "Vente de vêtements et accessoires",
            "ca_description": "Commerce de détail spécialisé dans la vente de vêtements, chaussures, sacs, bijoux et autres accessoires de mode."
        },
        {
            "ca_name": "Vente de produits agricoles",
            "ca_description": "Activité commerciale dédiée à la vente de produits issus de l’agriculture, tels que fruits, légumes, céréales, ou produits transformés."
        },
        {
            "ca_name": "Vente de produits cosmétiques",
            "ca_description": "Commerce spécialisé dans la distribution de produits de beauté, soins de la peau, maquillage, parfums et produits d’hygiène."
        },
        {
            "ca_name": "Conseil / Consulting",
            "ca_description": "Prestations de conseils stratégiques, opérationnels ou techniques aux entreprises pour optimiser leur organisation, leur gestion ou leur croissance."
        },
        {
            "ca_name": "Comptabilité / Audit / Fiscalité",
            "ca_description": "Services liés à la tenue des comptes, aux audits financiers et à la gestion des obligations fiscales des entreprises et particuliers."
        },
        {
            "ca_name": "Ressources humaines / Recrutement",
            "ca_description": "Services d'externalisation ou d'accompagnement dans la gestion du personnel, le recrutement, la formation et le développement des talents."
        },
        {
            "ca_name": "Sécurité / Gardiennage",
            "ca_description": "Prestations de sécurité physique, de surveillance, de contrôle d’accès et de gardiennage pour les biens, les personnes et les sites sensibles."
        },
        {
            "ca_name": "Maintenance et entretien",
            "ca_description": "Services de maintenance préventive et corrective des équipements, installations techniques, bâtiments ou infrastructures."
        },
        {
            "ca_name": "Déménagement / Logistique",
            "ca_description": "Services de transport, de déménagement de biens, d’objets ou d’équipements, ainsi que la gestion logistique de la chaîne d'approvisionnement."
        },
        {
            "ca_name": "Formation professionnelle",
            "ca_description": "Offres de formations qualifiantes ou continues pour renforcer les compétences des salariés, des demandeurs d’emploi ou des indépendants."
        },
        {
            "ca_name": "Service juridique / Avocat",
            "ca_description": "Prestations de conseils juridiques, d’assistance, de représentation en justice et de rédaction d’actes juridiques par des professionnels du droit."
        },
        {
            "ca_name": "Marketing / Communication",
            "ca_description": "Services liés à la promotion des entreprises, produits ou services via des stratégies de communication, de publicité, de branding ou de marketing digital."
        },
        {
            "ca_name": "Agence de traduction",
            "ca_description": "Services de traduction, d’interprétation et de localisation de documents, sites web ou contenus audio/vidéo dans plusieurs langues."
        },
        {
            "ca_name": "Service de nettoyage industriel",
            "ca_description": "Prestations de nettoyage professionnel pour les locaux industriels, bureaux, chantiers, usines, avec des équipements et produits adaptés."
        },  {
            "ca_name": "Coiffure / Esthétique / Spa",
            "ca_description": "Services de soins corporels incluant coiffure, soins esthétiques, massages, manucure, pédicure, maquillage et bien-être en institut ou à domicile."
        },
        {
            "ca_name": "Services ménagers / Aide à domicile",
            "ca_description": "Prestations d’assistance à domicile incluant le ménage, repassage, préparation des repas, aide aux personnes âgées ou en situation de handicap."
        },
        {
            "ca_name": "Réparation d’appareils électroniques",
            "ca_description": "Services de diagnostic et de réparation d’appareils électroniques tels que téléphones, ordinateurs, téléviseurs, électroménagers, etc."
        },
        {
            "ca_name": "Pressing / Blanchisserie",
            "ca_description": "Services de nettoyage à sec, lavage, repassage et entretien de vêtements, textiles ou linges professionnels ou domestiques."
        },
        {
            "ca_name": "Photographie / Vidéaste",
            "ca_description": "Prestations de captation photo et vidéo pour événements, publicités, portraits, projets artistiques ou communication visuelle."
        },
        {
            "ca_name": "Organisation d’événements",
            "ca_description": "Services de planification, coordination et gestion logistique d’événements privés, professionnels ou publics (mariages, séminaires, concerts, etc.)."
        },
        {
            "ca_name": "Transport de personnes (taxis, VTC, moto-taxi)",
            "ca_description": "Services de déplacement urbain ou interurbain via taxis, véhicules de transport avec chauffeur (VTC), moto-taxis ou autres solutions de mobilité."
        },
        {
            "ca_name": "Agence de voyage",
            "ca_description": "Organisation de séjours, ventes de billets, réservations d’hôtels, circuits touristiques et assistance pour les formalités de voyage."
        },  
        {
            "ca_name": "Développement web / mobile",
            "ca_description": "Conception, développement et maintenance de sites web, applications mobiles et plateformes digitales sur mesure pour entreprises ou particuliers."
        },
        {
            "ca_name": "Fourniture de matériel informatique",
            "ca_description": "Vente et distribution de matériel informatique tel que ordinateurs, imprimantes, périphériques, accessoires et équipements réseaux."
        },
        {
            "ca_name": "Maintenance informatique",
            "ca_description": "Services de dépannage, entretien et support technique pour les équipements informatiques, réseaux et logiciels d’entreprises ou de particuliers."
        },
        {
            "ca_name": "Agence de marketing digital",
            "ca_description": "Stratégies et services en ligne pour améliorer la visibilité, la notoriété et les ventes : réseaux sociaux, publicité en ligne, SEO, emailing, etc."
        },
        {
            "ca_name": "Télécommunications",
            "ca_description": "Fourniture de services de communication tels que la téléphonie fixe et mobile, les réseaux de données, les équipements de télécoms et solutions VoIP."
        },
        {
            "ca_name": "Hébergement web / Cloud",
            "ca_description": "Services d’hébergement de sites web, d’applications, de bases de données et de solutions cloud (stockage, serveurs virtuels, SaaS)."
        },
        {
            "ca_name": "Cybersécurité",
            "ca_description": "Solutions de protection des données, des réseaux et des systèmes informatiques contre les cyberattaques, fuites ou intrusions malveillantes."
        },
        {
            "ca_name": "Startup tech",
            "ca_description": "Jeune entreprise innovante utilisant les technologies pour développer des produits ou services disruptifs dans divers secteurs d’activité."
        },
        {
            "ca_name": "Fournisseur d’accès internet",
            "ca_description": "Entreprise fournissant des services de connexion à Internet pour les particuliers, les entreprises ou les institutions via divers moyens techniques."
        },  {
            "ca_name": "Microfinance",
            "ca_description": "Institution offrant des services financiers (crédit, épargne, assurance) aux personnes ou petites entreprises n’ayant pas accès aux banques traditionnelles."
        },
        {
            "ca_name": "Coopérative d’épargne et de crédit",
            "ca_description": "Organisation mutualiste qui collecte l’épargne de ses membres et leur accorde des prêts à des conditions avantageuses."
        },
        {
            "ca_name": "Assurance",
            "ca_description": "Entreprise proposant des couvertures contre les risques (santé, vie, habitation, automobile, etc.) en échange de primes d’assurance."
        },
        {
            "ca_name": "Banque",
            "ca_description": "Établissement financier autorisé à recevoir des dépôts, accorder des crédits, gérer les comptes et proposer divers services bancaires aux particuliers et entreprises."
        },
        {
            "ca_name": "Services de transfert d’argent",
            "ca_description": "Solutions permettant l’envoi et la réception rapide d’argent au niveau national ou international via des agences, applications ou partenaires."
        },
        {
            "ca_name": "Courtage financier",
            "ca_description": "Activité d’intermédiation entre clients et institutions financières pour l’obtention de prêts, d’assurances ou d’investissements adaptés."
        },
        {
            "ca_name": "Gestion de patrimoine",
            "ca_description": "Services spécialisés visant à optimiser, protéger et faire fructifier les actifs financiers, immobiliers ou successoraux d’un individu ou d’une entreprise."
        },  {
            "ca_name": "Clinique / Centre médical",
            "ca_description": "Établissement de santé privé ou public proposant des consultations médicales, des soins spécialisés et parfois des services de chirurgie ou d’hospitalisation."
        },
        {
            "ca_name": "Pharmacie",
            "ca_description": "Point de vente autorisé à délivrer des médicaments prescrits ou en libre accès, ainsi que des produits de santé, d’hygiène et de parapharmacie."
        },
        {
            "ca_name": "Laboratoire d’analyses médicales",
            "ca_description": "Structure médicale spécialisée dans la réalisation de prélèvements et d’analyses biologiques (sang, urine, etc.) pour le diagnostic et le suivi médical."
        },
        {
            "ca_name": "Cabinet dentaire",
            "ca_description": "Cabinet médical spécialisé dans les soins dentaires, incluant prévention, traitement des caries, orthodontie, chirurgie dentaire, etc."
        },
        {
            "ca_name": "Centre de kinésithérapie",
            "ca_description": "Établissement proposant des soins de rééducation physique et fonctionnelle par des techniques de massage, mobilisation et exercices thérapeutiques."
        },
        {
            "ca_name": "Nutritionniste / Diététicien",
            "ca_description": "Professionnel de la santé spécialisé dans la nutrition, offrant des conseils et des plans alimentaires adaptés à la santé, aux besoins ou aux pathologies du patient."
        },
        {
            "ca_name": "Centre de bien-être / Spa",
            "ca_description": "Espace dédié à la relaxation et aux soins du corps (massages, hammam, sauna, soins esthétiques), visant à améliorer le bien-être physique et mental."
        },
        {
            "ca_name": "Vente de matériel médical",
            "ca_description": "Commerce spécialisé dans la fourniture d’équipements médicaux et paramédicaux : fauteuils roulants, tensiomètres, lits médicaux, consommables, etc."
        },  {
            "ca_name": "École primaire / secondaire / supérieure",
            "ca_description": "Établissements scolaires offrant des formations générales aux niveaux primaire, collège, lycée ou enseignement supérieur classique."
        },
        {
            "ca_name": "Université / Institut",
            "ca_description": "Institutions d’enseignement supérieur dispensant des formations universitaires, des diplômes de licence, master, doctorat, et recherches académiques."
        },
        {
            "ca_name": "Centre de formation professionnelle",
            "ca_description": "Organismes spécialisés dans la formation pratique et technique visant à développer les compétences professionnelles et faciliter l’insertion sur le marché du travail."
        },
        {
            "ca_name": "Cours particuliers",
            "ca_description": "Services personnalisés d’enseignement individuel ou en petits groupes, pour accompagner l’apprentissage ou approfondir des matières spécifiques."
        },
        {
            "ca_name": "Soutien scolaire",
            "ca_description": "Accompagnement scolaire destiné à aider les élèves en difficulté ou souhaitant améliorer leurs résultats via des cours, ateliers ou tutorats."
        },
        {
            "ca_name": "Crèche / Garderie",
            "ca_description": "Structures d’accueil collectif destinées à la garde et à l’éveil des jeunes enfants en bas âge pendant la journée."
        },
        {
            "ca_name": "École de langue",
            "ca_description": "Établissements ou centres proposant des cours pour apprendre ou perfectionner une ou plusieurs langues étrangères à différents niveaux."
        },  {
            "ca_name": "Agence immobilière",
            "ca_description": "Entreprise spécialisée dans la vente, l’achat, la location et la gestion de biens immobiliers pour le compte de clients."
        },
        {
            "ca_name": "Construction / Rénovation",
            "ca_description": "Activités liées à la construction de bâtiments neufs ainsi qu’à la rénovation, réhabilitation et amélioration des structures existantes."
        },
        {
            "ca_name": "Gestion locative",
            "ca_description": "Service d’administration et de gestion des biens immobiliers loués, incluant la recherche de locataires, la perception des loyers et la maintenance."
        },
        {
            "ca_name": "Architecte / Bureau d’études",
            "ca_description": "Professionnels et structures spécialisées dans la conception architecturale, la planification technique et le suivi des projets de construction."
        },
        {
            "ca_name": "Vente de terrains / biens immobiliers",
            "ca_description": "Activité commerciale consistant à proposer à la vente des terrains, maisons, appartements ou autres biens immobiliers."
        },
        {
            "ca_name": "Décoration d’intérieur",
            "ca_description": "Services de conception et d’aménagement esthétique des espaces intérieurs pour améliorer leur fonctionnalité et leur ambiance."
        },  {
            "ca_name": "Transport de marchandises",
            "ca_description": "Service de déplacement et acheminement de biens et marchandises sur des distances locales, régionales ou nationales."
        },
        {
            "ca_name": "Transport international / fret",
            "ca_description": "Organisation et gestion du transport de marchandises entre différents pays, incluant les formalités douanières et logistiques."
        },
        {
            "ca_name": "Entreposage / stockage",
            "ca_description": "Services de conservation, gestion et manutention de marchandises dans des entrepôts ou centres de stockage sécurisés."
        },
        {
            "ca_name": "Transit douanier",
            "ca_description": "Processus d’acheminement des marchandises sous contrôle douanier avant leur importation, exportation ou transit vers un autre pays."
        },
        {
            "ca_name": "Livraison express",
            "ca_description": "Service rapide de livraison de colis ou marchandises, souvent avec des délais de livraison garantis à court terme."
        },
        {
            "ca_name": "Location de véhicules",
            "ca_description": "Mise à disposition de véhicules utilitaires ou de transport pour des durées variables, adaptés aux besoins professionnels ou personnels."
        },
        {
            "ca_name": "Transport maritime / aérien",
            "ca_description": "Services spécialisés dans le transport de marchandises ou passagers par voie maritime ou aérienne à l’échelle nationale ou internationale."
        },  {
            "ca_name": "Maison de production",
            "ca_description": "Entreprise spécialisée dans la production audiovisuelle, cinématographique ou musicale, gérant la création et la diffusion de contenus."
        },
        {
            "ca_name": "Salle de spectacle / théâtre",
            "ca_description": "Lieux dédiés à la présentation de spectacles vivants, concerts, pièces de théâtre, danse ou autres événements culturels."
        },
        {
            "ca_name": "Galerie d’art",
            "ca_description": "Espace d’exposition et de promotion d’œuvres d’art visuel, offrant souvent la vente d’œuvres aux collectionneurs et amateurs."
        },
        {
            "ca_name": "Agence de mannequins",
            "ca_description": "Agence représentant des mannequins pour des défilés, campagnes publicitaires, shootings photo ou autres activités liées à la mode."
        },
        {
            "ca_name": "Studio d’enregistrement",
            "ca_description": "Installation professionnelle équipée pour l’enregistrement, le mixage et la production de sons musicaux, voix ou autres contenus audio."
        },
        {
            "ca_name": "Blog / Média en ligne",
            "ca_description": "Plateforme numérique produisant et diffusant des contenus éditoriaux, vidéos, podcasts ou articles sur divers sujets et actualités."
        },
        {
            "ca_name": "Agence de communication culturelle",
            "ca_description": "Agence spécialisée dans la promotion et la valorisation d’événements, projets ou institutions culturelles via des stratégies de communication ciblées."
        },
        {
            "ca_name": "Restaurants gastronomiques",
            "ca_description": "Établissements haut de gamme offrant une cuisine raffinée, souvent préparée par des chefs renommés, avec un service soigné et une carte des vins élaborée."
        },
        {
            "ca_name": "Restaurants traditionnels",
            "ca_description": "Restaurants proposant des plats classiques issus de la cuisine locale ou régionale, avec un service à table et une ambiance familiale ou conviviale."
        },
        {
            "ca_name": "Fast-food",
            "ca_description": "Restaurants spécialisés dans la restauration rapide, avec des plats comme les burgers, frites, sandwiches ou pizzas, généralement à emporter ou servis rapidement sur place."
        },
        {
            "ca_name": "Food trucks",
            "ca_description": "Camions-restaurants mobiles servant des plats cuisinés sur place, souvent originaux ou spécialisés (tacos, crêpes, burgers, cuisine du monde, etc.)."
        },
        {
            "ca_name": "Restaurants végétariens / véganes",
            "ca_description": "Établissements proposant une cuisine sans viande (végétarien) ou sans aucun produit d'origine animale (végane), avec des alternatives saines et durables."
        },
        {
            "ca_name": "Restaurants spécialisés (cuisine du monde)",
            "ca_description": "Restaurants mettant à l'honneur une cuisine étrangère spécifique comme la cuisine chinoise, libanaise, italienne, indienne, japonaise, africaine, etc."
        },
        {
            "ca_name": "Rôtisseries / Grillades",
            "ca_description": "Restaurants ou stands proposant principalement des viandes rôties ou grillées (poulet braisé, brochettes, côtelettes, etc.) accompagnées de garnitures locales."
        },
        {
            "ca_name": "Pâtisseries / Boulangeries-salons de thé",
            "ca_description": "Établissements vendant des viennoiseries, pâtisseries, gâteaux, parfois avec un espace pour consommer sur place du café ou du thé."
        },
        {
            "ca_name": "Restaurants de fruits de mer",
            "ca_description": "Restaurants spécialisés dans les produits de la mer : poissons, crustacés, coquillages, souvent proposés grillés, frits ou en sauces."
        },
        {
            "ca_name": "Buffets / Libre-service",
            "ca_description": "Restaurants où les clients peuvent se servir eux-mêmes parmi un choix varié de plats disposés sur un buffet, souvent à volonté."
        },
        {
            "ca_name": "Traiteurs",
            "ca_description": "Professionnels de la restauration proposant des plats préparés à emporter ou des services de repas pour des événements (mariages, séminaires, réceptions)."
        },
        {
            "ca_name": "Sandwicheries / Snacks",
            "ca_description": "Établissements proposant des repas rapides à emporter : sandwiches, paninis, salades, wraps, jus frais, etc."
        },
        {
            "ca_name": "Bars à jus / Smoothie bars",
            "ca_description": "Lieux spécialisés dans la préparation de jus de fruits frais, smoothies, boissons detox, parfois accompagnés de snacks sains."
        },
        {
            "ca_name": "Cafétérias d’entreprise ou scolaires",
            "ca_description": "Services de restauration collective proposés au sein d’entreprises, d’écoles ou d’institutions, souvent avec des menus équilibrés et à prix réduit."
        },
        {
            "ca_name": "Bars",
            "ca_description": "Établissements servant des boissons alcoolisées ou non, souvent avec de la musique d’ambiance, des retransmissions sportives ou des animations thématiques."
        },
        {
            "ca_name": "Maquis",
            "ca_description": "Établissements populaires en Afrique de l’Ouest, combinant restauration, bar et ambiance musicale, souvent en plein air ou semi-ouverte, avec des plats locaux et un cadre convivial."
        },
        {
            "ca_name": "Boîtes de nuit / Clubs",
            "ca_description": "Lieux festifs ouverts en soirée et en nuit, proposant de la musique à fort volume, des DJ, une piste de danse, des soirées à thème et un bar."
        },
        {
            "ca_name": "Lounge bars / Rooftops",
            "ca_description": "Espaces haut de gamme offrant une ambiance détendue avec musique chill, cocktails, vue panoramique, souvent situés en terrasse ou sur les toits d’immeubles."
        },
        {
            "ca_name": "Salles de fêtes",
            "ca_description": "Espaces dédiés à l’organisation de cérémonies ou événements privés comme les mariages, anniversaires, baptêmes, avec possibilité de location, décoration et traiteur."
        },
        {
            "ca_name": "Restaurants ambiance live",
            "ca_description": "Restaurants qui offrent des repas accompagnés de spectacles live, musiciens, artistes locaux, ou karaoké pour créer une ambiance festive."
        },
        {
            "ca_name": "Espaces événementiels",
            "ca_description": "Lieux modulables destinés à accueillir des événements professionnels ou privés (séminaires, expositions, galas, soirées privées), souvent avec équipements audiovisuels."
        },
        {
            "ca_name": "Pub / Sports bar",
            "ca_description": "Bars avec une forte identité sportive, diffusant les matchs en direct sur écran géant, avec une carte de boissons et de snacks adaptée aux soirées sportives."
        },
        {
            "ca_name": "Karaoké bars",
            "ca_description": "Bars équipés de scènes ou cabines privées pour chanter sur des musiques populaires, en solo ou entre amis, dans une ambiance ludique."
        },
        {
            "ca_name": "Clubs privés",
            "ca_description": "Établissements sélectifs avec accès réservé aux membres ou à des invités, offrant une ambiance feutrée, des services haut de gamme et des événements exclusifs."
        },
        {
            "ca_name": "Parcs et jardins",
            "ca_description": "Espaces verts aménagés pour la détente, la promenade, les activités de plein air et les loisirs en famille ou entre amis."
        },
        {
            "ca_name": "Bibliothèques",
            "ca_description": "Établissements publics permettant la consultation et l’emprunt de livres, journaux, revues et autres ressources culturelles."
        },
        {
            "ca_name": "Musées et galeries",
            "ca_description": "Lieux de préservation et d’exposition d’œuvres d’art, d’objets historiques ou scientifiques ouverts au grand public."
        },
        {
            "ca_name": "Stades et complexes sportifs",
            "ca_description": "Infrastructures dédiées aux activités sportives, compétitions, entraînements et événements physiques publics ou privés."
        },
        {
            "ca_name": "Plages publiques",
            "ca_description": "Zones aménagées en bord de mer ou de lagune accessibles librement pour la baignade, le repos ou les activités nautiques."
        },
        {
            "ca_name": "Marchés et foires",
            "ca_description": "Espaces publics où se tiennent régulièrement des ventes de produits alimentaires, artisanaux ou vestimentaires."
        },
        {
            "ca_name": "Places publiques",
            "ca_description": "Espaces ouverts souvent situés au centre-ville, servant de lieu de rassemblement, de passage ou d’événements communautaires."
        },
        {
            "ca_name": "Lieux de culte",
            "ca_description": "Édifices religieux ouverts au public pour la prière, les cérémonies et les rassemblements spirituels."
        }

    ]

    for cat in categories_data:
        existing = Categories.query.filter_by(ca_name=cat["ca_name"]).first()
        if not existing:
            db.session.add(Categories(ca_name=cat["ca_name"], status=1, ca_description=cat["ca_description"], create_by=request.json.get('create_by')))
    
    db.session.commit()
    print("Catégories enregistrées avec succès.")



def CreateCategories():
    response = {}
    try:
        ca_name = request.json.get('name')
        ca_description = request.json.get('description')
        create_by = request.json.get('create_by')

        # Valide que create_by est renseigné
        if not create_by:
            return {'status': 'error', 'error_description': 'create_by est requis'}

        # Vérifie si create_by est admin ou teller
        status = None
        single_admin = Admin.query.filter_by(ad_uid=create_by).first()
        if single_admin:
            status = 1
        else:
            single_teller = Teller.query.filter_by(t_uid=create_by).first()
            if single_teller:
                status = 0

        if status is None:
            return {'status': 'error', 'error_description': "Utilisateur 'create_by' inconnu"}

        # Création de la nouvelle catégorie
        new_categories = Categories()
        new_categories.ca_name = ca_name
        new_categories.ca_description = ca_description
        new_categories.create_by = create_by
        new_categories.status = status

        db.session.add(new_categories)
        db.session.commit()

        response['status'] = 'success'
        response['ca_uid'] = new_categories.ca_uid
        response['ca_name'] = ca_name
        response['ca_description'] = ca_description

    except Exception as e:
        response['status'] = 'error'
        response['message'] = str(e)

    return response



def UpdateCategoryStatus():
    response = {}
    try:
        ca_uid = request.json.get('ca_uid')
        new_status = request.json.get('status')

        if ca_uid is None or new_status is None:
            return {'status': 'error', 'error_description': 'ca_uid et status sont requis'}

        if not isinstance(new_status, bool):
            if isinstance(new_status, str):
                if new_status.lower() == 'true':
                    new_status = 1
                elif new_status.lower() == 'false':
                    new_status = 0
                else:
                    return {'status': 'error', 'error_description': 'Status doit être un booléen'}
            else:
                return {'status': 'error', 'error_description': 'Status doit être un booléen'}

        category = Categories.query.filter_by(ca_uid=ca_uid).first()

        if not category:
            return {'status': 'error', 'error_description': 'Catégorie non trouvée'}

        category.status = new_status
        db.session.commit()

        response['status'] = 'success'
        response['ca_uid'] = ca_uid
        response['new_status'] = new_status

    except Exception as e:
        response['status'] = 'error'
        response['error_description'] = str(e)

    return response



def UpdateCategories():

    response = {}
    try:
        ca_uid = request.json.get('ca_uid')
        update_categories = Categories.query.filter_by(ca_uid = ca_uid).first_or_404()
        update_categories.ca_name = request.json.get('name', update_categories.ca_name)
        update_categories.ca_description = request.json.get('description', update_categories.ca_description)
     
        db.session.add(update_categories)
        db.session.commit() 

        rs  = {}
        rs['ca_uid'] = ca_uid
        rs['name'] = update_categories.ca_name
        rs['description'] = update_categories.ca_description
        rs['status'] = update_categories.ca_status
        
        response['status'] = 'success'
        response['categorie'] = rs

    except Exception as e:
        response['status'] = 'error'
        response['error_description'] = str(e)

    return response


def DeleteCategories():

    response = {}
    try:
        ca_uid = request.json.get('ca_uid')
        delete_categories = Categories.query.filter_by(ca_uid=ca_uid).first_or_404()
        db.session.delete(delete_categories)
        db.session.commit()

        response['status'] = 'success'

    except Exception as e:
        response['error_description'] = str(e)
        response['status'] = 'error' + str(e)

    return response



def ReadAllCategories():

    response = {}
    try:
        all_categirie = Categories.query.all()
        categories_info = []
        categorie_name = []
        for categorie in all_categirie:
            if categorie.status == 1:
                categorie_infos = {
                    'ca_uid': categorie.ca_uid,
                    'name': categorie.ca_name,              
                    'description': categorie.ca_description,              
                }
                name = {
                    'name': categorie.ca_name,              
                }
                categories_info.append(categorie_infos)
                categorie_name.append(name)

        response['status'] = 'success'
        response ['categorie_name'] = categorie_name
        response ['categories'] = categories_info

    except Exception as e:
        response['status'] = 'error'
        response['error_description'] = str(e)

    return response



def ReadSingleCategories():

    response = {}
    try:
        ca_uid = request.json.get('ca_uid')
        single_categories = Categories.query.filter_by(ca_uid=ca_uid).first_or_404()
        categories_infos = {
            'ca_uid': single_categories.ca_uid,
            'name': single_categories.ca_name,  
            'description': single_categories.ca_description,              
        }
        response['status'] = 'success'
        response['categorie'] = categories_infos

    except Exception as e:
        response['status'] = 'error'
        response['error_description'] = str(e)

    return response

