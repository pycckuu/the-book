---
title: "Electrons: Biology’s Currency"
---

Most environments aren’t short on carbon. They’re short on somewhere to put the electrons.

That sounds like a line from a strange economics lecture until you look closely at mud. The surface of wet sediment often wears a rusty color—orange-brown, like old metal left in the rain. A little deeper it can turn dark, even black, and if you disturb it you might catch a familiar warning in the air: that sharp, swampy “rotten egg” edge that tells you something has been reduced and something else has paid the price.

Those colors and smells are not decoration. They’re bookkeeping. They are the sediment’s way of telling you what the scarce resource is down here: **oxidizing power**, the capacity of the environment to accept electrons.

This chapter is about the hidden economy that follows from that scarcity. Microbes don’t make a living by “eating” in the everyday sense. They make a living by moving electrons from donors to acceptors—downhill—and capturing a small cut of the released energy.

Everything else—oxygen disappearing, iron dissolving, sulfate turning into sulfide, methane appearing—is the landscape that downhill motion carves.

## The most useful story: electrons falling
If you want a physics‑native mental model, start with something ordinary: a ball rolling down a hill.

The hill is not the ball’s personality. It’s a difference in potential. If the hill is steep enough, the ball has a lot of available energy to lose on the way down. If the hill is shallow, the ball still rolls, but slowly and with little payoff.

Redox chemistry is the same story in a different language. Electrons “fall” from **donors** (where they have higher chemical potential) to **acceptors** (where they end up at lower chemical potential). Microbes are the machinery that makes the fall usable. They do not create the hill; they learn how to harvest it.

Two practical consequences follow immediately:

- The size of the “drop” matters (how much energy is available per electron moved).
- The pathway matters (whether the fall is fast enough, and whether the microbe can capture some of it instead of losing it as heat).

## Donors, acceptors, and the redox economy
Calling electrons a currency is not just a metaphor; it’s a bookkeeping device. In many environments, carbon is abundant compared to the oxidants that make carbon oxidation profitable. In those cases, the scarce resource is often **electron‑accepting capacity**.

That’s why oxygen is so powerful. Oxygen is not “preferred” because microbes like it; it is preferred because it typically offers a large energy drop per electron transferred, and because diffusion can deliver it (at least near the surface). When oxygen runs out, the ecosystem doesn’t stop. It reorganizes around whatever acceptors remain.

In sediments and groundwater, this produces a recognizable pattern: environments often spend their most “expensive” oxidants first (in the sense of energy payoff), then move to thinner margins as the chemistry becomes more reduced. This is the intuition behind the redox ladder. We’ll treat the ladder as a tendency, not a law, but it’s still a useful first map.

## Physics‑forward bridge: chemistry to electricity
Chemistry already has a perfectly good way to talk about available work: $\Delta G$. Electrochemistry has another: voltage. They are the same story in two languages.

::: {.callout-note}
## Equation Corner — energy as voltage
For a reaction that transfers $n$ electrons,

$$
\Delta G = -nF\,\Delta E
$$

- $F$ is Faraday’s constant ($\approx 96485\ \mathrm{C\,mol^{-1}}$).
- $\Delta E$ is the potential drop the electrons experience (in volts).
- $\Delta G$ has units of $\mathrm{J\,mol^{-1}}$ of reaction as written.

Back‑of‑the‑envelope: a $0.20\ \mathrm{V}$ drop corresponds to about $19\ \mathrm{kJ\,mol^{-1}}$ **per mole of electrons** moved, because $F\times 0.20 \approx 19\,000\ \mathrm{J\,mol^{-1}}$.
:::

That estimate is one of the book’s recurring moves: it lets you look at a potential difference and immediately ask, “Is there enough payment here to cover the costs of being alive?”

## Voltage is not fixed: the Nernst translator
There’s a reason $E_h$ can be confusing at first. In many readers’ heads, “voltage” sounds like a property of a battery: fixed, intrinsic, stamped on the side.

Redox potentials in natural waters are not like that. They shift with context, because the “height” of the hill depends on the current mixture of reactants and products. The translator between concentrations and voltage is the Nernst equation.

::: {.callout-note}
## Equation Corner — Nernst in plain language
For a half‑reaction,

$$
E = E^\circ - \frac{RT}{nF}\ln Q
$$

Read it like this: $E$ moves up or down depending on what’s abundant and what’s scarce, because $Q$ encodes the ratio of products to reactants.

Think about oxygen in our mud jar. As microbes consume it, its concentration ($Q$) plummets. Because $Q$ is inside a logarithm, a drop in concentration translates directly into a drop in voltage. The "hill" gets shallower as the fuel runs out. The Nernst equation isn't just a formula; it's the rule that says *beggars can't be choosers*.

Back‑of‑the‑envelope at room temperature: $\frac{RT}{F} \approx 25.7\ \mathrm{mV}$. So concentration ratios do not need to be extreme to shift $E$ by tens of millivolts.
:::

This is why “what’s the redox potential here?” is never just a question about the environment’s identity. It is a question about composition, transport, and history—about what has been delivered, what has been consumed, and what has accumulated.

## The circuit picture: resistance inside and outside the microbe
Now we can make the circuit metaphor earn its keep.

Think of an electron donor and acceptor pair as the two terminals of a battery. The potential difference is the voltage. But the power you can actually draw depends on resistance.

- **Internal resistance**: enzymes, reaction pathways, regulation, and the microbe’s own maintenance costs.
- **External resistance**: transport limits—how quickly donors and acceptors are supplied, and products are removed.

In a well-mixed beaker, a microbe is living at an unlimited buffet. Resistance is negligible.

In mud, that same microbe is trying to drink a milkshake through a very long, very thin straw. The "battery" (the chemical potential) might be fully charged, but the "wire" (diffusion) is terrible. The organism is throttled not by the energy available, but by how fast the world can deliver it.

## What to measure if you want the electron story
The goal is not to worship a single number like $E_h$, but to assemble a set of measurements that tell you where electrons are coming from, where they are going, and what bottlenecks matter.

::: {.callout-note}
## Measurements that tell the electron story
In practice, you often learn the most from **profiles** (how things change with depth or distance):

- Dissolved oxygen
- Nitrate/nitrite
- Manganese and iron in reduced form (often $\mathrm{Mn^{2+}}$, $\mathrm{Fe^{2+}}$)
- Sulfate and sulfide
- Methane
- $pH$, alkalinity, and dissolved inorganic carbon (to constrain carbon cycling and buffering)
:::

Those measurements let you ask a physics‑style question: where is the gradient, and what flux would it imply? Later, when we build reaction–transport models, this is exactly the bridge we will formalize.

Once you learn to read these profiles, a landscape stops looking like just dirt and water. It starts looking like a patchwork of charged batteries waiting to be discharged.

The cliffs, the sediments, the buried organic matter—they are all terminals of a distinct voltage. The microbes are simply the wires that close the circuit.

## Takeaway
- Electrons are a bookkeeping device: metabolism is electron flow from donors to acceptors.
- The “energy payoff” can be read as a voltage drop: $\Delta G = -nF\Delta E$.
- Potentials are contextual: the Nernst equation translates concentration ratios into voltage shifts.
- Sediment redox structure emerges because biology runs through a medium where transport is limited.


