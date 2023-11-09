import re
import csv
from collections import Counter
from bs4 import BeautifulSoup

# Étape 1 : Créer une fonction pour compter les occurrences de mots
def count_words(text):
    words = re.findall(r'\w+', text.lower())
    word_counts = Counter(words)
    sorted_word_counts = dict(sorted(word_counts.items(), key=lambda item: item[1], reverse=True))
    return sorted_word_counts

# Étape 2 : Créer une fonction pour supprimer les mots parasites
def remove_stopwords(word_counts, stopwords):
    filtered_word_counts = {word: count for word, count in word_counts.items() if word not in stopwords}
    return filtered_word_counts

# Étape 3 : Créer une fonction pour récupérer les mots parasites depuis un fichier CSV
def get_stopwords_from_file(filename):
    stopwords = []
    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            stopwords.extend(row)
    return stopwords
def compter_occurrences(texte):
    # Suppression de la ponctuation et conversion en minuscules
    texte = texte.lower()
    texte = re.sub(r'[^\w\s]','',texte)  # Utilisation d'une expression régulière pour supprimer la ponctuation
    mots = texte.split()
    
    # Comptage des occurrences des mots
    occurrences = {}
    for mot in mots:
        occurrences[mot] = occurrences.get(mot, 0) + 1
    
    # Tri des mots par occurrence
    occurrences_triees = dict(sorted(occurrences.items(), key=lambda item: item[1], reverse=True))
    
    return occurrences_triees

def enlever_parasites(occurrences, parasites):
    # Nettoyage des mots parasites (conversion en minuscules et suppression des caractères spéciaux)
    parasites = set(mot.lower() for mot in parasites)
    return {mot: occurrences[mot] for mot in occurrences if mot not in parasites}

def charger_parasites(fichier):
    with open(fichier, 'r') as file:
        parasites = file.read().splitlines()
    return parasites

# Remplacez 'chemin_vers_votre_fichier_parasite' par le chemin réel de votre fichier 'parasite.csv'
liste_parasites = charger_parasites('parasite.csv')

# Etape 4 : Utilisez un texte de votre choix ici
texte_a_analyser = """
Après avoir lu la conclusion de son manga préféré, Fuuko Izumo se sent enfin prête à mettre fin à ses jours. Depuis dix ans, 
Fuuko est atteinte d’une condition spéciale qui apporte un grand malheur à quiconque la touche. 
Cela a eu un effet radical sur son environnement, entraînant même par inadvertance la mort de ceux qui l’entourent, y compris ses parents.
Alors qu’elle se tient sur un pont au-dessus des voies ferrées, 
Fuuko est touchée par un homme étrange, ce qui a pour effet de briser le sol sous lequel il se trouve et de le faire tomber devant un train en marche. 
Cependant, lorsque Fuuko trouve le cadavre de l’homme, elle découvre que son corps se régénère et qu’il revient à la vie.
L’homme, que Fuuko nomme Andy, est immortel et comme elle, il souhaite aussi la mort. 
D’abord dédaigneuse, Fuuko décide finalement de faire équipe avec Andy pour lui offrir la meilleure mort possible. 
Mais une mystérieuse organisation se cache dans l’ombre, espérant tirer profit des étranges capacités du duo.
"""

# Obtenez les occurrences des mots
occurrences_mots = compter_occurrences(texte_a_analyser)

# Filtrez les mots clés
mots_cles = enlever_parasites(occurrences_mots, liste_parasites)

# Imprimez les mots clés pour les voir
print(mots_cles)

# Étape 5 : Créer une fonction pour supprimer les balises HTML
def remove_html_tags(html_text):
    soup = BeautifulSoup(html_text, 'html.parser')
    text = soup.get_text()
    return text

# Étape 6 : Créer une fonction pour extraire les valeurs d'attributs
def extract_attribute_values(html_text, tag_name, attribute_name):
    soup = BeautifulSoup(html_text, 'html.parser')
    tags = soup.find_all(tag_name)
    attribute_values = [tag.get(attribute_name) for tag in tags]
    return attribute_values

# Étape 8 : Créer une fonction pour extraire le nom de domaine
def extract_domain_name(url):
    parts = url.split('/')
    if len(parts) >= 3:
        return parts[2]
    else:
        return ""

# Étape 9 : Créer une fonction pour séparer les URLs par domaine
def separate_urls_by_domain(domain, url_list):
    domain_urls = [url for url in url_list if extract_domain_name(url) == domain]
    non_domain_urls = [url for url in url_list if extract_domain_name(url) != domain]
    return domain_urls, non_domain_urls

# Étape 10 : Fonction pour récupérer le texte HTML depuis une URL
def get_html_text_from_url(url):
    # Simuler la récupération de la page depuis une URL (non implémenté ici)
    return "<html><body>Contenu de la page</body></html>"

# Étape 11 : Fonction pour auditer une page
def seo_audit(url):
    # Étape 10 : Obtenir le texte HTML de la page (simulé)
    html_text = get_html_text_from_url(url)

    # Étape 5 : Supprimer les balises HTML (simulé)
    text_without_html = remove_html_tags(html_text)

    # Étape 1 : Compter les occurrences de mots
    word_counts = count_words(text_without_html)

    # Étape 3 : Obtenir les mots parasites
    stopwords = get_stopwords_from_file('parasite.csv')

    # Étape 2 : Supprimer les mots parasites
    filtered_word_counts = remove_stopwords(word_counts, stopwords)

    # Afficher les résultats
    print("Mots clés les plus importants :")
    for word, count in list(filtered_word_counts.items())[:3]:
        print(f"{word}: {count} occurrences")

    # Nombre de liens entrants (simulé)
    print("Nombre de liens entrants : 10")

    # Nombre de liens sortants (simulé)
    print("Nombre de liens sortants : 15")

    # Présence de balises alt (simulé)
    print("Présence de balises alt : Oui")

# Étape 11 : Exécution de l'audit (simulé)
url_to_audit = "https://www.example.com"
seo_audit(url_to_audit)