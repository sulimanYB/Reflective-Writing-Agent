
import json
import numpy as np
import matplotlib.pyplot as plt


def plot_evaluation(evaluation: str):
    """Compare original and revised essay evaluation scores."""

    # Convert JSON string into a Python dictionary
    scores = json.loads(evaluation)

    criteria = [
        "structure",
        "clarity",
        "arguments",
        "writing_style"
    ]

    labels = [
        "Structure",
        "Clarity",
        "Arguments",
        "Writing Style"
    ]

    original = [scores[c]["original"] for c in criteria]
    revised = [scores[c]["revised"] for c in criteria]

    x = np.arange(len(labels))
    width = 0.35

    fig, ax = plt.subplots(figsize=(9, 5))

    ax.bar(x - width / 2, original, width, label="Original Draft")
    ax.bar(x + width / 2, revised, width, label="Revised Draft")

    ax.set_ylabel("Evaluation Score (1–10)")
    ax.set_title("Reflective Writing Agent — Essay Evaluation")
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.set_ylim(0, 10)
    ax.legend()

    plt.tight_layout()
    plt.show()
