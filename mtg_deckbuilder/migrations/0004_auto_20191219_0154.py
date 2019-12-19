# Generated by Django 3.0 on 2019-12-19 07:54

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('mtg_deckbuilder', '0003_deck_cardlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='deck',
            name='cardList2',
            field=multiselectfield.db.fields.MultiSelectField(choices=[(1, 'Abomination of Gudul'), (2, 'Abzan Ascendancy'), (3, 'Abzan Banner'), (4, 'Abzan Battle Priest'), (5, 'Abzan Charm'), (6, 'Abzan Falconer'), (7, 'Abzan Guide'), (8, 'Act of Treason'), (9, 'Ainok Bond-Kin'), (10, 'Ainok Tracker'), (11, 'Alabaster Kirin'), (12, 'Alpine Grizzly'), (13, 'Altar of the Brood'), (14, 'Anafenza, the Foremost'), (15, 'Ankle Shanker'), (16, 'Arc Lightning'), (17, "Archers' Parapet"), (18, 'Armament Corps'), (19, 'Arrow Storm'), (20, 'Ashcloud Phoenix'), (21, 'Avalanche Tusker'), (22, 'Awaken the Bear'), (23, 'Barrage of Boulders'), (24, "Bear's Companion"), (25, 'Become Immense'), (26, 'Bellowing Saddlebrute'), (27, 'Bitter Revelation'), (28, 'Blinding Spray'), (29, 'Bloodfell Caves'), (30, 'Bloodfire Expert'), (31, 'Bloodfire Mentor'), (32, 'Bloodsoaked Champion'), (33, 'Bloodstained Mire'), (34, 'Blossoming Sands'), (35, 'Brave the Sands'), (36, "Briber's Purse"), (37, 'Bring Low'), (38, 'Burn Away'), (39, 'Butcher of the Horde'), (40, 'Cancel'), (41, 'Canyon Lurkers'), (42, 'Chief of the Edge'), (43, 'Chief of the Scale'), (44, 'Clever Impersonator'), (45, 'Crackling Doom'), (46, 'Cranial Archive'), (47, "Crater's Claws"), (48, 'Crippling Chill'), (49, 'Dazzling Ramparts'), (50, 'Dead Drop'), (51, 'Death Frenzy'), (52, 'Debilitating Injury'), (53, 'Defiant Strike'), (54, 'Deflecting Palm'), (55, 'Despise'), (56, 'Dig Through Time'), (57, 'Disdainful Stroke'), (58, 'Dismal Backwater'), (59, 'Disowned Ancestor'), (60, 'Dragon Grip'), (61, 'Dragon Throne of Tarkir'), (62, "Dragon's Eye Savants"), (63, 'Dragon-Style Twins'), (64, 'Dragonscale Boon'), (65, 'Duneblast'), (66, 'Dutiful Return'), (67, 'Efreet Weaponmaster'), (68, 'Embodiment of Spring'), (69, 'Empty the Pits'), (70, 'End Hostilities'), (71, 'Erase'), (72, 'Feat of Resistance'), (73, 'Feed the Clan'), (74, 'Firehoof Cavalry'), (75, 'Flooded Strand'), (76, 'Flying Crane Technique'), (77, 'Force Away'), (78, 'Forest'), (79, 'Forest'), (80, 'Forest'), (81, 'Forest'), (82, 'Frontier Bivouac'), (83, 'Ghostfire Blade'), (84, 'Glacial Stalker'), (85, 'Goblinslide'), (86, 'Grim Haruspex'), (87, 'Gurmag Swiftwing'), (88, 'Hardened Scales'), (89, 'Heart-Piercer Bow'), (90, 'Heir of the Wilds'), (91, 'Herald of Anafenza'), (92, 'High Sentinels of Arashin'), (93, 'Highland Game'), (94, 'Highspire Mantis'), (95, 'Hooded Hydra'), (96, 'Hooting Mandrills'), (97, 'Horde Ambusher'), (98, 'Hordeling Outburst'), (99, 'Howl of the Horde'), (100, 'Icefeather Aven'), (101, 'Icy Blast'), (102, 'Incremental Growth'), (103, 'Island'), (104, 'Island'), (105, 'Island'), (106, 'Island'), (107, 'Ivorytusk Fortress'), (108, 'Jeering Instigator'), (109, 'Jeskai Ascendancy'), (110, 'Jeskai Banner'), (111, 'Jeskai Charm'), (112, 'Jeskai Elder'), (113, 'Jeskai Student'), (114, 'Jeskai Windscout'), (115, 'Jungle Hollow'), (116, 'Kheru Bloodsucker'), (117, 'Kheru Dreadmaw'), (118, 'Kheru Lich Lord'), (119, 'Kheru Spellsnatcher'), (120, 'Kill Shot'), (121, 'Kin-Tree Invocation'), (122, 'Kin-Tree Warden'), (123, 'Krumar Bond-Kin'), (124, 'Leaping Master'), (125, 'Lens of Clarity'), (126, 'Longshot Squad'), (127, 'Mantis Rider'), (128, 'Mardu Ascendancy'), (129, 'Mardu Banner'), (130, 'Mardu Blazebringer'), (131, 'Mardu Charm'), (132, 'Mardu Hateblade'), (133, 'Mardu Heart-Piercer'), (134, 'Mardu Hordechief'), (135, 'Mardu Roughrider'), (136, 'Mardu Skullhunter'), (137, 'Mardu Warshrieker'), (138, 'Master of Pearls'), (139, 'Master the Way'), (140, 'Meandering Towershell'), (141, 'Mer-Ek Nightblade'), (142, 'Mindswipe'), (143, 'Mistfire Weaver'), (144, 'Molting Snakeskin'), (145, 'Monastery Flock'), (146, 'Monastery Swiftspear'), (147, 'Mountain'), (148, 'Mountain'), (149, 'Mountain'), (150, 'Mountain'), (151, 'Murderous Cut'), (152, 'Mystic Monastery'), (153, 'Mystic of the Hidden Way'), (154, 'Narset, Enlightened Master'), (155, 'Naturalize'), (156, 'Necropolis Fiend'), (157, 'Nomad Outpost'), (158, 'Opulent Palace'), (159, 'Pearl Lake Ancient'), (160, 'Pine Walker'), (161, 'Plains'), (162, 'Plains'), (163, 'Plains'), (164, 'Plains'), (165, 'Polluted Delta'), (166, 'Ponyback Brigade'), (167, 'Quiet Contemplation'), (168, "Raiders' Spoils"), (169, 'Rakshasa Deathdealer'), (170, 'Rakshasa Vizier'), (171, "Rakshasa's Secret"), (172, 'Rattleclaw Mystic'), (173, 'Retribution of the Ancients'), (174, 'Ride Down'), (175, 'Rite of the Serpent'), (176, 'Riverwheel Aerialists'), (177, 'Roar of Challenge'), (178, 'Rotting Mastodon'), (179, 'Rugged Highlands'), (180, 'Rush of Battle'), (181, 'Ruthless Ripper'), (182, 'Sage of the Inward Eye'), (183, 'Sage-Eye Harrier'), (184, 'Sagu Archer'), (185, 'Sagu Mauler'), (186, 'Salt Road Patrol'), (187, 'Sandsteppe Citadel'), (188, 'Sarkhan, the Dragonspeaker'), (189, 'Savage Knuckleblade'), (190, 'Savage Punch'), (191, 'Scaldkin'), (192, 'Scion of Glaciers'), (193, 'Scoured Barrens'), (194, 'Scout the Borders'), (195, 'Secret Plans'), (196, 'See the Unwritten'), (197, 'Seek the Horizon'), (198, 'Seeker of the Way'), (199, 'Set Adrift'), (200, 'Shambling Attendants'), (201, 'Shatter'), (202, "Sidisi's Pet"), (203, 'Sidisi, Brood Tyrant'), (204, 'Siege Rhino'), (205, 'Siegecraft'), (206, 'Singing Bell Strike'), (207, 'Smite the Monstrous'), (208, 'Smoke Teller'), (209, 'Snowhorn Rider'), (210, 'Sorin, Solemn Visitor'), (211, 'Stubborn Denial'), (212, 'Sultai Ascendancy'), (213, 'Sultai Banner'), (214, 'Sultai Charm'), (215, 'Sultai Flayer'), (216, 'Sultai Scavenger'), (217, 'Sultai Soothsayer'), (218, 'Summit Prowler'), (219, 'Surrak Dragonclaw'), (220, 'Suspension Field'), (221, 'Swamp'), (222, 'Swamp'), (223, 'Swamp'), (224, 'Swamp'), (225, 'Swarm of Bloodflies'), (226, 'Swift Kick'), (227, 'Swiftwater Cliffs'), (228, "Taigam's Scheming"), (229, 'Take Up Arms'), (230, 'Temur Ascendancy'), (231, 'Temur Banner'), (232, 'Temur Charger'), (233, 'Temur Charm'), (234, 'Thornwood Falls'), (235, 'Thousand Winds'), (236, 'Throttle'), (237, 'Timely Hordemate'), (238, 'Tomb of the Spirit Dragon'), (239, 'Tormenting Voice'), (240, 'Trail of Mystery'), (241, 'Tranquil Cove'), (242, 'Trap Essence'), (243, 'Treasure Cruise'), (244, 'Trumpet Blast'), (245, 'Tusked Colossodon'), (246, 'Tuskguard Captain'), (247, "Ugin's Nexus"), (248, 'Unyielding Krumar'), (249, 'Utter End'), (250, 'Valley Dasher'), (251, 'Venerable Lammasu'), (252, 'Villainous Wealth'), (253, 'War Behemoth'), (254, 'War-Name Aspirant'), (255, 'Warden of the Eye'), (256, 'Watcher of the Roost'), (257, 'Waterwhirl'), (258, 'Weave Fate'), (259, 'Wetland Sambar'), (260, 'Whirlwind Adept'), (261, 'Wind-Scarred Crag'), (262, 'Windstorm'), (263, 'Windswept Heath'), (264, 'Wingmate Roc'), (265, 'Winterflame'), (266, 'Witness of the Ages'), (267, 'Wooded Foothills'), (268, 'Woolly Loxodon'), (269, 'Zurgo Helmsmasher'), (270, 'Abzan Ascendancy'), (271, 'Anafenza, the Foremost'), (272, 'Ankle Shanker'), (273, 'Ankle Shanker'), (274, 'Avalanche Tusker'), (275, 'Avalanche Tusker'), (276, 'Bloodsoaked Champion'), (277, 'Butcher of the Horde'), (278, 'Crackling Doom'), (279, "Crater's Claws"), (280, 'Deflecting Palm'), (281, 'Dig Through Time'), (282, 'Dragon Throne of Tarkir'), (283, 'Dragon-Style Twins'), (284, 'Duneblast'), (285, 'Flying Crane Technique'), (286, 'Grim Haruspex'), (287, 'Hardened Scales'), (288, 'Heir of the Wilds'), (289, 'Herald of Anafenza'), (290, 'High Sentinels of Arashin'), (291, 'Icy Blast'), (292, 'Ivorytusk Fortress'), (293, 'Ivorytusk Fortress'), (294, 'Jeering Instigator'), (295, 'Jeskai Ascendancy'), (296, 'Kheru Lich Lord'), (297, 'Mardu Ascendancy'), (298, 'Master of Pearls'), (299, 'Narset, Enlightened Master'), (300, 'Necropolis Fiend'), (301, 'Rakshasa Vizier'), (302, 'Rakshasa Vizier'), (303, 'Rattleclaw Mystic'), (304, 'Rattleclaw Mystic'), (305, 'Sage of the Inward Eye'), (306, 'Sage of the Inward Eye'), (307, 'Sidisi, Brood Tyrant'), (308, 'Siege Rhino'), (309, 'Sultai Ascendancy'), (310, 'Sultai Charm'), (311, 'Surrak Dragonclaw'), (312, 'Temur Ascendancy'), (313, 'Thousand Winds'), (314, 'Trail of Mystery'), (315, 'Trap Essence'), (316, 'Utter End'), (317, 'Utter End'), (318, 'Villainous Wealth'), (319, 'Zurgo Helmsmasher')], default=123, max_length=319),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='deck',
            name='cardList',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('name', 'Abomination of Gudul'), ('name', 'Abzan Ascendancy'), ('name', 'Abzan Banner'), ('name', 'Abzan Battle Priest'), ('name', 'Abzan Charm'), ('name', 'Abzan Falconer'), ('name', 'Abzan Guide'), ('name', 'Act of Treason'), ('name', 'Ainok Bond-Kin'), ('name', 'Ainok Tracker'), ('name', 'Alabaster Kirin'), ('name', 'Alpine Grizzly'), ('name', 'Altar of the Brood'), ('name', 'Anafenza, the Foremost'), ('name', 'Ankle Shanker'), ('name', 'Arc Lightning'), ('name', "Archers' Parapet"), ('name', 'Armament Corps'), ('name', 'Arrow Storm'), ('name', 'Ashcloud Phoenix'), ('name', 'Avalanche Tusker'), ('name', 'Awaken the Bear'), ('name', 'Barrage of Boulders'), ('name', "Bear's Companion"), ('name', 'Become Immense'), ('name', 'Bellowing Saddlebrute'), ('name', 'Bitter Revelation'), ('name', 'Blinding Spray'), ('name', 'Bloodfell Caves'), ('name', 'Bloodfire Expert'), ('name', 'Bloodfire Mentor'), ('name', 'Bloodsoaked Champion'), ('name', 'Bloodstained Mire'), ('name', 'Blossoming Sands'), ('name', 'Brave the Sands'), ('name', "Briber's Purse"), ('name', 'Bring Low'), ('name', 'Burn Away'), ('name', 'Butcher of the Horde'), ('name', 'Cancel'), ('name', 'Canyon Lurkers'), ('name', 'Chief of the Edge'), ('name', 'Chief of the Scale'), ('name', 'Clever Impersonator'), ('name', 'Crackling Doom'), ('name', 'Cranial Archive'), ('name', "Crater's Claws"), ('name', 'Crippling Chill'), ('name', 'Dazzling Ramparts'), ('name', 'Dead Drop'), ('name', 'Death Frenzy'), ('name', 'Debilitating Injury'), ('name', 'Defiant Strike'), ('name', 'Deflecting Palm'), ('name', 'Despise'), ('name', 'Dig Through Time'), ('name', 'Disdainful Stroke'), ('name', 'Dismal Backwater'), ('name', 'Disowned Ancestor'), ('name', 'Dragon Grip'), ('name', 'Dragon Throne of Tarkir'), ('name', "Dragon's Eye Savants"), ('name', 'Dragon-Style Twins'), ('name', 'Dragonscale Boon'), ('name', 'Duneblast'), ('name', 'Dutiful Return'), ('name', 'Efreet Weaponmaster'), ('name', 'Embodiment of Spring'), ('name', 'Empty the Pits'), ('name', 'End Hostilities'), ('name', 'Erase'), ('name', 'Feat of Resistance'), ('name', 'Feed the Clan'), ('name', 'Firehoof Cavalry'), ('name', 'Flooded Strand'), ('name', 'Flying Crane Technique'), ('name', 'Force Away'), ('name', 'Forest'), ('name', 'Forest'), ('name', 'Forest'), ('name', 'Forest'), ('name', 'Frontier Bivouac'), ('name', 'Ghostfire Blade'), ('name', 'Glacial Stalker'), ('name', 'Goblinslide'), ('name', 'Grim Haruspex'), ('name', 'Gurmag Swiftwing'), ('name', 'Hardened Scales'), ('name', 'Heart-Piercer Bow'), ('name', 'Heir of the Wilds'), ('name', 'Herald of Anafenza'), ('name', 'High Sentinels of Arashin'), ('name', 'Highland Game'), ('name', 'Highspire Mantis'), ('name', 'Hooded Hydra'), ('name', 'Hooting Mandrills'), ('name', 'Horde Ambusher'), ('name', 'Hordeling Outburst'), ('name', 'Howl of the Horde'), ('name', 'Icefeather Aven'), ('name', 'Icy Blast'), ('name', 'Incremental Growth'), ('name', 'Island'), ('name', 'Island'), ('name', 'Island'), ('name', 'Island'), ('name', 'Ivorytusk Fortress'), ('name', 'Jeering Instigator'), ('name', 'Jeskai Ascendancy'), ('name', 'Jeskai Banner'), ('name', 'Jeskai Charm'), ('name', 'Jeskai Elder'), ('name', 'Jeskai Student'), ('name', 'Jeskai Windscout'), ('name', 'Jungle Hollow'), ('name', 'Kheru Bloodsucker'), ('name', 'Kheru Dreadmaw'), ('name', 'Kheru Lich Lord'), ('name', 'Kheru Spellsnatcher'), ('name', 'Kill Shot'), ('name', 'Kin-Tree Invocation'), ('name', 'Kin-Tree Warden'), ('name', 'Krumar Bond-Kin'), ('name', 'Leaping Master'), ('name', 'Lens of Clarity'), ('name', 'Longshot Squad'), ('name', 'Mantis Rider'), ('name', 'Mardu Ascendancy'), ('name', 'Mardu Banner'), ('name', 'Mardu Blazebringer'), ('name', 'Mardu Charm'), ('name', 'Mardu Hateblade'), ('name', 'Mardu Heart-Piercer'), ('name', 'Mardu Hordechief'), ('name', 'Mardu Roughrider'), ('name', 'Mardu Skullhunter'), ('name', 'Mardu Warshrieker'), ('name', 'Master of Pearls'), ('name', 'Master the Way'), ('name', 'Meandering Towershell'), ('name', 'Mer-Ek Nightblade'), ('name', 'Mindswipe'), ('name', 'Mistfire Weaver'), ('name', 'Molting Snakeskin'), ('name', 'Monastery Flock'), ('name', 'Monastery Swiftspear'), ('name', 'Mountain'), ('name', 'Mountain'), ('name', 'Mountain'), ('name', 'Mountain'), ('name', 'Murderous Cut'), ('name', 'Mystic Monastery'), ('name', 'Mystic of the Hidden Way'), ('name', 'Narset, Enlightened Master'), ('name', 'Naturalize'), ('name', 'Necropolis Fiend'), ('name', 'Nomad Outpost'), ('name', 'Opulent Palace'), ('name', 'Pearl Lake Ancient'), ('name', 'Pine Walker'), ('name', 'Plains'), ('name', 'Plains'), ('name', 'Plains'), ('name', 'Plains'), ('name', 'Polluted Delta'), ('name', 'Ponyback Brigade'), ('name', 'Quiet Contemplation'), ('name', "Raiders' Spoils"), ('name', 'Rakshasa Deathdealer'), ('name', 'Rakshasa Vizier'), ('name', "Rakshasa's Secret"), ('name', 'Rattleclaw Mystic'), ('name', 'Retribution of the Ancients'), ('name', 'Ride Down'), ('name', 'Rite of the Serpent'), ('name', 'Riverwheel Aerialists'), ('name', 'Roar of Challenge'), ('name', 'Rotting Mastodon'), ('name', 'Rugged Highlands'), ('name', 'Rush of Battle'), ('name', 'Ruthless Ripper'), ('name', 'Sage of the Inward Eye'), ('name', 'Sage-Eye Harrier'), ('name', 'Sagu Archer'), ('name', 'Sagu Mauler'), ('name', 'Salt Road Patrol'), ('name', 'Sandsteppe Citadel'), ('name', 'Sarkhan, the Dragonspeaker'), ('name', 'Savage Knuckleblade'), ('name', 'Savage Punch'), ('name', 'Scaldkin'), ('name', 'Scion of Glaciers'), ('name', 'Scoured Barrens'), ('name', 'Scout the Borders'), ('name', 'Secret Plans'), ('name', 'See the Unwritten'), ('name', 'Seek the Horizon'), ('name', 'Seeker of the Way'), ('name', 'Set Adrift'), ('name', 'Shambling Attendants'), ('name', 'Shatter'), ('name', "Sidisi's Pet"), ('name', 'Sidisi, Brood Tyrant'), ('name', 'Siege Rhino'), ('name', 'Siegecraft'), ('name', 'Singing Bell Strike'), ('name', 'Smite the Monstrous'), ('name', 'Smoke Teller'), ('name', 'Snowhorn Rider'), ('name', 'Sorin, Solemn Visitor'), ('name', 'Stubborn Denial'), ('name', 'Sultai Ascendancy'), ('name', 'Sultai Banner'), ('name', 'Sultai Charm'), ('name', 'Sultai Flayer'), ('name', 'Sultai Scavenger'), ('name', 'Sultai Soothsayer'), ('name', 'Summit Prowler'), ('name', 'Surrak Dragonclaw'), ('name', 'Suspension Field'), ('name', 'Swamp'), ('name', 'Swamp'), ('name', 'Swamp'), ('name', 'Swamp'), ('name', 'Swarm of Bloodflies'), ('name', 'Swift Kick'), ('name', 'Swiftwater Cliffs'), ('name', "Taigam's Scheming"), ('name', 'Take Up Arms'), ('name', 'Temur Ascendancy'), ('name', 'Temur Banner'), ('name', 'Temur Charger'), ('name', 'Temur Charm'), ('name', 'Thornwood Falls'), ('name', 'Thousand Winds'), ('name', 'Throttle'), ('name', 'Timely Hordemate'), ('name', 'Tomb of the Spirit Dragon'), ('name', 'Tormenting Voice'), ('name', 'Trail of Mystery'), ('name', 'Tranquil Cove'), ('name', 'Trap Essence'), ('name', 'Treasure Cruise'), ('name', 'Trumpet Blast'), ('name', 'Tusked Colossodon'), ('name', 'Tuskguard Captain'), ('name', "Ugin's Nexus"), ('name', 'Unyielding Krumar'), ('name', 'Utter End'), ('name', 'Valley Dasher'), ('name', 'Venerable Lammasu'), ('name', 'Villainous Wealth'), ('name', 'War Behemoth'), ('name', 'War-Name Aspirant'), ('name', 'Warden of the Eye'), ('name', 'Watcher of the Roost'), ('name', 'Waterwhirl'), ('name', 'Weave Fate'), ('name', 'Wetland Sambar'), ('name', 'Whirlwind Adept'), ('name', 'Wind-Scarred Crag'), ('name', 'Windstorm'), ('name', 'Windswept Heath'), ('name', 'Wingmate Roc'), ('name', 'Winterflame'), ('name', 'Witness of the Ages'), ('name', 'Wooded Foothills'), ('name', 'Woolly Loxodon'), ('name', 'Zurgo Helmsmasher'), ('name', 'Abzan Ascendancy'), ('name', 'Anafenza, the Foremost'), ('name', 'Ankle Shanker'), ('name', 'Ankle Shanker'), ('name', 'Avalanche Tusker'), ('name', 'Avalanche Tusker'), ('name', 'Bloodsoaked Champion'), ('name', 'Butcher of the Horde'), ('name', 'Crackling Doom'), ('name', "Crater's Claws"), ('name', 'Deflecting Palm'), ('name', 'Dig Through Time'), ('name', 'Dragon Throne of Tarkir'), ('name', 'Dragon-Style Twins'), ('name', 'Duneblast'), ('name', 'Flying Crane Technique'), ('name', 'Grim Haruspex'), ('name', 'Hardened Scales'), ('name', 'Heir of the Wilds'), ('name', 'Herald of Anafenza'), ('name', 'High Sentinels of Arashin'), ('name', 'Icy Blast'), ('name', 'Ivorytusk Fortress'), ('name', 'Ivorytusk Fortress'), ('name', 'Jeering Instigator'), ('name', 'Jeskai Ascendancy'), ('name', 'Kheru Lich Lord'), ('name', 'Mardu Ascendancy'), ('name', 'Master of Pearls'), ('name', 'Narset, Enlightened Master'), ('name', 'Necropolis Fiend'), ('name', 'Rakshasa Vizier'), ('name', 'Rakshasa Vizier'), ('name', 'Rattleclaw Mystic'), ('name', 'Rattleclaw Mystic'), ('name', 'Sage of the Inward Eye'), ('name', 'Sage of the Inward Eye'), ('name', 'Sidisi, Brood Tyrant'), ('name', 'Siege Rhino'), ('name', 'Sultai Ascendancy'), ('name', 'Sultai Charm'), ('name', 'Surrak Dragonclaw'), ('name', 'Temur Ascendancy'), ('name', 'Thousand Winds'), ('name', 'Trail of Mystery'), ('name', 'Trap Essence'), ('name', 'Utter End'), ('name', 'Utter End'), ('name', 'Villainous Wealth'), ('name', 'Zurgo Helmsmasher')], max_length=1594, verbose_name='Cards'),
        ),
    ]