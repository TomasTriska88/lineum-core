import type { Concept } from '../concepts';

export const level2Concepts: Concept[] = [
  {
    id: "the-function-engine",
    chapterNumber: 1,
    chapterTitle: "The Machine (Functions $f(x)$)",
    title: "The Function Engine $y = f(x)$",
    hook: "Imagine dropping a raw block of wood into a roaring, automated conveyor belt machine.",
    explain: "A function isn't just a letter. It is an industrial factory line. You drop a raw material ($x$) into the input chute. The machine securely slices it, heavily paints it, and drops a completely new, finished product ($y$) into the output basket.",
    image: {
      path: "images/level2-function.png",
      prompt: "A mechanical factory box with an active conveyor belt. A raw block of wood enters, the internal gears process it under tension, and a shiny, perfectly shaped blue sphere exits. Industrial vector style, white background."
    },
    aha: "Functions ($f(x)$) aren't numbers; they are active machines that consistently transform any raw input into a specific, predictable output.",
    proseSegments: [
      {
        label: "Consider this...",
        body: "What if you chain two machines exactly together $f(g(x))$? You drop a block into the first machine, converting it cleanly into a sphere. The sphere smoothly rolls directly into the second machine, which paints it bright red. You are just chaining animations."
      }
    ],
    summary: "A function is a strict mechanical rule. Every single time you feed it the exact same input, you flawlessly receive the exact same output. It is the unbreaking heartbeat of predictable physics."
  },
  {
    id: "graphing-parabolas",
    chapterNumber: 1,
    chapterTitle: "The Machine (Functions $f(x)$)",
    title: "Graphing Parabolas ($y = x^2$)",
    hook: "Imagine tossing a heavy iron ball straight up into the air and watching it trace a perfect, sweeping arc back down to the grass.",
    explain: "Parabolas are not just abstract curved lines drawn on a page. They physically represent the exact flight path of a heavy projectile smoothly fighting against gravity in the engine's sky.",
    image: {
      path: "images/level2-parabola.png",
      prompt: "A projectile being forcefully launched from the ground, flying upward in a smooth, symmetrical arc, and landing solidly back on the floor. Dynamic vector style, white background."
    },
    aha: "A graph is deeply visual; it is just a time-lapse photograph of a moving object traversing the sky.",
    proseSegments: [
      {
        label: "Consider this...",
        body: "What if you safely add a plus variable $+ 5$ to the end of the rocket's code? The entire flight path doesn't change its internal shape; it just physically lifts up and hovers perfectly five inches higher off the ground."
      }
    ],
    summary: "Graphs are not abstract math drawings. They are literal flight blueprints. When the equation gently changes, the physical trajectory of the flying rocket smoothly bends, lifts, or lands in real-time."
  },
  {
    id: "the-concept-of-a-limit",
    chapterNumber: 2,
    chapterTitle: "The Edge of Reality (Limits)",
    title: "The Concept of a Limit ($\\lim_{x \\to a}$)",
    hook: "Imagine flying a spaceship directly toward a blazing sun, seeing how intensely close you can safely hover before the heat physically melts your hull.",
    explain: "A limit is mathematical cliff-walking. It is pushing the engine's simulation as close to an impossible boundary (like dividing by zero) as physically possible, just to carefully measure what the shape looks like a single millimeter before the matrix halts.",
    image: {
      path: "images/level2-limit.png",
      prompt: "A futuristic spaceship flying intensely close to a massive, burning sun, hovering dangerously precisely on a red warning line just before burning up. Action vector style, white background."
    },
    aha: "A Limit isn't reaching the final destination; it's measuring exactly what happens the split-second before you crash into the wall.",
    proseSegments: [
      {
        label: "Consider this...",
        body: "What if a graph has a massive, uncrossable crater blown right in the middle of the road? The limit is simply parking your car one pure inch before the hole, and writing down the exact GPS location of where the road theoretically should have safely continued."
      }
    ],
    summary: "Limits are the universe's ultimate scouting tool. They elegantly allow us to mathematically calculate the exact shape of black holes, infinities, and glitches without actually touching them and crashing the computer."
  },
  {
    id: "the-derivative",
    chapterNumber: 3,
    chapterTitle: "The Frozen Speedometer (Derivatives)",
    title: "The Derivative ($dy/dx$)",
    hook: "Imagine slamming the \"pause\" button on a video of a speeding racecar, then quietly walking up to look closely at its frozen dashboard speedometer.",
    explain: "Calculus tries to powerfully find the true speed of an object at one exact, perfectly frozen instant in time. A derivative is just a radar gun. It cleanly measures exactly how steep the road is beneath the car's tires at a single frozen movie frame.",
    image: {
      path: "images/level2-derivative.png",
      prompt: "A speeding racecar perfectly frozen in time on a steep hill. A glowing speedometer hovers directly above it, locking perfectly onto a single static number. Fast motion vector style, white background."
    },
    aha: "A derivative simply measures how fast a given shape is physically changing at one microscopic, totally frozen instant.",
    proseSegments: [
      {
        label: "Consider this...",
        body: "What if the derivative is suddenly exactly zero? The car has reached the absolute summit of the mountain. For one microscopic millisecond, the road is perfectly flat before the heavy car gracefully coasts down the other side."
      }
    ],
    summary: "When you \"derive\" a function, you are not doing complex algebra. You are smoothly peeling away the car's physical position, and instantly looking straight at its engine's raw speed. Differentiation is just measuring the angle of a changing hill."
  },
  {
    id: "the-integral",
    chapterNumber: 4,
    chapterTitle: "The Accumulation of Time (Integrals)",
    title: "The Integral ($\\int f(x) dx$)",
    hook: "Imagine slowly guiding a brightly colored paint roller across a floor over an entire hour, tracking exactly how much space it successfully covered.",
    explain: "While a derivative is a frozen radar gun, an integral is a patient, gathering collector. It sweeps up all the tiny, individual frozen moments of speed over time, stacking them painstakingly side-by-side like thin floor tiles until they merge cleanly into one massive, completely solid surface of 2D area.",
    image: {
      path: "images/level2-integral.png",
      prompt: "A heavy paint roller actively spreading a thick band of blue paint across a wide floor, slowly accumulating and coloring a massive, solid 2D square area. Clean geometric vector style, white background."
    },
    aha: "Integrals are just a giant, patient broom sweeping up a million frozen moments and gluing them together densely into solid geometric space.",
    proseSegments: [
      {
        label: "Consider this...",
        body: "What if the car completely reverses into negative speed? The paint roller physically pulls the paint back off the floor, perfectly erasing the area it just confidently created. You are smoothly accumulating negative space."
      }
    ],
    summary: "Calculus has only two master tools: The Derivative (slicing time cleanly to find speed) and The Integral (gluing speed together securely to build solid space). They are the exact, perfectly balanced physical opposites of each other."
  },
  {
    id: "sine-and-cosine",
    chapterNumber: 5,
    chapterTitle: "The Geometry of Waves",
    title: "Sine & Cosine (The Endless Engine)",
    hook: "Imagine tying a glowing pendulum to an endless conveyor belt. As the pendulum naturally swings side to side, it paints a perfect, smoothly repeating ocean wave.",
    explain: "Trigonometry isn't just about static triangles. It is the language of breathing, swinging, and heavy engines constantly rotating. Sine effortlessly traces the height of the spin; Cosine flawlessly traces the width.",
    image: {
      path: "images/level2-sine.png",
      prompt: "A spinning mechanical gear firmly attached to a rod that continuously draws a smooth, repeating blue wave on a vast, unrolling sheet of white paper. Flat mechanical vector style, white background."
    },
    aha: "Sine waves are just perfectly symmetrically circular rotations stretched cleanly across time.",
    proseSegments: [
      {
        label: "In Short",
        body: "If you spin the gear faster, the wave violently compresses, safely squeezing the peaks tightly together into a high-frequency hum. They are the fundamental blueprints for all cycles in the universe."
      }
    ],
    summary: "They are the fundamental blueprints for all cycles in the universe."
  },
  {
    id: "the-chain-rule",
    chapterNumber: 6,
    chapterTitle: "Advanced Calculus Maneuvers",
    title: "The Chain Rule (Machines Inside Machines)",
    hook: "Imagine a massive gear turning a smaller gear, which ultimately perfectly spins a tiny radar dish.",
    explain: "When an equation is trapped securely inside another equation ($f(g(x))$), their speeds stack. The Chain Rule patiently forces you to crack the heavy outer shell first before diagnosing the delicate inner movement.",
    image: {
      path: "images/level2-chain-rule.png",
      prompt: "A Russian nesting doll sliced surgically open, cleanly revealing smaller identical solid dolls locked perfectly inside. Minimalistic vector style, white background."
    },
    aha: "The Chain Rule is just gently peeling an onion layer by layer to unlock the true compounded speed.",
    proseSegments: [
      {
        label: "In Short",
        body: "If the massive outer gear stops, the inner gear physically cannot move. The derivative cleanly hits zero. Never panic when machines combine; just multiply their individual speeds together from the outside down to the absolute core."
      }
    ],
    summary: "Never panic when machines combine; just multiply their individual speeds together from the outside down to the absolute core."
  },
  {
    id: "optimization",
    chapterNumber: 6,
    chapterTitle: "Advanced Calculus Maneuvers",
    title: "Optimization (Hunting the Summits)",
    hook: "Imagine a drone sweeping gently over a massive mountain range, programmed to instantly lock onto the single highest physical peak of rock.",
    explain: "Since the derivative (speed) is exactly zero exactly at the beautifully flat top of a hill, we can legally force the engine to hunt for zeroes to instantly find the absolute maximum profit or minimum cost in any complex system.",
    image: {
      path: "images/level2-optimization.png",
      prompt: "A drone hovering over a 2D mountain graph, confidently dropping a glowing red flag squarely on the absolute highest rounded peak. Action vector style, white background."
    },
    aha: "Optimization is just smoothly forcing the derivative to equal zero to forcefully mathematically reveal the peak.",
    proseSegments: [
      {
        label: "In Short",
        body: "Optimization is the primary reason engineers actually use Calculus in reality. It is the ultimate digital compass for discovering absolute structural perfection."
      }
    ],
    summary: "Optimization is the ultimate digital compass for discovering absolute structural perfection."
  },
  {
    id: "sequences-and-series",
    chapterNumber: 7,
    chapterTitle: "The Deep Patterns",
    title: "Sequences & Series",
    hook: "Imagine building a massive staircase where every single new wooden step you place is exactly half the size of the previous step.",
    explain: "A sequence is just the predictable list of the steps ($1, 0.5, 0.25...$). A series is the heavy act of physically collecting and gluing them all securely together to measure the total total height.",
    image: {
      path: "images/level2-series.png",
      prompt: "A beautiful staircase built of solid blocks where every step ascending upward is perfectly exactly half the height of the one before it, safely approaching a visible ceiling line. Clean geometric vector style, white background."
    },
    aha: "Sequences are just cleanly organizing the raw materials; Series are the act of physically stacking them into a final tower.",
    proseSegments: [
      {
        label: "In Short",
        body: "Because the steps shrink infinitely smaller, the tower never forcefully breaks through the ceiling. Infinite series can gracefully add up to a perfectly safe, finite shape."
      }
    ],
    summary: "Infinite series can gracefully add up to a perfectly safe, finite shape."
  },
  {
    id: "logarithms",
    chapterNumber: 7,
    chapterTitle: "The Deep Patterns",
    title: "Logarithms",
    hook: "Imagine cleanly folding a giant piece of paper in half over and over until it is thick enough to easily touch the moon.",
    explain: "Exponents ask: \"How tall is the paper after 40 heavy folds?\" Logarithms calmly ask the exact reverse: \"How many physical folds does it take to finally hit the moon?\"",
    image: {
      path: "images/level2-logarithm.png",
      prompt: "A giant sheet of paper being folded repeatedly, with a glowing counter tracking the exact total number of tight physical folds smoothly executed. Minimalistic vector style, white background."
    },
    aha: "Logarithms do not measure massive sizes; they only measure the slow, ticking number of engine cycles required to reach that size.",
    proseSegments: [
      {
        label: "In Short",
        body: "Logarithms are the ultimate mathematical brake pedal. They take astronomical, violently large numbers and safely compress them beautifully down into incredibly small, manageable steps."
      }
    ],
    summary: "Logarithms take astronomical, violently large numbers and safely compress them beautifully down into incredibly small, manageable steps."
  },
  {
    id: "complex-numbers",
    chapterNumber: 7,
    chapterTitle: "The Deep Patterns",
    title: "Complex Numbers ($i$)",
    hook: "Imagine a car driving perfectly straight across a 1D line, but then magically rotating 90 degrees outward into a brand new, invisible sideways dimension.",
    explain: "Real numbers sit plainly on a flat map. The imaginary number ($i = \\sqrt{-1}$) isn't fake at all. It is simply a rigid geometric command telling the engine to rotate the shape exactly 90 degrees off the paper into the deep 2D complex plane.",
    image: {
      path: "images/level2-complex.png",
      prompt: "A straight horizontal line smoothly spawning a bright perpendicular vertical axis, lifting a geometric point safely off the flat path straight into the new empty sky. Dynamic vector style, white background."
    },
    aha: "Imaginary numbers are just the universe stepping firmly sideways to discover a massive hidden dimension of rotation.",
    proseSegments: [
      {
        label: "In Short",
        body: "Without complex numbers, engines like quantum mechanics and electrical engineering would violently crash. They provide the invisible rotational depth required to make waves function correctly."
      }
    ],
    summary: "They provide the invisible rotational depth required to make waves function correctly."
  }
];
