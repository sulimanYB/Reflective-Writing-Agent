from agents import (
    generate_draft,
    reflect_on_draft,
    revise_draft,
    evaluate_essays,
)

from visualise import plot_evaluation

# Define the essay topic
topic = "Should social media platforms be regulated by the government?"

# Step 1 — Generate initial draft
draft = generate_draft(topic)

print("\n=== STEP 1: INITIAL ESSAY DRAFT ===\n")
print(draft)

# Step 2 — Reflect on the draft
feedback = reflect_on_draft(draft)

print("\n=== STEP 2: REFLECTION AND FEEDBACK ===\n")
print(feedback)

# Step 3 — Revise the draft
revised = revise_draft(draft, feedback)

print("\n=== STEP 3: REVISED ESSAY ===\n")
print(revised)

# Step 4 — Evaluate both essays
evaluation = evaluate_essays(draft, revised)

print("\n=== STEP 4: EVALUATION ===\n")
print(evaluation)

# Step 5 — Visualise evaluation results
plot_evaluation(evaluation)

