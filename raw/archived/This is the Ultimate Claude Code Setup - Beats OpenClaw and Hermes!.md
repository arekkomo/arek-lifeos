---
title: "This is the Ultimate Claude Code Setup - Beats OpenClaw and Hermes!"
source: "https://www.youtube.com/watch?v=c2kJ7j3CgUs"
author:
  - "[[Simon Scrapes]]"
published: 2026-04-18
created: 2026-05-28
description: "🚀 Build agentic systems that run your business: https://skool.com/scrapesDon't miss the next build - https://www.youtube.com/@simonscrapes?sub_confirmation=1Agentic frameworks like Hermes and Open"
tags:
  - "clippings"
"User Comment": "this is isteresting for my setup, can you review it and compare to our current setup of Arek &Co and see what we can implement - i like the idea of self learning skils and communication through discord or telegram or whatsapp"
---
![](https://www.youtube.com/watch?v=c2kJ7j3CgUs)

🚀 Build agentic systems that run your business: https://skool.com/scrapes  
Don't miss the next build - https://www.youtube.com/@simonscrapes?sub\_confirmation=1  
  
Agentic frameworks like Hermes and OpenClaw promise a simple, hands-off future, but the reality is often a messy setup and extra costs. What if you could build a more powerful, integrated system yourself using only Claude Code? In this tutorial, I'll show you how to build your own "Agentic OS" by breaking down the five essential features that actually drive results, all from within your existing Claude subscription.  
  
00:00 - The Problem with Hermes & OpenClaw  
01:26 - The 5 Core Features of an Agentic System  
02:15 - Feature #1 - Building Persistent Memory  
06:22 - Feature #2 - Creating Self-Improving Skills  
09:13 - Feature #3 - The Multi-Goal Interface  
13:40 - Feature #4 - Setting Up Scheduled Tasks  
16:18 - Feature #5 - The Missing Ingredient  
18:14 - How The Full Agentic OS Works  
  
#claudecode #hermesagent #openclaw

## Transcript

### The Problem with Hermes & OpenClaw

**0:00** · So take a look at this for a second.

**0:01** · Install a skill, set a schedule for an automated job, and then get the result delivered to you on your phone. That's it. That is the pitch for Hermes and the pitch for Open Claw pretty much, too.

**0:11** · And honestly, when I first saw this, I was completely sold. Because in reality, this is exactly what every business owner wants. The work's going to get done in the background. You're going to get the good result. There's no babysitting. There's no back and forth.

**0:22** · But then you actually go to try it, and the setup's super messy and technical.

**0:26** · And if you want the best models, you're going to pay extra because it's not available on Claw subscription. So in reality, it looks simple, but it's actually not. And I know a lot of you are in this exact same spot because I've seen your comments on my YouTube videos.

**0:38** · Some of you are testing Hermes, trying Open Claw, or even thinking about building your own. And I was there, too.

**0:43** · And while I was going through it, I ended up actually just building my own version. One that runs on Claw subscription, so it doesn't cost me a fortune. Because every single thing in this diagram, you can already do inside Claw code. \[music\] And for a business owner, the Claw code version is actually better because you can see exactly what's going on inside the black box. So in this video, I'm going to break down the five features that actually make a system like this and share what I learned along the way. So if you're thinking about using Hermes, Open Claw, or even just building your own, you'll know exactly what to focus on to get started.

**1:13** · So when I ran Hermes and Open Claw side by side with my own setup, I noticed that they all have different wrappers, different UIs, different channels you can contact them from. But underneath, it's actually just the same five features driving everything. So the first is persistent memory. So think about memory that actually learns about you as you work with it. Then you've got skills that create themselves, first of all, and then get better over time. The third is how you actually interact with it, which is way bigger than just a chat interface on your phone, by the way.

### The 5 Core Features of an Agentic System

**1:42** · Then we've got scheduled tasks that actually run themselves, so not being at the computer window and still getting things done. And then finally, this is the big one, business context. How to inject the right context at the right time to make all your results contextualized to your business and produce therefore better outputs. So get all of these five inside Claw code, and you don't need a separate framework like Open Claw or Hermes, and you can even run it on Claw's most powerful models like Opus 4.7 released just days ago without paying for the API credits.

**2:10** · So you can use it on your Pro and Max subscription. So let me first start with the one that most people get wrong. And that's persistent memory. It's probably the biggest selling point of Hermes and Open Claw. So unlike temporary chat wrappers, they're supposed to maintain long-term searchable memory of past conversations and projects. And this is what gets us hooked initially because the idea that my agent will actually remember what we worked on yesterday, last week, and therefore contextualize and be better for the results going forward sounds amazing.

### Feature #1 - Building Persistent Memory

**2:39** · And if you've worked with Claw code for more than just a few sessions, you'll know just how important context management actually is for getting high-quality outputs. But Claw code actually already has all the ingredients for this. We just need to set them up properly. So I've distilled this into just four memory layers that you can use. The first is claw.md or agents.md if you want to actually use this with different models. So think of this just as your agent's operating instructions, who it is, how it behaves, what rules it follows, and it's going to load into every single session. Most of you will have this layer already.

**3:11** · Now layer two is brand context. So this is where your business context is actually going to live. Think your brand voice, how you speak, ICP, your positioning, all your client details will live in this brand context shared folder, and therefore every skill inside the repository can pull from the same folder. So when Claw writes a LinkedIn post for you, when it's doing client research, when it's building out your landing page, it's going to pull from the exact same business brain. And as you can imagine, it gets much better outputs that are hyper-focused on your business.

**3:42** · Now layer three builds on top of that, and this is what makes agents like Open Claw and Hermes and those frameworks feel so personal. So this is the agent context folder. So we have things like the soul.md and the user.md which describe how it should act and feel and the actions that you as a user using it commonly do, so it feels like it understands you. And finally, layer four, we have project memory. So each project you run actually keeps a history of exactly what's happened, as well as a plan that you can refer to.

**4:08** · So when you actually come back to a content repurposing project that you did three weeks later, Claw is going to know exactly what you built, what worked, what didn't work, and where we need to pick up on that. Now from this four-layer framework, here's the first key learning that I wanted to share with you. It doesn't matter how you set this up. You can put your project briefs anywhere, use whatever planning frameworks you like to write the plans.

**4:31** · So for example, we use GSD or the Get Done frameworks for more complex projects, for example. But the core ingredients are that you actually you're just loading in the right context at the right time, so you're not bloating context and experiencing context rot where the outputs are getting worse the more context you feed in. So your claw.md shouldn't be 2,000 lines long.

**4:50** · It shouldn't even be 1,000 lines long.

**4:52** · It should actually just reference the most important process steps that are going to get loaded in at the start of the conversation. So any additional context that needs to be pulled in at a specific point needs to be stored in a separate reference file. So now I keep my agents.md, if you want to work across models, or your claw.md, succinct and to the point, and then just point it to reference files. So see here where I've separated my brand context and tell it to load it in only when it needs it.

**5:18** · That way, Claw can actually load and offload into separate agents and maintain high-quality outputs because we're not bloating the context. And we use exactly the same approach with every single skill. Short entry skill.md file, detailed references which are only loaded and offloaded when needed. So the first feature then is a memory layer.

**5:37** · This is just about organizing context in a way that actually suits your business and your needs. So you just need to structure it properly, segment your context, point it to reference files, and not overload those context files.

**5:47** · And by the way, there are a bunch of different memory and context storage solutions that you can choose from. So you've got Obsidian, you've got the Open Claw style setup which we're showing here. We've got Carpathy's LLM Wiki, and even people are building custom-built frameworks for memory management. So there's a whole host of ones with different benefits depending on your use cases. So if you do actually want a comparison of these different memory models and when you use which, then drop a comment below and I'll do a full comparison about which one works for which use cases to help you get this memory system set up for your business.

**6:15** · But anyway, that's memory. So let's look at what actually uses that memory to get the work done, which is skills. So Hermes has two features that often get bundled together in all the demos. The first is a persistent learning loop. So think of skills that actually improve themselves over time. So an agent does a task, evaluates its performance, and then it's going to refine that skill over time. And the second is automatic skill creation. So you can generate a new skill, and then apparently share them via agentskills.io. And this is genuinely some seriously important features.

### Feature #2 - Creating Self-Improving Skills

**6:45** · Knowing now what I know about how important skills are for actual output quality. So skills are basically importing expertise to improve our output quality by giving it a really refined process document for a specific task. So you might have LinkedIn post creation skills. You might have copywriting skills. You might have lead generation research skills. All of those will be ported in skills. But again, if we reflect on the Claw code ecosystem, you can actually just build it in yourself to that system.

**7:11** · And the benefit of doing that is you know exactly how it works, too, and you can refine and iterate on it over time. So if we tackle creating skills first, Claw code has the skill creator skill, which you might have seen before. It's built by Anthropic themselves, and basically you give it a description of what skill you want, or you point it to a GitHub repo with an existing skill, or describe a process from scratch on how you do it, and it's going to build out the entire thing, the name, the description, and that determines the success rate of whether it's called or not. And then obviously the step-by-step process document of the actual skill.md file itself.

**7:42** · And if we reflect back on how we manage context, what we want to do is keep a refined skill.md file less than 200 lines and then strip out everything that's unnecessary. So we've actually adapted the Anthropic skill creator skill to do exactly that. Strip out the surplus information and keep that separate and only load it into context exactly when you need it.

**8:00** · Now on top of creating skills, every skill you build should have a self-learning for additional context, and you can go one step further with a learnings.md file or just a rules segment actually inside your skill.md, which are basically non-negotiable rules that each time you use that skill or each time Claw is going to use that skill, it will get better at abiding by those specific rules that we've added in.

**8:27** · So as part of the skill process, as one of the steps in the skill.md, you get it to ask you for feedback. So it effectively takes the feedback then that you give it, applies any rules inside your learnings.md or inside that skill file, and then always sticks to buy those rules when you use that skill again and again. So it's effectively a self-learning loop where the skills get better over time.

**8:47** · So inside Claw code, you can replace that functionality by actually just using the skill creator skill, and then you make them get better by applying rules inside a learnings.md or just rules inside the skill document itself if it's asking you for feedback every time. So so far we've got memory and we've got skills that create themselves and get smarter over time.

**9:06** · The next big question is, how do you actually interact with this system day-to-day? So it's no secret that every agentic framework in 2026 so far has been competing on interfaces. So Open Claw gave you Telegram, Discord, Slack, WhatsApp. Hermes is similar, and Claw code has been bringing out features left, right, and center to try and replicate this to give people access to message their agents from phone. So you can kick off a task while you're out, check the output whilst you're on the move. And that's all great, but here's the thing that nobody is actually talking about.

### Feature #3 - The Multi-Goal Interface

**9:37** · The interface question, in my opinion, isn't just, can I chat from an agent from my phone? The real question now that agents are so good is, how do we manage multiple conversations and multiple goals at the same time? The models are now so, so good that it's pushing us into a different role. We're now jumping into a supervisor role, and we need a better way to actually be able to manage multiple agents and multiple projects on the go, too. And all of the frameworks I've seen give you one conversation at a time.

**10:02** · So, you're going to open Telegram, you chat to one agent, you get one output back, which is great for a single task, but what happens when you've got six business goals all running in parallel? What happens when you want to set up a zero employee company and you run multiple departments through different agents? Like flicking between those chat threads and trying to remember which one was which, which one was writing your news letter, which one filled its context window is actually pretty difficult. So, let me show you how you can get Claude code to handle this and how I did it myself.

**10:30** · So, first, for quick asks, you've got the Claude code inbuilt channels feature. So, this is Anthropic's official feature that's going to work with Telegram, iMessage, and Discord out of the box. So, you don't need to do anything to actually access your conversation at your phone already. So, exactly what Hermes promises, but shipped natively by Anthropic now. And here's where it gets really interesting. If you're running a real business on Claude code, managing multiple conversations, then you need to actually abstract that and build a UI layer on top. So, I did exactly that and I call it the command center. And the idea is really simple.

**11:01** · So, instead of managing terminals or chat threads, you just manage your business goals. So, you drop in a business outcome, Claude is going to spin up an instance to handle it, and it's going to show up on your Kanban style board where you've got full visibility of all your goals running in parallel. You're able to click into one and see the full conversation, and you can have sub chats inside those conversations, too. And you can even have the plan on the right-hand side next to the chat window. So, you could have four agents working on different features here, and then the plan on the right-hand side, which is going to auto update as you run through the plan.

**11:32** · So, this is set out for larger, more complex projects. You still have the granularity of the individual chat interface, but you're able to abstract yourself to a supervisor role because you can see how the chats are working against the plan and how that is all working against an individual business goal, as well as then dig into the other business goals that you've currently got on the go. So, the workflow becomes then quick conversations while you're out and about.

**11:56** · You can just fire it into Telegram via the channels feature, but if you've got a big goal that you want to manage over a day or a week or a complex project, then, for example, I would drop it into my command center and come back to actually review the outputs here and manage multiple goals inside that. All of this, for example, you can build exactly for yourself. You can follow the structure that I'm showing you on screen, and it all runs locally and acts as just a UI wrapper on top of your terminal.

**12:20** · So, it abides by Anthropic's OAuth usage policies, meaning you can actually use it with your pro and max subscriptions. you want to get this up and running without having to build it yourself, it's just a one-line install as part of our paid community in the description below. And it includes all the underlying agentic operating system logic that we're covering today, too. So, full business context out of the box, 20-plus skills, scheduled workflows, the lot, all set up extremely quickly to handle tasks on behalf of you or your business. So, check out the link in the description below if you're interested in that.

**12:50** · So, how you interact with it matters way more than most people think. Most people are just jumping to actually interact with it on the phone, but phones are only good for quick asks, and you can use Claude code channels for that. But if you want to build out something managing multiple goals, then you need your own interaction layer. Now, the one caveat I'll put on this, Claude have just updated their own Claude desktop to actually accommodate for managing multiple goals.

**13:13** · However, it's still very technical, very focused on GitHub commits, and not focused on that high-level planning view with built-in planning frameworks like the way I built it out for myself. So, it depends what you're looking for as to what is the right solution for you. And that's how we interact with Claude code in a similar way to like Open Claude's mission control, for example. So, you've got memory, we've got skills, we've got the interaction layer. Now, let's look at the stuff that you should just be able to let run without you actually interfering with it.

**13:39** · So, Hermes lets you set up automated jobs on a schedule, so you can install a skill, create a recurring job, and then it's going to run automatically. And in Claude code, you can do exactly the same with the new routines feature inside their desktop app. But right now, the feature is limited to built-in connectors, so it's quite difficult with apps that aren't in their native built-in connectors, especially when you can actually build this out using Claude code to leverage the built-in functionality on your Mac or Windows machine. So, you don't need a virtual private server, you don't need extra infrastructure.

### Feature #4 - Setting Up Scheduled Tasks

**14:08** · Claude code can actually set up this logic for you in less than a few hours, so that you can just control your scheduled jobs from a few files. When they're noted as active, we're going to run those scheduled jobs, and when they're not active, we're not going to run those scheduled jobs. Now, most people are creating scheduled jobs to just insert a simple prompt, but actually the smartest people are actually using scheduled workflows to chain skills together inside a prompt.

**14:33** · So, you can schedule a task that's effectively going to run multiple skills in sequence. You might have a weekly content digest that runs every Monday at 9:00 a.m. So, it's going to pull the previous week's YouTube videos, run an analysis across those, and then generate three LinkedIn posts using your voice profile, and then drop them into a review folder. So, you come in on Monday morning, you've got all of those already ready in the review folder, and they're contextualized and followed all of the skill process documents that produce high-quality outputs.

**15:01** · So, many different skills all chained together to produce one output that you come back and you can approve or supervise. And the biggest learning when I started building this out, my original aim was to build out fully autonomous scheduled workflows, run the whole thing, ship the output, post it to LinkedIn, whatever, but it was actually pretty bad because 20% of the time, something wouldn't be quite right.

**15:22** · So, instead, I've actually built this framework now around doing 80% of the work automatically, the research, the narrowing of different topics, but what I've added in is always having a human checkpoint before anything goes live. So, I'm never going to post content that's just AI-generated stuff. I'm always going to have that human supervisor in the process until we can get to a level of quality where things can run autonomously and we're happy with them. So, all of my content drafts, for example, land in a folder so that I can actually come in and supervise them and review them and approve the outputs.

**15:52** · So, it's basically giving you the speed of the automation without the risk of shipping something that's just pure AI slop, which we do not want to contribute. So, you can effectively use scheduled jobs to chain multiple skills together and then add in a human checkpoint to actually approve or make sure the quality is high. Right, so that is four amazing features. Each one you can build inside Claude code using what's already there in just a few days, but here's the fifth, and honestly, this is the one that made me stop looking at Hermes and Open Claude because I did not see enough capacity for it to do this well.

### Feature #5 - The Missing Ingredient

**16:23** · Now, because Hermes and Open Claude are built solely to be agent frameworks, they're very tool-focused. So, it's all about installing a skill, running a job, getting an output, but they don't know anything really about your business. You can, of course, install ways to actually give it information about your business, but they don't, out of the box, know your brand voice, know your ICP, they don't know your positioning, they don't know who your clients are, what your tone in your emails usually is. All of these things are critical for high-quality outputs. And it's the equivalent of basically starting from zero when you run a new skill.

**16:53** · And this is what shifted me away from systems like Hermes and Open Claude to build my own system because I realized that the real unlock isn't actually the agents.

**17:02** · The agents and the models are getting better and better. It's the layer underneath, the context that we discussed at the start, the brand context folder, the voice profile, the audience avatar, all of that preloaded, pulling into the right skill at the right time is what actually generates high-quality outputs. So, I actually pulled together myself a set of skills that help me generate my voice profile, and I make sure that when I build out my skills using the skill creator skill, all of them reference the right context at the right time. So, if I have a skill that builds out LinkedIn posts, for example, it will always reference my brand voice.

**17:34** · It will understand the positioning because it understands who my clients are. And I used content as an example because it's relatable to a lot of different businesses. It doesn't mean you need to use these systems to actually generate your content. And the way that we've done this is basically moving everything, all of that context for my business, into a single brand context folder that every skill is able to reference. So, you update the information once, and every skill gets that update when it runs. So, business context is that compounding advantage that you cannot get right now.

**18:01** · So, build this right, and this totally underpins all of the other pillars that we've talked about today. You need to inject the right context at the right time, and that starts with actually having a shared context folder that focuses on your brand and you. So, when you bring this all together, this is exactly how it looks in a three-step process to compare to the one we showed at the start. We have your own agentic operating system where we have the business brain, which underpins and powers Claude code by injecting the right context at the right time.

### How The Full Agentic OS Works

**18:27** · We're able to then actually just write goals, whether that's to create a scheduled job or to manage multiple business goals in one place. Claude is then going to do the work in the background to break it down into subtasks, choose the right skills, etc. And what that enables is your system to deliver you a high-quality result that's contextualized by your business context, completely replacing the need for a framework like Hermes or Open Claude and without all of the technical overhead and cost implications of moving off the pro and max plans from Claude.

**18:54** · So, that's the five features that actually matter and how to build each one of them inside Claude code yourself. And if you're building out your own version right now, which a lot of you in the comments have told me you are, here's my honest advice from three months of getting this wrong and rebuilding it.

**19:10** · Start with this business brain. Don't start with the agents. Don't start with the multi-agent orchestration. I made this same mistake. Every feature I just walked through gets multiplied by having the solid context, the foundation layer underneath it. And none of them are going to work without that layer. And if you just want to skip the setup and grab the whole thing plug and play today, then check out the link below in the description for the agentic academy. So, you've got the agentic OS, the command center that you saw today with the dashboard, and all 20-plus skills ready to go with a one-line install.

**19:38** · And if you want to see exactly why I built out the command center in the first place, then check out the next video. Thanks for watching.