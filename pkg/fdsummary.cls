\def\fileversion{1.0}
\def\filedate{2020/04/29}
\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{fdsummary}[\filedate\space\fileversion\space FD Summary]


\def\fdsummary@language{none}
\def\fdsummary@todoopts{}
\def\fdsummary@class{tudreport}

\DeclareOption{notodo}{\def\fdsummary@todoopts{disable}}
\DeclareOption{german}{\def\fdsummary@language{german}}
\DeclareOption{english}{\def\fdsummary@language{english}}
\DeclareOption{pub}{\def\fdsummary@class{tudapub}}
\ProcessOptions\relax

\LoadClass[a4paper, 11pt, accentcolor = tud3b]{\fdsummary@class}


% Packages and commands required for class definition.
\RequirePackage{ifthen}
\ifthenelse{\equal{\fdsummary@language}{none}}
    {\PackageError{fdsummary}{No language given.}{Provide either option 'german' or 'english'.}}
    {\ifthenelse{\equal{\fdsummary@language}{german}}
        {\newcommand{\fdsummary@ifde}[1]{#1} \newcommand{\fdsummary@ifen}[1]{}}
        {\newcommand{\fdsummary@ifen}[1]{#1} \newcommand{\fdsummary@ifde}[1]{}}}


% Core Packages.
\RequirePackage[T1]{fontenc}
\RequirePackage[utf8]{inputenc}
\fdsummary@ifde{\RequirePackage[ngerman, english]{babel}}
\fdsummary@ifen{\RequirePackage[english, ngerman]{babel}}
% Other Packages.
\RequirePackage[ruled, vlined, linesnumbered]{algorithm2e}
\RequirePackage{caption}
\RequirePackage{csquotes}
\RequirePackage{enumitem}
\RequirePackage{float}
\RequirePackage{hyperref}
\RequirePackage{mathtools}
\RequirePackage{physics}
\RequirePackage{qtree}
\RequirePackage{siunitx}
\RequirePackage{stmaryrd}
\RequirePackage{tabto}
\RequirePackage{tikz}
\RequirePackage{xspace}
\RequirePackage[\fdsummary@todoopts]{todonotes}
% Load TikZ libraries.
\usetikzlibrary{arrows.meta, shapes, backgrounds, angles, calc, decorations.markings}


% Document information.
% Can be overwritten by using \author again.
\author{Fabian Damken}
\fdsummary@ifde{\subtitle{Zusammenfassung \\ \@author}}
\fdsummary@ifen{\subtitle{Summary         \\ \@author}}
\date{\today}



% ~ Styling. ~

% Description-list styling.
\SetLabelAlign{parright}{\parbox[t]{\labelwidth}{\raggedleft#1}}
\setlist[description]{style = multiline, leftmargin = 4cm, align = parright}

% Make TikZ arrow longer and paths bigger.
\tikzset{> = { Latex[length = 2.5mm] }}
\tikzstyle{every path} = [ very thick ]

% If somethis is quoted using "..", interpret it as \csquotes{..} for correct quotes.
\MakeOuterQuote{"}

% Make it possible to use vertical lines in a matrix. See https://tex.stackexchange.com/a/333383
\renewcommand*\env@matrix[1][*\c@MaxMatrixCols c]{%
    \hskip -\arraycolsep
    \let\@ifnextchar\new@ifnextchar
    \array{#1}
}

% Vector and matrix notation.
\renewcommand{\vec}[1]{\boldsymbol{\mathrm{#1}}}
\newcommand{\mat}[1]{\boldsymbol{\mathrm{#1}}}



% ~ Commands. ~

% Abbreviations.
\fdsummary@ifde{
    \newcommand{\bspw}{bspw.\xspace}
    \newcommand{\bzgl}{bzgl.\xspace}
    \newcommand{\bzw}{bzw.\xspace}
    \renewcommand{\dh}{d.\,h.\xspace}
    \newcommand{\ggf}{ggf.\xspace}
    \newcommand{\iA}{i.\,A.\xspace}
    \newcommand{\mglw}{mglw.\xspace}
    \newcommand{\vs}{vs.\xspace}
    \newcommand{\zB}{z.\,B.\xspace}
}
% Robotics.
\newcommand{\DIRKIN}{DIR\,KIN\xspace}
\newcommand{\INVKIN}{INV\,KIN\xspace}
\newcommand{\DIRJAC}{DIR\,JAC\xspace}
\newcommand{\INVJAC}{INV\,JAC\xspace}
\newcommand{\DIRDYN}{DIR\,DYN\xspace}
\newcommand{\INVDYN}{INV\,DYN\xspace}

% Math operators.
\fdsummary@ifde{\DeclareMathOperator{\Rang}{Rang}}
\fdsummary@ifde{\DeclareMathOperator{\Rank}{Rank}}
\DeclareMathOperator{\const}{const}
\DeclareMathOperator{\sign}{sign}

% Other mathy stuff.
% Numbers sets.
\newcommand{\N}{\mathbb{N}}
\newcommand{\Z}{\mathbb{Z}}
\newcommand{\Q}{\mathbb{Q}}
\newcommand{\R}{\mathbb{R}}
\newcommand{\C}{\mathbb{C}}
% Top-left index, e.g. for transformation matrices.
\newcommand{\inreferenceto}[2]{\prescript{#1}{}{#2}}
% One vertical line for probabilities, densities, expectations, etc.
\newcommand{\given}{\,\vert\,}
\newcommand{\biggiven}{\,\big\vert\,}
\newcommand{\Biggiven}{\,\Big\vert\,}
\newcommand{\bigggiven}{\,\bigg\vert\,}
\newcommand{\Bigggiven}{\,\Bigg\vert\,}

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
