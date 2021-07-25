import warnings
from typing import Callable, Dict, List, Tuple

import numpy as np
from tabulate import tabulate


def log_allowing_zeros(value: np.ndarray, base: float = 2.0):
    value = value.copy()
    value[np.isclose(value, 0.0)] = 1.0
    return np.log2(value) / np.log2(base)


def id3(data: List[Tuple[str, List[str], str]], features: List[Tuple[str, List[str]]], classes: List[str], feature_indices: Dict[str, int],
        criterion: Tuple[str, Callable[[np.ndarray], np.ndarray], bool], title: str):
    print(f"\n\n\n\n\nIteration {title}:")

    print("\nDaten:")
    print(tabulate(
        [data_features + [label] for _, data_features, label in data],
        headers=list(feature_indices.keys()) + ["Klasse"],
        showindex=[name for name, _, _ in data],
        tablefmt="github")
    )

    base_frequencies = []
    for class_label in classes:
        base_frequencies.append(0)
        for _, _, label in data:
            if label == class_label:
                base_frequencies[-1] += 1
    base_frequencies = np.array(base_frequencies)
    dominant_label = classes[np.argmax(base_frequencies)]
    if np.amax(base_frequencies) == len(data):
        print(f"\nNur eine Klasse ({dominant_label}) enthalten; Fertig.")
        return dominant_label
    if len(features) <= 0:
        warnings.warn(f"{title}: Keine Features mehr verfügbar! Wähle dominante Klasse.")
        print(f"\nKeine Features mehr verfügbar; wähle dominante Klasse ({dominant_label}).")
        return dominant_label
    base_probabilities = base_frequencies / base_frequencies.sum()
    criterion_base_val = criterion[1](base_probabilities.reshape((1, -1))).item()

    information_values = []
    for feature_name, features_values in features:
        print(f"\n\n{feature_name}:")
        frequencies, probabilities = [], []
        for feature_value in features_values:
            frequencies_for_value, probabilities_for_value = [], []
            for class_label in classes:
                frequencies_for_value.append(0)
                for _, data_features, label in data:
                    if data_features[feature_indices[feature_name]] == feature_value and label == class_label:
                        frequencies_for_value[-1] += 1
            frequencies_for_value.append(np.sum(frequencies_for_value))
            frequencies.append(frequencies_for_value)
            probabilities.append(list(np.array(frequencies_for_value[:-1]) / max(1, frequencies_for_value[-1])))
        frequencies.append(list(np.sum(frequencies, axis=0)))
        frequencies, probabilities = np.asarray(frequencies), np.asarray(probabilities)
        print("\nKlassenhäufigkeiten:")
        print(tabulate(frequencies, headers=classes + ["Gesamt"], showindex=features_values + ["Gesamt"], tablefmt="github"))
        print(f"\nBedingte Wahrscheinlichkeiten (P(Klasse = $Spalte | {feature_name} = $Zeile)):")
        print(tabulate(probabilities, headers=classes, showindex=features_values, tablefmt="github"))
        criterion_vals = criterion[1](probabilities)
        print("\nKriteriumswert:")
        print(tabulate(criterion_vals.reshape((-1, 1)), headers=[criterion[0]], showindex=features_values, tablefmt="github"))
        information_values.append((frequencies[:-1, -1] / frequencies[-1, -1] * criterion_vals).sum().item())
    information_values = np.asarray(information_values)

    print(f"\n\nBasiskriteriumswert: {criterion_base_val}")
    print("\nGewichteter Kriteriumswert:")
    print(tabulate((-1 if criterion[2] else 1) * information_values.reshape((-1, 1)), headers=["Information"], showindex=[name for name, _ in features], tablefmt="github"))
    gains = []
    for (feature_name, _), information_value in zip(features, information_values):
        gains.append(information_value - criterion_base_val)
    gains = np.asarray(gains)
    print("\nGains:")
    print(tabulate((-1 if criterion[2] else 1) * gains.reshape((-1, 1)), headers=["Gain"], showindex=[name for name, _ in features], tablefmt="github"))

    chosen_feature_index = np.argmin(gains)
    chosen_feature = features[chosen_feature_index][0]
    print(f"\nWähle Merkmal {repr(chosen_feature)}.")
    result = []
    for feature_value in features[chosen_feature_index][1]:
        result.append((
            feature_value,
            id3(
                # Get index again to circumvent removal of features.
                [dat for dat in data if dat[1][feature_indices[chosen_feature]] == feature_value],
                list([feature for feature in features if feature[0] != chosen_feature]),
                classes,
                feature_indices,
                criterion,
                f"{title}/{chosen_feature}={feature_value}"
            ),
        ))
    return chosen_feature, result


def main():
    # Last item describes if the value should be negated when printing the gain.
    entropy_criterion = ("Entropie", lambda p: -(p * log_allowing_zeros(p)).sum(axis=1), True)
    gini_criterion = ("Gini-Index", lambda p: (p ** 2).sum(axis=1), False)

    data = [
        ("T1", ["Sonnig", "Warm", "Hoch", "Schwach"], "Nein"),
        ("T2", ["Sonnig", "Warm", "Hoch", "Stark"], "Nein"),
        ("T3", ["Bewölkung", "Warm", "Hoch", "Schwach"], "Ja"),
        ("T4", ["Regen", "Mild", "Hoch", "Schwach"], "Ja"),
        ("T5", ["Regen", "Kühl", "Normal", "Schwach"], "Ja"),
        ("T6", ["Regen", "Kühl", "Normal", "Stark"], "Nein"),
        ("T7", ["Bewölkung", "Kühl", "Normal", "Stark"], "Ja"),
        ("T8", ["Sonnig", "Mild", "Hoch", "Schwach"], "Nein"),
        ("T9", ["Sonnig", "Kühl", "Normal", "Schwach"], "Ja"),
        ("T10", ["Regen", "Mild", "Normal", "Schwach"], "Ja"),
        ("T11", ["Sonnig", "Mild", "Normal", "Stark"], "Ja"),
        ("T12", ["Bewölkung", "Mild", "Hoch", "Stark"], "Ja"),
        ("T13", ["Bewölkung", "Warm", "Normal", "Schwach"], "Ja"),
        ("T14", ["Regen", "Mild", "Hoch", "Stark"], "Nein"),
    ]
    features = [
        ("Ausblick", ["Sonnig", "Bewölkung", "Regen"]),
        ("Temperatur", ["Warm", "Mild", "Kühl"]),
        ("Luftfeuchtigkeit", ["Hoch", "Normal"]),
        ("Wind", ["Schwach", "Stark"]),
    ]
    # data = [
    #     ("T1", ["Sonnig", "Schwach"], "Nein"),
    #     ("T2", ["Sonnig", "Schwach"], "Nein"),
    #     ("T3", ["Sonnig", "Schwach"], "Ja"),
    #     ("T4", ["Sonnig", "Stark"], "Ja"),
    #     ("T5", ["Sonnig", "Stark"], "Nein"),
    #     ("T6", ["Regen", "Schwach"], "Ja"),
    #     ("T7", ["Regen", "Stark"], "Nein"),
    #     ("T8", ["Regen", "Stark"], "Nein"),
    #     ("T9", ["Bewölkung", "Stark"], "Ja"),
    #     ("T10", ["Bewölkung", "Schwach"], "Ja"),
    # ]
    # features = [
    #     ("Ausblick", ["Sonnig", "Bewölkung", "Regen"]),
    #     ("Wind", ["Schwach", "Stark"]),
    # ]
    classes = ["Ja", "Nein"]

    tree = id3(data, features, classes, feature_indices={features[i][0]: i for i in range(len(features))}, criterion=entropy_criterion, title="Wurzel")

    print("\n\nResultierender Baum:")
    print(tree)


if __name__ == '__main__':
    main()
