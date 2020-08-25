# Python-Application-Framework

## Abstract
I create tools and projects in python pretty frequently and condensing my frequetly used functions into a submodule is extreamly helpful. Typically this module attempts to be as pragmatic as possible. While many pip modules exist that may solve some of these issues, paf has a 'do it yourself' mentality. This usually results in a smaller dependency list for each of my projects and faster speed as feature are nativly implemented in python. I attempt to keep 'hacky' functions out of this module unless python forces my hand.

## Using PAF
To add paf to your own python project simply add it as a submodule using:\
`git submodule add https://github.com/JustinTimperio/paf.git`

You can now import paf directly into your project and call functions with the following syntax:\
```
import paf

subdirs = paf.find_subdirs('/path/to/search')
```
