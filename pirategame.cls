% pirategame.cls
\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{pirategame}[2024/12/20 Class for Pirate Game Rules]

% Load base article class
\LoadClass[a4paper,14pt]{article}

% Package imports
\RequirePackage[utf8]{inputenc}
\RequirePackage[T1]{fontenc}
\RequirePackage{geometry}
\RequirePackage{graphicx}
\RequirePackage{background}
\RequirePackage{tikz} % Pour les effets graphiques
\RequirePackage{titlesec}
\RequirePackage{hyperref}
\RequirePackage{xcolor}
\RequirePackage{multicol}
\RequirePackage[shortlabels]{enumitem}
\RequirePackage{pgffor} % Pour les boucles
\RequirePackage{geometry} % Pour ajuster les marges
\RequirePackage{array}
\RequirePackage{amsmath}
\geometry{margin=1in}

\usetikzlibrary{calc,fadings}
\tikzfading[name=fade l,left color=transparent!100,right color=transparent!0]
\tikzfading[name=fade r,right color=transparent!100,left color=transparent!0]
\tikzfading[name=fade d,bottom color=transparent!100,top color=transparent!0]
\tikzfading[name=fade u,top color=transparent!100,bottom color=transparent!0]

% Geometry
\geometry{margin=1in}

% Background settings
\RequirePackage{fancyhdr}
\newcommand\setBackground[1]{%
  \backgroundsetup{
    scale=1,                           % Force la mise à l'échelle de l'image
    color=black,                       % Couleur (inutile ici)
    opacity=0.8,                         % Transparence (1 = opaque)
    angle=0,                           % Rotation
    position=current page.center,      % Centre la position
    contents={\includegraphics[width=\paperwidth,height=\paperheight,keepaspectratio=false]{#1}}
  }
}

% Command to add a logo with gradient borders
\newcommand\addLogoWithGradient[2][0.4]{% #1 = Scale (default 40% width)
  \begin{tikzpicture}
      % Add the logo
      \node[anchor=center, inner sep=0pt] (image) at (0,0)
      {\includegraphics[width=#1\textwidth]{#2}};
      % Add gradient transparency around the logo
    %   \shade[inner color=transparent!0, outer color=transparent!100]
    %   ([xshift=-1cm, yshift=-1cm]image.south west) -- 
    %   ([xshift=1cm, yshift=-1cm]image.south east) --
    %   ([xshift=1cm, yshift=1cm]image.north east) --
    %   ([xshift=-1cm, yshift=1cm]image.north west) -- cycle;
  \end{tikzpicture}
}
% Title formatting
\titleformat{\section}{\LARGE\bfseries}{\thesection.}{1em}{} % \Large → \LARGE
\titleformat{\subsection}{\Large\bfseries}{\thesubsection.}{1em}{} % \large → \Large


% Custom commands
\newcommand{\important}[1]{\textbf{\textcolor{red}{#1}}}

% Hyperlinks
\hypersetup{
    colorlinks=true,
    linkcolor=blue,
    urlcolor=blue
}

% Document start hook
\AtBeginDocument{
  \pagestyle{plain}
}
