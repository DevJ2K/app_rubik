import numpy as np
from collections import Counter

# Définition des positions des stickers pour chaque pièce (face, ligne, colonne)
CORNERS = [
    (('U', 2, 2), ('F', 0, 0), ('R', 0, 0)),  # UFR
    (('U', 2, 0), ('L', 0, 0), ('F', 0, 2)),  # ULF
    (('U', 0, 0), ('B', 0, 2), ('L', 0, 2)),  # UBL
    (('U', 0, 2), ('R', 0, 2), ('B', 0, 0)),  # URB
    (('D', 2, 2), ('R', 2, 0), ('F', 2, 0)),  # DFR
    (('D', 2, 0), ('F', 2, 2), ('L', 2, 0)),  # DLF
    (('D', 0, 0), ('L', 2, 2), ('B', 2, 0)),  # DBL
    (('D', 0, 2), ('B', 2, 2), ('R', 2, 2))   # DRB
]

EDGES = [
    (('U', 1, 2), ('R', 1, 0)),  # UR
    (('U', 0, 1), ('B', 1, 0)),  # UB
    (('U', 1, 0), ('L', 1, 0)),  # UL
    (('U', 2, 1), ('F', 1, 0)),  # UF
    (('F', 1, 2), ('R', 1, 1)),  # FR
    (('R', 1, 2), ('B', 1, 1)),  # RB
    (('B', 1, 2), ('L', 1, 1)),  # BL
    (('L', 1, 2), ('F', 1, 1)),  # LF
    (('D', 1, 2), ('R', 1, 2)),  # DR
    (('D', 0, 1), ('B', 1, 1)),  # DB
    (('D', 1, 0), ('L', 1, 2)),  # DL
    (('D', 2, 1), ('F', 1, 2))   # DF
]

def normalize_piece(piece):
    """
    Normalise une pièce en triant ses couleurs.
    
    :param piece: Tuple des couleurs de la pièce.
    :return: Tuple normalisé des couleurs.
    """
    return tuple(sorted(piece))

def verify_color_distribution(state):
    """
    Vérifie la distribution des couleurs sur le Rubik's Cube.
    
    :param state: Dictionnaire représentant le cube avec les faces en matrices 3x3.
    :return: True si la distribution est correcte, False sinon.
    """
    colors = []
    for face in ['U', 'R', 'F', 'D', 'L', 'B']:
        if face not in state:
            print(f"Face {face} manquante dans l'état du cube.")
            return False
        if state[face].shape != (3,3):
            print(f"Face {face} n'est pas une matrice 3x3.")
            return False
        colors.extend(state[face].flatten())
    counts = Counter(colors)
    for color, count in counts.items():
        if count != 9:
            print(f"Couleur {color} apparaît {count} fois au lieu de 9.")
            return False
    return True

def get_corners(state):
    """
    Extrait les couleurs des coins à partir de l'état du cube.
    
    :param state: Dictionnaire représentant le cube avec les faces en matrices 3x3.
    :return: Liste de tuples représentant les couleurs des coins.
    """
    corners = []
    for corner in CORNERS:
        try:
            colors = tuple(state[face][line][col] for face, line, col in corner)
        except IndexError:
            print(f"Erreur d'index lors de l'extraction des coins pour la pièce {corner}.")
            return []
        corners.append(colors)
    return corners

def get_edges(state):
    """
    Extrait les couleurs des arêtes à partir de l'état du cube.
    
    :param state: Dictionnaire représentant le cube avec les faces en matrices 3x3.
    :return: Liste de tuples représentant les couleurs des arêtes.
    """
    print(state)
    edges = []
    for edge in EDGES:
        try:
            colors = tuple(state[face][line][col] for face, line, col in edge)
        except IndexError:
            print(f"Erreur d'index lors de l'extraction des arêtes pour la pièce {edge}.")
            return []
        edges.append(colors)
    return edges

def find_piece_index(current_piece, solved_mapping):
    """
    Trouve l'index d'une pièce actuelle dans le mapping résolu en utilisant la normalisation.
    
    :param current_piece: Tuple représentant les couleurs actuelles de la pièce.
    :param solved_mapping: Dictionnaire de pièces résolues normalisées à leurs indices.
    :return: Index de la pièce résolue correspondante ou None si non trouvé.
    """
    normalized = normalize_piece(current_piece)
    return solved_mapping.get(normalized, None)

def calculate_parity(permutation):
    """
    Calcule la parité d'une permutation.
    
    :param permutation: Liste représentant la permutation.
    :return: 0 si la parité est paire, 1 si impaire.
    """
    inversions = 0
    perm = permutation.copy()
    n = len(perm)
    for i in range(n):
        for j in range(i + 1, n):
            if perm[i] > perm[j]:
                inversions += 1
    return inversions % 2

def verify_permutation(state, state_ref):
    """
    Vérifie la permutation des coins et des arêtes d'un Rubik's Cube.
    
    :param state: Dictionnaire représentant l'état actuel du cube.
    :param state_ref: Dictionnaire représentant l'état résolu de référence.
    :return: Tuple (permutation_valide, corner_permutation, edge_permutation)
             permutation_valide: True si les permutations sont valides, False sinon.
             corner_permutation: Liste des indices des coins permutés.
             edge_permutation: Liste des indices des arêtes permutées.
    """
    # Extraire les coins et les arêtes de l'état résolu et de l'état actuel
    corners_solved = get_corners(state_ref)
    edges_solved = get_edges(state_ref)

    corners_current = get_corners(state)
    edges_current = get_edges(state)
    print(edges_current)

    if not corners_solved or not edges_solved or not corners_current or not edges_current:
        print("Erreur lors de l'extraction des pièces.")
        return False, None, None

    # Créer des mappings normalisés pour retrouver l'index d'une pièce résolue
    corner_to_index = {}
    for idx, piece in enumerate(corners_solved):
        normalized = normalize_piece(piece)
        corner_to_index[normalized] = idx

    edge_to_index = {}
    for idx, piece in enumerate(edges_solved):
        normalized = normalize_piece(piece)
        edge_to_index[normalized] = idx

    # Mapper les coins actuels aux indices résolus
    corner_permutation = []
    for piece in corners_current:
        # print(piece, corner_to_index)
        mapped_idx = find_piece_index(piece, corner_to_index)
        print(mapped_idx)
        if mapped_idx is None:
            print(f"Coin {piece} non reconnu dans l'état résolu.")
            return False, None, None
        corner_permutation.append(mapped_idx)

    # Mapper les arêtes actuelles aux indices résolus
    edge_permutation = []
    for piece in edges_current:
        mapped_idx = find_piece_index(piece, edge_to_index)
        if mapped_idx is None:
            print(f"Arête {piece} non reconnue dans l'état résolu.")
            return False, None, None
        edge_permutation.append(mapped_idx)

    # Calculer la parité des permutations
    corner_parity = calculate_parity(corner_permutation)
    edge_parity = calculate_parity(edge_permutation)

    if corner_parity != edge_parity:
        print("La parité des permutations des coins et des arêtes ne correspond pas.")
        return False, None, None

    return True, corner_permutation, edge_permutation

def verify_orientation(state, state_ref):
    """
    Vérifie l'orientation des coins et des arêtes d'un Rubik's Cube.
    
    :param state: Dictionnaire représentant l'état actuel du cube.
    :param state_ref: Dictionnaire représentant l'état résolu de référence.
    :return: True si les orientations sont valides, False sinon.
    """
    corners_current = get_corners(state)
    edges_current = get_edges(state)
    corners_solved = get_corners(state_ref)
    edges_solved = get_edges(state_ref)

    if not corners_current or not edges_current:
        print("Erreur lors de l'extraction des pièces pour l'orientation.")
        return False

    # Création d'un mapping résolu normalisé pour les orientations
    solved_corner_orientations = {}
    for idx, piece in enumerate(corners_solved):
        solved_corner_orientations[idx] = piece

    # Calculer la somme des orientations des coins
    corner_orientation_sum = 0
    for current_piece, solved_piece in zip(corners_current, corners_solved):
        # Trouver l'index résolu de la pièce actuelle
        normalized = normalize_piece(current_piece)
        solved_idx = find_piece_index(current_piece, {normalize_piece(p): i for i, p in enumerate(corners_solved)})
        if solved_idx is None:
            print(f"Coin {current_piece} non reconnu dans l'état résolu pour l'orientation.")
            return False
        solved_piece = corners_solved[solved_idx]
        # Déterminer l'orientation
        # L'orientation est définie par la position de la couleur U ou D
        # On suppose que la première couleur de solved_piece correspond à la face U ou D
        try:
            orientation = current_piece.index(solved_piece[0])
        except ValueError:
            orientation = 0  # Par défaut
        corner_orientation_sum += orientation

    if corner_orientation_sum % 3 != 0:
        print("La somme des orientations des coins n'est pas un multiple de 3.")
        return False

    # Calculer le nombre d'arêtes mal orientées
    edge_flip = 0
    for current_piece, solved_piece in zip(edges_current, edges_solved):
        # Une arête est mal orientée si ses couleurs sont inversées par rapport à l'état résolu
        if current_piece != solved_piece:
            if current_piece[::-1] == solved_piece:
                edge_flip += 1
            else:
                print(f"Arête flippée invalide: {current_piece}")
                return False

    if edge_flip % 2 != 0:
        print("Le nombre d'arêtes mal orientées n'est pas pair.")
        return False

    return True

def is_solvable(state):
    """
    Vérifie si un Rubik's Cube représenté en tableau 3D est solvable.
    
    :param state: Dictionnaire représentant l'état actuel du cube.
    :return: True si le cube est solvable, False sinon.
    """
    if not verify_color_distribution(state):
        return False

    # État résolu de référence
    state_ref = {
        'U': np.array([['U', 'U', 'U'],
                      ['U', 'U', 'U'],
                      ['U', 'U', 'U']]),
        'R': np.array([['R', 'R', 'R'],
                      ['R', 'R', 'R'],
                      ['R', 'R', 'R']]),
        'F': np.array([['F', 'F', 'F'],
                      ['F', 'F', 'F'],
                      ['F', 'F', 'F']]),
        'D': np.array([['D', 'D', 'D'],
                      ['D', 'D', 'D'],
                      ['D', 'D', 'D']]),
        'L': np.array([['L', 'L', 'L'],
                      ['L', 'L', 'L'],
                      ['L', 'L', 'L']]),
        'B': np.array([['B', 'B', 'B'],
                      ['B', 'B', 'B'],
                      ['B', 'B', 'B']])
    }

    # Vérifier les permutations
    permutation_valide, corner_perm, edge_perm = verify_permutation(state, state_ref)
    if not permutation_valide:
        return False

    # Vérifier les orientations
    if not verify_orientation(state, state_ref):
        return False

    return True

if __name__ == "__main__":
    # Exemple d'état résolu (solvable)
    solved_cube = {
        'U': np.array([['U', 'U', 'U'],
                      ['U', 'U', 'U'],
                      ['U', 'U', 'U']]),
        'R': np.array([['R', 'R', 'R'],
                      ['R', 'R', 'R'],
                      ['R', 'R', 'R']]),
        'F': np.array([['F', 'F', 'F'],
                      ['F', 'F', 'F'],
                      ['F', 'F', 'F']]),
        'D': np.array([['D', 'D', 'D'],
                      ['D', 'D', 'D'],
                      ['D', 'D', 'D']]),
        'L': np.array([['L', 'L', 'L'],
                      ['L', 'L', 'L'],
                      ['L', 'L', 'L']]),
        'B': np.array([['B', 'B', 'B'],
                      ['B', 'B', 'B'],
                      ['B', 'B', 'B']])
    }

    # Exemple d'état mélangé (solvable)
    # Ici, nous effectuons quelques rotations simples pour mélanger le cube
    # Note: Pour un test réel, assurez-vous que l'état est mélangé mais solvable

    # Exemple d'état mélangé simple : tourner la face U dans le sens horaire
    # Ceci devrait déplacer quelques coins et arêtes sans rendre le cube non-solvable
    def rotate_face(face_matrix):
        """
        Effectue une rotation horaire de la face (matrice 3x3).
        
        :param face_matrix: Numpy array 3x3 représentant une face.
        :return: Numpy array 3x3 représentant la face après rotation.
        """
        return np.rot90(face_matrix, -1)

    mixed_cube = {
        'U': rotate_face(solved_cube['U']),
        'R': solved_cube['R'].copy(),
        'F': rotate_face(solved_cube['F']),
        'D': solved_cube['D'].copy(),
        'L': solved_cube['L'].copy(),
        'B': rotate_face(solved_cube['B'])
    }

    # Vous pouvez définir votre propre état mélangé ici
    # Pour cet exemple, utilisons l'état résolu et l'état mélangé
    test_cubes = {
        "Résolu": solved_cube,
        "Mélangé": mixed_cube
    }

    for description, current_state in test_cubes.items():
        print(f"\nVérification de l'état: {description}")
        if is_solvable(current_state):
            print("Le Rubik's Cube est solvable.")
        else:
            print("Le Rubik's Cube n'est pas solvable.")
