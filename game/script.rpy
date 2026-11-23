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
image bg markets = im.Scale("bg markets.jpg", config.screen_width, config.screen_height)
image bg prison = im.Scale("bg prison.jpg", config.screen_width, config.screen_height)

image king = Transform("images/king.png", zoom=1.1)
image william = Transform("images/william.png", zoom=0.9)


default lover = "single"
default wedding_ring = "none"


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
    show vance at left
    show william at right
    v "The morning air is warm, and the sun shines on your skin."
    v "You don't get many moments like this"
    v "Moments of solitude"
    v "Further up in the path, you spot someone walking towards you."
    v "You go to say hello"
    v "Hey!"
    w "Hi-Vance? Is that your name?"
    v "That is correct"
    w "Your the kings son, right?"
    v "That is also correct."
    w "Well, I'll see you around"
    w "My mother and I are new to Dorpat, we moved in from the south"
    v "well if you need anything, feel free to ask me"
    v "You and him pass ways."
    v "He was nice."
    v "Eventually you arrive at the pub."
    #change scene to pub
    v "The pub is empty. Its the morning."
    v "What a useless walk."
    v "You walk back home, to your room, upset with the faliure of this morning."
    v "Its the afternoon, so you meet up with Runa for your market visit"
    jump markets

label bored:
    v "I'm so bored"
    v "What could I do?"
    menu:
        "Write some Poetry":
            v "You get out your notebook and a pen"
            v "You write some words on a pain paper"
            v "After you have finished it reads"
            v "A lover I must, fall in love, My father belives, forces me, into something I hate."
            v "You don't know if your proud of it."
            v "Before you know it, its the afternoon, and time to go to the markets with Runa"
            jump markets
        "Read a book":
            v "You go over to your book shelf, and pick out a book"
            menu:
                "Sweets: A Cookbook":
                    v "You open the cookbook and read it"
                    v "+1 cooking"
                    jump reading
                
                "The Dragons Quest":
                    v "You read a chapter of the book"
                    v "+1 Creativity"
                    jump reading

                "A history of Europe":
                    v "You learn about the Roman Empire"
                    v "+1 Knowledge"
                    jump reading

label reading:
    v "You finish your book, and head down to the pond to meet Runa to go to the Markets"
    jump markets

label markets:
    scene bg fountain
    show runa at left 
    show vance at right
    r "Vance, You made it."
    v "Yes, I'm here"
    r "Good, I thought you wouldn't come"
    v "Why?"
    r "Vance, your so unreliable"
    r "You always forget whenever we have something on."
    v "That is not true runa. Besides if anyone forgets, its always you."
    r "Stop trying to put the blame on me."
    v "Fine."
    v "You and Runa, walk over to the markets."
    scene bg forest with fade
    show runa at left 
    show vance at right
    v "My dad is forcing me to get married."
    r "What?"
    v "I know, its so unlike him. He's always been so softly spoken"
    v "never controlling"
    v "but today, he was different."
    r "sounds so odd"
    r "so what are you going to do?"
    r "do you have anyone in mind?"
    v "no, not right now. do you have any ideas?"
    r "i mean.. I could be your wife"
    menu:
        "reject":
            v "i will kindly pass runa"
            r "don't worry, I was just joking"
            v "I know, I know."
            v "the rest of the trip over is really akward"
            jump markets_scene
        "accept":
            $ lover = "Runa"
            v "runa."
            r "yes."
            v "you really love me?"
            r "i mean, I don't hate you. and our star signs align"
            v "I mean, i have never considered you as a partner"
            v "but I'm open to it"
            r "amazing!"
            r "she leans in to give you a kiss."
            v "wow, moving fast you think."
            v "you and her walk until you reach the markets"
            jump markets_scene

label markets_scene:
    scene bg markets
    r "we are here!"
    r "it is so busy!"
    v "yes, what did you say you wanted to get again?"
    r "some produce and some supplies for work"
    v "sounds good"
    r "there is something I have to do by myself quickly though, so I'll meet you here in 10 minutes"
    v "what is it?"
    r "I can't tell you, its a secret."
    v "runa!"
    v "runa runs off in a different direction to run her errand. What do you do?"
    if lover == "Runa":
        menu:
            "buy a wedding ring for luna":
                jump wedding_ring
            "look at swords":
                jump look_at_swords
            "walk around": 
                jump walk_around_markets
    else:
        menu:
            "find a wife":
                jump markets_wife_looking
            "look at swords":
                jump look_at_swords
            "walk around":
                jump walk_around_markets
    
label markets_wife_looking:
    v "you walk around the markets, looking for a potential partner"
    v "nobody really strikes your eye."
    v "10 minutes pass, and you spot Runa in the distance, finishing her errand."
    v "you walk over to her."
    r "lets get the rest of the groceries, shall we?"
    jump groceries

label look_at_swords:
    v "You go over to a sword stall, and look at the swords"
    v "Nothing catches your eye in particular"
    v "Besides, you already have a vast collection of swords at home."
    v "You turn around, and spot Runa in the distance, finishing her errand."
    v "you walk over to her."
    r "lets get the rest of the groceries, shall we?"
    jump groceries

label walk_around_markets:
    v "You look around the food stall, and go to buy a chicken leg"
    v "You devour it."
    v "delicious"
    v "10 minutes pass, and you spot Runa in the distance, finishing her errand."
    v "you walk over to her."
    r "lets get the rest of the groceries, shall we?"
    jump groceries

label wedding_ring:
    v "you walk over to a ring stall, and as the person their for a ring"
    # add in tha ring vendor sprite/person hier
    v "Could I please look at your wedding rings?"
    v "-Ring vendor- What is your budget?"
    v "1500 denarius"
    v "He pulls out a tray from below him."
    v "-Ring vendor- Sir, you are looking at the finest rings from my collection."
    v "-Ring vendor- Do you see anything you fancy?"
    menu:
        "Red Saphire with Bronze Band - 1000p":
            $ wedding_ring = "saphire"
            jump buy_ring
        "Silver Band with Emerald - 1500p":
            $ wedding_ring = "emerald"
            jump buy_ring
        "Gold Band with Amythest - 2000p":
            $ wedding_ring = "amythest"
            jump buy_ring
        "None":
            jump dont_buy_ring

label buy_ring:
    v "You purchase the ring, and put it inside your pocket"
    jump groceries

label dont_buy_ring:
    v "unfortunatly, I am not a fan of any of theese rings"
    v "-ring vendour- that is fine sir, I hope to do buisness with you another day."
    v "you check your watch and it 10 minutes have passed, you spot runa"
    v "so runa, are you going to tell me what you were doing."
    r "no."
    if lover == "Runa":
        v "we are going to get married, and your already keeping secrets from me."
        v "just tell me."
        r "what if its a gift for you?"
        v "oh. I'm sorry runa."
        r "its okay. you will find out soon."
        jump groceries
    else:
        jump groceries

label groceries:
    v "runa pulls out a list of groceries and you and her visit all the shops, talking while you do it."
    v "you buy fruits, vegetables, meat, insnece, and some herb remedies."
    if lover == "none":
        r "vance,"
        v "what?"
        r "I got you something"
        v "She pulls out a vile of liquid."
        r "its a love potion."
        r "so when you see the perfect wife, you can make her love you immeditaly."
        v "thanks runa."
        jump post_markets
    else:
        jump post_markets

label post_markets:
    v "you and runa continue walking through."
    v "after a while, the sun sets and it is time to go home"
    scene bg forest with fade
    v "You and runa walk home"
    v "you eventually have to split paths"
    v "you think your late, so you run the rest of the way home"
    v "you make home just in time for dinner."
    # change this to dining room
    scene bg throneroom
    k "How was your day son?"
    v "It was good."
    k "Any progress on finding a lover?"
    if lover == "Runa":
        v "actually, I did."
        k "Who?"
        v "Runa."
        k "the castle seer?"
        v "Yes. Shes pretty and kind and funny, and I enjoy spending time with her."
        k "You two were just freinds"
        v "Yes."
        k "So when are you going to get married?"
        v "I haven't disscussed it with her yet, but soon I belive."
        if wedding_ring == "none":
            jump dinner_discussion
        else:
            v "I have bought her a beautiful ring though. She will love it."
            a "may I see?"
            v "Sure mother"
            v "You pull the beautiful shining ring out of your pocket"
            v "its beautiful, isn't it"
            a "yes, you have good taste son."
            k "and how much did this cost?"
            if wedding_ring == "saphire":
                v "1000p I belive"
                k "You got a good deal son."
                jump dinner_discussion
            elif wedding_ring == "emerald":
                v "1500p I belive"
                k "You got a bad deal son."
                a "but as long as she will like the ring, It is alright"
                jump dinner_discussion
            elif wedding_ring == "amythest":
                k "You got a horrific deal son."
                v "But I love it. And Runa will love it."
                a "but as long as she will like the ring, It is alright"
                jump dinner_discussion
            else:
                v "I don't remember."
                jump dinner_discussion

            
    else:
        v "no, I didn't have any luck."
        k "keep trying son, and eventually you shall suceed"
        a "but what if he doen't sucseed richard"
        k "he shall not go on any crusaides, fights or battles. I will not let him."
        jump dinner_discussion

label dinner_discussion:
    k "Did you do anything interesting astrid?"
    a "I started working on a new artwork. It is going very well."
    k "I heard their was this new disease coming into our country."
    k "its called the Plauge"
    a "Probably will be nothing, things like this happen all of the time."
    v "Yes, I agree."
    k "I recived quite an odd letter this afternoon."
    v "What did it read?"
    k "I know this is quite odd, but it read 'fear for your life'"
    a "that is quite odd Richard"
    v "The dinner room goes silent, and everybody finishes their meals"
    a "The dinner ends promptly"
    scene bg bedroom
    v "You go to bed, full of food and your eyes tired and sore."
    scene bg bedroom with fade
    v "all of the house is dark. Your blinds have been shut close."
    v "Your mother walks into the room, sheilded by a black veil."
    a "I am a widow!"
    v "Tears run down her face, obviously in distress."
    v "What Happened!"
    v "Your eyes are still sore, and your head still confused from just waking up."
    a "Your father is dead! Last night."
    v "You and her break into tears sitting on your bed."
    v "Hours pass, this extreeme sadness still bubbling inside of you"
    a "I think we must get up. I think it is better for us to do something, to take our minds off of it."
    v "No. I cannot. Pa is dead. Dead."
    a "I understand that."
    v "Do they know what caused his death?"
    a "No. I beleive its a murder."
    v "What? Why?"
    a "Your father was in perfectly good health."
    a "What would cause him to die so abrubtly?"
    v "That disease he was talking about last night, the plauge? Maybe he caught it?"
    a "unlikly. How would he have caught it if he hasn't been out of town."
    v "How is it even possible if you were in bed with him the whole night?"
    a "I have not figured that part out yet."
    v "and who would even want to murder him?"
    a "now vance, I need you to answer my question entirely honestly."
    v "yes"
    a "Did you murder your father?"
    v "of course not! Why would I murder my father, that I love?"
    a "He is forcing you to marry."
    v "Thats not enough a reason to kill him!"
    a "I know you did it, Vance."
    v "But I didn't! I don't have a clue why you are blaming this on me."
    v "Your mother has an evil smile, knowing what she did."
    v "You murdered him!"
    a "But unfortunatley vance, that is not true. It is unfortunate though, that your hair was found all along his body, along with all the servants, who saw you near his room last night."
    v "So your framing me? Your framing me for my fathers murder. A murder YOU commited?"
    a "That is not the truth, for all I know, you commited the murder."
    a "Guards!"
    v "A group of guards come in, and take you to a prison sell."
    scene bg prison with hpunch
    return
