# Prompt Engineering

Tags: AI, AI Automation, Prompting
Description: cross-platform framework for Prompt Engineering—the art of crafting effective prompts for large language models (LLMs) like GPT, Claude, and Gemini
URL: https://www.youtube.com/watch?v=zAkMuMddM2E&list=WL&index=105
Date Added: November 15, 2025 6:29 PM
Type: Note
Archive: No
Spark: No

- 

This video presents a reusable, cross-platform framework for **Prompt Engineering**—the art of crafting effective prompts for large language models (LLMs) like GPT, Claude, and Gemini.

Here is a summary of the framework and key advanced techniques:

### **The Prompt Engineering Framework**

The framework is structured into sections, often separated using an "XML sandwich" structure (`<SECTION></SECTION>`) for clarity [[01:28](http://www.youtube.com/watch?v=zAkMuMddM2E&t=88)].

| Section | Purpose | Best Practice / Pro-Tip |
| --- | --- | --- |
| **Role** | Sets the persona, expertise, audience, and communication style of the AI [[01:58](http://www.youtube.com/watch?v=zAkMuMddM2E&t=118)]. | Be highly **specific** (e.g., "senior financial analyst" is better than "expert") to help the model calibrate its response [[02:08](http://www.youtube.com/watch?v=zAkMuMddM2E&t=128)]. |
| **Task** | Defines the main objective and action verb (e.g., analyze, draft, create) [[02:46](http://www.youtube.com/watch?v=zAkMuMddM2E&t=166)]. | **Break down the main objective** into 2-4 sub-objectives to steer the model's execution. Don't make the model guess [[03:06](http://www.youtube.com/watch?v=zAkMuMddM2E&t=186)]. |
| **Context** | Your single source of truth; where you place all information, data, and background details [[03:57](http://www.youtube.com/watch?v=zAkMuMddM2E&t=237)]. | For GPT, Claude, and Gemini, **the more context the better** (use as much context window as possible). For reasoning models (e.g., 03/04 mini), **less is more** [[04:23](http://www.youtube.com/watch?v=zAkMuMddM2E&t=263)]. |
| **Example** | (Optional) Show the model a few examples of "what good looks like" (few-shot prompting) [[04:54](http://www.youtube.com/watch?v=zAkMuMddM2E&t=294)]. | **Highly powerful** for GPT, Claude, and Gemini (use 3-5 examples for consistent tone/formatting). **Skip entirely** for reasoning models (03/04 mini) and Perplexity, as it can confuse them [[05:26](http://www.youtube.com/watch?v=zAkMuMddM2E&t=326)]. |
| **Output** | Specifies your desired format, flow, and length of the response [[06:21](http://www.youtube.com/watch?v=zAkMuMddM2E&t=381)]. | Be **surgical** (e.g., "create a markdown table, three columns," not "create a table"). Specify length (e.g., 300-400 words) and structure (e.g., summary, then analysis, then recommendations) [[06:32](http://www.youtube.com/watch?v=zAkMuMddM2E&t=392)]. |
| **Constraints** | Establishes guardrails, style rules, and boundaries for the model [[07:15](http://www.youtube.com/watch?v=zAkMuMddM2E&t=435)]. | Use **specific constraints** (e.g., "maximum three sentences per paragraph") instead of vague ones [[07:23](http://www.youtube.com/watch?v=zAkMuMddM2E&t=443)]. |
| **Instructions** | Used to apply advanced meta-techniques and reasoning steps [[07:33](http://www.youtube.com/watch?v=zAkMuMddM2E&t=453)]. | Use **Chain of Thought** (e.g., "think through your approach step by step") to significantly increase performance for standard models, but **remove this section** for reasoning models [[07:45](http://www.youtube.com/watch?v=zAkMuMddM2E&t=465)]. |

### **Advanced Prompting Techniques**

- **Chain of Thought (CoT):** An instruction to the AI to first think through its reasoning step-by-step before providing the final answer. This generally boosts performance by 20-30% on standard models, but is not recommended for OpenAI's reasoning models as they have a hidden CoT built-in [[07:45](http://www.youtube.com/watch?v=zAkMuMddM2E&t=465)].
- **Chain Verification:** A technique where the AI is instructed to double-check its own reasoning, identify gaps, cross-reference evidence, and revise its summary before presenting the final answer [[09:41](http://www.youtube.com/watch?v=zAkMuMddM2E&t=581)].
    - **Tip:** When asking the AI to make a statement, you can instruct it to also provide a percentage of how sure it is, which reduces hallucinations [[08:06](http://www.youtube.com/watch?v=zAkMuMddM2E&t=486)].
- **Reverse Prompting:** Instead of writing the perfect prompt yourself, you tell the AI what you want, and then let it design and run the optimal prompt to achieve it [[10:57](http://www.youtube.com/watch?v=zAkMuMddM2E&t=657)]. This is effective because the model knows the "internal prompting dialect" it responds best to [[11:11](http://www.youtube.com/watch?v=zAkMuMddM2E&t=671)].

### **Context Engineering vs. Prompt Engineering**

- **Context Engineering:** Forecasted to be the next big AI thing, it focuses on leveraging the right external information (like external databases or memory features) to feed the model [[12:35](http://www.youtube.com/watch?v=zAkMuMddM2E&t=755)].
- **They Work Together:** The idea that Context Engineering will make Prompt Engineering obsolete is a misconception. Prompt Engineering is *how* you interact with the model, and Context Engineering is *what* you feed it [[13:31](http://www.youtube.com/watch?v=zAkMuMddM2E&t=811)]. Keeping your prompting skills sharp will be necessary to effectively utilize new context features [[14:11](http://www.youtube.com/watch?v=zAkMuMddM2E&t=851)].

---

# **Role**

**Define the Expert Persona**

Establish the AI's expertise, audience awareness, and communication approach:

<role>

You are a [specific role/expert] with expertise in [domain].

Your audience: [description + knowledge level]

Communication style: [tone + specific requirements]

</role>

**Example**

You are a senior business strategy consultant with expertise in competitive analysis. Your audience: C-suite executives with limited time for deep technical details. Communication style: Concise, data-driven, and actionable with a confident tone.

# **Task**

**Specify the Objective**

Clearly articulate what needs to be accomplished with explicit requirements:

<task>

[Action verb] + [specific objective]

Key requirements:

- [Requirement 1]
- [Requirement 2]
- [Requirement 3]

</task>

**Example**

Analyze the competitive positioning of our SaaS product against three main competitors.

Key requirements:

- Identify unique differentiators and vulnerabilities
- Quantify market share implications where possible
- Provide actionable recommendations for Q1 strategy

# **Context**

**Provide Relevant Background**

Supply the information needed to understand and complete the task:

<context>

[Paste relevant information, documents, data, or background details here]

</context>

**Example**

Our product: Project management tool for remote teams, $49/month, 50K users

Competitor A: Asana - 100K users, extensive integrations

Competitor B: Monday.com - 80K users, visual interface focus

Competitor C: ClickUp - 60K users, feature-rich, lower price point ($35/month)

Recent customer feedback highlights our superior mobile experience but mentions lack of time-tracking features.

# **Example**

**Provide Example Outputs**

Explain what good output looks like:

<examples>

Example 1:

[Show what good output looks like for scenario 1]

Example 2..n:

[Show what good output looks like for scenario 2]

</examples>

**Example**

Example 1:

"Our $49/month price point positions us as a premium option compared to ClickUp's $35/month. This 40% price premium must be justified through: (1) superior mobile UX, (2) enterprise-grade security, (3) white-glove onboarding. Risk: Price-sensitive SMBs may churn to ClickUp unless we demonstrate clear ROI advantage."

# **Output**

**Define Expected Results**

Specify format, length, and structure of the desired output:

<output>

Format: [specific format - e.g., "markdown table with 3 columns"]

Length: [constraint - e.g., "300-400 words"]

Structure: [if applicable - e.g., "Introduction → Analysis → Recommendations"]

</output>

**Example**

Format: Executive summary (1 paragraph) + comparison table (4 columns: Feature/Us/Competitors/Impact) + 3 strategic recommendations

Length: 400-500 words total

Structure: Summary → Comparison → Recommendations

# **Constraints**

**Set Boundaries & Guidelines**

Establish what should and shouldn't be included:

<constraints>

- [Specific do's and don'ts]
- [Style requirements]
- [Any limitations or boundaries]

</constraints>

**Example**

- No jargon or technical implementation details
- Focus only on strategic business implications
- Avoid speculating on competitors' future roadmaps
- Do not recommend features that would take >6 months to build

# **Instructions**

**Guide the Process**

Provide meta-guidance on how to approach the task:

<instructions>

For complex tasks: Think through your approach step-by-step, then provide the final answer in the requested format.

If information is missing or uncertain, state this explicitly rather than guessing.

</instructions>

**Example**

For complex tasks: Think through your approach step-by-step, then provide the final answer in the requested format.

If information is missing or uncertain, state this explicitly rather than guessing.

---

**Prompt Engineering Framework**

<role>

You are a [specific role/expert] with expertise in [domain].

Your audience: [description + knowledge level]

Communication style: [tone + specific requirements]

</role>

<task>

[Action verb] + [specific objective]

Key requirements:

- [Requirement 1]
- [Requirement 2]
- [Requirement 3]

</task>

<context>

[Paste relevant information, documents, data, or background details here]

</context>

<examples>

Example 1:

[Show what good output looks like for scenario 1]

Example 2..n:

[Show what good output looks like for scenario 2]

</examples>

<output>

Format: [specific format - e.g., "markdown table with 3 columns"]

Length: [constraint - e.g., "300-400 words"]

Structure: [if applicable - e.g., "Introduction → Analysis → Recommendations"]

</output>

<constraints>

- [Specific do's and don't]
- [Style requirements]
- [Any limitations or boundaries]

</constraints>

<instructions>

For complex tasks: Think through your approach step-by-step, then provide the final answer in the requested format.

If information is missing or uncertain, state this explicitly rather than guessing.

</instructions>

**Chain of Verification (CoV)**

Before providing your final response:

- 1. Identify at least three potential gaps or uncertainties in your reasoning.
- 2. Reference the evidence that supports or contradicts each.
- 3. Revise your summary accordingly.
- 4. Present only the final, verified version.

**Reverse Prompting**

I want to [describe the task or goal].

Write the optimal prompt that would generate the best possible result for this task, following prompt-engineering best practices.

Then, execute that prompt and show me the final answer.