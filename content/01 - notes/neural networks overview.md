---
tags:
  - permanent
  - compsci
  - publish
created: 2024-11-21T21:37
modified: 2024-12-02T05:19
---
Neural networks are computational models inspired by the human brain's network of neurons. By analyzing data, they learn patterns and relationships to make decisions or predictions.

```tikz
\usepackage{tikz}

\begin{document}

\begin{tikzpicture}
  % Define layer sizes
  \def\inputsize{3}
  \def\hiddensize{4}
  \def\outputsize{2}
  
  % Define node styles
  \tikzstyle{neuron}=[circle, draw=black, fill=white, minimum size=16pt, inner sep=0pt]
  \tikzstyle{input neuron}=[neuron, fill=blue!20]
  \tikzstyle{hidden neuron}=[neuron, fill=green!20]
  \tikzstyle{output neuron}=[neuron, fill=red!20]
  \tikzstyle{annot} = [text width=4em, text centered]

  % Draw input layer nodes
  \foreach \i in {1,...,\inputsize} {
    \node[input neuron] (I-\i) at (0,-\i) {};
  }

  % Draw hidden layer nodes
  \foreach \i in {1,...,\hiddensize} {
    \node[hidden neuron] (H-\i) at (2,-\i+0.5) {};
  }

  % Draw output layer nodes
  \foreach \i in {1,...,\outputsize} {
    \node[output neuron] (O-\i) at (4,-\i-0.5) {};
  }

  % Connect input layer to hidden layer
  \foreach \i in {1,...,\inputsize} {
    \foreach \j in {1,...,\hiddensize} {
      \draw[-] (I-\i) -- (H-\j);
    }
  }

  % Connect hidden layer to output layer
  \foreach \i in {1,...,\hiddensize} {
    \foreach \j in {1,...,\outputsize} {
      \draw[-] (H-\i) -- (O-\j);
    }
  }

  % Annotations
  \node[annot, above of=I-1, node distance=1cm] {Input Layer};
  \node[annot, above of=H-1, node distance=1cm] {Hidden Layer};
  \node[annot, above of=O-1, node distance=1cm] {Output Layer};

\end{tikzpicture}

\end{document}
```

## Components of a neural network

### Neurons
A neuron is a mathematical function in a neural network which takes an input, processes data, then produces an output.

$$z=∑(w_i​⋅x_i​)+b$$

On its own, a neuron by itself cannot do much. It evaluates inputs, weighs their importance, and decides how much of the information should influence the next stage. This output is *meaningless* without the broader system which interprets this information. 

### Input layer
The input layer receives the data that will be processed by the network. It doesn’t do any learning or transformation on the data, it simply a lens through which the world is viewed.

### Hidden layer
The hidden layers do the heavy lifting through the use of neurons. These neurons act as “pattern spotters” as they interpret data into something meaningful and useful.

### Output layer
The output layer aggregates the refined data from the hidden layer and outputs a result that’s relevant to the task. This may be making a prediction or decision.