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
image bg bedroom = im.Scale("bg bedroom.jpg", config.screen_width, config.screen_height)
image bg forest = im.Scale("bg forest.jpg", config.screen_width, config.screen_height)

image king = Transform("images/king.png", zoom=1.1)

default lover = False


init -1 python:
    import store

    cast = {
        "vance": "centerleft",
        "runa": "centerright",
        "king": "centerright",
        "astrid": "centerrightright",
        "william":"right",
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
define w = Character("William", image="william", callback=speaker("william"))

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
    v "I understand that Pa! Your wisdom offers me no closure."
    v "Now why did you ask me to have a meeting with you?"
    k "I have to discuss something very important with you."
    v "Well tell me Pa!"
    k "I'm getting to it Vance, be pacient son."
    k "I'm heavy hearted about your Amours."
    v "My Amours? But i'm a knight. I'm to busy for love pa"
    v "and i'm only 23"
    k "The perfect time to get married!"
    v "I'm be out on conquests all the time. I don't see the point Pa."
    k "When I was your age, I wanted to fall in love with a lovley woman was my dream."
    k "You for one, don't seem to be interested in the matter at all."
    v "It's just a matter of preferences Pa, and I don't want to get married, or for one find a lover."
    k "Well. If you don't want to, Your not going on any sieges until you get married."
    a "I think we should just let him have his way Richard"
    k "I will not be moved"
    menu:
        "Fight the matter":
            v "No Pa. I wish not to get married, I have so much of my life ahead to do so."
            k "Well I will not budge either, but I can stop you from going on battles"
            v "Please Pa, respect my wishes."
            k "I will give you 20 days"
            v "Pa."
            k "I will not budge. 20 days vance."
            v "You storm away to your room with a bitter taste in your mouth"
            v "You feel like you have never been able to love"
            v "You have always been different from other men your age."
            v "As teenagers, they all had girlfreinds, and lovers"
            v "Wheras you, were always just a bachelor"
            v "As your frends called you, alone forever."
            jump post_argument

        "Agree with his terms":
            v "Fine Pa"
            k "You have 30 days to find a lover."
            v "Yes."
            v "And what happens if I don't?"
            k "I assure you son, that will not be happening"
            k "Now go on. Those days will pass as fast as a cannon."
            k "I reccomend The Boar’s Head to find your wife."
            k "Its where I met your mother."
            a "And that was the best decision of my life, saying yes to you, when you came up to me."
            v "You and your parents continue flirting."
            v "Gross."
            v "You walk away, down to your room do lie down and sleep."
            jump post_argument
    
label post_argument:
    scene bg bedroom with fade 
    v "Agh."
    menu:
        "Find a Wife":
            jump wife_looking
        
        "Find something else to do":
            jump bored




label wife_looking:
    v "Ugh, I'll guess I will go."
    v "You walk begin walking down do the towns pub, named The Boars Head"
    scene bg forest with fade
    v "The morning air is warm, and the sun shines on your skin."
    v "You don't get many moments like this"
    v "Moments of solitude"
    v "Further up in the path, you spot someone walking towards you."
    v "You go to say hello"
    v "Hey!"
    w ""

    jump markets

label bored:
    jump markets

label markets:
    r "Vance, I made it."
    v "Yes, I'm here"
    r "Good, I thought you wouldn't come"
    v "Why?"
    r "Vance, your so unreliable"
    r "You always forget whenever we have something on."
    return