# Hunyuan Video 1.5 — Camera Movement Prompting

Tags: AI Video
Description: guide to the camera moves in Hunyuan Video 1.5
Date Added: December 16, 2025 9:20 AM
Type: Note
Archive: No
Spark: No

## Core Principle

**Hunyuan Video 1.5 does NOT rely on special camera-control tokens.**

Camera motion is inferred from **natural language**, similar to cinematic direction notes.

You can use:

- Plain English (“camera slowly moves closer”)
- Film terminology (“dolly in”, “pan right”)
- Or a mix of both

The model interprets intent probabilistically, not via strict keyword parsing.

---

## Recognized Camera Movement Types

Hunyuan consistently understands the following **camera motion concepts**:

### Push / Pull (Depth Movement)

- **Dolly in** – camera moves physically closer
- **Dolly out / pull back** – camera moves away
- Also works: “camera moves closer”, “camera pulls back”

### Zoom (Lens Change)

- **Zoom in / zoom out**
- Less physically consistent than dolly, but supported

### Pan / Tilt (Pivot in Place)

- **Pan left / pan right**
- **Tilt up / tilt down**
- Camera stays in place and rotates

### Horizontal / Vertical Translation

- **Tracking shot / truck left / truck right**
- **Crane shot / pedestal up / pedestal down**

### Rotation / Orbit

- **Orbit around the subject**
- **Camera rotates / rolls slightly**
- Partial or full 360° works

### Follow & Static Modes

- **Follow shot**: “The camera follows the subject”
- **Static shot**: “The camera remains static”

### Shot Feel (Optional)

- “Handheld camera”
- “Steadicam shot”
- “Smooth cinematic movement”

---

## Recommended Prompt Structure (Flexible)

A reliable pattern for **Image → Video**:

**Subject + Scene + Action + Camera Movement + Style/Lighting**

Example:

> “A man sitting at a desk in a dark room, he looks up slowly, camera gently dollies in, cinematic lighting.”
> 

⚠️ This is a **guideline**, not a required format.

---

## Best Practices (Important)

- **Use one main camera move**
    
    (Avoid: “dolly in + orbit + zoom + pan”)
    
- **Place camera direction early or mid-prompt**
- **Be explicit when needed**
    
    “camera pans right to reveal the ocean” works better than “camera moves”
    
- If technical terms fail, **simplify to plain English**

---

## Mixing Movements (Advanced)

You *can* combine motions if they are physically compatible:

✔️ “Dolly in and tilt up”

✔️ “Orbit slowly while pulling back”

Avoid stacking unrelated actions.

---

## Zoom vs Dolly (Reality Check)

- **Dolly** = physical camera movement → more reliable
- **Zoom** = focal length change → supported but less consistent
- When precision matters, prefer **dolly**

---

## Final Truth

Both cinematic phrasing **and** technical keywords work because

Hunyuan Video 1.5 responds to **intent**, not rigid syntax.

### Practical rule

- Start natural
- Add technical terms only if needed
- Keep motion simple and readable