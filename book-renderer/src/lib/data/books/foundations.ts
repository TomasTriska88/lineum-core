import type { Concept } from '../concepts';

export const level1Concepts: Concept[] = [
  {
    "id": "addition",
    "chapterNumber": 1,
    "chapterTitle": "The Flow of Numbers (Basic Intuition)",
    "title": "Addition ($+$)",
    "hook": "Imagine two small pools of water merging on a flat surface.",
    "explain": "Addition is the act of bringing pieces together. The water combines into a single, deeper pool.",
    "image": {
      "path": "images/level1-addition.png",
      "prompt": "Two streams of blue water merging into a single larger puddle. Flat vector style, white background."
    },
    "aha": "Positive numbers add size without creating conflict.",
    "summary": "Addition adds pieces into the exact same space to build a larger shape.",
    "proseSegments": [
      {
        "label": "What it is.",
        "body": "Addition calculates the total amount of two separate groups."
      },
      {
        "label": "How to solve.",
        "body": "Line up the numbers vertically by place value. Add the columns from right to left. If a column totals more than 9, carry the extra 1 over to the next column."
      },
      {
        "label": "Why it works.",
        "body": "When you add positive numbers, you extend a straight line in one direction. The shape grows longer."
      }
    ]
  },
  {
    "id": "subtraction",
    "chapterNumber": 1,
    "chapterTitle": "The Flow of Numbers (Basic Intuition)",
    "title": "Subtraction ($-$)",
    "hook": "Imagine rowing a boat upstream and hitting a fast river current.",
    "explain": "A minus sign fights your progress. You move forward, but the current pushes you backward.",
    "image": {
      "path": "images/level1-subtraction.png",
      "prompt": "A yellow boat pushing forward, while a red water current pushes it backward. Flat vector style, white background."
    },
    "aha": "A minus sign pushes backward against your forward movement.",
    "summary": "Subtracting measures opposing numbers. You calculate if your forward movement is bigger than the backward push.",
    "proseSegments": [
      {
        "label": "What it is.",
        "body": "Subtraction calculates the difference between two numbers. It determines what remains after pieces are removed."
      },
      {
        "label": "How to solve.",
        "body": "Line the numbers up vertically. Subtract the bottom digit from the top. If the top digit is smaller, borrow 1 from the next column before subtracting."
      },
      {
        "label": "Why it works.",
        "body": "Subtraction shrinks the original shape. When you apply a minus, the shape slides backward along the grid, making it shorter."
      }
    ]
  },
  {
    "id": "negativenumbersstandalone",
    "chapterNumber": 1,
    "chapterTitle": "The Flow of Numbers (Basic Intuition)",
    "title": "Negative Numbers (Standalone)",
    "hook": "Imagine a flat landscape. Positive numbers build towers upwards. Negative numbers dig holes downward.",
    "explain": "A negative number represents debt or depth.",
    "image": {
      "path": "images/level1-negative-numbers.png",
      "prompt": "A flat ground line with a red hole dug into the earth, placed directly next to a blue rising tower. Minimalistic vector style, white background."
    },
    "aha": "Negative numbers extend the world downward below zero.",
    "summary": "Removing a hole means filling it. Two negatives flip to form a positive block.",
    "proseSegments": [
      {
        "label": "What it is.",
        "body": "A negative number is any value less than zero. It is the exact opposite of a positive amount."
      },
      {
        "label": "How to solve.",
        "body": "To subtract a negative number, like $5 - (-3)$, change the double minus into a plus. The equation becomes $5 + 3 = 8$."
      },
      {
        "label": "Why it works.",
        "body": "Removing a deep hole is the exact geometric equivalent of filling it with dirt. The double negative flips a downward hole into an upward block."
      }
    ]
  },
  {
    "id": "absolutevalue5",
    "chapterNumber": 1,
    "chapterTitle": "The Flow of Numbers (Basic Intuition)",
    "title": "Absolute Value ($|-5|$)",
    "hook": "Imagine driving a car. Driving five miles forward consumes fuel. Driving five miles in reverse consumes the same fuel.",
    "explain": "Absolute value ignores whether you traveled forward or backward. It focuses exclusively on the total distance.",
    "image": {
      "path": "images/level1-absolute-value.png",
      "prompt": "Two cars parked side by side facing opposite directions. Both leave a yellow trail exactly 5 blocks long. Flat vector style, white background."
    },
    "aha": "Absolute value is the total distance traveled, ignoring direction entirely.",
    "summary": "Absolute value removes minus signs and reports the raw size of the number.",
    "proseSegments": [
      {
        "label": "What it is.",
        "body": "Absolute value calculates the strict distance a number sits from zero."
      },
      {
        "label": "How to solve.",
        "body": "Look at the number inside the parallel bars $|-5|$. Remove the negative sign. The result is always positive or zero. $|-5|$ becomes 5."
      },
      {
        "label": "Why it works.",
        "body": "The parallel bars act as a geometric filter. They remove direction from the grid and force the object to report its total size."
      }
    ]
  },
  {
    "id": "multiplyingvariablesxcdotx",
    "chapterNumber": 2,
    "chapterTitle": "Weaving Surfaces (Multiplication & Division)",
    "title": "Multiplying Variables ($x \\cdot x$)",
    "hook": "Imagine weaving horizontal blue threads crosswise with vertical red threads.",
    "explain": "When you multiply a variable by another variable, you weave them together. You take lines and lock them into a flat 2D surface ($x^2$).",
    "image": {
      "path": "images/level1-multiplying-variables.png",
      "prompt": "Horizontal blue strings and vertical red strings locking tightly crosswise to create a flat 2D square. Flat vector style, white background."
    },
    "aha": "Multiplying variables weaves lines into solid flat shapes.",
    "summary": "Multiplying variables creates shapes. Variables like $x^2$ act as physical objects, not abstract letters.",
    "proseSegments": [
      {
        "label": "What it is.",
        "body": "Multiplying letters builds a new term with a higher exponent."
      },
      {
        "label": "How to solve.",
        "body": "Count the number of identical letters being multiplied. Write that number as a small exponent at the top right. For $x \\cdot x$, write $x^2$."
      },
      {
        "label": "Why it works.",
        "body": "A single $x$ is a flat line. Mutiplying it by another $x$ stretches that line sideways to make a square. Multiplying a third time stretches the square upward to form a 3D box."
      }
    ]
  },
  {
    "id": "multiplyingbynumbers5cdotx",
    "chapterNumber": 2,
    "chapterTitle": "Weaving Surfaces (Multiplication & Division)",
    "title": "Multiplying by Numbers ($5 \\cdot x$)",
    "hook": "Imagine turning the volume dial on a speaker.",
    "explain": "Standard numbers act as amplifiers. Multiplying a glowing wire by 5 makes it glow 5 times brighter. The shape of the wire stays identical.",
    "image": {
      "path": "images/level1-multiplying-numbers.png",
      "prompt": "A single straight line glowing intensely next to an analog volume dial. Minimalistic vector style, white background."
    },
    "aha": "Numbers act as amplifiers, scaling the amount without altering the shape.",
    "summary": "Multiplying by a number ($5x$) scales the amount, while multiplying the variables ($x^2$) builds a completely new shape.",
    "proseSegments": [
      {
        "label": "What it is.",
        "body": "Multiplying a variable by a raw number increases the quantity of that item."
      },
      {
        "label": "How to solve.",
        "body": "When you add $2x + 3x$, you add the numbers together to get $5x$. You never change the exponent."
      },
      {
        "label": "Why it works.",
        "body": "You are placing five individual wires side-by-side ($5x$). Because they never cross, they cannot weave into a square. The shape stays flat."
      }
    ]
  },
  {
    "id": "divisiondiv",
    "chapterNumber": 2,
    "chapterTitle": "Weaving Surfaces (Multiplication & Division)",
    "title": "Division ($\\div$)",
    "hook": "Imagine breaking a large chocolate bar into equal smaller squares.",
    "explain": "The top number is the total size. The bottom number is how many pieces you must break it into.",
    "image": {
      "path": "images/level1-division.png",
      "prompt": "A large blue square actively splitting cleanly into four identical smaller squares. Flat vector style, white background."
    },
    "aha": "Division separates a total amount into identical pieces.",
    "summary": "Division cracks a big shape perfectly into smaller, identical pieces.",
    "proseSegments": [
      {
        "label": "What it is.",
        "body": "Division splits a total amount into equal groups to see how much goes into each piece."
      },
      {
        "label": "How to solve.",
        "body": "To solve $20 \\div 4$, ask yourself what number multiplied by 4 equals 20. The answer is 5."
      },
      {
        "label": "Why it works.",
        "body": "Division breaks a large block into a grid of smaller exact squares. The starting shape is cut into equal pieces."
      }
    ]
  },
  {
    "id": "exponentsx2x3",
    "chapterNumber": 3,
    "chapterTitle": "Mastering the Dimensions (Exponents & Roots)",
    "title": "Exponents ($x^2, x^3$)",
    "hook": "Imagine a thin wooden rod inflating sideways to become a solid flat table.",
    "explain": "Squaring an object ($x^2$) pulls a 1D line into a 2D plane. Cubing it ($x^3$) raises that plane vertically into a 3D box.",
    "image": {
      "path": "images/level1-exponents.png",
      "prompt": "A thin line inflating outward horizontally to form a solid flat square. Minimalistic vector style, white background."
    },
    "aha": "Exponents scale objects upward into entirely new dimensions of space.",
    "summary": "Exponents stretch shapes from lines, to squares, to boxes.",
    "proseSegments": [
      {
        "label": "What it is.",
        "body": "An exponent tells you how many times to multiply the base number by itself."
      },
      {
        "label": "How to solve.",
        "body": "To solve $4^3$, you multiply $4 \\times 4 \\times 4$. The first pair equals 16. Then multiply $16 \\times 4$ to get 64."
      },
      {
        "label": "Why it works.",
        "body": "Exponents stretch shapes. You drag a line into a square, and pull that square upwards into a box."
      }
    ]
  },
  {
    "id": "squarerootssqrtx",
    "chapterNumber": 3,
    "chapterTitle": "Mastering the Dimensions (Exponents & Roots)",
    "title": "Square Roots ($\\sqrt{x}$)",
    "hook": "Imagine an industrial press flattening a solid box back down to the floor.",
    "explain": "Roots reverse shape expansion. A square root compresses a 2D square firmly back down into a 1D line.",
    "image": {
      "path": "images/level1-square-roots.png",
      "prompt": "A heavy iron plate crushing a 2D square strictly down into a 1D straight line. Flat industrial vector style, white background."
    },
    "aha": "Roots compress shapes down into lower dimensions.",
    "summary": "While exponents inflate shapes, roots compress them flat.",
    "proseSegments": [
      {
        "label": "What it is.",
        "body": "A square root asks what original base number was multiplied by itself to produce the current value."
      },
      {
        "label": "How to solve.",
        "body": "To find $\\sqrt{25}$, find the number that equals 25 when multiplied by itself. Because $5 \\times 5 = 25$, the answer is 5."
      },
      {
        "label": "Why it works.",
        "body": "A root presses a shape flat downward. It finds the exact length of one side of a square and discards the rest of the shape."
      }
    ]
  },
  {
    "id": "scientificnotationatimes10b",
    "chapterNumber": 3,
    "chapterTitle": "Mastering the Dimensions (Exponents & Roots)",
    "title": "Scientific Notation ($a \\times 10^b$)",
    "hook": "Imagine packing a massive banner into a highly compressed zip file.",
    "explain": "Writing out 300,000,000 is inefficient. Scientific notation packages all the trailing zeros into a compact format ($3 \\times 10^8$).",
    "image": {
      "path": "images/level1-scientific-notation.png",
      "prompt": "A massive line of zeroes zip-compressing into a tiny capsule labeled '10^x'. Clean vector style, white background."
    },
    "aha": "Scientific notation acts as simple data packing for massive numbers of zeros.",
    "summary": "Scientific notation manages massive sizes cleanly without wasting space.",
    "proseSegments": [
      {
        "label": "What it is.",
        "body": "It is a shorthand method for writing extremely large or extremely tiny numbers."
      },
      {
        "label": "How to solve.",
        "body": "Count the jumps from the original decimal point to the new location behind the first digit. Write that jump count as the exponent. $4,500,000$ becomes $4.5 \\times 10^6$."
      },
      {
        "label": "Why it works.",
        "body": "Instead of drawing a long flat line, you fold the distance onto itself into a small package that keeps the total length."
      }
    ]
  },
  {
    "id": "balancingequations2x410",
    "chapterNumber": 4,
    "chapterTitle": "The Scale and The Map (Equations & Geometry)",
    "title": "Balancing Equations ($2x + 4 = 10$)",
    "hook": "Imagine a brass scale delicately hovering in perfect balance.",
    "explain": "If you remove a weight from the left side, the scale tilts. To fix it, you must remove the exact same amount from the right.",
    "image": {
      "path": "images/level1-balancing-equations.png",
      "prompt": "A balance scale. The left plate shows a heavy block being removed, causing the right plate to dip downward. Flat vector style, white background."
    },
    "aha": "Equations require you to adjust both sides identically to maintain physical balance.",
    "summary": "You strip weights from both sides equally to expose the hidden value.",
    "proseSegments": [
      {
        "label": "What it is.",
        "body": "An equation states that the left side and the right side are exactly equal, even if they look different."
      },
      {
        "label": "How to solve.",
        "body": "Isolate the unknown letter. If the equation is $2x + 4 = 10$, subtract 4 from both sides to get $2x = 6$. Then divide both sides by 2 to find that $x = 3$."
      },
      {
        "label": "Why it works.",
        "body": "A balanced shape must stay balanced. If you cut a block off the left side of a flat scale, you must cut the exact same block off the right side to keep it flat."
      }
    ]
  },
  {
    "id": "linearlinesymxb",
    "chapterNumber": 4,
    "chapterTitle": "The Scale and The Map (Equations & Geometry)",
    "title": "Linear Lines ($y = mx + b$)",
    "hook": "Imagine aiming a laser pointer into the night sky from a specific step on a ladder.",
    "explain": "The constant '$b$' is the exact step on the ladder where the laser starts. The slope '$m$' is the angle of the beam pointing upward.",
    "image": {
      "path": "images/level1-linear-lines.png",
      "prompt": "A red laser beam originating from a blue dot on the Y-axis wall, angling upward across a minimal grid. Flat vector style, white background."
    },
    "aha": "A linear equation is the blueprint for a straight line.",
    "summary": "Linear lines establish a starting height, set an angle, and travel straight forever.",
    "proseSegments": [
      {
        "label": "What it is.",
        "body": "It is the standard equation used to draw straight lines predictably on a graph."
      },
      {
        "label": "How to solve.",
        "body": "Mark your starting point on the vertical Y-axis using '$b$'. Look at the slope '$m$' as a fraction. Move up the 'rise' number, and right the 'run' number to plot your next dot."
      },
      {
        "label": "Why it works.",
        "body": "The line climbs perfectly without bending, creating identical triangles at every step."
      }
    ]
  },
  {
    "id": "percentages",
    "chapterNumber": 4,
    "chapterTitle": "The Scale and The Map (Equations & Geometry)",
    "title": "Percentages ($\\%$)",
    "hook": "Imagine a transparent grid that slices any shape directly into exactly 100 equal sections.",
    "explain": "Percentages force different objects into the exact same 100-piece scale. \"50%\" indicates you select exactly half of those available sections.",
    "image": {
      "path": "images/level1-percentages.png",
      "prompt": "A large circle and a tiny circle covered by an identical transparent grid composed of exactly 100 squares. Minimalistic vector style, white background."
    },
    "aha": "Percentages force completely different shapes into a universal 100-piece scale.",
    "summary": "Percentages allow completely different sizes to share the exact same 100-piece grid.",
    "proseSegments": [
      {
        "label": "What it is.",
        "body": "A percentage is a ratio that compares a number specifically out of a set of 100."
      },
      {
        "label": "How to solve.",
        "body": "To find 30% of a number, convert the percentage into a decimal by moving the dot two places left ($0.30$). Then multiply the original number by $0.30$."
      },
      {
        "label": "Why it works.",
        "body": "You put a universal mask over random shapes. By chopping every object into 100 identical pieces, comparing sizes becomes easy."
      }
    ]
  },
  {
    "id": "percentageincreasedecrease",
    "chapterNumber": 4,
    "chapterTitle": "The Scale and The Map (Equations & Geometry)",
    "title": "Percentage Increase/Decrease",
    "hook": "Imagine a grid of 100 blocks expanding outward to add 20 new edge pieces.",
    "explain": "Applying a 20% increase tells the system to attach 20 fresh blocks directly to the rim of the original shape.",
    "image": {
      "path": "images/level1-percentage-increase.png",
      "prompt": "A 100-unit square grid inflating outward, gaining 20 new external grid pixels snapping onto the rim. Minimalistic vector style, white background."
    },
    "aha": "Percentage increases add calculated modular blocks directly onto an existing structure.",
    "summary": "You dynamically scale the object based on how many extra 100-scale blocks fall away or attach.",
    "proseSegments": [
      {
        "label": "What it is.",
        "body": "It calculates the exact amount a value grows or shrinks relative to its initial size."
      },
      {
        "label": "How to solve.",
        "body": "To increase 50 by 20%, multiply $50 \\times 1.20$. The '1' keeps the original value intact, while the '.20' calculates the brand new addition. The answer is 60."
      },
      {
        "label": "Why it works.",
        "body": "Expansion snaps pieces directly onto the outside border. The shape widens evenly."
      }
    ]
  },
  {
    "id": "thecoordinatesgridxandy",
    "chapterNumber": 4,
    "chapterTitle": "The Scale and The Map (Equations & Geometry)",
    "title": "The Coordinates Grid ($X$ and $Y$)",
    "hook": "Imagine walking through a city block grid using exact directions.",
    "explain": "To find a location, you determine a starting point, walk a precise number of units right (the $X$ axis), turn 90 degrees, and walk forward (the $Y$ axis).",
    "image": {
      "path": "images/level1-coordinates.png",
      "prompt": "A floor grid made of square tiles. A bright red target dot rests on a crossing. Arrows trace the path along the bottom edge, then straight upward to the dot. Flat vector style, white background."
    },
    "aha": "The coordinate system is a rigid map locating points perfectly.",
    "summary": "Coordinates act as an irrefutable GPS map pinning geometry perfectly down.",
    "proseSegments": [
      {
        "label": "What it is.",
        "body": "It is a 2D mapping system that uses a horizontal and vertical number line to pinpoint locations."
      },
      {
        "label": "How to solve.",
        "body": "Plot the point $(3, -4)$. Start at the absolute center $(0,0)$. Move 3 units right on the X-axis. Move 4 units down on the Y-axis. Place your dot."
      },
      {
        "label": "Why it works.",
        "body": "Coordinates pin shapes onto a flat floor. The grid stops a point from drifting away completely."
      }
    ]
  },
{
    "id": "fractions",
    "layer": "core",
    "chapterNumber": 4,
    "chapterTitle": "The Scale and The Map (Equations & Geometry)",
    "title": "Fractions",
    "hook": "Imagine a solid brick shattered into exactly identical pieces.",
    "explain": "A fraction records how many pieces exist (top) compared to how many pieces make a whole brick (bottom).",
    "image": {
      "path": "images/level1-fractions.png",
      "prompt": "A solid rectangular brick alongside another identical brick broken into exactly three perfect slices. Clean minimalist vector."
    },
    "aha": "Fractions aren't incomplete numbers; they are perfectly rigid geometry locked into grids.",
    "summary": "Fractions establish rigorous part-to-whole relationships mapped over universally locked structural grids.",
    "proseSegments": [
      {
        "label": "What it is.",
        "body": "A ratio comparing a part of an object strictly against its absolute whole."
      },
      {
        "label": "How to solve.",
        "body": "To add or subtract, you must force the bottom numbers (the structural grid) to be identical first. To multiply, just multiply straight across to create a completely new grid."
      },
      {
        "label": "Why it works.",
        "body": "You cannot add a slice of a 3-part grid to a slice of a 4-part grid directly. You must subdivide both into a universal 12-part grid before combining them physically."
      }
    ]
  },
  {
    "id": "ratios-proportions",
    "layer": "core",
    "chapterNumber": 4,
    "chapterTitle": "The Scale and The Map (Equations & Geometry)",
    "title": "Ratios & Proportions",
    "hook": "Imagine mixing exactly two cups of blue paint with three cups of yellow to make green.",
    "explain": "A ratio locks two separate objects into a permanent relationship. If one scales up, the other must scale up identically to maintain the structure.",
    "image": {
      "path": "images/level1-ratios.png",
      "prompt": "Two blue blocks locked to three yellow blocks, scaling up to four blue blocks and six yellow blocks. Abstract vector style."
    },
    "aha": "Proportions operate like physical gears; turning one forces the other to turn in lockstep.",
    "summary": "Proportions lock independent objects together so they dynamically expand or shrink in absolute structural harmony.",
    "proseSegments": [
      {
        "label": "What it is.",
        "body": "A mathematical gear connecting two completely different units together permanently."
      },
      {
        "label": "How to solve.",
        "body": "Set two fractions equal to each other. Cross-multiply the diagonals to form a straight equation, then solve for the missing piece."
      },
      {
        "label": "Why it works.",
        "body": "Cross-multiplication acts as a geometric pivot, balancing the missing mass across the center of the equation."
      }
    ]
  },
  {
    "id": "inequalities",
    "layer": "core",
    "chapterNumber": 4,
    "chapterTitle": "The Scale and The Map (Equations & Geometry)",
    "title": "Inequalities ($<$, $>$)",
    "hook": "Imagine measuring the minimum height required to ride a roller coaster.",
    "explain": "An equation demands exact equality. An inequality establishes a strict boundary line where an infinite amount of valid answers extend endlessly in one direction.",
    "image": {
      "path": "images/level1-inequalities.png",
      "prompt": "A solid line drawn on a grid, with a massive glowing area shaded strictly below it. Conceptual abstract vector."
    },
    "aha": "An inequality doesn't point to a single dot; it highlights an entire infinite territory.",
    "summary": "Inequalities map entire infinite oceans of acceptable values rather than highlighting a single isolated geometric dot.",
    "proseSegments": [
      {
        "label": "What it is.",
        "body": "A mathematical statement dictating that one side must strictly remain physically larger or smaller than the other."
      },
      {
        "label": "How to solve.",
        "body": "Solve exactly like a standard equation. However, if you multiply or divide by a negative number, you must physically flip the inequality symbol."
      },
      {
        "label": "Why it works.",
        "body": "Multiplying by a negative physically flips the geometry across the zero-axis perfectly into a mirror dimension, reversing the territory completely."
      }
    ]
  },
  {
    "id": "basic-geometry",
    "layer": "core",
    "chapterNumber": 4,
    "chapterTitle": "The Scale and The Map (Equations & Geometry)",
    "title": "Geometry (Area, Perimeter, Volume)",
    "hook": "Imagine tracing a fence around a yard, laying sod on the grass, and filling a pool with water.",
    "explain": "Perimeter is the 1D line wrapping the object. Area is the flat 2D surface. Volume is the 3D space contained inside.",
    "image": {
      "path": "images/level1-basic-geometry.png",
      "prompt": "A glowing wireframe box. The edges are red, one flat face is blue, and the hollow interior glows yellow. Abstract conceptual vector."
    },
    "aha": "Geometry calculates precise mass across progressing dimensions.",
    "summary": "Basic geometry provides the exact spatial capacity scaling entirely from 1D outlines to 3D physical containment.",
    "proseSegments": [
      {
        "label": "What it is.",
        "body": "The rigid measurement of physical boundary lines, flat spans, and 3D containment."
      },
      {
        "label": "How to solve.",
        "body": "Perimeter: add the edges. Area: multiply base length by height. Volume: multiply the flat area by the deep dimension."
      },
      {
        "label": "Why it works.",
        "body": "You drag a 1D line to weave a 2D mat, and stack 2D mats upward to construct a solid 3D box."
      }
    ]
  },
  {
    "id": "intro-functions",
    "layer": "core",
    "chapterNumber": 4,
    "chapterTitle": "The Scale and The Map (Equations & Geometry)",
    "title": "Intro to Functions ($f(x)$)",
    "hook": "Imagine dropping a raw block of wood into a carving machine.",
    "explain": "A function is a perfect industrial machine. You drop one raw number in ($x$), it performs an action, and it drops exactly one finished product out the other side ($y$).",
    "image": {
      "path": "images/level1-intro-functions.png",
      "prompt": "A mechanical conveyor belt feeding generic blocks into a glowing machine, producing perfectly carved spheres. Industrial abstract vector."
    },
    "aha": "A function guarantees absolute predictability: one physical input produces exactly one physical output.",
    "summary": "Functions act as perfectly reliable input-output pathways, ensuring every starting point maps cleanly to exactly one destination.",
    "proseSegments": [
      {
        "label": "What it is.",
        "body": "A rigid geometric rule mapping every individual dot from an origin set to a destination set."
      },
      {
        "label": "How to solve.",
        "body": "Replace the $x$ inside the parenthesis with your input number, execute the math stated, and record the final value acting as the output."
      },
      {
        "label": "Why it works.",
        "body": "The graph of a function creates an unbroken curve spanning from left to right, preventing a single input from fracturing into two erratic outputs."
      }
    ]
  },
  {
  "id": "primenumbers-basic",
  "layer": "enrichment",
  "chapterNumber": 5,
  "chapterTitle": "Enrichment: Intrinsic Patterns",
  "title": "Prime Numbers (The Atoms)",
  "hook": "Imagine an indivisible crystal block that refuses to shatter into smaller perfect squares.",
  "explain": "Prime numbers construct the foundation of all other numbers. Every number is either a prime or built exclusively by multiplying primes together.",
  "image": {
    "path": "images/enrichment-primes.png",
    "prompt": "A single solid glowing crystal block alongside a shattered block. Abstract dark conceptual vector style."
  },
  "aha": "Primes are the elemental atoms that weave all other mathematical quantities.",
  "summary": "Because primes cannot be divided evenly, they act as the base structural material for the entire number line.",
  "proseSegments": [
    {
      "label": "What it is.",
      "body": "A prime number can solely be divided by itself and 1. Examples include 2, 3, 5, 7, and 11."
    },
    {
      "label": "How to explore",
      "body": "Attempt to arrange a prime number of physical blocks into a perfect 2D grid. You will always be forced to leave them in a single 1D line."
    },
    {
      "label": "Why it works.",
      "body": "Geometrically, primes refuse to fold into secondary dimensions evenly. The lack of divisors gives them immense structural strength, which modern cryptography relies upon absolutely."
    }
  ]
},
{
  "id": "fibonacci-basic",
  "layer": "enrichment",
  "chapterNumber": 5,
  "chapterTitle": "Enrichment: Intrinsic Patterns",
  "title": "The Fibonacci Sequence",
  "hook": "Imagine a spiral seashell expanding its chambers by continuously adding its two previous structural walls.",
  "explain": "The sequence generates numbers by adding the two previous numbers together: 1, 1, 2, 3, 5, 8. It serves as nature's native algorithm for biological scaling.",
  "image": {
    "path": "images/enrichment-fibonacci.png",
    "prompt": "A geometric spiral seashell overlaid with ascending square boxes mapping the golden spiral. Abstract deep conceptual vector style."
  },
  "aha": "The sequence is memory-driven; the future always directly inherits the sum of its past.",
  "summary": "By constantly adding the immediate past, the sequence creates a perfectly proportional scaling factor found across tree branches and spiral galaxies.",
  "proseSegments": [
    {
      "label": "What it is.",
      "body": "An unbroken chain of numbers where every new tier is precisely the sum of the two tiers directly beneath it."
    },
    {
      "label": "Why it works.",
      "body": "Geometrically, if you build squares matching these values, they pack perfectly into a tightening spiral. Nature optimizes physical space by growing through this exact additive ratio."
    }
  ]
},
{
  "id": "goldenratio-basic",
  "layer": "enrichment",
  "chapterNumber": 5,
  "chapterTitle": "Enrichment: Intrinsic Patterns",
  "title": "The Golden Ratio ($\\phi$)",
  "hook": "Imagine cutting a wooden plank so that the ratio of the long half relates to the short half perfectly identically as the whole plank relates to the long half.",
  "explain": "The Golden Ratio ($1 : 1.618$) is the universal constant of harmonious asymmetry. It balances structure between monotonous symmetry and chaotic randomness.",
  "image": {
    "path": "images/enrichment-golden-ratio.png",
    "prompt": "A glowing rectangle sliced into the golden proportion, overlaying ancient architectural columns. Deep abstract minimalist vector."
  },
  "aha": "The Golden Ratio is the mathematical blueprint for aesthetic stability in the physical world.",
  "summary": "This specific ratio allows physical and visual elements to scale infinitely while preserving identical internal harmony.",
  "proseSegments": [
    {
      "label": "What it is.",
      "body": "A specific geometric proportion, approximately 1.618, heavily observed in art, architecture, and biological leaf arrangements."
    },
    {
      "label": "Why it works.",
      "body": "It represents the absolute limit where proportion becomes self-similar. Splitting a space by the Golden Ratio ensures the visual weight of light and structure never collapses."
    }
  ]
}
];
