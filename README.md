# SongBoard
A song writing storyboard for rapid prototyping of song ideas.

I want to sketch chord progessions and be able to play them in order to try out different melodies on it. Further, I want to structure these chord progressions into the typical elements of a song, like intro, verse and chorus, so that I can subsequently compose my song very fast on a chord progression base. 

This is intended to be a prototype to explore how the app would ideally look like and easily fiddle around with different ways of doing the GUI and doing the complete SW architecture of the app. I know, tkinter is a very rustical decision as GUI library, but allows me to try things fast. Later I might change to a different GUI library or framework, or I might throw this prototype away and write a native iOS app for it. So this python app is really about finding out how the app should be like and also exploring the SW architecture. Even if I rewrite everything later e.g. in SWIFT, the SW architecture can be re-used and will not change dramatically when going to an iOS app and implementing it in SWIFT (at least that is how I do things and this is my working hypothesis).

Idea list:
- midi playback
- text/lyrics with chord relation with printable output view
- easy shifting of the parts per drag & drop
- easy transfer of the song ideas to Logic Pro X and maybe also Garage Band
- native app for iOS

See this architecture context diagram for an overview:

<div hidden>
    @startuml firstDiagram
    Alice -> Bob: Hello
    Bob -> Alice: Hi!
    @enduml
</div>

![](firstDiagram.svg)

Some more markdown.