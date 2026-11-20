
# creates centerleft 
transform centerleft:
    xcenter 0.25
    yalign 1.0

#creates centreright
transform centerright:
    xcenter 0.75
    yalign 1.0

#scales up image to fill up whole screen
image bg fountain = im.Scale("bg fountain.jpg", config.screen_width, config.screen_height)

#defines characters
define v = Character("Vance", image="vance")
define l = Character("Lucian", image="")
define a = Character("Queen Astrid", image="astrid")
define r = Character("Runa", image="runa")

# custom cursor

init python:
    scale = 0.25
    w, h = renpy.image_size("images/cursor.png")

    config.mouse = None
    config.mouse_displayable = MouseDisplayable(
        im.FactorScale("images/cursor.png", scale),
        int(w * scale) - 2, 
        2                    
    )

# The game starts here.

label start:
    #opening scene - fountain fortune telling - LOL THAT SOUNDS SO AI BUT ITS NOT
    scene bg fountain
    show vance at centerleft 
    show runa at centerright
    v "{i}You and Runa, the castles seer sit by the fountain{/i}"
    v "{i}The sky is cloudy, and it is morning{/i}"
    v "{i}Runa has been in a trance for a while now.{/i}"
    v "{i}Runa's eyes are rolled back, her body unconcious{/i}"
    v "Runa?"
    v "{i}She quickly snaps out of the trance shes in, present with you. Her eyes turn to look towards you.{/i}"
    r "No. its not looking good vance."
    v "What?"
    r "Your fate is very bad."
    r "Your next battle is going to be unsucsessful"
    r ""
    
    return

