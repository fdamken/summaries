\def\fileversion{1.0}
\def\filedate{2020/04/29}
\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{fdsummary}[\filedate\space\fileversion\space FD Summary]


\def\fdsummary@language{none}
\def\fdsummary@todoopts{}

\DeclareOption{notodo}{\def\fdsummary@todoopts{disable}}
\DeclareOption{german}{\def\fdsummary@language{ngerman}}
\DeclareOption{english}{\def\fdsummary@language{english}}
\ProcessOptions\relax

\let\fdsummary@author=\@author

% dark Mode
\ExplSyntaxOn
\RequirePackage{darkmode, graphicx} % Used for dark Mode

\newcommand{\includeinvertablegraphics}[2][]{% Grafik wird beim Dark Mode automatisch Invertiert (rgb)
	\IfDarkModeTF{\includegraphics[decodearray={1.0~0.0~1.0~0.0~1.0~0.0},#1]{#2}}{\includegraphics[#1]{#2}}
}
\newcommand{\includeinvertablegrayscalegraphics}[2][]{% Grafik wird beim Dark Mode automatisch Invertiert (grayscale)
	\IfDarkModeTF{\includegraphics[decodearray={1.0~0.0},#1]{#2}}{\includegraphics[#1]{#2}}
}

% DARK_MODE environment check (enable if DARK_MODE=1)
\sys_get_shell:nnN { kpsewhich ~ --var-value ~ DARK_MODE } { } \l_dark_mode_env_var_tl
\tl_trim_spaces:N \l_dark_mode_env_var_tl
\tl_if_eq:NnT \l_dark_mode_env_var_tl {1} {\enabledarkmode{}}
\ExplSyntaxOff

% Packages and commands required for class definition.
\newread\fdsummary@metadata
\openin\fdsummary@metadata=metadata.txt
\read\fdsummary@metadata to \filelinea
\if\relax\filelinea\relax\else
\def\fdsummary@author{\filelinea}
\fi
\read\fdsummary@metadata to \filelinet
\if\relax\filelinet\relax\else
\def\fdsummary@title{\filelinet}
\fi
\closein\fdsummary@metadata

\RequirePackage{ifthen}
\ifthenelse{\equal{\fdsummary@language}{none}}
    {\PackageError{fdsummary}{No language given.}{Provide either option 'german' or 'english'.}}
    {\ifthenelse{\equal{\fdsummary@language}{ngerman}}
        {\newcommand{\fdsummary@ifde}[1]{#1} \newcommand{\fdsummary@ifen}[1]{}}
        {\newcommand{\fdsummary@ifen}[1]{#1} \newcommand{\fdsummary@ifde}[1]{}}}


% Load the parent class.
\LoadClass[\fdsummary@language, a4paper, fontsize=11pt, accentcolor=3b, class=report, custommargins=false, marginpar=false, pdfa=false]{tudapub}


% Core Packages.
\ifLuaTeX
    \RequirePackage[utf8]{luainputenc}
\else
    \RequirePackage[T1]{fontenc}
    \RequirePackage[utf8]{inputenc}
\fi
\fdsummary@ifde{\RequirePackage[main = ngerman, USenglish]{babel}}
\fdsummary@ifen{\RequirePackage[main = USenglish, ngerman]{babel}}
% Other Packages.
\RequirePackage{acronym}
\RequirePackage[ruled, vlined, linesnumbered]{algorithm2e}
\RequirePackage[normalem]{ulem}
\RequirePackage{amsmath}
\RequirePackage{amssymb}
\RequirePackage{amsthm}
\RequirePackage{attachfile}
\RequirePackage{bbm}
\RequirePackage{bitpattern}
\RequirePackage{booktabs}
\RequirePackage{bm}
\RequirePackage{bytefield}
\RequirePackage{caption}
\RequirePackage{csquotes}
\RequirePackage{enumitem}
\RequirePackage{eqparbox}
\RequirePackage{fancyvrb}
\RequirePackage{float}
\RequirePackage{hyperref}
\RequirePackage{listings}
\RequirePackage{makecell}
\RequirePackage{mathtools}
\RequirePackage{mdframed}
\RequirePackage{multicol}
\RequirePackage{newunicodechar}
\RequirePackage{pgfgantt}
\RequirePackage{pgfplots}
\RequirePackage{physics}
\RequirePackage{prftree}
\RequirePackage{qcircuit}
\RequirePackage{qtree}
\RequirePackage{rotating}
\RequirePackage{siunitx}
\RequirePackage{stmaryrd}
\RequirePackage{subcaption}
\RequirePackage{syntax}
\RequirePackage{tabto}
\RequirePackage{textcomp}
\RequirePackage{tikz-uml}
\RequirePackage{tikzpeople}
\RequirePackage{tikz}
\RequirePackage{xfrac}
\RequirePackage{xspace}
\RequirePackage{xstring}
\RequirePackage[\fdsummary@todoopts]{todonotes}
\pgfplotsset{compat = newest}
% Load TikZ libraries.
%\usetikzlibrary{arrows.meta, shapes, backgrounds, angles, calc, positioning, decorations.markings}
\usetikzlibrary{arrows.meta, shapes, backgrounds, angles, calc, chains, scopes, decorations.pathmorphing, patterns, er, positioning}


% Document information.
\author{\fdsummary@author}
\title{\fdsummary@title}
\fdsummary@ifde{\subtitle{Zusammenfassung}}
\fdsummary@ifen{\subtitle{Summary}}
\date{\today}




% ~ Styling. ~

% Colors.
\colorlet{ambiguityorange}{TUDa-8\IfDarkModeTF{a}{b}}
\colorlet{changedpurple}{TUDa-11a}
\colorlet{colorDensity}{TUDa-1\IfDarkModeTF{a}{b}}
\colorlet{irl}{TUDa-0\IfDarkModeTF{a}{a}}
\colorlet{lerrorred}{TUDa-9\IfDarkModeTF{a}{b}}
\colorlet{lstcomments}{TUDa-4\IfDarkModeTF{a}{c}}
\colorlet{lstkeywords}{TUDa-9\IfDarkModeTF{a}{d}}
\colorlet{lstlinenumbers}{TUDa-0\IfDarkModeTF{b}{c}}
\colorlet{lststrings}{TUDa-2\IfDarkModeTF{a}{c}}
\colorlet{fgcolor}{.} % If we need the default Font Color but . is currently overwritten

% Description-list styling.
\SetLabelAlign{parright}{\parbox[t]{\labelwidth}{\raggedleft#1}}
\setlist[description]{style = multiline, leftmargin = 4cm, align = parright}

% Some stuff for statistics and neural networks.
\tikzstyle{neuron}        = [circle,fill=.!25!\thepagecolor,minimum size=17pt,inner sep=0pt]
\tikzstyle{input neuron}  = [neuron, fill=green!50!\thepagecolor]
\tikzstyle{output neuron} = [neuron, fill=red!50!\thepagecolor]
\tikzstyle{hidden neuron} = [neuron, fill=blue!50!\thepagecolor]
\tikzstyle{annot}         = [text width=4em, text centered]
\tikzstyle{density}       = [colorDensity, line width = 2pt]
\tikzset{declare function = { gaussian(\x,\m,\S) = 1/sqrt(2*pi*\S) * e^(-1/(2*\S) * (\x-\m)^2); }}

% Make TikZ arrow longer and paths bigger.
%\tikzstyle{every path} = [ very thick ]
\tikzset{> = { Latex[length = 2mm] }}

% Disable teletyper-font in algorithm2e comments.
\SetCommentSty{}

% If somethis is quoted using "..", interpret it as \csquotes{..} for correct quotes.
\MakeOuterQuote{"}

% Only number an equation if it is references.
\mathtoolsset{showonlyrefs,showmanualtags}

% Make it possible to use vertical lines in a matrix. See https://tex.stackexchange.com/a/333383
\renewcommand*\env@matrix[1][*\c@MaxMatrixCols c]{%
    \hskip -\arraycolsep
    \let\@ifnextchar\new@ifnextchar
    \array{#1}
}

% Vector and matrix notation.
\renewcommand{\vec}[1]{\bm{#1}}
\newcommand{\mat}[1]{\bm{#1}}

% Listings settings (use TUDa colors for highlighting).
\lstdefinestyle{base}{
    moredelim = **[is][\color{errorred}]{@@!}{@@@},
    moredelim = **[is][\color{changedpurple}]{@@?}{@@@}
}
\lstset{
    backgroundcolor = \color{\thepagecolor},
    basicstyle = \ttfamily\scriptsize\color{.},
    breakatwhitespace = true,
    breaklines = true,
    breakautoindent = true,
    commentstyle = \color{lstcomments},
    escapeinside = {{*@}{@*}},
    keywordstyle = \color{lstkeywords},
    numbers = left,
    numberstyle = \tiny\color{lstlinenumbers},
    showstringspaces = false,
    stringstyle = \color{lststrings},
    tabsize = 4,
    rulecolor=\color{\thepagecolor},
    emphstyle=\color{fgcolor},
    style = base
}

% Make it possible to include matplotlib plots with negative numbers.
\newunicodechar{−}{--}

% Align captions right or, if they are to small, center them.
\captionsetup{justification=RaggedRight, singlelinecheck=true}

% mdframed settings.
\mdfsetup{%
    backgroundcolor=\thepagecolor,%
    fontcolor=.,%
    linecolor=fgcolor,%
    frametitlefontcolor=fgcolor,%
    shadowcolor==fgcolor!50!\thepagecolor,%
    subtitlebackgroundcolor=\thepagecolor,%
    subsubtitlebackgroundcolor=\thepagecolor,%
    subtitleabovelinecolor=fgcolor,%
    subtitlebelowlinecolor=fgcolor,%
    subsubtitleabovelinecolor=fgcolor,%
    subsubtitlebelowlinecolor=fgcolor,%
}%



% ~ Commands. ~

\newcommand{\HREF}[1]{\href{#1}{#1}}
\newcommand\circled[1]{\tikz[baseline=(char.base)]{\node[shape=circle,draw,inner sep=2pt] (char) {#1};}}

% Reference the matrix cookbook - always a good idea.
\newcommand{\matrixcookbook}{matrix cookbook\footnote{\url{https://www.math.uwaterloo.ca/~hwolkowi/matrixcookbook.pdf}}\xspace}

% We need to go deeper!
\newcommand{\subsubparagraph}[1]{\hspace{1cm} \textbf{#1:}}

% Include code as lstlisting and attachment.
\newcommand{\code}[1]{\attachfile[icon = Paperclip]{#1} \lstinputlisting{#1}}

% Generic way to highligh definitions and so on.
\newcommand{\definition}[2]{\subparagraph{Definition (#1)} #2}
\newcommand{\notation}[2]{\subparagraph{Notation (#1)} #2}
\newcommand{\theorem}[1]{\subparagraph{Theorem} #1}
\newcommand{\intuition}[1]{\subsubparagraph{Intuition} #1}
\fdsummary@ifde{\newcommand{\answer}[1]{\subparagraph{Antwort} #1}}
\fdsummary@ifen{\newcommand{\answer}[1]{\subparagraph{Answer} #1}}

% Quad erat demonstrandum.
\renewcommand{\qed}{\hfill\( \Box \)}


% Boxes surrounded by borders for information and warnings.
\newcommand{\info}[1]{
    \begin{figure}[H]
        \centering
        \fbox{\parbox[c]{0.5\textwidth}{#1}}
    \end{figure}
}
\newcommand{\warning}[1]{
    \begin{figure}[H]
        \centering
        \fbox{\parbox[c]{0.5\textwidth}{\textbf{Warning:} #1}}
    \end{figure}
}

% Network.
\newcommand{\ciscoInternet}[3]{\node[label = #3, #2](#1){\includegraphics{cisco/cloud\IfDarkModeT{-inverted}}}}
\newcommand{\ciscoModem}[3]{\node[label = #3, #2](#1){\includegraphics{cisco/cable_modem\IfDarkModeT{-inverted}}}}
\newcommand{\ciscoRouter}[3]{\node[label = #3, #2](#1){\includegraphics{cisco/router\IfDarkModeT{-inverted}}}}
\newcommand{\ciscoSwitch}[3]{\node[label = #3, #2](#1){\includegraphics{cisco/workgroup_switch\IfDarkModeT{-inverted}}}}
\newcommand{\ciscoClient}[3]{\node[label = #3, #2](#1){\includegraphics{cisco/pc\IfDarkModeT{-inverted}}}}
\newcommand{\ciscoFirewall}[3]{\node[label = #3, #2](#1){\includegraphics{cisco/firewall\IfDarkModeT{-inverted}}}}
\newcommand{\ciscoServer}[3]{\node[label = #3, #2](#1){\includegraphics{cisco/file_server\IfDarkModeT{-inverted}}}}
\newcommand{\ciscoIdP}[3]{\node[label = #3, #2](#1){\includegraphics{cisco/key\IfDarkModeT{-inverted}}}}
\newcommand{\tikzTimeDiagram}[3][1]{\foreach \x in { 1, ..., #2 } { \draw [->] (\x*5*#1, 0) to (\x*5*#1, -#3-1); }}

% Other.
\newcommand{\outputlisting}[1]{\lstinputlisting[numbers = none]{#1}}
\newcommand{\inlinePromela}[1]{\lstinline[language = PROMELA]|#1|}
\newcommand{\inlineJava}[1]{\lstinline[language = Java]|#1|}

% Abbreviations.
\fdsummary@ifde{
    \newcommand{\bspw}{bspw.\xspace}
    \newcommand{\bzgl}{bzgl.\xspace}
    \newcommand{\bzw}{bzw.\xspace}
    \newcommand{\ca}{ca.\xspace}
    \newcommand{\gdw}{gdw.\xspace}
    \newcommand{\ggf}{ggf.\xspace}
    \newcommand{\iA}{i.\,A.\xspace}
    \newcommand{\mglw}{mglw.\xspace}
    \newcommand{\vs}{vs.\xspace}
    \newcommand{\zB}{z.\,B.\xspace}
    \renewcommand{\dh}{d.\,h.\xspace}
}
% Robotics.
\newcommand{\DIRKIN}{DIR\,KIN\xspace}
\newcommand{\INVKIN}{INV\,KIN\xspace}
\newcommand{\DIRJAC}{DIR\,JAC\xspace}
\newcommand{\INVJAC}{INV\,JAC\xspace}
\newcommand{\DIRDYN}{DIR\,DYN\xspace}
\newcommand{\INVDYN}{INV\,DYN\xspace}

% Math operators.
\fdsummary@ifde{\newcommand{\ggT}{\ensuremath{\textrm{ggT}}}}
\DeclareMathOperator*{\argmax}{arg\,max}
\DeclareMathOperator*{\argmin}{arg\,min}
\DeclareMathOperator{\Bias}{Bias}
\DeclareMathOperator{\Cliques}{Cliques}
\DeclareMathOperator{\cond}{cond}
\DeclareMathOperator{\const}{const}
\DeclareMathOperator{\Ch}{Ch}
\DeclareMathOperator{\Cov}{Cov}
\DeclareMathOperator{\Dec}{Dec}
\DeclareMathOperator{\Des}{Des}
\DeclareMathOperator{\dom}{dom}
\DeclareMathOperator{\diag}{diag}
\DeclareMathOperator{\Eig}{Eig}
\DeclareMathOperator{\emp}{emp}
\DeclareMathOperator{\Enc}{Enc}
\DeclareMathOperator{\eps}{eps}
\DeclareMathOperator{\Family}{Family}
\DeclareMathOperator{\gl}{gl}
\DeclareMathOperator{\HMAC}{HMAC}
\DeclareMathOperator{\MAC}{MAC}
\DeclareMathOperator{\MSE}{MSE}
\DeclareMathOperator{\marg}{marg.}
\DeclareMathOperator{\ND}{ND}
\DeclareMathOperator{\rd}{rd}
\DeclareMathOperator{\Pa}{Pa}
\DeclareMathOperator{\Sep}{Sep}
\DeclareMathOperator{\sign}{sign}
\DeclareMathOperator{\Sig}{Sig}
\DeclareMathOperator{\sinc}{sinc}
\DeclareMathOperator{\sort}{sort}
\DeclareMathOperator{\val}{val}
\DeclareMathOperator{\Var}{Var}
\DeclareMathOperator{\Vf}{Vf}
% Logic.
\DeclareMathOperator{\Fml}{Fml}
\DeclareMathOperator{\FSym}{FSym}
\DeclareMathOperator{\Program}{Program}
\DeclareMathOperator{\ProgVSym}{ProgVSym}
\DeclareMathOperator{\PSym}{PSym}
\DeclareMathOperator{\Trm}{Trm}
\DeclareMathOperator{\TSym}{TSym}
\DeclareMathOperator{\VSym}{VSym}
% Databases.
\DeclareMathOperator{\Schema}{Schema}
\DeclareMathOperator{\KEYS}{KEYS}
\DeclareMathOperator{\PK}{PK}
\DeclareMathOperator{\DB}{DB}
% RL.
\DeclareMathOperator{\KL}{KL}
\DeclareMathOperator{\clip}{clip}

% Footnotes.
\newcommand{\oversetfootnotemark}[1]{\stepcounter{footnote} \overset{\mathclap{(\thefootnote)}}{#1}}
\let\realfootnote\footnote
\let\realfootnotetext\footnotetext
\renewcommand{\footnote}[1]{\realfootnote{#1}}
\renewcommand{\footnotetext}[1]{\realfootnotetext{#1}}
\newcommand{\doublefootnotetext}[2]{\addtocounter{footnote}{-1} \footnotetext{#1} \stepcounter{footnote} \footnotetext{#2}}
\newcommand{\triplefootnotetext}[3]{\addtocounter{footnote}{-2} \footnotetext{#1} \stepcounter{footnote} \footnotetext{#2} \stepcounter{footnote} \footnotetext{#3}}

% Other mathy stuff.
% Numbers sets.
\newcommand{\N}{\mathbb{N}}
\newcommand{\Z}{\mathbb{Z}}
\newcommand{\Q}{\mathbb{Q}}
\newcommand{\R}{\mathbb{R}}
\providecommand{\C}{} % Make Sure \C exists
\renewcommand{\C}{\mathbb{C}}
% Expectation.
\newcommand{\E}{\mathbb{E}}
% Top-left index, e.g. for transformation matrices.
\newcommand{\inreferenceto}[2]{\prescript{#1}{}{#2}}
% Approximate proportional to.
\newcommand{\approxproptoinn}[2]{\mathrel{\vcenter{\offinterlineskip\halign{\hfil$##$\cr#1\propto\cr\noalign{\kern2pt}#1\sim\cr\noalign{\kern-2pt}}}}}
\newcommand{\approxpropto}{\mathpalette\approxproptoinn\relax}
% One vertical line for probabilities, densities, expectations, etc.
\newcommand{\subgiven}{\vert}
\newcommand{\given}{\,\vert\,}
\newcommand{\biggiven}{\,\big\vert\,}
\newcommand{\Biggiven}{\,\Big\vert\,}
\newcommand{\bigggiven}{\,\bigg\vert\,}
\newcommand{\Bigggiven}{\,\Bigg\vert\,}
% One vertical line for set definitions.
\newcommand{\forwhich}{\,\vert\,}
\newcommand{\bigforwhich}{\,\big\vert\,}
\newcommand{\Bigforwhich}{\,\Big\vert\,}
\newcommand{\biggforwhich}{\,\bigg\vert\,}
\newcommand{\Biggforwhich}{\,\Bigg\vert\,}
% Short forms.
\newcommand{\dotsrange}[2]{#1,\,\cdots\!,#2}
\newcommand{\subdotsrange}[2]{#1,\,\cdots\!,\,#2}
\newcommand{\liminfty}[1][n]{\lim_{#1 \to \infty}}
\newcommand{\suminfty}[1][n]{\sum_{#1 = 0}^\infty}
\newcommand{\limx}[1][x]{\lim_{#1 \to #1_0 }}
\newcommand{\parallelAsync}{\ensuremath{\,\lvert\vert\rvert\,}}
% Logic.
\newcommand{\eqv}{\leftrightarrow}
\newcommand{\always}{\square}
\newcommand{\btlFor}{\ensuremath{\textit{For}_\textit{BTL}}}
\newcommand{\lf}{\ensuremath{\mathfrak{f}}}
\newcommand{\lt}{\ensuremath{\mathfrak{t}}}
\newcommand{\pFor}{\ensuremath{\textit{For}_0}}
\newcommand{\sometimes}{\lozenge}
\newcommand{\subof}{\sqsubseteq}
\newcommand{\tempty}{\perp}
\newcommand{\tuni}{\top}
\newcommand{\until}{\mathcal{U}}
% For InfMan NLP.
\newcommand{\ambiguity}[1]{\textcolor{ambiguityorange}{#1}}
% Stuff for PGM.
\newcommand{\from}{\leftarrow}
\newcommand{\fromto}{\leftrightarrow}
% QC.
\newcommand{\ID}{\mathbbm{1}}
\newcommand{\longto}{\longrightarrow}
\newcommand{\CZ}{\mathit{CZ}}
\newcommand{\CNOT}{\mathit{CNOT}}
\newcommand{\CCNOT}{\mathit{CCNOT}}
% RL.
\newcommand{\transposed}{{\!\top\!}}
\newcommand{\MSVE}{\overline{\mathit{VE}}}
\renewcommand{\H}{\mathbb{H}}

% BIG!
\makeatletter
\newcommand{\BIG}{\bBigg@{4}}
\newcommand{\BIGG}{\bBigg@{5}}
\makeatother

% Quadtree.
\newcommand{\grayBox}{%
    \begin{tikzpicture}
    \draw [fill = gray] (0, 0) -- (0, 0.5) -- (0.5, 0.5) -- (0.5, 0) -- cycle;
    \end{tikzpicture}
}
\newcommand{\whiteBox}{%
    \begin{tikzpicture}
    \draw [fill = white] (0, 0) -- (0, 0.5) -- (0.5, 0.5) -- (0.5, 0) -- cycle;
    \end{tikzpicture}
}
\newcommand{\blackBox}{%
    \begin{tikzpicture}
    \draw [fill = black] (0, 0) -- (0, 0.5) -- (0.5, 0.5) -- (0.5, 0) -- cycle;
    \end{tikzpicture}
}


% Workarounds and similar stuff.
\newcommand{\infer}[2]{\prftree{#2}{#1}}
\DeclareOldFontCommand{\it}{\normalfont\itshape}{\mathit}

\DeclareSIUnit{\sibyte}{B}

\let\definition\undefined
\let\theorem\undefined
\theoremstyle{definition}
\newtheorem{definition}{Definition}
\theoremstyle{plain}
\newtheorem{example}{Example}
\newtheorem{theorem}{Theorem}
\newtheorem{postulate}{Postulate}
\newtheorem{remark}{Remark}

\newacro{QC}{quantum computing}
\newacro{QM}{quantum mechanics}
\newacro{BQP}{Bounded-Error Quantum Polynomial}
\newacro{CFE}{continued fraction expansion}
\newacro{GME}{genuine multipartite entangled}
\newacro{QEC}{quantum error correction}
\newacro{QKD}{quantum key distribution}
\newacro{QFT}{quantum Fourier transform}
\newacro{AI}{artificial intelligence}
\newacro{RL}{reinforcement learning}
\newacro{RBF}{radial basis function}
\newacro{ML}{machine learning}
\newacro{NN}{neural network}
\newacro{MDP}{Markov decision process}  \newacroplural{MDP}{Markov decision processes}
\newacro{MRP}{Markov reward process}  \newacroplural{MRP}{Markov reward processes}
\newacro{DP}{dynamic programming}
\newacro{PI}{policy iteration}
\newacro{VI}{value iteration}
\newacro{MC}{Monte-Carlo}
\newacro{TD}{temporal difference}
\newacro{GLIE}{greedy in the limit of infinite exploration}
\newacro{SARSA}{state, action, reward, state, action}  \acused{SARSA}
\newacro{DQN}{deep Q-network}
\newacro{A2C}{advantage actor-critic}
\newacro{TRPO}{trust-region actor-critic}
\newacro{PPO}{proximal policy optimization}
\newacro{DDPG}{deep deterministic policy gradient}
\newacro{TD3}{twin delayed \acs{DDPG}}
\newacro{SAC}{soft actor-critic}
\newacro{MSVE}{mean squared value error}
\newacro{SGD}{stochastic gradient descent}
\newacro{LSTD}{least-squares \ac{TD}}
\newacro{LSPI}{least-squares \ac{PI}}
\newacro{LSTDQ}{\ac{LSTD} for action-value functions}  \acused{LSTDQ}
\newacro{PG}{policy gradient}
\newacro{LSFD}{least-squares-based finite difference}
\newacro{POMDP}{partially observable \ac{MDP}}
\newacro{GPOMDP}{gradient of \ac{POMDP}}  \acused{GPOMDP}
\newacro{FIM}{Fisher information matrix}
\newacro{KL}{Kullback-Leibler}
\newacro{KKT}{Karush-Kuhn-Tucker}
\newacro{MSE}{mean squared error}
\newacro{SOTA}{state of the art}
\newacro{CFA}{compatible function approximation}
\newacro{eNAC}{episodic natural actor-critic}
\newacro{NG}{natural gradient}
\newacro{DDQN}{double \ac{DQN}}
\newacro{KDE}{kernel density estimation}
\newacro{PGT}{policy gradient theorem}
\newacro{GAE}{generalized advantage estimation}
\newacro{CG}{conjugate gradient}
\newacro{POMCP}{partially observable \ac{MC} planning}
\newacro{SMDP}{semi-Markov decision process}
\newacro{HAM}{hierarchy of abstract machines}
\newacro{PILCO}{probabilistic inference for learning control}
\newacro{GPS}{guided policy search}
\newacro{MBRL}{model-based \ac{RL}}
