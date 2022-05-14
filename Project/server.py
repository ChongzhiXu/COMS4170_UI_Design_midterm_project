from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)

app.config['TEMPLATES_AUTO_RELOAD'] = True

# Zelda legendary Weaponary and all info comes from https://zelda.fandom.com/wiki
data = [
        {
        "id": 0,
        "name": "Golden Key",
        "img": "https://cdn-icons-png.flaticon.com/512/7006/7006890.png",
        "attack": 0,
        "durability": 30,
        "summary": "This is a special unique weapon that is used for sabataging the chest monster. It's made of pure gold and it is very significant for players who wants to get the lengendary weapon.",
        "description": "The Golden Key is an item from The Legend of Zelda: Breath of the Wild. It is given at the start of the game and required to to use instantly to open the first treasure",
        "reviews": [
            {
                "player": "Avocado",
                "comment": "So...useless but important."
            }
        ],
        "location": "Ancient Shrines"
    },
        {
        "id": 1,
        "name": "Aladdin's lamp",
        "img": "https://cdn-icons-png.flaticon.com/512/7006/7006894.png",
        "attack": 0,
        "durability": 20,
        "summary": "It is the most interesting so called weapon, it can be used before the combat and have the buff of tenacity and combat ability.",
        "description": "The Aladdin's lamp is an item from The Legend of Zelda: Breath of the Wild. It is chainsaw-like sword forged using Ancient Sheikah technology. Its unique chainsaw-like design gives it impressive cutting power. Link can have it forged by Cherry at the Akkala Ancient Tech Lab after completing the side quest 'Robbie's Research' for 1000 Rupees, 15 Ancient Screw, 5 Ancient Shafts, and 2 Ancient Cores.",
        "reviews": [
            {
                "player": "Dogman",
                "comment": "I just don't like the weapon because it is the most useless one of the game, the time last is so short and the increasenment is really exiguity。"
            }
        ],
        "location": "Ancient Shrines"
    },
        {
        "id": 2,
        "name": "Ancient Torch",
        "img": "https://cdn-icons-png.flaticon.com/512/7007/7007037.png",
        "attack": 25,
        "durability": 35,
        "summary": "This one-handed torch was made using the stick and fire. Its using is to luminate the surroundings in dark place, while it is also a weapon.",
        "description": "The Ancient Torch is an item from The Legend of Zelda: Breath of the Wild. It is really useful to combat with enemies with fur, when going somewhere dark, you will of course need it.",
        "reviews": [
            {
                "player": "Catman",
                "comment": "No comment, just use for lightness, avoid using it for combat."
            }
        ],
        "location": "Akkala Tech Lab"
    },

    {
        "id": 3,
        "name": "Royal Guard's Sword",
        "img": "https://gamepedia.cursecdn.com/zelda_gamepedia_en/f/f8/BotW_Royal_Guard%27s_Sword_Icon.png?version=c29b97b7aa24be9a2978470f49a0e3d3",
        "attack": 48,
        "durability": 14,
        "summary": "A Sheikah-made replica of the sword that seals the darkness. It was made with ancient technology to oppose the Great Calamity, but its low durability made it inefficient.",
        "description": "The Royal Guard's Sword is an item from The Legend of Zelda: Breath of the Wild. It is an one-handed sword with a base attack power of 48 and a base durability of 14. Link can find it in Hyrule Castle. One can be found in a pedestal behind a breakable wall in the hallways above the Castle's Armory that is a reference to the Master Sword it is based on.",
        "reviews": [
            {
                "player": "e1owl",
                "comment": "I found the broadsword which was sitting in a pedestal behind a cracked wall that you can break with bombs in one of the corridors inside Hyrule castle. It does 48 damage and for me it had a long throw bonus."
            },
            {
                "player": "DanTheGoodman_",
                "comment": "There's a few royal guard weapons in the lockup underneath the castle. Go to the west side of the castle, there will be tunnels leading to the underground of the castle. Continue along them and eventually you should find the lockup."
            }
        ],
        "location": "Hyrule Castle"
    },

    {
        "id": 4,
        "name": "Dragonbone Moblin Club",
        "img": "https://gamepedia.cursecdn.com/zelda_gamepedia_en/e/e5/BotW_Dragonbone_Moblin_Club_Icon.png?version=edff6b3bff1749bcdcdc6f2704f5ec6b",
        "attack": 45,
        "durability": 24,
        "summary": "The bone of an ancient beast has been affixed to this Moblin club, further increasing its damage. Moblins carrying these in battle are particularly dangerous.",
        "description": "The Dragonbone Moblin Club is an item from The Legend of Zelda: Breath of the Wild. It is a Moblin Club with dragonbone affixed to it to further increase its damage and is the strongest Moblin-made club. It has a base attack of 45, though this may be increased by certain weapon bonuses. However it is made of wood and will burn in exposed to fire or volcanic temperatures.",
        "reviews": [
            {
                "player": "Most-Impressive",
                "comment": "The Dragonbone Moblin Club is the best sneakstriking weapon in the game (math and farming map inside)"
            }
        ],
        "location":"Eldin Mountains"
    },

    {
        "id": 5,
        "name": "Ancient Battle Axe+",
        "img": "https://gamepedia.cursecdn.com/zelda_gamepedia_en/b/b1/BotW_Ancient_Battle_Axe%EF%BC%8B_Icon.png?version=8b2c9b7593ad89e1c2fb528cc694311f",
        "attack": 45,
        "durability": 20,
        "summary": "This ancient battle axe's damage output has been increased to maximum. It's sharp enough to cut through almost anything, so it may have been used to forge new routes.",
        "description": "The Ancient Battle Axe+ is a stronger version of the Ancient Battle Axe with a base attack of 45, but this may be increased by certain Weapon Bonuses. It is used by higher level Guardian Scouts encountered in certain Shrines. Link can obtain it by defeating them.",
        "reviews": [
            {
                "player": "PaulTheCarman",
                "comment": "In the side quest 'Weapon Connoisseur,' you are tasked with finding a series of weapons for a kid in Hateno village. One of the weapons you have to find is an ancient battle axe +, which are obtained from the Moderate Tests of Strength."
            }
        ],
        "location": "Ancient Shrines"
    },

    {
        "id": 6,
        "name": "Stone Smasher",
        "img": "https://gamepedia.cursecdn.com/zelda_gamepedia_en/c/cf/BotW_Stone_Smasher_Icon.png?version=15e75c635c0abea58ce3399fd351f46e",
        "attack": 42,
        "durability": 40,
        "summary": "A two-handed weapon forged from a rare metal mined in Goron City. Its center of gravity is at its tip, so it uses centrifugal force and its sheer weight to smash opponents flat.",
        "description": "The Stone Smasher is an item in The Legend of Zelda: Breath of the Wild. It is Goron-made Sword which while normally can be wielded one-handed by Gorons, Lizalfos, and Moblins due to their strength, it is primarily a two-handed sword when wielded by Hylians and Bokoblins. Like all Goron made swords, the blade itself is blunt and as a result relies instead on blunt force to damage enemies and cannot be used to cut grass or trees. As a result, the Stone Smasher and other Goron swords function more like Hammers, thus like the Iron Sledgehammer can be used as a tool for mining Ore Deposits. As a result this weapon can be consider a hammer-sword hybrid.",
        "reviews": [
            {
                "player": "mallsoft",
                "comment": "I start at goron city, put the shiekah sensor on a stone smasher and walk around until I catch one"
            }
        ],
        "location": "Eldin Canyon"
    },

    {
        "id": 7,
        "name": "Ancient Short Sword",
        "img": "https://gamepedia.cursecdn.com/zelda_gamepedia_en/6/65/BotW_Ancient_Short_Sword_Icon.png?version=8ec67e0eece0b2b5d0a8679c035f65be",
        "attack": 40,
        "durability": 54,
        "summary": "The blade of this sword was made using an ancient power lost to this modern age. Its blade appears only when drawn, and its cutting power surpasses metal swords.",
        "description": "The Ancient Short Sword is an item from The Legend of Zelda: Breath of the Wild. It is a sword crafted with the ancient Sheikah technology. It was developed through research of the Guardian and ancient technology researcher, Doctor Robbie as Ancient Soldier Gear, Anti-Calamity armaments he developed to be wielded by Link after he awoke from the Slumber of Restoration. Like the Guardian Sword and other ancient blades, its energy blade only appears when drawn (or mounted in Link's House) and its cutting power is said to suprasses metal swords. However the Ancient Short Sword cannot be obtained from Guardian Scouts.",
        "reviews": [
            {
                "player": "jabberwagon",
                "comment": "The Ancient Short Sword does more damage per hit to Guardians (50% more), plus it can benefit from the Ancient Proficiency buff (80% more) and an Attack Up meal (50% more) at the same time. For those keeping track, that's around 4.05 times normal damage, or 162 damage per hit when fully buffed and used against Guardians."
            }
        ],
        "location": "Akkala Tech Lab"
    },

    {
        "id": 8,
        "name": "Guardian Sword++",
        "img": "https://gamepedia.cursecdn.com/zelda_gamepedia_en/d/d5/BotW_Guardian_Sword%EF%BC%8B%EF%BC%8B_Icon.png?version=9c9867a324b1048d0a9838f8767ad4da",
        "attack": 40,
        "durability": 32,
        "summary": "The abilities of this Guardian sword have been boosted to the maximum, as evidenced by its increase in size. It slices through armor like a hot knife through butter!",
        "description": "This Guardian Sword is a major improvement overall over the base Guardian Sword, now boasting double the damage of the original model (40 over 20) and greatly increased durability, which is also roughly doubled to 32. The Guardian Sword++ can only be found in Shrines proposing \"A Major Test of Strength\" trials, requiring the player to defeat the Guardian Scout IV lurking there. After completing one of these combat trials and obtaining its Shrine's Spirit Orb, these trials will reset after midnight on a Blood Moon allowing Link to obtain replacements. Visually, it is much larger than the base model. Its damage is on par with the Ancient Short Sword, although it is inferior by having lower durability (roughly 20 less than the Short Sword) and by having a lower damage multiplier against Guardians (30% vs 50%). Additionally, it is unable to be reforged, unlike the Ancient Short Sword.",
        "reviews": [
            {
                "player": "GameWinner5",
                "comment": "I wanted to celebrate maxing my Ancient Armor Set by loading up on Ancient++ weapons, but they seem to be running out of durability fairly quickly. Are they more frail than, say, Savage Lynel weapons? Or other weapons in general? They do tons of damage so I would understand if they don't have the best durability but it's still upsetting going through one camp of mobs and losing 1-2 really valuable weapons. Most of them have Durability+ as well."
            },
            {
                "player": "ziggurism",
                "comment": "Yes, guardian weapons have fairly low durability. It is one of the ways that ancient weapons (from Akkala tech lab) distinguish themselves from the guardian class weapons. They're like the guardian weapons, in that they have a bonus against guardians (an even strong buff than guardian class), and are also enhanced by ancient proficiency. They have lower attack, but higher durability."
            }
        ],
        "location": "Ancient Shrines"
    },

    {
        "id": 9,
        "name": "Demon Carver",
        "img": "https://gamepedia.cursecdn.com/zelda_gamepedia_en/9/90/BotW_Demon_Carver_Icon.png?version=e1ac0fd72843893aa476af0c5c793be0",
        "attack": 40,
        "durability": 25,
        "summary": "This lethal weapon is forged by the Yiga. Its unique shape facilitates the sound dispatching of any target and strikes fear into the hearts of all who see it.",
        "description": "The Demon Carver is an item from The Legend of Zelda: Breath of the Wild. It is a circular blade forged by the Sheikah Yiga Clan. It is used by both Yiga Footsoldiers and Blademasters. Like most enemy weapons, Link can pick it up and wield it. It can be used to cut down trees in one hit instead of the usual two. Once Master Kohga has been defeated, Yiga Footsoldiers disguised as travelers wield Demon Carvers instead of Vicious Sickles.",
        "reviews": [
            {
                "player": "Tosh_v",
                "comment": "Found out Demon Carver fits nicely around a round shield."
            }
        ],
        "location": "Ancient Shrines"
    },

    {
        "id": 10,
        "name": "Windcleaver",
        "img": "https://gamepedia.cursecdn.com/zelda_gamepedia_en/3/3a/BotW_Windcleaver_Icon.png?version=d79a688518e82184a834f13cadac790c",
        "attack": 40,
        "durability": 25,
        "summary": "This sword is favored by high-ranking members of the Yiga. When wielded by a proficient fighter, its unique shape cleaves the very wind and creates a vacuum.",
        "description": "The Windcleaver is an item from The Legend of Zelda: Breath of the Wild. It is a single-edged sword with a base attack rating of 40, though this may be increased by certain weapon bonuses. It is used by Yiga Blademasters of the Sheikah Yiga Clan and like most enemy weapons, Link can pick it up and use it himself, but it is notably less powerful in his hands compared to Blademasters due to their expertise with the blade.",
        "reviews": [
            {
                "player": "littlemantry",
                "comment": "Big Yiga guys start to ambush you as you play across the world map and always carry the windcleaver."
            },
            {
                "player": "Hte_D0ngening2",
                "comment": "The Windcleaver is a semi-rare drop from Yiga Blademasters. Just keep killing them and you should find one eventually. Unfortunately, grinding for Yiga weapons is very time-consuming, especially since Yiga members carrying high-damage weapons like the Demon Carver or Windcleaver have a much lower spawn rate than the ones carrying Vicious Sickles or Duplex Bows."
            }
        ],
        "location": "West Necluda"
        
    },

    {
        "id": 11,
        "name": "Knight's Claymore",
        "img": "https://gamepedia.cursecdn.com/zelda_gamepedia_en/f/f4/BotW_Knight%27s_Claymore_Icon.png?version=757d750dc7f9c51ef1a5ef703f824fea",
        "attack": 38,
        "durability": 30,
        "summary": "Only the most confident of Hyrule Castle's knights carried this two-handed sword. Its cutting edge is finely honed.",
        "description": "The Knight's Claymore is an item from The Legend of Zelda: Breath of the Wild. It is a two-handed sword with a base attack power of 38, though this may increase if it has certain weapon bonuses. It is occasionally wielded by monsters such as Lizalfos in Tabantha Tundra in the Tabantha Frontier region. One also spawns near a bottomless pool in the Military Training Camp in the Great Hyrule Forest region. One spawns in the Guards' Chamber of Hyrule Castle.",
        "reviews": [
            {
                "player": "SAOkirito1",
                "comment": "Does anyone else wonder what's up with the knight's claymore? Seriously, it looks like something from Attack on Titan."
            },
            {
                "player": "Flopjacks",
                "comment": "It's probably supposed to be based on Goron weapons"
            }
        ],
        "location": "Tabantha Frontier"
    },

    {
        "id": 12,
        "name": "Royal Broadsword",
        "img": "https://gamepedia.cursecdn.com/zelda_gamepedia_en/e/e6/BotW_Royal_Broadsword_Icon.png?version=380420d22a9e937659754387341bfeee",
        "attack": 36,
        "durability": 36,
        "summary": "The Hyrulean royal family would award this sword to knights who achieved remarkable feats. A sword that balances strength and beauty as elegantly as this one is a rare find.",
        "description": 'The Royal Broadsword is an item from The Legend of Zelda: Breath of the Wild. It is a sword with a base attack power of 36, though this may be increased by certain weapon bonuses. It can be obtained in Akkala Highlands, Tabantha Frontier, and Hyrule Castle. One spawns in the Military Training Camp. It is also occasionally wielded by enemies. Silver Bokoblins, Silver Moblins, and Silver Lizalfos often wield these and other "Royal" series equipment. Hinox tend to wear them as jewelry on their necklaces and if Link is stealthy he can remove it from a Hinox as it sleeps gaining a valuable weapon while avoiding a fight.',
        "reviews": [
            {
                "player": "Scoutdad",
                "comment": "Amiibo also hand them out frequently for me at my current level in the game. I frequently have to leave them on the chests."
            },
            {
                "player": "NewAgeWizard",
                "comment": "You could always try recycling rusty broadswords via rock octorocks (but I don't know how common royal weapons are with that method)"
            }
        ],
        "location": "Akkala Highlands"
    },

    {
        "id": 13,
        "name": "Lizal Tri-Boomerang",
        "img": "https://gamepedia.cursecdn.com/zelda_gamepedia_en/6/66/BotW_Lizal_Tri-Boomerang_Icon.png?version=d368e1c08f35bee5ffe1448424a5ce64",
        "attack": 36,
        "durability": 27,
        "summary": "More blades means more attack power! It can be used as a boomerang, but all those blades makes that a bit more dangerous. Carried by Black Lizalfos seasoned in battle.",
        "description": "The Lizal Tri-Boomerang is an item in The Legend of Zelda: Breath of the Wild. It is a Lizalfos made Boomerang which in addition to being thrown can be used as a single-handed melee weapon, allowing them to wield it in conjunction with Lizalfos made Shields. Link can equip it as a melee weapon which can be thrown or used as a melee weapon. It is the strongest of the Lizalfos made Boomerangs with a base attack power of 36 but this can be increased by certain weapon bonuses. Additionally it is the strongest boomerang in terms of base attack power, as it is even stronger than the Giant Boomerang despite that boomerang being a larger two-handed weapon, though it lacks the Giant Boomerang's durability. Its even stronger than the Sea-Breeze Boomerang obtained via the amiibo Rune. It is mainly wielded by Black Lizalfos, though may be wielded by Silver Lizalfos or Stalizalfos. Link may also encounter other monsters wielding one such as Moblins.",
        "reviews": [
            {
                "player": "G0ldenEye5",
                "comment": "I love the boomerang weapons, I always get excited whenever I find a giant boomerang even though I never use it for its intended purpose"
            },
            {
                "player": "Scadooot",
                "comment": "Yeah boomerangs are so much fun, i like them because they provide an interesting alternative to arrows"
            }
        ],
        "location": "Akkala Highlands"
    },

    {
        "id": 14,
        "name": "Mighty Lynel Sword",
        "img": "https://gamepedia.cursecdn.com/zelda_gamepedia_en/6/61/BotW_Mighty_Lynel_Sword_Icon.png?version=760ec436f339d448423d6c81a0596e3b",
        "attack": 36,
        "durability": 22,
        "summary": "This Lynel-made sword boasts more blades and more attack power. A skilled Lynel can draw this sword simply in passing and still cut a foe in two.",
        "description": "The Mighty Lynel Sword is an item from The Legend of Zelda: Breath of the Wild. It is a sword wielded by Blue-Maned and White-Maned Lynels which Link can obtain by defeating them. It is the second strongest of the three Lynel-made swords.",
        "reviews": [
            {
                "player": "LoopyBullet",
                "comment": "Can't find Mighty Lynel Bow. Blue-Maned Lynels drop Savage Bows only. Help! Any reason why this would be? I thought Blue-Maned Lynels drop Mighty stuff only? Was there some kind of update to get rid of the Mighty Lynel Bow? Do the Lynel bows scale faster than the other weapons for some reason? Sounds like I've just permanently missed out on the Mighty Bow. :("
            },
            {
                "player": "PseudoTwili",
                "comment": "The blue-maned Lynel in Hyrule Castle always carries Mighty gear. Now, normally the Lynels in the two gatehouses don't leave their gear behind after you slay them, but there's a way you can still get it. After entering the gatehouse by the main gate and seeing the Lynel drop down, save your game and reload the save. After this just fight the Lynel and he should leave his gear behind on his defeat."
            }
        ],
        "location": "Lanayru Great Spring"
    },

    {
        "id": 15,
        "name": "Dragonbone Boko Bat",
        "img": "https://gamepedia.cursecdn.com/zelda_gamepedia_en/6/61/BotW_Dragonbone_Boko_Bat_Icon.png?version=d70b299d6b5a4d506475023514e73550",
        "attack": 36,
        "durability": 16,
        "summary": "Used by only the toughest Bokoblin warriors, this Boko bat has been fortified by fossilized bone. It boasts a high durability and is strong enough to beat down powerful foes.",
        "description": "The Dragonbone Boko Bat is an item from The Legend of Zelda: Breath of the Wild. It is a Boko Bat that has been fortified with a fossilized dragonbone. This bat is the strongest Boko Bat and is generally wielded by high tier Bokoblins though rarely Stalkoblin and Moblins may wield them in certain places. They are most commonly found in the Hyrule Ridge and Necluda Sea regions according to the Hyrule Compendium. The Hinox (Youngest Kin) in Hanu Pond wears one as necklace jewelry.",
        "reviews": [
            {
                "player": "browndaw004",
                "comment": "Equipped Creature gets +1/+0, trample, Second Strike(this creature deals damage after the other), and {1}: This creature gains menace until end of turn."
            }
        ],
        "location": "Hyrule Ridge"
    },

    {
        "id": 16,
        "name": "Lynel Crusher",
        "img": "https://gamepedia.cursecdn.com/zelda_gamepedia_en/c/c9/BotW_Lynel_Crusher_Icon.png?version=25b429cf9f6ac785134e7b183a916b32",
        "attack": 36,
        "durability": 20,
        "summary": "This two-handed weapon is favored by the Lynels. It may be more accurate to call it a lump of metal than a weapon, but if wielded by a Lynel, it can pound you into a fine dust.",
        "description": "The Lynel Crusher is an item from The Legend of Zelda: Breath of the Wild. It is a two-handed mace-like weapon. Link can obtained it after defeating a Lynel. It has a base attack power of 36 though this may be increased by an Attack Up weapon bonus. It is the weakest of the Lynel-made Crusher weapons.",
        "reviews": [
            {
                "player": "InfiniteEdge18",
                "comment": "The swords are 1 handed so their great for quick attacks, the crushers deal massive damage, but their slow 2 handed weapons, and Idk about the spears also, You'll have an easier time farming the swords than crushers"
            }
        ],
        "location": "Gerudo Highlands"
    },

    {
        "id": 17,
        "name": "Great Flameblade",
        "img": "https://gamepedia.cursecdn.com/zelda_gamepedia_en/7/7d/BotW_Great_Flameblade_Icon.png?version=6cb5751fb8b51ca7877a70d2c56e0dea",
        "attack": 34,
        "durability": 50,
        "summary": "This magic-infused greatsword was forged in the fires of Death Mountain by Goron smiths in an ancient age. Attack when the blade glows red to expel flames.",
        "description": "The Great Flameblade is an item from The Legend of Zelda: Breath of the Wild. It is a two-handed greatsword forged by Goron smiths in the fires of Death Mountain in ancient times and infused with magic that causes it to expel red flames when its blade glows causing fire damage to enemies. Link can find it at the Ancient Tree Stump in Central Hyrule, at the Eldin Great Skeleton in the Eldin Mountains or in the Treasure Chests of Rona Kachta Shrine and Shai Yota Shrine.",
        "reviews": [
            {
                "player": "Stephanie Williams",
                "comment": "I really want to make the Great Flameblade from LoZ: Breath of the Wild. I haven't really messed around with programming LEDs. Is regular worbla transparent enough for LEDs to glow through, or would I use all clear worbla for the blade part? Reference pictures below."
            }
        ],
        "location": "Eldin Canyon"
    },

    {
        "id": 18,
        "name": "Scimitar of the Seven",
        "img": "https://gamepedia.cursecdn.com/zelda_gamepedia_en/a/a5/BotW_Scimitar_of_the_Seven_Icon.png?version=3ade31176fd3dd3d713597a99304fb7d",
        "attack": 32,
        "durability": 60,
        "summary": "A famous sword once beloved by the Gerudo Champion Urbosa. It is said that when Urbosa swung this sword in battle, her movements resembled a beautiful dance.",
        "description": "The Scimitar of the Seven is an item from The Legend of Zelda: Breath of the Wild. It is a single-handed sword with a base attack power of 32. It can be obtained by Link along with the Daybreaker as a reward for completing the Divine Beast Vah Naboris dungeon. It is the strongest single-handed Gerudo made sword.",
        "reviews": [
            {
                "player": "Mic",
                "comment": "Urbosa's one-handed sword can be repaired if you have a diamond, five flint and a Gerudo Scimitar. The Gerudo Scimitar can be found on a bundle of boxes immediately to the left of the entrance to Gerudo Town and up a small set of stairs. Once you have all that, take it to the guard standing next to the throne in Gerudo Town — she'll give you a new Scimitar of the Seven in return."
            }
        ],
        "location": "Gerudo Town"
    },

    {
        "id": 19,
        "name": "Eightfold Longblade",
        "img": "https://gamepedia.cursecdn.com/zelda_gamepedia_en/c/ce/BotW_Eightfold_Longblade_Icon.png?version=4d5717805deac51ed5078944da6c4ec3",
        "attack": 32,
        "durability": 25,
        "summary": "A single-edged sword seldom seen in Hyrule. This weapon is passed down through the Sheikah tribe and has an astonishingly sharp edge ideal for slicing.",
        "description": "Eightfold Longblades are items from The Legend of Zelda: Breath of the Wild. They are Sheikah longswords with a base attack power of 32, though this may increase if they have certain weapon bonuses. One can be obtained in a Treasure Chest found in the Shee Vaneer Shrine. They are also occasionally wielded by enemies, such as a Lizalfos on Samasa Plain near the Rucco Maag Shrine. The swords are rarely seen in Hyrule, and were forged using Ancient Sheikah technology. When charged, instead of doing a heavy spin-attack, Link will hold it like he's about to draw it from a side sheath and do a quick slash when the button is released.",
        "reviews": [
            {
                "player": "RegulusMagnus",
                "comment": "The charge attack for this weapon is also somewhat unique (shared only with the windblade, but that charge attack also does something else)"
            }
        ],
        "location": "West Necluda"
    },

    {
        "id": 20,
        "name": "Great Thunderblade",
        "img": "https://gamepedia.cursecdn.com/zelda_gamepedia_en/a/a4/BotW_Great_Thunderblade_Icon.png?version=165746e3691e250f7422f806aeda69ad",
        "attack": 32,
        "durability": 50,
        "summary": "	This magic-infused greatsword was forged by the Hyrulean royal family using lightning from the Hyrule Hills. Attack when the blade glows golden to expel lightning.",
        "description": "The Great Thunderblade is an item from The Legend of Zelda: Breath of the Wild. It is a two-handed elemental sword filled with lightning power from the Hyrule Hills, shocking and causing electric damage to enemies save for those resistant to electricity. They are among several rare weapons forged by the Royal Family of Hyrule. As with the other elemental weapons in Breath of the Wild it's high durability and magical effects make it a good backup to the Master Sword during it's recharge period.",
        "reviews": [
            {
                "player": "KonohaJonin",
                "comment": "IIRC theres a Great Flameblade that's super accessible right by the Great Plateau, Excalibur'd into a makeshift pedestal on top of the giant ancient tree stump that is next to the Coliseum."
            }
        ],
        "location": "Hyrule Field"
    },

        {
        "id": 21,
        "name": "Royal Guard's Spear",
        "img": "https://gamepedia.cursecdn.com/zelda_gamepedia_en/8/8d/BotW_Royal_Guard%27s_Spear_Icon.png?version=2376354ee6907314dbbef3255e1d9e3f",
        "attack": 32,
        "durability": 15,
        "summary": "This Sheikah-made spear was created using ancient technology to combat the Calamity. Its attack power is very high, but a critical design flaw left it with poor durability.",
        "description": "The Royal Guard's Spear is an item from The Legend of Zelda: Breath of the Wild. It is a spear created using Ancient Sheikah technology to combat Calamity Ganon and its design was based on the Royal Halberd, though it has a darker coloration. While its attack power is very high, a critical design flaw left it with poor durability, making it less effective.",
        "reviews": [
            {
                "player": "ziggurism",
                "comment": "Royal guard gear is different than royal gear. Royal gear can be found all over the map. Royal guard gear can only be found at the castle."
            }
        ],
        "location": "Hyrule Castle"
    },

    {
        "id": 22,
        "name": "Guardian Sword+",
        "img": "https://gamepedia.cursecdn.com/zelda_gamepedia_en/f/f3/BotW_Guardian_Sword%EF%BC%8B_Icon.png?version=4b3011fe36c98b12ca73c3671c208056",
        "attack": 30,
        "durability": 26,
        "summary": "This Guardian sword has enhanced power over the standard model. Its cutting capabilities are improved, and its durability has seen a slight uptick.",
        "description": 'This Guardian Sword is a good improvement overall over the base Guardian Sword, with significantly more damage (30 base over 20) and has a decent durability increase (from 17 to 26). It can be only found in Shrines proposing "A Modest Test of Strength" trial, where the player must defeat a Guardian Scout III wielding it. Visually, the sword is somewhat larger, on par with most other swords, when compared to the small-looking standard Guardian Sword.',
        "reviews": [
            {
                "player": "ziggurism",
                "comment": "guardian weapons have fairly low durability. It is one of the ways that ancient weapons (from Akkala tech lab) distinguish themselves from the guardian class weapons. They're like the guardian weapons, in that they have a bonus against guardians (an even strong buff than guardian class), and are also enhanced by ancient proficiency. They have lower attack, but higher durability."
            }
        ],
        "location": "Ancient Shrines"
    },

    {
        "id": 23,
        "name": "Master Sword",
        "img": "https://gamepedia.cursecdn.com/zelda_gamepedia_en/0/05/BotW_Master_Sword_Icon.png?version=26bf023b97f5f966351641d9d0a54f7a",
        "attack": 30,
        "durability": 40,
        "summary": "The Master Sword, also known as the Blade of Evil's Bane, the Legendary Sword, the Sword of Legend, the Master Sword of Resurrection, the Sword that Seals the Darkness",
        "description": "The Master Sword was originally crafted by the goddess Hylia as the Goddess Sword, and was later forged into the Master Sword by the Goddess's chosen hero and its spirit, Fi, who bathed it in the three Sacred Flames located across the land that would become the Kingdom of Hyrule. Din's Flame in particular imbued the sword with the Power to Repel Evil, a power augmented after the Sword received the blessing of Zelda, which transformed the blade into the True Master Sword. It is usually the only Sword that can defeat Ganon in the games it appears in, and the Sacred Sword, is a recurring legendary Sword in the The Legend of Zelda series..",
        "reviews": [
            {
                "player": "Cydni Gadsden",
                "comment": "The master sword made this so easy!!"
            },
            {
                "player": "Daniel Martinez",
                "comment": "I did it. 3rd time really was the charm. I actually finished the main storyline. Got the Master Sword. All 120 of the shrines. All memories. All Divine Beasts. (No, I will not go after all 900 koroks). Yeah, it only took 3 tries in 3 years, but that was incredible. Master Mode, Trials and other DLC will be played eventually. For now I'm just going to take it all in. Damn great experience.🗡🗡🗡🗡🗡🗡🗡🗡🗡🗡🗡🗡🗡🗡🗡 PS: The final boss encounter is one of the best I ever played. Up there with other boss fights like the Psycho Mantis encounter in Metal Gear Solid. 🗡🗡🗡🗡🗡🗡🗡🗡🗡🗡🗡🗡🗡🗡"
            }
        ],
        "location": "Ancient Shrines"
    },

    {
        "id": 24,
        "name": "Savage Lynel Crusher",
        "img": "https://gamepedia.cursecdn.com/zelda_gamepedia_en/f/f4/BotW_Savage_Lynel_Crusher_Icon.png?version=6ecaf55221ff1890d39a76de59316f78",
        "attack": 78,
        "durability": 35,
        "summary": "This Lynel-made two-handed weapon is immensely heavy thanks to a rare metal from Death Mountain's peak. The power of its downward swing is in a class all its own.",
        "description": "The Savage Lynel Crusher is an item from The Legend of Zelda: Breath of the Wild. It is a two-handed mace-like weapon wielded by White-Maned Lynels and Silver Lynels which Link can obtain by defeating them. It is the strongest of the three Lynel-made Crusher weapons crafted by skilled Lynels blacksmiths from a rare metal acquired from the peak of Death Mountain. This crusher has the second highest DPS of any two-handed weapon and a staggering base attack power of 78. It is outclassed only by the Ancient Battle Axe ++ when worn with the full Ancient armor set. However, in terms of overall damage dealt before the weapon breaks, the Crusher's dominance is contested by the Boulder Breaker and Ancient Bladesaw.",
        "reviews": [
            {
                "player": "bradboii",
                "comment": "Really getting into fighting lynels now and I'm proud of this"
            },
            {
                "player": "kokiden88",
                "comment": "I got the exact same one. Except it's 108 instead of 107.I am never letting that one break. I use that very same Lynel crusher to farm Lynels by jumping on their back and killing them that way. Weapon doesn’t get damaged that way."
            }
        ],
        "location": "Eldin Mountains"
    },

    {
        "id": 25,
        "name": "Royal Guard's Claymore",
        "img": "https://gamepedia.cursecdn.com/zelda_gamepedia_en/2/2d/BotW_Royal_Guard%27s_Claymore_Icon.png?version=6ec44e8ee5d1ba0bd7c91a21fb77a0bb",
        "attack": 72,
        "durability": 15,
        "summary": "The Sheikah used the very essence of ancient technology to forge this greatsword. It was designed to oppose the Calamity, but its low durability made it impractical in battle.",
        "description": "The Royal Guard's Claymore is an item from The Legend of Zelda: Breath of the Wild. It is a two-handed sword with an attack rating of 72, though this may be increased by certain weapon bonuses. A Royal Guard's Claymore can be found in one of the cells in Hyrule Castle (Breath of the Wild) Lockup. A Moblin in the Guards' Chamber wield one as well and will respawn with one each Blood Moon.",
        "reviews": [
            {
                "player": "PozPoz_",
                "comment": "Just got a 115 damage Royal Guard's Claymore from Hyrule Castle (Attack Up +43)"
            }
        ],
        "location": "Hyrule Castle"
    },

    {
        "id": 26,
        "name": "Boulder Breaker",
        "img": "https://gamepedia.cursecdn.com/zelda_gamepedia_en/2/2a/BotW_Boulder_Breaker_Icon.png?version=a5efeb7de1551696e3e47780ce4c47b8",
        "attack": 60,
        "durability": 60,
        "summary": "This two-handed weapon was once wielded by the Goron Champion Daruk. Daruk made swinging it around look easy, but a Hylian would need an immense amount of strength.",
        "description": "The Boulder Breaker is an item from The Legend of Zelda: Breath of the Wild. It is a Goron sword originally wielded by Goron Champion Daruk. Like most Goron swords, it functions more akin to a Hammer due to its blunt blade and weight, as in they mine ore better than all other weapons. As a result this weapon can be considered a hammer-sword hybrid.",
        "reviews": [
            {
                "player": "goro-n",
                "comment": "Is this weapon okay for breaking ore? I have been using it since it seems to be made of stone, but I don't want to wreck durability."
            }
        ],
        "location": "Goron City" 
    },

    {
        "id": 27,
        "name": "Ancient Battle Axe++",
        "img": "https://gamepedia.cursecdn.com/zelda_gamepedia_en/2/2e/BotW_Ancient_Battle_Axe%EF%BC%8B%EF%BC%8B_Icon.png?version=83e3512d130c1b68ce31b84839f0aedc",
        "attack": 60,
        "durability": 25,
        "summary": "This ancient battle axe's damage output is scaled up to peak performance. Ancient technology makes it possible to enhance cutting power beyond metal weapons' limits.",
        "description": 'The Ancient Battle Axe++ is the strongest version of the Ancient Battle Axe with a base attack of 60, but this may be increased by certain Weapon Bonuses. It is used by the strongest Guardian Scouts. Link can obtain it by defeating them. With certain techniques such as using "Ancient Proficiency" bonus from a Level 2 "Ancient" armor set and dishes granting "Attack Up", the Ancient Battle Axe++ is one of the strongest weapons.',
        "reviews": [
            {
                "player":"DanTheGoodman_",
                "comment": "I have only found the ancient battle axe from the major test of strength, does anyone know where else these kinds can be found? I am basically looking to get one for each weapon type."
            }
        ],
        "location": "Ancient Shrines"
    },

    {
        "id": 28,
        "name": "Savage Lynel Sword",
        "img": "https://gamepedia.cursecdn.com/zelda_gamepedia_en/8/85/BotW_Savage_Lynel_Sword_Icon.png?version=fe793958528cc7c9cca75eacf29da7e2",
        "attack": 58,
        "durability": 41,
        "summary": "A brutal sword carried by white-haired Lynels. The savage blades are strong enough to cut down any foe, no matter how strong.",
        "description": "The Savage Lynel Sword is an item from The Legend of Zelda: Breath of the Wild. It is a sword wielded by White-Maned Lynels and Silver Lynels which Link can obtain by defeating them. It is the strongest of the three Lynel-made swords with a base attack of 58. Furthermore, it is also arguably the most powerful one-handed sword in the game (excluding the awakened Master Sword).",
        "reviews": [
            {
                "player": "Electric_Sheep22",
                "comment": "I just got a 100 power savage lynel sword with +42 attack up!"
            }
        ],
        "location": "Hyrule Field"
    },

    {
        "id": 29,
        "name": "Ancient Bladesaw",
        "img": "https://gamepedia.cursecdn.com/zelda_gamepedia_en/c/ce/BotW_Ancient_Bladesaw_Icon.png?version=c6cc462869ee457c47372baa829c6c3a",
        "attack": 55,
        "durability": 50,
        "summary": "This two-handed sword was forged using ancient Sheikah technology. Its unique rotating blades give it impressive cutting power that will slice enemies to shreds.",
        "description": "The Ancient Bladesaw is an item from The Legend of Zelda: Breath of the Wild. It is chainsaw-like sword forged using Ancient Sheikah technology. Its unique chainsaw-like design gives it impressive cutting power. Link can have it forged by Cherry at the Akkala Ancient Tech Lab after completing the side quest 'Robbie's Research' for 1000 Rupees, 15 Ancient Screw, 5 Ancient Shafts, and 2 Ancient Cores.",
        "reviews": [
            {
                "player": "Le_avocado",
                "comment": "So... just recently purchased the ancient armor set from Robbie by farming guardian parts from Major Tests of Strength (and guardian stalkers) and got a few Ancient Battle axes ++ and was wondering, whether they are better than the Ancient Bladesaw at the Akkala Ancient Tech Lab that you can buy. Since they are both 2 handed weapons and the battleaxe has a better attack stat is it better than the bladesaw? And is there no point in spending rupees and ancient parts to buy the Bladesaw?"
            }
        ],
        "location": "Akkala Tech Lab"
    },
{
        "id": 30,
        "name": "Mighty Lynel Crusher",
        "img": "https://gamepedia.cursecdn.com/zelda_gamepedia_en/d/df/BotW_Mighty_Lynel_Crusher_Icon.png?version=08679757fccbcbab8b359039b50b9a95",
        "attack": 54,
        "durability": 25,
        "summary": "This Lynel-made two-handed weapon has been reinforced to increase its durability and striking power. Its overwhelming heft will crush your foe, shield and all.",
        "description": "The Mighty Lynel Crusher is an item from The Legend of Zelda: Breath of the Wild. It is a two-handed mace-like weapon wielded by Blue-Maned Lynels which Link can obtain by them. It is the second strongest of the three Lynel Crusher weapons.",
        "reviews": [
            {
                "player": "CarterWilliams777",
                "comment": "I've seen a couple 108 or 109 lynel crushers before. They probably get even higher on occasion."
            }
        ],
        "location": "Hebra Mountains"
    },

    {
        "id": 31,
        "name": "Royal Claymore",
        "img": "https://gamepedia.cursecdn.com/zelda_gamepedia_en/2/23/BotW_Royal_Claymore_Icon.png?version=e8e20338503b986761abe5e3f3de1158",
        "attack": 52,
        "durability": 40,
        "summary": "A two-handed sword issued to the Hyrulean royal family's immediate guard detail. Its powerful strikes are said to crush an opponent's body and resolve alike.",
        "description": "The Royal Claymore is an item from The Legend of Zelda: Breath of the Wild. It is a two-handed sword with a base attack power of 52, though this may be increased by certain weapon bonuses. The claymore is originally issued to the Royal Family of Hyrule's guard detail.",
        "reviews": [
            {
                "player": "laughpuppy23",
                "comment": "i wast trying to get the climbing set as easly as possible in the game, but one of them was gated by a major test of strength and I had all starter weapons. i waited until I found a royal claymore and went to him, and It broke halfway through! it's one of the strongest weapons in the game no?! regardless of how you feel of the weapon breaking mechanic, I can't help but feel that late game weapons should be a bit sturdier than that..."
            }
        ],
        "location": "Gerudo Desert"
    },

    {
        "id": 32,
        "name": "Edge of Duality",
        "img": "https://gamepedia.cursecdn.com/zelda_gamepedia_en/0/0c/BotW_Edge_of_Duality_Icon.png?version=57187f3c058bb810ca34a4c5df83ea48",
        "attack": 48,
        "durability": 35,
        "summary": "A curious double-edged sword crafted using Sheikah technology. It was originally made for Hyrulean knights unfamiliar with single-edged blades.",
        "description": "The Edge of Duality is an item from The Legend of Zelda: Breath of the Wild. It is a Sheikah sword with a base attack rating of 50 though this may be increased by certain weapon bonuses. The Edge of Duality is a two-handed double-edged sword which was crafted using Ancient Sheikah technology. It was originally intended for Knights of Hyrule unfamiliar with single-edged blades traditionally used by the Sheikah tribe. Unlike the Royal Guard weapons created using Sheikah technology to combat Calamity Ganon, it does not suffer from low durability. It is implied the Edge of Duality was a conventional greatsword developed by the ancient Sheikah for the Knights of Hyrule ten millennia before Breath of the Wild as some are found within Shrines which are 10,000 years old.",
        "reviews": [
            {
                "player": "Sarahneth",
                "comment": "In case someone searches this weapon up on Reddit the Edge of Duality spawns in a cave just north of the Gerudo Tower, about halfway between Karusa Valley and Sapphia's Table. It's behind some rocks that you need to use Stasis to move"
            }
        ],
        "location": "Hyrule Field"
    }
]

current_id = 32

def get_names():
    names = []
    for item in data:
        names.append(item["name"])
    return names

# def get_autoComplete():
#     autoCom = ["Gerudo Highlands", "Hebra Mountains", "Tabantha Frontier", "Gerudo Desert", "Hyrule Field", "West Necluda",
#                 "Hyrule Castle", "Hebra Mountains", "Eldin Mountains", "Ancient Shrines", "Eldin Canyon", "Akkala Ancient Tech Lab",
#                 "Akkala Highlands", "Lanayru Great Spring", "Hyrule Ridge", "Necluda Sea", "Gerudo Town", "Goron City"]
#     for item in data:
#         autoCom.append(item["name"])
#     print(autoCom)
#     return autoCom

@app.route('/')
def main():

    # return render_template('index.html', data=data[-3:], names=get_names(), autoCom=get_autoComplete())
    return render_template('index.html', data=data[0:3], names=get_names())


@app.route('/search/<keys>', methods=['GET', 'POST'])
def search(keys):

    global data
    
    search_result = []
    for item in data:

        if keys.lower() in item["name"].lower():
            item_found = item
            item_found["matched"] = "name"
            item_found["position_st"] = item["name"].lower().find(keys.lower())
            item_found["position_en"] = item_found["position_st"] + len(keys)
            search_result.append(item_found)

        elif keys.lower() in item["summary"].lower():
            item_found = item
            item_found["matched"] = "summary"
            item_found["position_st"] = item["summary"].lower().find(keys.lower())
            item_found["position_en"] = item_found["position_st"] + len(keys)
            search_result.append(item_found)

        elif keys.lower() in item["location"].lower():
            item_found = item
            item_found["matched"] = "location"
            item_found["position_st"] = item["location"].lower().find(keys.lower())
            item_found["position_en"] = item_found["position_st"] + len(keys)
            search_result.append(item_found)
    print(search_result)

    # return render_template('results.html', n_items=len(search_result), results=search_result, names=get_names(), autoCom=get_autoComplete())
    return render_template('results.html', n_items=len(search_result), results=search_result, names=get_names())


@app.route('/view/<id>')
def view(id=0):

    global data

    # Get the item with the exact id
    for item in data:
        if item["id"] == int(id):
            # return render_template('view.html', names=get_names(), item=item, autoCom=get_autoComplete())
            return render_template('view.html', names=get_names(), item=item, id=id)

    else:
        print("id not valid")


@app.route('/create')
def create():
    # return render_template("create.html", names=get_names(), autoCom=get_autoComplete())
    return render_template("create.html", names=get_names())


@app.route('/add_item', methods=['GET', 'POST'])
def add_item():

    global data
    global current_id
    new_item = request.get_json()
    current_id += 1
    new_item["id"] = current_id

    data.append(new_item)

    return jsonify(url="view/"+str(new_item["id"]))


@app.route('/delete', methods=['GET', 'POST'])
def delete():

    global data
    global current_id

    id = request.get_json()
    print(id)
    id = int(id)

    # The pop() method removes the item at the given index from the list and returns the removed item.
    data.pop(id)
    current_id -= 1

    for i, item in enumerate(data):
        item["id"] = i
    return jsonify(data=data)


@app.route('/edit/<id>')
def edit(id):
    global data
    
    # Get the item with the exact id
    for item in data:
        if item["id"] == int(id):
            return render_template('edit.html', item=item, names=get_names(), id=id)
    else:
        print("id not valid")


@app.route('/add_review', methods=['GET', 'POST'])
def add_review():

    global data

    json_data = request.get_json()
    id = json_data["id"]
    
    data[id]["reviews"].append(
        {
            "player": json_data["player"],
            "comment": json_data["comment"],
            "marked_as_deleted": False
        }
    )

    return jsonify(0)

@app.route('/delete_review', methods=['GET', 'POST'])
def delete_review():

    global data

    json_data = request.get_json()
    id = json_data["weapon_id"]
    comment_id = int(float(json_data["comment_id"]))
    print(comment_id, type(comment_id))
    data[id]["reviews"][comment_id]["marked_as_deleted"] = True

    return jsonify(0)

@app.route('/recover_review', methods=['GET', 'POST'])
def recover_review():

    global data

    json_data = request.get_json()
    id = json_data["weapon_id"]
    comment_id = int(float(json_data["comment_id"]))
    print(comment_id, type(comment_id))
    data[id]["reviews"][comment_id]["marked_as_deleted"] = False

    return jsonify(0)

if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True)