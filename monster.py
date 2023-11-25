import random
mob1 = {"name":"Goblin","media":"https://telegra.ph/file/fc186551d3779a508d7a9.mp4",
    "atk":4,"hp":10,"speed":40}

#outer_dungeon_mobs
mob1={'id':1001,"name":"Green Slime","element":"Dark","media":"https://graph.org/file/764cf2b8835bc13e226fc.jpg","atk":12,"def":5,"hp":50,"speed":30,"crit_rate":5,'crit_dmg':50}
mob2={'id':1002,"name":"Goblin Mage","element":"Fire","media":"https://graph.org/file/5c1569044898ec823ca01.jpg","atk":15,"def":2,"hp":45,"speed":70,"crit_rate":5,'crit_dmg':50}
mob3={'id':1003,"name":"Fighter Goblin","element":"Physical","media":"https://graph.org/file/becd0df0ded29686ac658.jpg","atk":13,"def":4,"hp":50,"speed":80,"crit_rate":5,'crit_dmg':50}
mob4={'id':1004,"name":"Skeleton Knight","element":"Physical","media":"https://graph.org/file/43ff9d2dab616fe852a7e.jpg","atk":10,"def":2,"hp":30,"speed":120,"crit_rate":12,'crit_dmg':50}
mob5={'id':1005,"name":"Lizard-Man","element":"Physical","media":"https://graph.org/file/77d350ff7e86531817a9a.jpg","atk":14,"def":4,"hp":40,"speed":70,"crit_rate":5,'crit_dmg':50}
mob6={'id':1006,"name":"Lonely Goblin","element":"Physical","media":"https://graph.org/file/2aa03544d29782176b690.jpg","atk":10,"def":3,"hp":40,"speed":120,"crit_rate":5,'crit_dmg':50}
mob7={'id':1007,"name":"Illuminated Sylph","element":"Light","media":"https://graph.org/file/e82834bf4bc17db4e767c.jpg","atk":16,"def":6,"hp":50,"speed":60,"crit_rate":5,'crit_dmg':50}
mob8={'id':1008,"name":"Flower Gardener","element":"Fire","media":"https://graph.org/file/edc81e0c25b1a8511922d.jpg","atk":16,"def":6,"hp":50,"speed":60,"crit_rate":5,'crit_dmg':50}
mob9={'id':1009,"name":"Chained Ogre","element":"Physical","media":"https://graph.org/file/77102cdf1edd82e66eb9a.jpg","atk":15,"def":8,"hp":50,"speed":70,"crit_rate":5,'crit_dmg':50}
mob10={'id':1010,"name":"Centipede-Infested Monk","element":"Dark","media":"https://graph.org/file/3d333ff6aa888162cf46c.jpg","atk":21,"def":1,"hp":40,"speed":20,"crit_rate":5,'crit_dmg':50}


#MOBS
slimes_mob={'water_slime':{'id':1,"name":"Slime","element":"Water","media":"https://graph.org/file/f598d29851589a6a84e9f.jpg","atk":4,"def":3,"hp":50,"speed":50,"crit_rate":5,'crit_dmg':50},
            'fire_slime':{'id':2,"name":"Slime","element":"Fire","media":"https://graph.org/file/63b509578903b915965da.jpg","atk":4,"def":3,"hp":50,"speed":50,"crit_rate":5,'crit_dmg':50},
            'air_slime':{'id':3,"name":"Slime","element":"Wind","media":"https://graph.org/file/8fa7831eeec3826c87cf1.jpg","atk":4,"def":3,"hp":50,"speed":50,"crit_rate":5,'crit_dmg':50},
            'ice_slime':{'id':4,"name":"Slime","element":"Ice","media":"https://graph.org/file/5d36525523cf4969e195e.jpg","atk":4,"def":3,"hp":50,"speed":50,"crit_rate":5,'crit_dmg':50}}
goblin_mob={'mage_goblin':{'id':5,"name":"Goblin Mage","element":"Fire","media":"https://graph.org/file/739de4046c1e92aa9b453.jpg","atk":6,"def":4,"hp":45,"speed":45,"crit_rate":5,'crit_dmg':50},
            'knife_goblin':{'id':6,"name":"Goblin With Knife","element":"Physcial","media":"https://graph.org/file/f6aca8f1e8786e7f7af7d.jpg","atk":5,"def":3,"hp":50,"speed":65,"crit_rate":5,'crit_dmg':50},
            'hammer_goblin':{'id':7,"name":"Goblin With a Hammer","element":"Physcial","media":"https://graph.org/file/3703e9bb486316634bc85.jpg","atk":8,"def":3,"hp":55,"speed":30,"crit_rate":5,'crit_dmg':50},
            'king_goblin':{'id':8,"name":"Goblin King","element":"Physical","media":"https://graph.org/file/eb9ed401e2d8aa3fcfb87.jpg","atk":7,"def":4,"hp":50,"speed":70,"crit_rate":10,'crit_dmg':60}}
kobold_mob={'mage_kobold':{'id':9,"name":"Kobold Mage","element":"Dark","media":"https://graph.org/file/0da7a97d44e11d852f505.jpg","atk":10,"def":3,"hp":42,"speed":40,"crit_rate":5,'crit_dmg':60},
            'singer_kobold':{'id':10,"name":"Kobold Singer","element":"Physcial","media":"https://graph.org/file/5fe12279b5ef003fe5093.jpg","atk":12,"def":4,"hp":45,"speed":50,"crit_rate":5,'crit_dmg':60},
            'spear_kobold':{'id':11,"name":"Kobold With Spear","element":"Physcial","media":"https://graph.org/file/df89b2e83bfb1d8ba4064.jpg","atk":8,"def":3,"hp":52,"speed":75,"crit_rate":5,'crit_dmg':60},
            'knife_kobold':{'id':12,"name":"Kobold with knife","element":"Physical","media":"https://graph.org/file/d375c7e8870babf5c93fc.jpg","atk":7,"def":4,"hp":42,"speed":80,"crit_rate":5,'crit_dmg':60}}
skeleton_mob={'undead_skeleton':{'id':13,"name":"Undead Skeleton","element":"Dark","media":"https://telegra.ph/file/d1a6537291c9dc8bee15a.jpg","atk":15,"def":2,"hp":50,"speed":120,"crit_rate":5,'crit_dmg':60},
            'priest_skeleton':{'id':14,"name":"Skeleton Priest","element":"Light","media":"https://telegra.ph/file/ce30195119524798cdd75.jpg","atk":18,"def":1,"hp":55,"speed":150,"crit_rate":5,'crit_dmg':60},
            'mage_skeleton':{'id':15,"name":"Skeleton Mage","element":"Fire","media":"https://telegra.ph/file/80d2155db0b29800674f8.jpg","atk":20,"def":3,"hp":40,"speed":95,"crit_rate":5,'crit_dmg':60},
            'dragon_skeleton':{'id':16,"name":"Skeleton Dragon","element":"Physical","media":"https://telegra.ph/file/e0b9125fb4635b9aa31d3.jpg","atk":27,"def":4,"hp":70,"speed":50,"crit_rate":5,'crit_dmg':60}}



#dungeon level wise
dungeon_1_mobs=[slimes_mob['water_slime'],slimes_mob['fire_slime'],slimes_mob['ice_slime'],slimes_mob['air_slime']]
dungeon_2_mobs=[goblin_mob['mage_goblin'],goblin_mob['knife_goblin'],goblin_mob['hammer_goblin'],goblin_mob['king_goblin']]
dungeon_3_mobs=[kobold_mob['mage_kobold'],kobold_mob['singer_kobold'],kobold_mob['spear_kobold'],kobold_mob['knife_kobold']]
dungeon_4_mobs=[skeleton_mob['undead_skeleton'],skeleton_mob['priest_skeleton'],skeleton_mob['mage_skeleton'],skeleton_mob['dragon_skeleton']]

#dungeon
dungeon_mobs={"level_1":dungeon_1_mobs,"level_2":dungeon_2_mobs,"level_3":dungeon_3_mobs,"level_4":dungeon_4_mobs}

#hell_region MOBS
mobs=[mob1,mob2,mob3,mob4,mob5,mob6,mob7,mob8,mob9,mob10]

#tower_mons
fire_boss={'level_1':{'id':10001,"name":"IFRIT","element":"Fire","media":"https://graph.org/file/dc87234b08096395ee287.jpg","atk":12,"def":5,"hp":100,"speed":10,"crit_rate":10,'crit_dmg':50,'level':1},
           'level_2':{'id':10001,"name":"IFRIT","element":"Fire","media":"https://graph.org/file/dc87234b08096395ee287.jpg","atk":15,"def":6,"hp":200,"speed":20,"crit_rate":10,'crit_dmg':50,'level':2},
           'level_3':{'id':10001,"name":"IFRIT","element":"Fire","media":"https://graph.org/file/dc87234b08096395ee287.jpg","atk":18,"def":7,"hp":300,"speed":30,"crit_rate":10,'crit_dmg':50,'level':3},
           'level_4':{'id':10001,"name":"IFRIT","element":"Fire","media":"https://graph.org/file/dc87234b08096395ee287.jpg","atk":21,"def":8,"hp":400,"speed":40,"crit_rate":10,'crit_dmg':50,'level':4},
           'level_5':{'id':10001,"name":"IFRIT","element":"Fire","media":"https://graph.org/file/dc87234b08096395ee287.jpg","atk":25,"def":9,"hp":500,"speed":50,"crit_rate":10,'crit_dmg':50,'level':5},
           'level_6':{'id':10001,"name":"IFRIT","element":"Fire","media":"https://graph.org/file/dc87234b08096395ee287.jpg","atk":30,"def":10,"hp":600,"speed":60,"crit_rate":10,'crit_dmg':50,'level':6}}

ice_boss={'level_1':{'id':10002,"name":"ICE DRAGON","element":"Ice","media":"https://graph.org/file/6ff082013758e1a538eb9.jpg","atk":10,"def":5,"hp":100,"speed":10,"crit_rate":20,'crit_dmg':60,'level':1},
          'level_2':{'id':10002,"name":"ICE DRAGON","element":"Ice","media":"https://graph.org/file/6ff082013758e1a538eb9.jpg","atk":12,"def":6,"hp":200,"speed":20,"crit_rate":21,'crit_dmg':60,'level':2},
          'level_3':{'id':10002,"name":"ICE DRAGON","element":"Ice","media":"https://graph.org/file/6ff082013758e1a538eb9.jpg","atk":15,"def":7,"hp":300,"speed":30,"crit_rate":22,'crit_dmg':60,'level':3},
          'level_4':{'id':10002,"name":"ICE DRAGON","element":"Ice","media":"https://graph.org/file/6ff082013758e1a538eb9.jpg","atk":20,"def":8,"hp":400,"speed":40,"crit_rate":23,'crit_dmg':60,'level':4},
          'level_5':{'id':10002,"name":"ICE DRAGON","element":"Ice","media":"https://graph.org/file/6ff082013758e1a538eb9.jpg","atk":22,"def":9,"hp":500,"speed":50,"crit_rate":24,'crit_dmg':60,'level':5},
          'level_6':{'id':10002,"name":"ICE DRAGON","element":"Ice","media":"https://graph.org/file/6ff082013758e1a538eb9.jpg","atk":25,"def":10,"hp":600,"speed":60,"crit_rate":25,'crit_dmg':60,'level':6}}

wind_boss={'level_1':{'id':10003,"name":"DIAMONES","element":"Wind","media":"https://graph.org/file/ae1a4099565a134676ed2.jpg","atk":11,"def":5,"hp":105,"speed":200,"crit_rate":5,'crit_dmg':50,'level':1},
           'level_2':{'id':10003,"name":"DIAMONES","element":"Wind","media":"https://graph.org/file/ae1a4099565a134676ed2.jpg","atk":14,"def":6,"hp":205,"speed":210,"crit_rate":5,'crit_dmg':50,'level':2},
           'level_3':{'id':10003,"name":"DIAMONES","element":"Wind","media":"https://graph.org/file/ae1a4099565a134676ed2.jpg","atk":16,"def":7,"hp":305,"speed":220,"crit_rate":5,'crit_dmg':50,'level':3},
           'level_4':{'id':10003,"name":"DIAMONES","element":"Wind","media":"https://graph.org/file/ae1a4099565a134676ed2.jpg","atk":19,"def":8,"hp":405,"speed":230,"crit_rate":5,'crit_dmg':50,'level':4},
           'level_5':{'id':10003,"name":"DIAMONES","element":"Wind","media":"https://graph.org/file/ae1a4099565a134676ed2.jpg","atk":23,"def":9,"hp":505,"speed":240,"crit_rate":5,'crit_dmg':50,'level':5},
           'level_6':{'id':10003,"name":"DIAMONES","element":"Wind","media":"https://graph.org/file/ae1a4099565a134676ed2.jpg","atk":26,"def":10,"hp":605,"speed":250,"crit_rate":5,'crit_dmg':50,'level':6}}

water_boss={'level_1':{'id':10004,"name":"OSIAL","element":"Water","media":"https://graph.org/file/720a9f16e6b8aeaf968e0.jpg","atk":10,"def":6,"hp":110,"speed":10,"crit_rate":5,'crit_dmg':50,'level':1},
            'level_2':{'id':10004,"name":"OSIAL","element":"Water","media":"https://graph.org/file/720a9f16e6b8aeaf968e0.jpg","atk":12,"def":7,"hp":250,"speed":20,"crit_rate":5,'crit_dmg':50,'level':2},
            'level_3':{'id':10004,"name":"OSIAL","element":"Water","media":"https://graph.org/file/720a9f16e6b8aeaf968e0.jpg","atk":15,"def":8,"hp":380,"speed":30,"crit_rate":5,'crit_dmg':50,'level':3},
            'level_4':{'id':10004,"name":"OSIAL","element":"Water","media":"https://graph.org/file/720a9f16e6b8aeaf968e0.jpg","atk":18,"def":9,"hp":430,"speed":40,"crit_rate":5,'crit_dmg':50,'level':4},
            'level_5':{'id':10004,"name":"OSIAL","element":"Water","media":"https://graph.org/file/720a9f16e6b8aeaf968e0.jpg","atk":20,"def":10,"hp":560,"speed":50,"crit_rate":5,'crit_dmg':50,'level':5},
            'level_6':{'id':10004,"name":"OSIAL","element":"Water","media":"https://graph.org/file/720a9f16e6b8aeaf968e0.jpg","atk":23,"def":12,"hp":700,"speed":60,"crit_rate":5,'crit_dmg':50,'level':6}}

earth_boss={'level_1':{'id':10005,"name":"GENESIS","element":"Earth","media":"https://graph.org/file/d0a8efa73b2fa89e7cfb0.jpg","atk":10,"def":7,"hp":100,"speed":10,"crit_rate":5,'crit_dmg':50,'level':1},
            'level_2':{'id':10005,"name":"GENESIS","element":"Earth","media":"https://graph.org/file/d0a8efa73b2fa89e7cfb0.jpg","atk":12,"def":9,"hp":200,"speed":20,"crit_rate":5,'crit_dmg':50,'level':2},
            'level_3':{'id':10005,"name":"GENESIS","element":"Earth","media":"https://graph.org/file/d0a8efa73b2fa89e7cfb0.jpg","atk":15,"def":12,"hp":300,"speed":30,"crit_rate":5,'crit_dmg':50,'level':3},
            'level_4':{'id':10005,"name":"GENESIS","element":"Earth","media":"https://graph.org/file/d0a8efa73b2fa89e7cfb0.jpg","atk":18,"def":17,"hp":400,"speed":40,"crit_rate":5,'crit_dmg':50,'level':4},
            'level_5':{'id':10005,"name":"GENESIS","element":"Earth","media":"https://graph.org/file/d0a8efa73b2fa89e7cfb0.jpg","atk":21,"def":20,"hp":500,"speed":50,"crit_rate":5,'crit_dmg':50,'level':5},
            'level_6':{'id':10005,"name":"GENESIS","element":"Earth","media":"https://graph.org/file/d0a8efa73b2fa89e7cfb0.jpg","atk":24,"def":25,"hp":600,"speed":60,"crit_rate":5,'crit_dmg':50,'level':6}}

electro_boss={'level_1':{'id':10006,"name":"ELECTRO WARRIO","element":"Electric","media":"https://graph.org/file/aed1a67aee81cd153ad3f.jpg","atk":10,"def":5,"hp":100,"speed":100,"crit_rate":5,'crit_dmg':50,'level':1},
              'level_2':{'id':10006,"name":"ELECTRO WARRIO","element":"Electric","media":"https://graph.org/file/aed1a67aee81cd153ad3f.jpg","atk":12,"def":6,"hp":200,"speed":200,"crit_rate":5,'crit_dmg':50,'level':2},
              'level_3':{'id':10006,"name":"ELECTRO WARRIO","element":"Electric","media":"https://graph.org/file/aed1a67aee81cd153ad3f.jpg","atk":15,"def":7,"hp":300,"speed":300,"crit_rate":5,'crit_dmg':50,'level':3},
              'level_4':{'id':10006,"name":"ELECTRO WARRIO","element":"Electric","media":"https://graph.org/file/aed1a67aee81cd153ad3f.jpg","atk":18,"def":8,"hp":400,"speed":400,"crit_rate":5,'crit_dmg':50,'level':4},
              'level_5':{'id':10006,"name":"ELECTRO WARRIO","element":"Electric","media":"https://graph.org/file/aed1a67aee81cd153ad3f.jpg","atk":20,"def":9,"hp":500,"speed":500,"crit_rate":5,'crit_dmg':50,'level':5},
              'level_6':{'id':10006,"name":"ELECTRO WARRIO","element":"Electric","media":"https://graph.org/file/aed1a67aee81cd153ad3f.jpg","atk":23,"def":10,"hp":600,"speed":550,"crit_rate":5,'crit_dmg':50,'level':6}}

light_boss={'level_1':{'id':10006,"name":"LIGHT MENDER","element":"Light","media":"https://graph.org/file/c13f935b1112199d19f4c.jpg","atk":11,"def":6,"hp":100,"speed":20,"crit_rate":5,'crit_dmg':50,'level':1},
            'level_2':{'id':10006,"name":"LIGHT MENDER","element":"Light","media":"https://graph.org/file/c13f935b1112199d19f4c.jpg","atk":13,"def":7,"hp":200,"speed":40,"crit_rate":5,'crit_dmg':50,'level':2},
            'level_3':{'id':10006,"name":"LIGHT MENDER","element":"Light","media":"https://graph.org/file/c13f935b1112199d19f4c.jpg","atk":16,"def":8,"hp":300,"speed":60,"crit_rate":5,'crit_dmg':50,'level':3},
            'level_4':{'id':10006,"name":"LIGHT MENDER","element":"Light","media":"https://graph.org/file/c13f935b1112199d19f4c.jpg","atk":19,"def":9,"hp":400,"speed":80,"crit_rate":5,'crit_dmg':50,'level':4},
            'level_5':{'id':10006,"name":"LIGHT MENDER","element":"Light","media":"https://graph.org/file/c13f935b1112199d19f4c.jpg","atk":22,"def":10,"hp":500,"speed":100,"crit_rate":5,'crit_dmg':50,'level':5},
            'level_6':{'id':10006,"name":"LIGHT MENDER","element":"Light","media":"https://graph.org/file/c13f935b1112199d19f4c.jpg","atk":26,"def":11,"hp":600,"speed":120,"crit_rate":5,'crit_dmg':50,'level':6}}

dark_boss={'level_1':{'id':10007,"name":"CHARISMATIC FLAWLESS","element":"Dark","media":"https://graph.org/file/cc9adcdc9e393ccaddbd0.jpg","atk":11,"def":6,"hp":100,"speed":20,"crit_rate":5,'crit_dmg':70,'level':1},
           'level_2':{'id':10007,"name":"CHARISMATIC FLAWLESS","element":"Dark","media":"https://graph.org/file/cc9adcdc9e393ccaddbd0.jpg","atk":14,"def":7,"hp":200,"speed":40,"crit_rate":5,'crit_dmg':70,'level':2},
           'level_3':{'id':10007,"name":"CHARISMATIC FLAWLESS","element":"Dark","media":"https://graph.org/file/cc9adcdc9e393ccaddbd0.jpg","atk":16,"def":8,"hp":300,"speed":60,"crit_rate":5,'crit_dmg':70,'level':3},
           'level_4':{'id':10007,"name":"CHARISMATIC FLAWLESS","element":"Dark","media":"https://graph.org/file/cc9adcdc9e393ccaddbd0.jpg","atk":19,"def":9,"hp":400,"speed":80,"crit_rate":5,'crit_dmg':70,'level':4},
           'level_5':{'id':10007,"name":"CHARISMATIC FLAWLESS","element":"Dark","media":"https://graph.org/file/cc9adcdc9e393ccaddbd0.jpg","atk":23,"def":10,"hp":500,"speed":100,"crit_rate":5,'crit_dmg':70,'level':5},
           'level_6':{'id':10007,"name":"CHARISMATIC FLAWLESS","element":"Dark","media":"https://graph.org/file/cc9adcdc9e393ccaddbd0.jpg","atk":26,"def":12,"hp":600,"speed":120,"crit_rate":5,'crit_dmg':70,'level':6}}

physical_boss={'level_1':{'id':10008,"name":"ISSHIN","element":"Physical","media":"https://graph.org/file/83c92efaab164cce53293.jpg","atk":10,"def":5,"hp":95,"speed":20,"crit_rate":5,'crit_dmg':70,'level':1},
               'level_2':{'id':10008,"name":"ISSHIN","element":"Physical","media":"https://graph.org/file/83c92efaab164cce53293.jpg","atk":15,"def":6,"hp":190,"speed":50,"crit_rate":5,'crit_dmg':70,'level':2},
               'level_3':{'id':10008,"name":"ISSHIN","element":"Physical","media":"https://graph.org/file/83c92efaab164cce53293.jpg","atk":18,"def":7,"hp":285,"speed":80,"crit_rate":5,'crit_dmg':70,'level':3},
               'level_4':{'id':10008,"name":"ISSHIN","element":"Physical","media":"https://graph.org/file/83c92efaab164cce53293.jpg","atk":24,"def":8,"hp":380,"speed":100,"crit_rate":5,'crit_dmg':70,'level':4},
               'level_5':{'id':10008,"name":"ISSHIN","element":"Physical","media":"https://graph.org/file/83c92efaab164cce53293.jpg","atk":28,"def":9,"hp":475,"speed":120,"crit_rate":5,'crit_dmg':70,'level':5},
               'level_6':{'id':10008,"name":"ISSHIN","element":"Physical","media":"https://graph.org/file/83c92efaab164cce53293.jpg","atk":32,"def":10,"hp":570,"speed":150,"crit_rate":5,'crit_dmg':70,'level':6}}

tower_mons={"tow_fire":fire_boss,"tow_ice":ice_boss,"tow_wind":wind_boss,"tow_water":water_boss,'tow_earth':earth_boss,'tow_electric':electro_boss,'tow_light':light_boss,'tow_dark':dark_boss,'tow_physical':physical_boss}