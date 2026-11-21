define config.default_textshader = "typewriter"
default preferences.text_cps = 40

transform centerleft:
    xcenter 0.25
    yalign 1.0

transform centerright:
    xcenter 0.75
    yalign 1.0

transform centerrightright:
    xcenter 0.90
    yalign 1.0

transform speaking:
    ease 0.25 zoom 1

transform idle:
    ease 0.25 zoom 0.95


image bg fountain = im.Scale("bg fountain.jpg", config.screen_width, config.screen_height)
image bg castle = im.Scale("bg castle.jpg", config.screen_width, config.screen_height)
image bg throneroom = im.Scale("bg throneroom.jpg", config.screen_width, config.screen_height)

image king = Transform("images/king.png", zoom=1.1)


init -1 python:
    import store

    cast = {
        "vance": "centerleft",
        "runa": "centerright",
        "king": "centerright",
        "astrid": "centerrightright",
    }

    def focus(tag):
        for t, pos in cast.items():
            if renpy.showing(t):
                tf = store.speaking if t == tag else store.idle
                renpy.show(t, at_list=[getattr(store, pos), tf])

    def speaker(tag):
        def cb(event, interact=True, **kwargs):
            if event == "begin":
                focus(tag)
        return cb

define v = Character("Vance", image="vance", callback=speaker("vance"))
define r = Character("Runa", image="runa", callback=speaker("runa"))
define l = Character("Lucian")
define a = Character("Queen Astrid", image="astrid", callback=speaker("astrid"))
define k = Character("King Keoghan", image="king", callback=speaker("king"))

init python:
    cursor_scale = 0.25
    cursor_w, cursor_h = renpy.image_size("images/cursor.png")

    config.mouse = None
    config.mouse_displayable = MouseDisplayable(
        im.FactorScale("images/cursor.png", cursor_scale),
        int(cursor_w * cursor_scale) - 2,
        2
    )

label start:
    # first scene - seer scene
    scene bg fountain
    show vance at centerleft, idle
    show runa at centerright, idle

    v "{i}You and Runa, the castle's seer, sit by the fountain.{/i}"
    v "{i}The sky is cloudy, and it is morning.{/i}"
    v "{i}Runa has been in a trance for a while now.{/i}"
    v "{i}Runa's eyes are rolled back, her body unconscious.{/i}"
    v "Runa?"
    v "{i}She quickly snaps out of the trance she's in, present with you. Her eyes turn to look towards you.{/i}"
    r "No. It's not looking good, Vance."
    v "What?"
    r "Your fate is very bad."
    r "Your next battle is going to be unsuccessful."
    v "What?"
    r "That is all."
    v "Runa, you have to stop giving me half the story."
    r "That is all I can see into the future."
    r "What I say is all I know."
    v "I know, it's just, how am I supposed to stop this?"
    r "I do not know that, Vance. That is for you to figure out."
    r "But the answer, Vance, is in you. Follow your instincts."
    v "Yes."
    v "Well, thank you, Runa, for this session."
    v "Would you like to come down with me to the town markets?"
    r "Sure, Vance. I am in need of some new jewelry."
    v "Very well. We will meet here in three hours."
    v "{i}You walk over to the main castle, to have a meeting with your father.{/i}"

    # second scene - father interaction
    scene bg throneroom with fade
    show astrid at centerrightright, idle
    show king at centerright, idle
    show vance at left

    k "Vance, you're here."
    v "Yes Pa. I was talking with Runa"
    k "Did she say anything significant?"
    v "Yes. She said that my next conquest would be unsucessful"
    k "I'm very worried for you Vance. Runa is almost never wrong."


    return