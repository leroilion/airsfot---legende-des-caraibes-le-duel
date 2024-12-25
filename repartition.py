import random


def repartition_containers(nb_containers, inside_treasures, variations=None):
    # Initialisation des containers
    containers = [{k: 0 for k in inside_treasures} for _ in range(nb_containers)]

    if variations is None:
        variations = {k: 1 for k in inside_treasures}

    max_treasure = {k: int(v/nb_containers) + variations[k] for k, v in inside_treasures.items()}

    for treasure, quantity in inside_treasures.items():
        while quantity > 0:
            index = random.randint(0, len(containers) - 1)
            if containers[index][treasure] < max_treasure[treasure]:
                containers[index][treasure] += 1
                quantity -= 1


    return containers

def compute_value(nb_gamers, squad_size, treasure_by_team, treasures, distribution):

    treasures = treasures.copy()

    nb_teams = int(nb_gamers / squad_size)
    nb_treasures_remaining = treasure_by_team * nb_teams - sum([v[0] for k, v in treasures.items() if v[0] is not None])

    # Compute QTY of piece and gem
    for treasure in [k for k,v in treasures.items() if v[0] is None]:
        treasure_qty = 0
        for k, v in {k:round(v['qty'] * nb_treasures_remaining) for k, v in distribution.items()}.items():
            if k not in treasure:
                treasures[k] = (v, 0)
            treasure_qty += v * distribution[k][treasure]

        treasures[treasure] = (treasure_qty, treasures[treasure][1])

    # Compute value of statuette and gold mask
    remaining_point = round(sum([v[0] * v[1] for k, v in treasures.items() if v[0] is not None and v[1] is not None]) / 2)
    qty = sum([v[0] for k,v in treasures.items() if v[1] is None])
    qty_with_coef = sum([max(1, qty / v[0] / 2) * v[0] for k, v in treasures.items() if v[1] is None])
    for treasure in [k for k, v in treasures.items() if v[1] is None]:
        treasures[treasure] = (treasures[treasure][0], round(max(1, qty / treasures[treasure][0] / 2) / qty_with_coef * remaining_point))

    return treasures


def repartition_chest_and_pouch(treasures, distribution):
    containers = {}
    for k, v in {k: v for k, v in treasures.items() if v[1] == 0}.items():
        inside_treasure = {l: m  * v[0] for l, m in distribution[k].items() if l != 'qty'}
        containers[k] = repartition_containers(v[0], inside_treasure, {'piece': 2, 'gem': 1})

    return containers


def generate_space(size):
    return " " * size * 2


def make_tabular(nb_gamers, squad_size, treasure_by_team, treasures, rep):
    output = []
    indent = 0
    output.append(f"\\subsection*{{Exemple pour {nb_gamers} joueurs réparti en squad de {squad_size} avec {treasure_by_team} trésors à trouver}}")
    output.append(f"\\centering")
    output.append(f"{generate_space(indent)}\\begin{{tabular}}{{|l|c|c|}}")
    indent += 1
    output.append(f"{generate_space(indent)}\\hline")
    output.append(f"{generate_space(indent)}\\multicolumn{{3}}{{|c|}}{{\\textbf{{Répartition des trésors}}}} \\\\ \\hline")
    output.append(f"{generate_space(indent)}\\textbf{{Element de jeu}} & \\textbf{{Quantité}} & \\textbf{{Valeur}} \\\\ \\hline")
    for k, v in treasures.items():
        output.append(f"{generate_space(indent)}{k} & {v[0]} & {v[1] if v[1] != 0 else '-'} \\\\ \\hline")
    indent -= 1
    output.append(f"{generate_space(indent)}\\end{{tabular}}")
    output.append("")
    output.append(f"{generate_space(indent)}\\bigskip")
    output.append("")
    for container, repartition in rep.items():
        output.append(f"{generate_space(indent)}\\begin{{tabular}}{{|l|c|c|c|}}")
        indent += 1
        output.append(f"{generate_space(indent)}\\hline")
        output.append(f"{generate_space(indent)}\\multicolumn{{3}}{{|c|}}{{\\textbf{{Exemple de répartition détaillée des {container}}}}} \\\\ \\hline")
        for index, treasure in enumerate(repartition):
            if index == 0:
                names = [k for k, _  in treasure.items()]
                output.append(f"{generate_space(indent)}\\textbf{{Numéro du {container}}} & \\textbf{{{names[0]}}} & \\textbf{{{names[1]}}} \\\\ \\hline")
            values = [v for _, v in treasure.items()]
            output.append(f"{generate_space(indent)}{container} {index + 1} & {values[0]} & {values[1]} \\\\ \\hline")
        indent -= 1
        output.append(f"{generate_space(indent)}\\end{{tabular}}")
        output.append("")
        output.append(f"{generate_space(indent)}\\bigskip")
        output.append("")

    return "\n".join(output)


if __name__ == "__main__":
    # nb_gamers = 40
    # squad_size = 4
    # treasure_by_team = 2
    treasures = {
        "piece": (None, 1),
        "gem": (None, 2),
        "statuette": (2, None),
        "gold_mask": (1, None)
    }

    distribution = {
        "pouch": {
            "qty": 2/3,
            "piece": 3,
            "gem": 1
        },
        "chest": {
            "qty": 1/3,
            "piece": 5,
            "gem": 2
        }
    }

    traductions = {
        'piece': 'Pièces',
        'gem': 'Gemmes',
        'statuette': 'Statuettes',
        'gold_mask': 'Masque en or',
        'pouch': 'Bourses',
        'chest': 'Coffres'
    }


    with open("repartition.tex", "w", encoding="utf-8") as fd:

        for nb_gamers in [20, 40, 50, 60]:
            for squad_size in [4]:
                for treasure_by_team in [2]:
        # for nb_gamers in [40]:
        #     for squad_size in [4]:
        #         for treasure_by_team in [2]:
                    result = compute_value(nb_gamers, squad_size, treasure_by_team, treasures, distribution)

                    rep = repartition_chest_and_pouch(result, distribution)

                    latex_source_code = make_tabular(nb_gamers, squad_size, treasure_by_team, result, rep)
                    for src, dst in traductions.items():
                        latex_source_code = latex_source_code.replace(src, dst)

                    fd.write(latex_source_code)
