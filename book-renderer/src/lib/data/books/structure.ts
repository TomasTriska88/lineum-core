import type { Concept } from '../concepts';

export const level3Concepts: Concept[] = [
  {
    id: "what-is-a-vector",
    chapterNumber: 1,
    chapterTitle: "The Muscular Arrow (Vectors)",
    title: "What is a Vector? ($\\vec{v}$)",
    hook: "Imagine a glowing arrow that isn't just statically pointing, but it is actively flexing and steadily pushing with a massive, heavy physical force.",
    explain: "A vector isn't a dead pair of coordinates on a map. It is a raw instruction of pure physical thrust and direction. It acts as the muscular code that tells a spaceship engine exactly how hard to violently burn and in what exact diagonal heading to fly peacefully through the void.",
    image: {
      path: "images/level3-vector.png",
      prompt: "A thick, glowing arrow actively pushing heavily against a solid concrete block, seamlessly sliding it diagonally across a grid floor. Dynamic vector style, white background."
    },
    aha: "Vectors are not static map locations; they are active packages of physical, directional muscle.",
    proseSegments: [
      {
        label: "Consider this...",
        body: "What if you smoothly multiply a vector by the regular number 5 ($5\\vec{v}$)? The arrow doesn't change its internal direction. It just physically violently stretches to become 5 times longer, instantly pumping five times more muscular thrust into that exact same diagonal trajectory."
      }
    ],
    summary: "A vector is just a geometric delivery boy. It carries exactly two pieces of code: \"Where am I perfectly pointing?\" and \"How powerfully am I steadily pushing?\" Nothing more, nothing less."
  },
  {
    id: "adding-vectors",
    chapterNumber: 1,
    chapterTitle: "The Muscular Arrow (Vectors)",
    title: "Adding Vectors ($\\vec{a} + \\vec{b}$)",
    hook: "Imagine a wind blowing your heavy ship firmly north, while a steady ocean current simultaneously glides you east.",
    explain: "When two vectors add together, they don't awkwardly crash. They smoothly blend their muscular forces gracefully. Your ship calmly obeys both the wind and the river at the exact same time, successfully cutting a smooth, angled diagonal line right down the absolute middle of both paths.",
    image: {
      path: "images/level3-adding-vectors.png",
      prompt: "A sailing ship being pushed heavily forward by blue wind arrows while simultaneously being coasted sideways by red ocean current arrows, leaving a thick, single purple diagonal path in its wake. Minimalistic vector style, white background."
    },
    aha: "Adding vectors is just letting two completely different physical forces seamlessly compromise on a final geometric direction.",
    proseSegments: [
      {
        label: "Consider this...",
        body: "What if two exactly identical vectors push physically violently against each other face-to-face? The engine completely, quietly balances them out. Their heavy physical muscle is perfectly matched. The ship completely stops, safely resting at a pure zero vector ($\\vec{0}$)."
      }
    ],
    summary: "Vector addition is the peaceful resolution of conflict. It gracefully gathers all the forces sliding around the room and automatically calculates the exact geometric compromise where the physical hull will comfortably settle."
  },
  {
    id: "what-is-a-matrix",
    chapterNumber: 2,
    chapterTitle: "The Giant Transformers (Matrices)",
    title: "What is a Matrix? ($M$)",
    hook: "Imagine a giant, invisible mechanical crane cleanly grabbing the four corners of your entire physical bedroom and smoothly stretching it into a tilted, elongated diamond room.",
    explain: "A matrix is heavily misunderstood as a boring spreadsheet. In the engine, a Matrix is a massive, violent terraforming tool. When a Matrix \"multiplies\" with your world, it grabs the entire X/Y grid of space and instantly rotates it, flattens it, or folds it in a single fluid motion.",
    image: {
      path: "images/level3-matrix.png",
      prompt: "A giant, invisible mechanical claw actively grabbing a perfect square-tiled floor grid and gracefully stretching it sideways into a massive slanted diamond-shaped web. Industrial vector style, white background."
    },
    aha: "Matrices are giant spatial cranes that beautifully fold, stretch, bend, and rotate the entire universe exactly at once.",
    proseSegments: [
      {
        label: "Consider this...",
        body: "What if a Matrix rotates the entire world exactly 90 degrees? Every single vector string, solid box, and planet resting safely on that map is seamlessly rotated with it. A Matrix doesn't directly touch the objects inside the room; it just mechanically, smoothly rotates the entire floor directly beneath them."
      }
    ],
    summary: "If you want to move one single chair, you load a Vector arrow. If you want to grab the entire house, tip it elegantly upside down, and violently reshape the entire roof, you fire a Matrix."
  },
  {
    id: "matrix-multiplication",
    chapterNumber: 2,
    chapterTitle: "The Giant Transformers (Matrices)",
    title: "Matrix Multiplication ($A \\cdot B$)",
    hook: "Imagine running a flat piece of heavy metal solidly through an industrial flattening press, and then immediately throwing it through a massive, roaring curling machine.",
    explain: "Deep matrix algebra is just physically grouping two giant factory commands closely together. First, the room gets smoothly squashed. Then, the squashed room gets gracefully rotated. You are just writing a single macro script of chained sweeping animations.",
    image: {
      path: "images/level3-matrix-multiplication.png",
      prompt: "A heavy metal block going forcefully through a flattening press, then the flattened sheet actively entering a spinning wheel to be cleanly curled, forming a completely continuous fluid chain reaction. Action vector style, white background."
    },
    aha: "Matrix multiplication is just confidently forcing the central engine to play two massive space-bending animations rapidly back-to-back.",
    proseSegments: [
      {
        label: "Consider this...",
        body: "What if you perfectly reverse the order? ($B \\cdot A$). The metal changes totally! Gracefully curling a block of steel *before* you crush it flat yields a completely different physical end shape than wildly flattening it first and then rolling out a thin curled sheet."
      }
    ],
    summary: "In standard math, $3 \\times 4$ is beautifully identical to $4 \\times 3$. But in the elegant world of Matrices, order is remarkably strict. The exact chronological order of the factory tools firmly determines the final architectural reality of your 3D room."
  },
  {
    id: "eigenvectors-and-eigenvalues",
    chapterNumber: 3,
    chapterTitle: "The Unbreakable Bones (Eigenvalues)",
    title: "Eigenvectors & Eigenvalues",
    hook: "Imagine a block of thick blue jelly. When you crash your hand down onto it, the jelly squashes out violently in all directions, except for two unbreakable cocktail sticks hidden deep inside that utterly refuse to visibly wobble.",
    explain: "When a Matrix gracefully rotates and forcefully folds space, almost everything gets shifted cleanly off its original path. **Eigenvectors** are the magical, hidden permanent bones of the universe that refuse to get knocked gently off-course during the transformation. They solely stretch, but they absolutely never geometrically deviate.",
    image: {
      path: "images/level3-eigenvectors.png",
      prompt: "A wobbly, blue block of thick jelly being firmly compressed from the top, while a glowing red cocktail stick pierced straight through the center perfectly maintains its exact straight angle safely without bending. Clean geometric vector style, white background."
    },
    aha: "Eigenvectors are the actual skeleton of the matrix—the only pure mathematical lines that survive violent space-bending entirely without losing their original foundational course.",
    proseSegments: [
      {
        label: "Consider this...",
        body: "What if the transformation smoothly compresses the whole room down to firmly half its height? The indestructible bone (Eigenvector) stubbornly points in the identical direction, but it shrinks beautifully to exactly half its physical length. That predictable \"1/2\" shrinkage size is called its true Eigenvalue."
      }
    ],
    summary: "If you want to understand how a massive transformation (like Google's PageRank algorithm) fundamentally operates, you don't track the wobbling jelly. You cleanly isolate the absolute unbending bones. They faithfully reveal exactly where the core gravity of the digital system is permanently anchored."
  },
  {
    id: "the-null-space",
    chapterNumber: 4,
    chapterTitle: "The Power of Null (Space Deletion)",
    title: "The Null Space (The Void)",
    hook: "Imagine a massive industrial press that folds full 3D cars strictly down into completely flat 2D metal pancakes.",
    explain: "Matrices can seamlessly and irreversibly collapse higher dimensions straight into nothing. The Null Space accurately tracks all the exact arrows, depths, and solid shapes that were gracefully wiped straight into a zero coordinate completely during the heavy press.",
    image: {
      path: "images/level3-null-space.png",
      prompt: "A heavy 3D car being cleanly flattened by a grey industrial press. A blue arrow points to the car's height dimension, which is suddenly, magically deleted from existence into a flat shadow floor. Minimalistic vector style, white background."
    },
    aha: "The Null Space is the quiet geometric graveyard tracking every single dimension the Matrix forcefully erased.",
    proseSegments: [
      {
        label: "In Short",
        body: "If the whole world violently collapses to a single tiny dot, everything in the universe was just sucked silently down into the Null Space. It represents absolute information loss; once a 3D building folds beautifully flat, you can never reconstruct its true height backwards from a pure zero."
      }
    ],
    summary: "It represents absolute information loss; once a 3D building folds beautifully flat, you can never reconstruct its true height backwards from a pure zero."
  },
  {
    id: "ordinary-differential-equations",
    chapterNumber: 5,
    chapterTitle: "Navigating Chaos",
    title: "Ordinary Differential Equations (The River of Wind)",
    hook: "Imagine trying to row perfectly straight across a deep river, while a gentle gust of wind pushes you west, and a heavy underwater current actively pulls you steadily south.",
    explain: "Differential equations don't give you a fixed, static number. They securely provide a real-time reactive wind-map. As your boat moves to a brand new spot, the wind instantly shifts its own physical absolute direction based securely on exactly where you just arrived.",
    image: {
      path: "images/level3-odes.png",
      prompt: "A small yellow boat floating smoothly on an absolute grid composed of thousands of tiny active blue arrows (vector field), all shifting their rigid angles instantly to wildly push the boat in a swirling pattern. Dynamic vector style, white background."
    },
    aha: "A differential equation is literally just a localized engine map of the wind. Your only job is to calculate where the leaf will eventually safely settle.",
    proseSegments: [
      {
        label: "In Short",
        body: "If the boat violently hits the center of a strong whirlpool, the vectors simply spiral inward indefinitely, forcefully dragging the boat safely to the absolute core. Differential equations seamlessly animate all fluid physics in video games."
      }
    ],
    summary: "Differential equations seamlessly animate all fluid physics in video games."
  },
  {
    id: "probability-and-deep-statistics",
    chapterNumber: 6,
    chapterTitle: "The Logic of Chance",
    title: "Probability & Deep Statistics",
    hook: "Imagine dropping a handful of smooth marbles down a massive wall of perfectly spaced, rigid wooden pegs.",
    explain: "Probability isn't desperately guessing the future. It is simply mapping the invisible tracks of the universe. One individual marble drops completely wildly, bouncing purely with chaos. But when you solidly drop 10,000 marbles, they perfectly, gracefully form a beautifully smooth, undeniable bell curve at the bottom floor every single time.",
    image: {
      path: "images/level3-probability.png",
      prompt: "A handful of metallic marbles actively bouncing rapidly down a dense pegboard wall, finally settling below into a perfectly symmetrical, completely smooth bell curve of piled shapes. Action vector style, white background."
    },
    aha: "Deep statistics proves that absolute chaos safely transforms into a rigid, highly predictable geometric shape when observed from perfectly far away.",
    proseSegments: [
      {
        label: "In Short",
        body: "Statistics allows the matrix to comfortably tame pure randomness. It maps uncertainty completely into a beautifully reliable, structural equation that engineers securely gamble billions of dollars on safely."
      }
    ],
    summary: "It maps uncertainty completely into a beautifully reliable, structural equation that engineers securely gamble billions of dollars on safely."
  },
  {
    id: "markov-chains",
    chapterNumber: 6,
    chapterTitle: "The Logic of Chance",
    title: "Markov Chains",
    hook: "Imagine a wandering dog traversing a three-room house blindly, absolutely completely forgetting which room he just naturally came from.",
    explain: "Markov Chains are probability state machines that explicitly exist purely in the exact 'now'. The dog's chances of gracefully stepping into the Kitchen only mathematically depend on him currently standing firmly in the Hallway. His heavy history is completely wiped instantly.",
    image: {
      path: "images/level3-markov.png",
      prompt: "A floorplan of three colored rooms. A dog sits squarely in the blue room, encircled by glowing percentile arrows firmly pointing exclusively to the next two immediate adjacent open doors. Minimalistic geometric vector style, white background."
    },
    aha: "Markov chains powerfully model futures that safely rely solely on the raw present state, deliberately forgetting all physical history.",
    proseSegments: [
      {
        label: "In Short",
        body: "From advanced weather forecasting to AI text generation algorithms completely deciding the absolute best next word, they are the silent, memoryless engine running massive chains of seamless, probable chance."
      }
    ],
    summary: "They are the silent, memoryless engine running massive chains of seamless, probable chance."
  },
  {
    id: "discrete-math",
    chapterNumber: 7,
    chapterTitle: "The Grid of Reality",
    title: "Discrete Math",
    hook: "Imagine a universe possessing absolutely zero fractions, where everything mathematically jumps forcefully in hard, indestructible chunks.",
    explain: "In Calculus, space confidently and beautifully flows like wet water. In Discrete Math, space is a jagged, heavy staircase. A computer logically cannot comprehend a smooth curve; it gracefully chops it totally down into a rigid line of individual digital zeroes and ones.",
    image: {
      path: "images/level3-discrete.png",
      prompt: "A smooth, perfectly analog curve drawn cleanly next to a rigid, jagged line comprised entirely of heavy, discrete square staircase steps entirely lacking fractional depth. Clean geometry vector style, white background."
    },
    aha: "Discrete math is the fundamental language of computers because silicon definitively cannot beautifully understand 'half' of a switch.",
    proseSegments: [
      {
        label: "In Short",
        body: "Cryptography, internet security, and all global processing power rely firmly on this logic. It violently restricts the engine's physics purely to safe, absolute integers, building impenetrable digital walls."
      }
    ],
    summary: "Cryptography, internet security, and all global processing power rely firmly on this logic. It violently restricts the engine's physics purely to safe, absolute integers, building impenetrable digital walls."
  },
  {
    id: "graph-theory",
    chapterNumber: 7,
    chapterTitle: "The Grid of Reality",
    title: "Graph Theory (The Matrix Web)",
    hook: "Imagine dropping a spider firmly onto a gigantic net of glowing dots strung tightly together, and commanding it to walk beautifully to the exit without touching the same glowing thread exactly twice.",
    explain: "Graph theory strips fluid reality safely down to a remarkably simple question: \"Is it connected, or is it broken?\" It is the completely invisible, hidden skeletal language gracefully dictating the global internet, modern GPS maps, and heavy social networks.",
    image: {
      path: "images/level3-graph-theory.png",
      prompt: "A glowing black web of heavy nodes and rigid white threads. A spider actively highlights its exact shortest walking path mathematically from the bottom node securely to the top node in bright neon green. Flat geometric vector style, white background."
    },
    aha: "Forget distances, fluids, and angles completely. Graph theory is solely the pure, raw logic of counting locked doors and open tunnels.",
    proseSegments: [
      {
        label: "In Short",
        body: "Every algorithm that actively calculates the fastest drive home, or the safest internet server leap for your physical data packet, is fundamentally just a digital spider cleanly navigating a rigid Graph Theory web."
      }
    ],
    summary: "Every algorithm that actively calculates the fastest drive home is fundamentally just a digital spider cleanly navigating a rigid Graph Theory web."
  },
{
    "id": "solving-systems",
    "layer": "core",
    "chapterNumber": 4,
    "chapterTitle": "The Architecture of Logic (Systems & Statistics)",
    "title": "Solving Systems ($Ax = B$)",
    "hook": "Imagine two laser beams intersecting perfectly on a grid. You need the exact coordinates of the collision.",
    "explain": "Solving a system uses substitution or elimination to mechanically destroy unknown variables until only the exact geometric point of intersection remains standing.",
    "image": {
      "path": "images/level3-systems.png",
      "prompt": "Two overlapping grids violently colliding, highlighting a single perfect red intersection point. Dark abstract conceptual vector."
    },
    "aha": "Solving systems forcefully crunches multidimensional lines down into a singular physical dot.",
    "summary": "Solving systems forcefully crunches overlapping multidimensional lines down until only their identical physical collision point survives.",
    "proseSegments": [
      {
        "label": "What it is.",
        "body": "The algebraic extraction of an intersection coordinate spanning multiple overlapping functions simultaneously."
      },
      {
        "label": "How to solve.",
        "body": "Use Gaussian Elimination. Methodically subtract rows from each other structurally to obliterate terms, isolating variables linearly downward."
      },
      {
        "label": "Why it works.",
        "body": "Subtracting equations from each other calculates the exact distance between lines. When the distance zeroes out, you hit the structural crossing point."
      }
    ]
  },
  {
    "id": "statistics-basics",
    "layer": "core",
    "chapterNumber": 4,
    "chapterTitle": "The Architecture of Logic (Systems & Statistics)",
    "title": "Statistics (Distributions)",
    "hook": "Imagine dropping identical marbles uniformly bouncing down a pegboard to form an organic glowing mound.",
    "explain": "Statistics mathematically stabilizes massive chaos. Variance determines exactly how wide and flat the resulting marble pile stretches.",
    "image": {
      "path": "images/level3-statistics.png",
      "prompt": "A perfectly symmetrical bell curve composed of hundreds of glowing falling dots resting on a line. Abstract deep vector."
    },
    "aha": "True randomness acts incredibly predictably when forced into massive aggregated quantities.",
    "summary": "Statistics translates sprawling physical chaos into predictable, stable central masses anchored by geometric variance.",
    "proseSegments": [
      {
        "label": "What it is.",
        "body": "The calculation of the central mass (Mean) and the boundary dissipation rate (Variance) of enormous datasets."
      },
      {
        "label": "How to solve.",
        "body": "Calculate the mean by evening the weight of all terms. Calculate variance by measuring the exact squared tension pulling each point away from the center anchor."
      },
      {
        "label": "Why it works.",
        "body": "Squaring the distance removes minus signs, ensuring erratic data points that stray too far from the anchor generate exponential tension against the structural mean."
      }
    ]
  },
  {
    "id": "combinatorics",
    "layer": "core",
    "chapterNumber": 4,
    "chapterTitle": "The Architecture of Logic (Systems & Statistics)",
    "title": "Combinatorics",
    "hook": "Imagine spinning the combination lock of an impenetrable vault.",
    "explain": "Combinatorics calculates exact factorial permutations without forcing you to manually map every singular physical combination possible.",
    "image": {
      "path": "images/level3-combinatorics.png",
      "prompt": "A branching fractal tree breaking down into massive exponential endpoints spanning a matrix grid. Clean conceptual vector style."
    },
    "aha": "Combinatorics mathematically constructs infinite branching timelines instantly.",
    "summary": "Combinatorics maps massive branching timelines instantly, reducing chaotic infinite sets into structured, solvable algorithms.",
    "proseSegments": [
      {
        "label": "What it is.",
        "body": "The rigorous mathematics governing counting, recursive arrangements, and discrete structural grouping."
      },
      {
        "label": "How to solve.",
        "body": "Utilize factorials ($!$). If order matters, use Permutations ($n!/(n-r)!$). If order is irrelevant, collapse the duplicates using physical Combinations."
      },
      {
        "label": "Why it works.",
        "body": "A tree branches out continuously. The math fundamentally multiplies the number of paths extending forward, mapping massive timeline grids onto a single equation."
      }
    ]
  },
  {
  "id": "benfords-law-probability",
  "layer": "enrichment",
  "chapterNumber": 5,
  "chapterTitle": "Enrichment: The Global Network",
  "title": "Benford & Probability Scales",
  "hook": "Imagine auditing a massive tax spreadsheet spanning thousands of accounts. The subtle distribution of leading digits will expose human fraud.",
  "explain": "When analyzing deep statistical matrices, Benford's Law emerges as an irrefutable mathematical truth. Any fabricated data typically features random, evenly distributed leading digits, which flagrantly breaks the natural logarithmic hierarchy.",
  "image": {
    "path": "images/enrichment-benford-fraud.png",
    "prompt": "A massive matrix grid glowing blue, with artificial anomalies highlighted violently in red. Deep abstract conceptual vector view."
  },
  "aha": "Nature generates numbers via multiplicative scale; humans fabricate numbers via additive randomness.",
  "summary": "Utilizing probabilities driven by logarithms acts as an unassailable verification mechanism against artificial system interference.",
  "proseSegments": [
    {
      "label": "What it is.",
      "body": "The application of Benford's macroscopic distribution properties to detect systemic localized tampering within stochastic data."
    },
    {
      "label": "Why it works.",
      "body": "Because random number generators output flat distributions naturally, they fail entirely to replicate the delayed velocity curves inherent to multiplicative organic world-growth. The matrix mismatch exposes the fabrication."
    }
  ]
},
{
  "id": "pareto-principle",
  "layer": "enrichment",
  "chapterNumber": 5,
  "chapterTitle": "Enrichment: The Global Network",
  "title": "The Pareto Principle (80/20)",
  "hook": "Imagine recognizing that 80% of an entire empire's wealth is monopolized by merely 20% of its architects.",
  "explain": "The Pareto Principle observes that for numerous events in structural, economic, and network systems, roughly 80% of the consequences stem from exactly 20% of the causes.",
  "image": {
    "path": "images/enrichment-pareto.png",
    "prompt": "A heavy unbalanced lever highlighting a massive glowing cluster of output derived from a tiny glowing source node. Abstract physics vector art."
  },
  "aha": "Systems are inherently unequal; input almost never maps linearly to output.",
  "summary": "Pareto reveals that networks establish steep hierarchical dependencies rather than flat, even distributions.",
  "proseSegments": [
    {
      "label": "What it is.",
      "body": "A power-law probability distribution detailing extreme inequality in cause-to-effect mappings across discrete nodes."
    },
    {
      "label": "Why it works.",
      "body": "In a connected topology, success acts as an attractor. The nodes possessing slight initial traffic dynamically accumulate vastly higher exponential returns, consolidating structural load mathematically rather than fairly."
    }
  ]
},
{
  "id": "riemann-teaser",
  "layer": "enrichment",
  "chapterNumber": 5,
  "chapterTitle": "Enrichment: The Global Network",
  "title": "The Riemann Zeros (Teaser)",
  "hook": "Imagine discovering that the erratic, chaotic distribution of prime numbers is actually perfectly orchestrated by a hidden oscillating wave.",
  "explain": "The Riemann Hypothesis suggests that the elemental primes (the atoms of math) are not entirely chaotic. Instead, they are the harmonic beats governed by the zeros of a complex multidimensional spectrum.",
  "image": {
    "path": "images/enrichment-riemann.png",
    "prompt": "A glowing complex coordinate plane with points precisely aligned on an imaginary axis line of 1/2. Deep enigmatic celestial vector."
  },
  "aha": "The apparent randomness of the primes masks an acoustic structure echoing from higher dimensions.",
  "summary": "While remaining formally unsolved, Riemann implies that absolute chaos in the real dimension resolves into perfect symphony in the complex dimension.",
  "proseSegments": [
    {
      "label": "What it is.",
      "body": "A conjecture identifying the critical, non-trivial zeroes of the Riemann Zeta Function mapped atop the complex plane of reality."
    },
    {
      "label": "Why it works.",
      "body": "By analyzing the shadow of the prime numbers using imaginary wave frequencies, the erratic nature condenses into a rigid, structured line. It represents the ultimate bridge between absolute arithmetic structure and continuous wave physics."
    }
  ]
}
];
