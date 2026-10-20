from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()


def generate_draft(topic: str, model: str = "gpt-4o-mini") -> str:
    """Generate an initial essay draft on a given topic."""

    prompt = f"""
    Write a complete, well-structured essay on the following topic:

    {topic}

    Include an introduction, several body paragraphs,
    and a conclusion. Use clear and coherent language.
    """

    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=1.0,
    )

    return response.choices[0].message.content


def reflect_on_draft(draft: str, model: str = "gpt-4o-mini") -> str:
    """Critically evaluate an essay draft and provide feedback."""

    prompt = f"""
    Review the following essay draft and provide
    critical but constructive feedback.

    Evaluate the essay based on:
    1. Structure and organisation.
    2. Clarity and coherence.
    3. Strength of arguments and supporting evidence.
    4. Writing style, grammar, and readability.

    Identify specific weaknesses and suggest practical
    improvements.

    Provide your feedback in paragraph form.
    Do not rewrite the essay.

    Essay draft:
    {draft}
    """

    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=1.0,
    )

    return response.choices[0].message.content


def revise_draft(
    original_draft: str,
    reflection: str,
    model: str = "gpt-4o-mini"
) -> str:
    """Revise an essay using feedback from the Reflection Agent."""

    prompt = f"""
    Revise the following essay using the constructive
    feedback provided.

    Improve the essay's structure, clarity, coherence,
    strength of arguments, writing style, and overall flow.

    Address the weaknesses identified in the feedback
    while preserving the original topic and main ideas.

    Original essay:
    {original_draft}

    Reflection and feedback:
    {reflection}

    Return only the complete revised essay.
    Do not include explanations or commentary.
    """

    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=1.0,
    )

    return response.choices[0].message.content



def evaluate_essays(
    original_draft: str,
    revised_draft: str,
    model: str = "gpt-4o-mini"
) -> str:
    """Compare two essays and return structured JSON scores."""

    prompt = f"""
    You are an impartial academic writing evaluator.

    Compare the original and revised essays.

    Evaluate both versions on:
    - structure
    - clarity
    - arguments
    - writing_style

    Assign each criterion a score from 1 to 10
    for both essays.

    Return a JSON object with exactly this structure:

    {{
        "structure": {{"original": 0, "revised": 0}},
        "clarity": {{"original": 0, "revised": 0}},
        "arguments": {{"original": 0, "revised": 0}},
        "writing_style": {{"original": 0, "revised": 0}},
        "overall_assessment": "Your assessment here"
    }}

    Replace the zeros with actual scores.
    Evaluate both essays fairly.
    Do not assume the revised essay is better.

    Original essay:
    {original_draft}

    Revised essay:
    {revised_draft}
    """

    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
        response_format={"type": "json_object"},
    )

    return response.choices[0].message.content
