#!/usr/bin/env python
# coding: utf-8


data_list = [['first_name', 'last_name', 'city', 'state', 'post', 'phone1', 'email',]
 ['Rebbecca', 'Didio', 'Leith', 'TAS', 7315, '03-8174-9123', 'rebbecca.didio@didio.com.au',]
 ['Stevie', 'Hallo', 'Proston', 'QLD', 4613, '07-9997-3366', 'stevie.hallo@hotmail.com',]
 ['Mariko', 'Stayer', 'Hamel', 'WA', 6215, '08-5558-9019', 'mariko_stayer@hotmail.com',]
 ['Gerardo', 'Woodka', 'Talmalmo', 'NSW', 2640, '02-6044-4682', 'gerardo_woodka@hotmail.com',]
 ['Mayra', 'Bena', 'Lane Cove', 'NSW', 1595, '02-1455-6085', 'mayra.bena@gmail.com',]
 ['Idella', 'Scotland', 'Cartmeticup', 'WA', 6316, '08-7868-1355', 'idella@hotmail.com',]
 ['Sherill', 'Klar', 'Nyamup', 'WA', 6258, '08-6522-8931', 'sklar@hotmail.com',]
 ['Ena', 'Desjardiws', 'Bendick Murrell', 'NSW', 2803, '02-5226-9402', 'ena_desjardiws@desjardiws.com.au',]
 ['Vince', 'Siena', 'Purrawunda', 'QLD', 4356, '07-3184-9989', 'vince_siena@yahoo.com',]
 ['Theron', 'Jarding', 'Blanchetown', 'SA', 5357, '08-6890-4661', 'tjarding@hotmail.com',]
 ['Amira', 'Chudej', 'Rockside', 'QLD', 4343, '07-8135-3271', 'amira.chudej@chudej.net.au',]
 ['Marica', 'Tarbor', 'Rosegarland', 'TAS', 7140, '03-1174-6817', 'marica.tarbor@hotmail.com',]
 ['Shawna', 'Albrough', 'Ringwood', 'QLD', 4343, '07-7977-6039', 'shawna.albrough@albrough.com.au',]
 ['Paulina', 'Maker', 'Maylands', 'WA', 6931, '08-8344-8929', 'paulina_maker@maker.net.au',]
 ['Rose', 'Jebb', 'Wooloowin', 'QLD', 4030, '07-4941-9471', 'rose@jebb.net.au',]
 ['Reita', 'Tabar', 'Arthurville', 'NSW', 2820, '02-3518-7078', 'rtabar@hotmail.com',]
 ['Maybelle', 'Bewley', 'Mapleton', 'QLD', 4560, '07-9387-7293', 'mbewley@yahoo.com',]
 ['Camellia', 'Pylant', 'Tuggerawong', 'NSW', 2259, '02-5171-4345', 'camellia_pylant@gmail.com',]
 ['Roy', 'Nybo', 'Red Hill', 'ACT', 2603, '02-5311-7778', 'rnybo@nybo.net.au',]
 ['Albert', 'Sonier', 'Inverlaw', 'QLD', 4610, '07-9354-2612', 'albert.sonier@gmail.com',]
 ['Hayley', 'Taghon', 'Eugowra', 'NSW', 2806, '02-1638-4380', 'htaghon@taghon.net.au',]
 ['Norah', 'Daleo', 'Kotara Fair', 'NSW', 2289, '02-5322-6127', 'ndaleo@daleo.net.au',]
 ['Rosina', 'Sidhu', 'Burpengary', 'QLD', 4505, '07-6460-4488', 'rosina_sidhu@gmail.com',]
 ['Royal', 'Costeira', 'Ellis Beach', 'QLD', 4879, '07-5338-6357', 'royal_costeira@costeira.com.au',]
 ['Barrie', 'Nicley', 'Fish Creek', 'VIC', 3959, '03-6443-2786', 'bnicley@nicley.com.au',]
 ['Linsey', 'Gedman', 'Kennedy', 'QLD', 4816, '07-4785-3781', 'lgedman@gedman.net.au',]
 ['Laura', 'Bourbonnais', 'Cape Portland', 'TAS', 7264, '03-6543-6688', 'laura.bourbonnais@yahoo.com',]
 ['Fanny', 'Stoneking', 'Warra', 'QLD', 4411, '07-3721-9123', 'fstoneking@hotmail.com',]
 ['Kristian', 'Ellerbusch', 'Wanguri', 'NT', 810, '08-2748-1250', 'kristian@yahoo.com',]
 ['Gwen', 'Julye', 'Alvie', 'VIC', 3249, '03-7063-6734', 'gjulye@hotmail.com',]
 ['Ben', 'Majorga', 'Wherrol Flat', 'NSW', 2429, '02-8171-9051', 'ben.majorga@hotmail.com',]
 ['Trina', 'Oto', 'Placid Hills', 'QLD', 4343, '07-1153-8567', 'trina@oto.com.au',]
 ['Emelda', 'Geffers', 'Nedlands', 'WA', 6909, '08-7097-3947', 'emelda.geffers@gmail.com',]
 ['Zana', 'Ploszaj', 'Auchenflower', 'QLD', 4066, '07-7991-8880', 'zana_ploszaj@ploszaj.net.au',]
 ['Shaun', 'Rael', 'Buninyong', 'VIC', 3357, '03-8998-5485', 'shaun.rael@rael.com.au',]
 ['Oren', 'Lobosco', 'Dangar Island', 'NSW', 2083, '02-5046-1307', 'olobosco@hotmail.com',]
 ['Catherin', 'Aguele', 'Sunny Nook', 'QLD', 4605, '07-6476-1399', 'caguele@gmail.com',]
 ['Pearlene', 'Boudrie', 'Minden', 'QLD', 4311, '07-4463-7223', 'pboudrie@boudrie.net.au',]
 ['Kathryn', 'Bonalumi', 'Tibradden', 'WA', 6532, '08-3071-2258', 'kathryn.bonalumi@yahoo.com',]
 ['Suzan', 'Landa', 'Clermont', 'QLD', 4721, '07-1576-1412', 'suzan.landa@gmail.com',]
 ['Sommer', 'Agar', 'Kadina', 'SA', 5554, '08-9130-3372', 'sagar@agar.net.au',]
 ['Keena', 'Rebich', 'Sawtell', 'NSW', 2452, '02-4972-3570', 'krebich@rebich.net.au',]
 ['Rupert', 'Hinkson', 'East Gosford', 'NSW', 2250, '02-7160-2066', 'rupert_hinkson@hinkson.net.au',]
 ['Aleta', 'Poarch', 'Fosterville', 'VIC', 3557, '03-2691-1298', 'apoarch@gmail.com',]
 ['Jamal', 'Korczynski', 'Bateau Bay', 'NSW', 2261, '02-3877-9654', 'jamal_korczynski@gmail.com',]
 ['Luz', 'Broccoli', 'Glenmoral', 'QLD', 4719, '07-2679-1774', 'luz_broccoli@hotmail.com',]
 ['Janessa', 'Ruthers', 'Bolivia', 'NSW', 2372, '02-2367-6845', 'janessa@yahoo.com',]
 ['Lavonne', 'Esco', 'East Melbourne', 'VIC', 3002, '03-3474-2120', 'lavonne.esco@yahoo.com',]
 ['Honey', 'Lymaster', 'Taringa', 'QLD', 4068, '07-8087-2603', 'honey_lymaster@lymaster.net.au',]
 ['Jean', 'Cecchinato', 'Koolan Island', 'WA', 6733, '08-5263-2786', 'jean.cecchinato@gmail.com',]
 ['Katlyn', 'Flitcroft', 'Maleny', 'QLD', 4552, '07-1778-9968', 'kflitcroft@hotmail.com',]
 ['Cassie', 'Soros', 'Yelverton', 'WA', 6280, '08-2666-6390', 'csoros@gmail.com',]
 ['Rolf', 'Gene', 'Flinders', 'NSW', 2529, '02-4458-2810', 'rolf_gene@gene.com.au',]
 ['Darnell', 'Moothart', 'Empire Bay', 'NSW', 2257, '02-3996-9188', 'darnell_moothart@yahoo.com',]
 ['Cherilyn', 'Fraize', 'Rose Bay North', 'NSW', 2030, '02-4873-1914', 'cherilyn_fraize@fraize.net.au',]
 ['Lynda', 'Lazzaro', 'Macks Creek', 'VIC', 3971, '03-4933-4205', 'lynda.lazzaro@gmail.com',]
 ['Leigha', 'Capelli', 'East Toowoomba', 'QLD', 4350, '07-4823-9785', 'leigha.capelli@capelli.com.au',]
 ['Delfina', 'Binnie', 'Bimbijy', 'WA', 6472, '08-3692-5784', 'delfina_binnie@binnie.net.au',]
 ['Carlota', 'Gephardt', 'Kundabung', 'NSW', 2441, '02-5078-4389', 'carlota.gephardt@gephardt.com.au',]
 ['Alida', 'Helger', 'Pinnacle', 'QLD', 4741, '07-1642-3251', 'alida@helger.com.au',]
 ['Donte', 'Resureccion', 'Watsonville', 'QLD', 4887, '07-2373-6048', 'donte.resureccion@yahoo.com',]
 ['Lou', 'Kriner', 'Seaforth', 'NSW', 2092, '02-7328-3350', 'lou.kriner@hotmail.com',]
 ['Dortha', 'Vrieze', 'White Hills', 'TAS', 7258, '03-1981-6209', 'dortha@vrieze.net.au',]
 ['Genevive', 'Sanborn', 'Bellangry', 'NSW', 2446, '02-6246-5711', 'genevive@hotmail.com',]
 ['Alease', 'Strawbridge', 'Ascot', 'QLD', 4359, '07-3760-1546', 'alease_strawbridge@strawbridge.com.au',]
 ['Veda', 'Mishkin', 'Stafford Heights', 'QLD', 4053, '07-6034-2422', 'veda.mishkin@mishkin.com.au',]
 ['Craig', 'Vandersloot', 'Bygalorie', 'NSW', 2669, '02-5487-7528', 'craig_vandersloot@yahoo.com',]
 ['Lauran', 'Tovmasyan', 'Boolaroo', 'NSW', 2284, '02-2546-5344', 'ltovmasyan@tovmasyan.net.au',]
 ['Aaron', 'Kloska', 'Brookhill', 'QLD', 4816, '07-9896-4827', 'aaron_kloska@kloska.net.au',]
 ['Francene', 'Skursky', 'Hillston', 'NSW', 2675, '02-5941-3178', 'francene.skursky@skursky.net.au',]
 ['Zena', 'Daria', 'Ivanhoe East', 'VIC', 3079, '03-2822-8156', 'zdaria@gmail.com',]
 ['Brigette', 'Breckenstein', 'Caniambo', 'VIC', 3630, '03-5722-3451', 'brigette@breckenstein.com.au',]
 ['Jeniffer', 'Jezek', 'Myrniong', 'VIC', 3341, '03-3268-5102', 'jeniffer@gmail.com',]
 ['Selma', 'Elm', 'Woolamai', 'VIC', 3995, '03-9183-9493', 'selm@elm.net.au',]
 ['Elenora', 'Handler', 'Wardering', 'WA', 6311, '08-5671-3318', 'ehandler@yahoo.com',]
 ['Nadine', 'Okojie', 'Kukerin', 'WA', 6352, '08-9746-2341', 'nadine.okojie@okojie.com.au',]
 ['Kristin', 'Shiflet', 'Somers', 'VIC', 3927, '03-4529-7210', 'kristin@hotmail.com',]
 ['Melinda', 'Fellhauer', 'Wayatinah', 'TAS', 7140, '03-4387-3800', 'melinda_fellhauer@fellhauer.com.au',]
 ['Kirby', 'Litherland', 'Alligator Creek', 'QLD', 4740, '07-5284-3845', 'kirby.litherland@hotmail.com',]
 ['Kent', 'Ivans', 'Camp Mountain', 'QLD', 4520, '07-8661-4016', 'kent_ivans@yahoo.com',]
 ['Dan', 'Platz', 'Brandy Creek', 'QLD', 4800, '07-4306-1623', 'dan_platz@hotmail.com',]
 ['Millie', 'Pirkl', 'Sovereign Hill', 'VIC', 3350, '03-6023-2680', 'millie_pirkl@gmail.com',]
 ['Moira', 'Qadir', 'Arno Bay', 'SA', 5603, '08-7687-4883', 'moira.qadir@gmail.com',]
 ['Reta', 'Qazi', 'Maffra', 'VIC', 3860, '03-1974-9948', 'reta.qazi@yahoo.com',]
 ['Brittney', 'Lolley', 'Ulverstone', 'TAS', 7315, '03-4072-7094', 'brittney@lolley.net.au',]
 ['Leandro', 'Bolka', 'Wattle Hill', 'TAS', 7172, '03-8157-4609', 'leandro_bolka@hotmail.com',]
 ['Edison', 'Sumera', 'Bower', 'SA', 5374, '08-9114-1763', 'edison.sumera@sumera.net.au',]
 ['Breana', 'Cassi', 'Stonehaven', 'VIC', 3221, '03-2305-8627', 'breana@yahoo.com',]
 ['Jarvis', 'Nicols', 'East Newdegate', 'WA', 6355, '08-2117-5217', 'jarvis@gmail.com',]
 ['Felicitas', 'Orlinski', 'Emerald', 'VIC', 3782, '03-2451-1896', 'felicitas_orlinski@orlinski.com.au',]
 ['Geraldine', 'Neisius', 'Katunga', 'VIC', 3640, '03-8243-2999', 'geraldine@gmail.com',]
 ['Alfred', 'Pacleb', 'Willunga', 'SA', 5172, '08-9450-7978', 'alfred@pacleb.net.au',]
 ['Leatha', 'Block', 'Two Rocks', 'WA', 6037, '08-7635-8350', 'leatha_block@gmail.com',]
 ['Jacquelyne', 'Rosso', 'Caldwell', 'NSW', 2710, '02-4565-6425', 'jacquelyne.rosso@yahoo.com',]
 ['Jonelle', 'Epps', 'Coppabella', 'QLD', 4741, '07-8085-8351', 'jepps@hotmail.com',]
 ['Rosamond', 'Amlin', 'Calala', 'NSW', 2340, '02-8007-5034', 'rosamond.amlin@gmail.com',]
 ['Johnson', 'Mcenery', 'Nambucca Heads', 'NSW', 2448, '02-1718-4983', 'johnson@gmail.com',]
 ['Elliot', 'Scatton', 'Mccullys Gap', 'NSW', 2333, '02-3647-9507', 'elliot.scatton@hotmail.com',]
 ['Gerri', 'Perra', 'Toowoomba South', 'QLD', 4350, '07-6019-7861', 'gerri@yahoo.com',]
 ['Rosendo', 'Jelsma', 'Applecross', 'WA', 6953, '08-7712-4785', 'rosendo_jelsma@hotmail.com',]
 ['Eveline', 'Brickhouse', 'Camberwell West', 'VIC', 3124, '03-9517-9800', 'eveline@yahoo.com',]
 ['Laurene', 'Bennett', 'North Perth', 'WA', 6906, '08-2969-2908', 'laurene_bennett@gmail.com',]
 ['Tegan', 'Ebershoff', 'Coombell', 'NSW', 2470, '02-6604-9720', 'tegan_ebershoff@hotmail.com',]
 ['Tracie', 'Huro', 'Pacific Heights', 'QLD', 4703, '07-1951-6787', 'thuro@gmail.com',]
 ['Mertie', 'Kazeck', 'Guildford', 'WA', 6935, '08-5475-6162', 'mertie.kazeck@kazeck.com.au',]
 ['Clare', 'Bortignon', 'Herron', 'WA', 6210, '08-9256-6135', 'clare_bortignon@hotmail.com',]
 ['Rebeca', 'Baley', 'Mirrool', 'NSW', 2665, '02-7049-7728', 'rebeca_baley@hotmail.com',]
 ['Nilsa', 'Pawell', 'Bundaberg West', 'QLD', 4670, '07-8997-8513', 'npawell@pawell.net.au',]
 ['Samuel', 'Arellanes', 'Lane Cove', 'NSW', 1595, '02-7995-6787', 'samuel.arellanes@arellanes.net.au',]
 ['Ivette', 'Servantes', 'Reservoir', 'VIC', 3073, '03-9801-9429', 'ivette_servantes@servantes.com.au',]
 ['Merrilee', 'Fajen', 'Upper Kedron', 'QLD', 4055, '07-9104-1459', 'merrilee@fajen.net.au',]
 ['Gianna', 'Eilers', 'Buchan', 'VIC', 3885, '03-4328-5253', 'gianna@yahoo.com',]
 ['Hyman', 'Phinazee', 'Beltana', 'SA', 5730, '08-5756-9456', 'hphinazee@yahoo.com',]
 ['Buck', 'Pascucci', 'Kingswood', 'SA', 5062, '08-9279-1731', 'buck@yahoo.com',]
 ['Kenny', 'Leicht', 'Nicholls Rivulet', 'TAS', 7112, '03-6240-8274', 'kenny@leicht.com.au',]
 ['Tabetha', 'Bai', 'Upper Mount Gravatt', 'QLD', 4122, '07-6813-6477', 'tabetha.bai@gmail.com',]
 ['Alonso', 'Popper', 'Ridgley', 'TAS', 7321, '03-7036-7071', 'alonso_popper@hotmail.com',]
 ['Alonzo', 'Polek', 'Tubbut', 'VIC', 3888, '03-2403-7167', 'alonzo_polek@polek.net.au',]
 ['Son', 'Magnotta', 'Collingullie', 'NSW', 2650, '02-2376-7653', 'son.magnotta@magnotta.net.au',]
 ['Jesusita', 'Druck', 'Munno Para', 'SA', 5115, '08-3605-3943', 'jesusita@druck.net.au',]
 ['Annice', 'Kunich', 'Tyagarah', 'NSW', 2481, '02-6769-6153', 'annice_kunich@kunich.net.au',]
 ['Delila', 'Buchman', 'Redgate', 'WA', 6286, '08-1791-7668', 'delila.buchman@hotmail.com',]
 ['Iraida', 'Sionesini', 'Modewarre', 'VIC', 3240, '03-4812-5654', 'iraida.sionesini@yahoo.com',]
 ['Alona', 'Driesenga', 'Stirling Range National Park', 'WA', 6338, '08-6777-4159', 'alona_driesenga@hotmail.com',]
 ['Lajuana', 'Vonderahe', 'Trowutta', 'TAS', 7330, '03-5661-2424', 'lajuana.vonderahe@yahoo.com',]
 ['Madelyn', 'Maestri', 'Rouse Hill', 'NSW', 2155, '02-2129-8131', 'madelyn.maestri@yahoo.com',]
 ['Louann', 'Susmilch', 'Wyandra', 'QLD', 4489, '07-5035-4889', 'louann_susmilch@yahoo.com',]
 ['William', 'Devol', 'Goondi Hill', 'QLD', 4860, '07-4963-5297', 'wdevol@devol.net.au',]
 ['Corazon', 'Grafenstein', 'Hill River', 'WA', 6521, '08-1624-7236', 'cgrafenstein@gmail.com',]
 ['Fairy', 'Burket', 'Fairview Park', 'SA', 5126, '08-9159-7562', 'fairy_burket@burket.com.au',]
 ['Lashawn', 'Urion', 'Bar Beach', 'NSW', 2300, '02-4794-6673', 'lurion@yahoo.com',]
 ['Ronald', 'Gayner', 'University Of Tasmania', 'TAS', 7005, '03-7734-9557', 'rgayner@hotmail.com',]
 ['Shizue', 'Hayduk', 'Regent West', 'VIC', 3072, '03-2297-9891', 'shayduk@gmail.com',]
 ['Nida', 'Fitz', 'Oxley', 'QLD', 4075, '07-7445-2572', 'nfitz@hotmail.com',]
 ['Amos', 'Limberg', 'Don', 'TAS', 7310, '03-4539-9131', 'alimberg@limberg.com.au',]
 ['Dexter', 'Prosienski', 'Nyora', 'VIC', 3987, '03-2454-6523', 'dexter@prosienski.net.au',]
 ['Ludivina', 'Calamarino', 'Croydon', 'QLD', 4871, '07-5378-4498', 'lcalamarino@yahoo.com',]
 ['Ariel', 'Stavely', 'Scottsdale', 'TAS', 7260, '03-6510-4788', 'ariel_stavely@stavely.com.au',]
 ['Haley', 'Vaughn', 'Montrose', 'VIC', 3765, '03-7035-6484', 'haley_vaughn@vaughn.net.au',]
 ['Raelene', 'Legeyt', 'Oak Park', 'VIC', 3046, '03-4878-1766', 'raelene@gmail.com',]
 ['Micaela', 'Shiflett', 'Nailsworth', 'SA', 5083, '08-8856-8589', 'micaela_shiflett@shiflett.com.au',]
 ['Alpha', 'Prudhomme', 'Tarong', 'QLD', 4615, '07-9053-8045', 'aprudhomme@hotmail.com',]
 ['Zack', 'Warman', 'Kensington Park', 'SA', 5068, '08-9948-2940', 'zwarman@gmail.com',]
 ['Wilford', 'Pata', 'Ashmore', 'QLD', 4214, '07-7445-2538', 'wilford_pata@pata.net.au',]
 ['Carman', 'Robasciotti', 'Granya', 'VIC', 3701, '03-1570-9956', 'carman_robasciotti@hotmail.com',]
 ['Carylon', 'Bayot', 'Alexandra', 'VIC', 3714, '03-8858-7088', 'carylon@gmail.com',]
 ['Gladys', 'Schmale', 'Wirrulla', 'SA', 5661, '08-4564-2338', 'gschmale@schmale.net.au',]
 ['Matilda', 'Peleg', 'Weymouth', 'TAS', 7252, '03-1130-5685', 'matilda.peleg@hotmail.com',]
 ['Jacklyn', 'Wojnar', 'Summer Hill', 'NSW', 2287, '02-6287-8787', 'jacklyn@hotmail.com',]
 ['Tashia', 'Charney', 'Shailer Park', 'QLD', 4128, '07-7659-5711', 'tashia.charney@charney.net.au',]
 ['Dorian', 'Eischens', 'Bell', 'NSW', 2786, '02-7739-6600', 'deischens@gmail.com',]
 ['Jesus', 'Merkt', 'Licola', 'VIC', 3858, '03-9341-9757', 'jesus_merkt@merkt.net.au',]
 ['Brandee', 'Svoboda', 'Walyormouring', 'WA', 6460, '08-3614-5966', 'brandee_svoboda@svoboda.net.au',]
 ['Edda', 'Mcquaide', 'Boronia', 'VIC', 3155, '03-1465-8645', 'emcquaide@yahoo.com',]
 ['Felix', 'Bumby', 'Baddaginnie', 'VIC', 3670, '03-1431-3996', 'felix.bumby@bumby.com.au',]
 ['Ben', 'Kellman', 'Berrilee', 'NSW', 2159, '02-7968-9243', 'ben_kellman@kellman.net.au',]
 ['Mickie', 'Upton', 'Barmaryee', 'QLD', 4703, '07-7647-5420', 'mickie.upton@yahoo.com',]
 ['Phung', 'Krome', 'Longford', 'TAS', 7301, '03-9617-5392', 'pkrome@yahoo.com',]
 ['Lashonda', 'Langanke', 'Simson', 'VIC', 3465, '03-9838-7533', 'lashonda@langanke.net.au',]
 ['Patria', 'Popa', 'Killabakh', 'NSW', 2429, '02-6522-3993', 'patria.popa@gmail.com',]
 ['Nidia', 'Horr', 'Paluma', 'QLD', 4816, '07-8441-8214', 'nidia@gmail.com',]
 ['Skye', 'Culcasi', 'Barnawartha', 'VIC', 3688, '03-9075-3104', 'skye_culcasi@hotmail.com',]
 ['Kanisha', 'Reyelts', 'Holwell', 'TAS', 7275, '03-2921-8418', 'kreyelts@yahoo.com',]
 ['Hector', 'Barras', 'Combienbar', 'VIC', 3889, '03-3017-8394', 'hector.barras@barras.com.au',]
 ['Stefan', 'Mongolo', 'Port Adelaide', 'SA', 5015, '08-4563-6214', 'stefan_mongolo@mongolo.net.au',]
 ['Francoise', 'Byon', 'Klemzig', 'SA', 5087, '08-3914-9404', 'francoise@hotmail.com',]
 ['Lindy', 'Vandermeer', 'Emu Park', 'QLD', 4710, '07-9407-9202', 'lindy@vandermeer.com.au',]
 ['Arthur', 'Diniz', 'Travancore', 'VIC', 3032, '03-2517-3453', 'arthur@gmail.com',]
 ['Nicholle', 'Hulme', 'Whetstone', 'QLD', 4387, '07-7144-4719', 'nicholle_hulme@hulme.com.au',]
 ['Tijuana', 'Mesch', 'Corella', 'QLD', 4570, '07-1415-9307', 'tijuana_mesch@gmail.com',]
 ['Lorenza', 'Schoenleber', 'Humpty Doo', 'NT', 836, '08-8081-7779', 'lorenza.schoenleber@schoenleber.com.au',]
 ['Iola', 'Baird', 'Goode Beach', 'WA', 6330, '08-2325-5905', 'ibaird@baird.net.au',]
 ['Sang', 'Weigner', 'Heidelberg Rgh', 'VIC', 3081, '03-8912-5755', 'sweigner@gmail.com',]
 ['Leonor', 'Prez', 'Waterloo', 'NSW', 2017, '02-7463-8776', 'lprez@prez.com.au',]
 ['Silvana', 'Whelpley', 'Minyip', 'VIC', 3392, '03-5175-6193', 'swhelpley@yahoo.com',]
 ['Anthony', 'Stever', 'Hunchy', 'QLD', 4555, '07-7092-8542', 'anthony.stever@hotmail.com',]
 ['Wenona', 'Carmel', 'Grosvenor Place', 'NSW', 1220, '02-2832-1545', 'wenona@gmail.com',]
 ['Isadora', 'Yurick', 'Pacific Paradise', 'QLD', 4564, '07-9595-6042', 'iyurick@hotmail.com',]
 ['Mose', 'Vonseggern', 'Hungerford', 'QLD', 4493, '07-5769-8004', 'mose_vonseggern@hotmail.com',]
 ['Marci', 'Aveline', 'Boya', 'WA', 6056, '08-3342-3889', 'marci.aveline@hotmail.com',]
 ['Michel', 'Hoyne', 'Elizabeth West', 'SA', 5113, '08-6183-9260', 'michel@hoyne.com.au',]
 ['Stephania', 'Connon', 'Gumly Gumly', 'NSW', 2652, '02-5725-5992', 'stephania.connon@connon.com.au',]
 ['Charolette', 'Turk', 'Wilmington', 'SA', 5485, '08-4735-5054', 'cturk@yahoo.com',]
 ['Katie', 'Magro', 'Pagewood', 'NSW', 2035, '02-7265-9702', 'katie_magro@gmail.com',]
 ['Inocencia', 'Angeron', 'Tawonga', 'VIC', 3697, '03-6268-2647', 'inocencia.angeron@angeron.net.au',]
 ['Nikita', 'Novosel', 'Hamlyn Heights', 'VIC', 3215, '03-5716-1053', 'nikita_novosel@novosel.net.au',]
 ['Malcolm', 'Gohlke', 'Southtown', 'QLD', 4350, '07-9826-3950', 'malcolm@yahoo.com',]
 ['Desiree', 'Englund', 'East Bowes', 'WA', 6535, '08-5289-4594', 'denglund@gmail.com',]
 ['Holley', 'Worland', 'Blue Haven', 'NSW', 2262, '02-9885-9593', 'holley.worland@hotmail.com',]
 ['Maryann', 'Tates', 'Cramphorne', 'WA', 6420, '08-1520-4093', 'mtates@yahoo.com',]
 ['Ling', 'Dibello', 'Beelbi Creek', 'QLD', 4659, '07-1330-6750', 'ling_dibello@yahoo.com',]
 ['Hailey', 'Kopet', 'Tanbar', 'QLD', 4481, '07-3799-1667', 'hailey_kopet@kopet.com.au',]
 ['Farrah', 'Malboeuf', 'Ringwood', 'VIC', 3134, '03-7139-6376', 'farrah@malboeuf.com.au',]
 ['Candra', 'Deritis', 'Battery Point', 'TAS', 7004, '03-4231-3633', 'candra@deritis.net.au',]
 ['Reuben', 'Hegland', 'Milton', 'NSW', 2538, '02-1402-5215', 'reuben@yahoo.com',]
 ['Anglea', 'Andrion', 'Laura', 'QLD', 4871, '07-3239-2830', 'anglea.andrion@andrion.com.au',]
 ['Paris', 'Tuccio', 'Kidman Park', 'SA', 5025, '08-8868-2010', 'paris.tuccio@hotmail.com',]
 ['Latricia', 'Schmoyer', 'Woodville', 'SA', 5011, '08-5444-3296', 'latricia_schmoyer@hotmail.com',]
 ['Jeffrey', 'Leuenberger', 'Pedler Creek', 'SA', 5171, '08-1267-4421', 'jleuenberger@yahoo.com',]
 ['Dean', 'Vollstedt', 'Muckleford South', 'VIC', 3462, '03-6776-1146', 'dvollstedt@vollstedt.com.au',]
 ['Deane', 'Haag', 'Sydney South', 'NSW', 1235, '02-9718-2944', 'dhaag@hotmail.com',]
 ['Edelmira', 'Pedregon', 'Bandy Creek', 'WA', 6450, '08-8484-3223', 'edelmira_pedregon@hotmail.com',]
 ['Andrew', 'Keks', 'Carwarp', 'VIC', 3494, '03-5251-3153', 'andrew@gmail.com',]
 ['Miesha', 'Decelles', 'Eltham', 'VIC', 3095, '03-5185-6258', 'mdecelles@decelles.net.au',]
 ['Javier', 'Osmer', 'Doncaster East', 'VIC', 3109, '03-8369-6924', 'javier@osmer.com.au',]
 ['Kizzy', 'Stangle', 'Welbungin', 'WA', 6477, '08-1937-3980', 'kizzy.stangle@yahoo.com',]
 ['Sharan', 'Wodicka', 'Shenton Park', 'WA', 6008, '08-4712-2157', 'sharan@wodicka.net.au',]
 ['Novella', 'Fritch', 'Girraween', 'NSW', 2145, '02-2612-1455', 'nfritch@fritch.com.au',]
 ['German', 'Dones', 'Woronora', 'NSW', 2232, '02-2393-3289', 'german@gmail.com',]
 ['Robt', 'Blanck', 'Woodbury', 'TAS', 7120, '03-6517-9318', 'robt.blanck@yahoo.com',]
 ['Rossana', 'Biler', 'Lee Point', 'NT', 810, '08-9855-2125', 'rossana.biler@biler.net.au',]
 ['Henriette', 'Gish', 'Baranduda', 'VIC', 3691, '03-9935-5135', 'henriette.gish@gish.net.au',]
 ['Buffy', 'Stitely', 'Police Point', 'TAS', 7116, '03-1600-5230', 'buffy_stitely@stitely.com.au',]
 ['Christiane', 'Osmanski', 'Williamstown', 'WA', 6430, '08-9693-9052', 'christiane@gmail.com',]
 ['Annamae', 'Lothridge', 'Civic Square', 'ACT', 2608, '02-1919-3941', 'alothridge@hotmail.com',]
 ['Vanesa', 'Glockner', 'Taragoola', 'QLD', 4680, '07-7052-4547', 'vanesa@glockner.com.au',]
 ['Gennie', 'Pastorino', 'Charleston', 'SA', 5244, '08-4753-2870', 'gennie.pastorino@gmail.com',]
 ['Tamra', 'Kenfield', 'Kealy', 'WA', 6280, '08-5614-9153', 'tkenfield@kenfield.com.au',]
 ['Tien', 'Kinney', 'Lillimur', 'VIC', 3420, '03-7767-6169', 'tien_kinney@kinney.com.au',]
 ['Malcom', 'Leja', 'Officer', 'VIC', 3809, '03-2477-9133', 'malcom@leja.com.au',]
 ['Claudia', 'Gawrych', 'Lilli Pilli', 'NSW', 2229, '02-4246-3092', 'claudia@gmail.com',]
 ['Page', 'Entzi', 'Blue Rocks', 'TAS', 7255, '03-2484-5500', 'page@entzi.net.au',]
 ['Lorita', 'Roches', 'Westminster', 'WA', 6061, '08-2358-3115', 'lorita_roches@roches.net.au',]
 ['Annita', 'Lek', 'Karama', 'NT', 812, '08-3384-3181', 'annita.lek@lek.net.au',]
 ['Eliseo', 'Mikovec', 'Ocean Shores', 'NSW', 2483, '02-9829-2371', 'emikovec@mikovec.com.au',]
 ['Tyisha', 'Layland', 'Eastwood', 'SA', 5063, '08-2158-6758', 'tyisha@yahoo.com',]
 ['Colene', 'Tolbent', 'Gloucester', 'NSW', 2422, '02-4376-1104', 'colene.tolbent@tolbent.net.au',]
 ['Francis', 'Senters', 'Heidelberg Rgh', 'VIC', 3081, '03-5933-7288', 'fsenters@gmail.com',]
 ['Hester', 'Dollins', 'The Risk', 'NSW', 2474, '02-1622-6412', 'hester_dollins@gmail.com',]
 ['Susana', 'Baumgarter', 'Yanco', 'NSW', 2703, '02-5410-5137', 'susana.baumgarter@yahoo.com',]
 ['Dahlia', 'Tummons', 'Port Fairy', 'VIC', 3284, '03-8216-8640', 'dahlia.tummons@gmail.com',]
 ['Osvaldo', 'Falvey', 'Queenton', 'QLD', 4820, '07-4854-5045', 'osvaldo.falvey@yahoo.com',]
 ['Armando', 'Barkley', 'Watercarrin', 'WA', 6407, '08-8161-8201', 'armando.barkley@yahoo.com',]
 ['Torie', 'Deras', 'Yeppoon', 'QLD', 4703, '07-8371-4719', 'torie_deras@yahoo.com',]
 ['Tamie', 'Hollimon', 'Bobalong', 'WA', 6320, '08-7046-5484', 'tamie@hollimon.com.au',]
 ['Lettie', 'Hessenthaler', 'Wurdiboluc', 'VIC', 3241, '03-5855-5156', 'lettie_hessenthaler@hessenthaler.net.au',]
 ['Chaya', 'Muhlbauer', 'North Dandalup', 'WA', 6207, '08-5943-4352', 'chaya_muhlbauer@muhlbauer.net.au',]
 ['Terina', 'Wildeboer', 'Seddon', 'VIC', 3011, '03-9107-7349', 'terina_wildeboer@wildeboer.com.au',]
 ['Lisbeth', 'Agney', 'Hindmarsh', 'WA', 6462, '08-1184-4145', 'lisbeth.agney@agney.net.au',]
 ['Lillian', 'Dominique', 'Julia Creek', 'QLD', 4823, '07-3594-6592', 'lillian@hotmail.com',]
 ['Corrina', 'Lindblom', 'Salter Point', 'WA', 6152, '08-7915-5110', 'clindblom@gmail.com',]
 ['Dylan', 'Chaleun', 'Lilydale', 'QLD', 4344, '07-2319-2889', 'dylan_chaleun@hotmail.com',]
 ['Jerrod', 'Luening', 'Tea Gardens', 'NSW', 2324, '02-9554-9632', 'jerrod_luening@luening.com.au',]
 ['Gracie', 'Vicente', 'Oxley', 'VIC', 3678, '03-2444-8291', 'gracie.vicente@hotmail.com',]
 ['Barabara', 'Amedro', 'Yallah', 'NSW', 2530, '02-3449-6894', 'barabara@amedro.net.au',]
 ['Delsie', 'Ducos', 'Cavendish', 'VIC', 3314, '03-1361-8465', 'dducos@hotmail.com',]
 ['Cassie', 'Digregorio', 'Condobolin', 'NSW', 2877, '02-7922-5417', 'cdigregorio@digregorio.net.au',]
 ['Tamekia', 'Kajder', 'West Tamworth', 'NSW', 2340, '02-7498-8576', 'tamekia_kajder@yahoo.com',]
 ['Johanna', 'Saffer', 'Campsie', 'NSW', 2194, '02-5970-1748', 'johanna@yahoo.com',]
 ['Sharita', 'Kruk', 'Merrylands', 'NSW', 2160, '02-7386-4544', 'sharita_kruk@gmail.com',]
 ['Gerald', 'Chrusciel', 'Townsville Milpo', 'QLD', 4813, '07-7446-6315', 'gerald@chrusciel.net.au',]
 ['Ardella', 'Dieterich', 'Runnymede', 'QLD', 4615, '07-3581-9462', 'ardella.dieterich@yahoo.com',]
 ['Jackie', 'Kellebrew', 'Coominya', 'QLD', 4311, '07-9840-6419', 'jackie.kellebrew@kellebrew.com.au',]
 ['Mabelle', 'Ramero', 'Aroona', 'QLD', 4551, '07-8857-6463', 'mabelle.ramero@ramero.net.au',]
 ['Jonell', 'Biasi', 'Duramana', 'NSW', 2795, '02-5095-2983', 'jbiasi@biasi.net.au',]
 ['Linwood', 'Wessner', 'Saltwater River', 'TAS', 7186, '03-6053-2447', 'linwood.wessner@hotmail.com',]
 ['Samira', 'Heninger', 'Bluff', 'QLD', 4702, '07-9512-2457', 'sheninger@yahoo.com',]
 ['Julieta', 'Cropsey', 'Kingaroy', 'QLD', 4610, '07-4217-6258', 'julieta@yahoo.com',]
 ['Serita', 'Barthlow', 'Nangetty', 'WA', 6522, '08-2941-7378', 'serita_barthlow@gmail.com',]
 ['Tori', 'Tepley', 'Uarbry', 'NSW', 2329, '02-2493-1870', 'tori@tepley.net.au',]
 ['Nancey', 'Whal', 'Cudgera Creek', 'NSW', 2484, '02-3248-3283', 'nancey@whal.net.au',]
 ['Wilbert', 'Beckes', 'East Nanango', 'QLD', 4615, '07-9178-6430', 'wilbert@hotmail.com',]
 ['Werner', 'Hermens', 'Oakleigh South', 'VIC', 3167, '03-9085-5714', 'whermens@hermens.net.au',]
 ['Sunny', 'Catton', 'Gununa', 'QLD', 4871, '07-1217-9907', 'scatton@catton.com.au',]
 ['Keva', 'Moehring', 'Salamander Bay', 'NSW', 2317, '02-9187-4769', 'keva.moehring@moehring.net.au',]
 ['Mary', 'Dingler', 'Bundaberg North', 'QLD', 4670, '07-3963-4469', 'mary.dingler@gmail.com',]
 ['Huey', 'Bukovac', 'Middleton', 'SA', 5213, '08-5236-2143', 'huey.bukovac@hotmail.com',]
 ['Antonio', 'Eighmy', 'Eaglemont', 'VIC', 3084, '03-6144-7318', 'antonio.eighmy@yahoo.com',]
 ['Quinn', 'Weissbrodt', 'Premer', 'NSW', 2381, '02-7239-9923', 'qweissbrodt@weissbrodt.com.au',]
 ['Carin', 'Georgiades', 'Trott Park', 'SA', 5158, '08-8343-3550', 'cgeorgiades@gmail.com',]
 ['Jill', 'Davoren', 'Boynewood', 'QLD', 4626, '07-1698-9047', 'jill_davoren@davoren.net.au',]
 ['Sanjuana', 'Goodness', 'Maraylya', 'NSW', 2765, '02-2208-2711', 'sgoodness@goodness.net.au',]
 ['Elin', 'Koerner', 'Wayville', 'SA', 5034, '08-5221-9700', 'elin_koerner@koerner.com.au',]
 ['Charlena', 'Decamp', 'Burnside', 'WA', 6285, '08-7615-2416', 'charlena@gmail.com',]
 ['Annette', 'Breyer', 'Daradgee', 'QLD', 4860, '07-5417-9612', 'abreyer@hotmail.com',]
 ['Alexis', 'Morguson', 'Weetulta', 'SA', 5573, '08-1895-1457', 'amorguson@morguson.com.au',]
 ['Princess', 'Saffo', 'Auburn', 'NSW', 1835, '02-2656-6234', 'princess_saffo@hotmail.com',]
 ['Ashton', 'Sutherburg', 'South Hobart', 'TAS', 7004, '03-9215-3224', 'asutherburg@gmail.com',]
 ['Elmer', 'Redlon', 'Forbes', 'NSW', 2871, '02-1075-4690', 'elmer@hotmail.com',]
 ['Aliza', 'Akiyama', 'Forest Reefs', 'NSW', 2798, '02-9324-7803', 'aliza@yahoo.com',]
 ['Ora', 'Handrick', 'Rocklands', 'VIC', 3401, '03-8357-4617', 'ora.handrick@gmail.com',]
 ['Brent', 'Ahlborn', 'Oaklands Park', 'SA', 5046, '08-4563-9520', 'bahlborn@ahlborn.com.au',]
 ['Tora', 'Telch', 'Buckland Park', 'SA', 5120, '08-8808-8104', 'tora@telch.net.au',]
 ['Hildred', 'Eilbeck', 'Longwood', 'SA', 5153, '08-2922-4115', 'hildred_eilbeck@eilbeck.net.au',]
 ['Dante', 'Freiman', 'Varsity Lakes', 'QLD', 4227, '07-1964-4238', 'dante_freiman@freiman.net.au',]
 ['Emmanuel', 'Avera', 'Appin', 'NSW', 2560, '02-1987-8525', 'emmanuel@yahoo.com',]
 ['Keshia', 'Wasp', 'Adelaide River', 'NT', 846, '08-1683-9243', 'kwasp@wasp.net.au',]
 ['Sherman', 'Mahmud', 'Harris Park', 'NSW', 2150, '02-2621-3361', 'sherman@mahmud.com.au',]
 ['Lore', 'Brothers', 'Kallista', 'VIC', 3791, '03-8780-3473', 'lore@hotmail.com',]
 ['Shawn', 'Weibe', 'Camena', 'TAS', 7316, '03-9480-9611', 'shawn@hotmail.com',]
 ['Karima', 'Cheever', 'Woodberry', 'NSW', 2322, '02-5977-8561', 'karima_cheever@hotmail.com',]
 ['Francesco', 'Kloos', 'Rocky Gully', 'WA', 6397, '08-1687-4873', 'fkloos@kloos.com.au',]
 ['King', 'Picton', 'Preston Beach', 'WA', 6215, '08-7605-2080', 'king@hotmail.com',]
 ['Mica', 'Simco', 'Brigalow', 'QLD', 4412, '07-1037-3391', 'msimco@gmail.com',]
 ['Lamonica', 'Princiotta', 'Beermullah', 'WA', 6503, '08-5227-2620', 'lamonica@hotmail.com',]
 ['Curtis', 'Ware', 'Ridgewood', 'WA', 6030, '08-6278-9532', 'curtis@ware.net.au',]
 ['Sabrina', 'Rabena', 'Bayles', 'VIC', 3981, '03-5662-3542', 'sabrina_rabena@hotmail.com',]
 ['Denae', 'Saeteun', 'Moorabbin Airport', 'VIC', 3194, '03-2802-7434', 'denae_saeteun@hotmail.com',]
 ['Anastacia', 'Carranzo', 'Waratah West', 'NSW', 2298, '02-6078-3417', 'anastacia@yahoo.com',]
 ['Irving', 'Plocica', 'Cullulleraine', 'VIC', 3496, '03-9050-2741', 'irving@hotmail.com',]
 ['Elenor', 'Siefken', 'Cairns City', 'QLD', 4870, '07-5085-8138', 'elenor.siefken@yahoo.com',]
 ['Mary', 'Irene', 'Warding East', 'WA', 6405, '08-8012-6469', 'mirene@gmail.com',]
 ['Crista', 'Padua', 'North Haven', 'NSW', 2443, '02-9472-5814', 'crista_padua@gmail.com',]
 ['Lawana', 'Yuasa', 'Cape Paterson', 'VIC', 3995, '03-2324-3472', 'lawana_yuasa@yuasa.net.au',]
 ['Maryrose', 'Cove', 'Cabramatta', 'NSW', 2166, '02-8010-8344', 'mcove@hotmail.com',]
 ['Lindsey', 'Rathmann', 'Kongorong', 'SA', 5291, '08-1269-1489', 'lindsey_rathmann@rathmann.com.au',]
 ['Lynelle', 'Koury', 'Digby', 'VIC', 3309, '03-5213-8219', 'lynelle.koury@koury.net.au',]
 ['Brice', 'Bogacz', 'Sedan', 'SA', 5353, '08-5203-2193', 'bbogacz@hotmail.com',]
 ['Laine', 'Killean', 'Braybrook', 'VIC', 3019, '03-2813-6426', 'laine@gmail.com',]
 ['Rachael', 'Crawley', 'Inkpen', 'WA', 6302, '08-2089-8553', 'rachael@gmail.com',]
 ['Della', 'Selestewa', 'Gillieston Heights', 'NSW', 2321, '02-4885-8382', 'della.selestewa@gmail.com',]
 ['Thomasena', 'Graziosi', 'Neerabup', 'WA', 6031, '08-4849-4417', 'thomasena@gmail.com',]
 ['Frederic', 'Schimke', 'Mount Martha', 'VIC', 3934, '03-4829-5695', 'fschimke@schimke.com.au',]
 ['Halina', 'Dellen', 'Appila', 'SA', 5480, '08-6742-2308', 'halina.dellen@dellen.com.au',]
 ['Ryann', 'Riston', 'Milton', 'QLD', 4064, '07-9920-3550', 'ryann@hotmail.com',]
 ['Shawn', 'Vugteveen', 'Etty Bay', 'QLD', 4858, '07-3103-8372', 'svugteveen@vugteveen.net.au',]
 ['Leah', 'Milsap', 'Lower Hermitage', 'SA', 5131, '08-4040-9192', 'leah@milsap.com.au',]
 ['Ira', 'Zihal', 'Degilbo', 'QLD', 4621, '07-4724-9987', 'ira.zihal@yahoo.com',]
 ['Paris', 'Kinnison', 'Eastern Heights', 'QLD', 4305, '07-4518-4450', 'paris.kinnison@gmail.com',]
 ['Shayne', 'Sundahl', 'Normanville', 'SA', 5204, '08-8587-1196', 'shayne.sundahl@gmail.com',]
 ['Ernestine', 'Paavola', 'Yorkrakine', 'WA', 6409, '08-1140-6357', 'ernestine.paavola@paavola.com.au',]
 ['Eleonore', 'Everline', 'Kialla East', 'VIC', 3631, '03-5355-5505', 'eeverline@hotmail.com',]
 ['Misty', 'Leriche', 'Glen Boughton', 'QLD', 4871, '07-5486-1002', 'mleriche@yahoo.com',]
 ['Na', 'Hodges', 'Ongerup', 'WA', 6336, '08-8215-1588', 'na_hodges@hotmail.com',]
 ['Juan', 'Knudtson', 'Clunes', 'VIC', 3370, '03-9173-6140', 'juan@gmail.com',]
 ['Gerald', 'Kloepper', 'Pierces Creek', 'QLD', 4355, '07-4297-4607', 'gerald@yahoo.com',]
 ['Desmond', 'Tarkowski', 'Andergrove', 'QLD', 4740, '07-6793-5954', 'desmond_tarkowski@hotmail.com',]
 ['Tommy', 'Gennusa', 'Concord West', 'NSW', 2138, '02-5444-1961', 'tommy@hotmail.com',]
 ['Adrianna', 'Poncio', 'Bethania', 'QLD', 4205, '07-6113-9653', 'adrianna@poncio.com.au',]
 ['Adaline', 'Galagher', 'Barooga', 'NSW', 3644, '02-3225-1954', 'adaline.galagher@galagher.com.au',]
 ['Tammi', 'Schiavi', 'Willetton', 'WA', 6155, '08-9707-2679', 'tammi.schiavi@hotmail.com',]
 ['Virgilio', 'Phay', 'Stratton', 'WA', 6056, '08-8147-9584', 'vphay@phay.com.au',]
 ['Emeline', 'Sotelo', 'Elimbah', 'QLD', 4516, '07-7240-6480', 'emeline@gmail.com',]
 ['Marcos', 'Seniff', 'Emerald', 'VIC', 3782, '03-6340-5010', 'marcos_seniff@gmail.com',]
 ['Yuonne', 'Carabajal', 'Changerup', 'WA', 6394, '08-7432-4632', 'ycarabajal@carabajal.com.au',]
 ['Gladis', 'Kazemi', 'Varsity Lakes', 'QLD', 4227, '07-6444-3666', 'gkazemi@kazemi.net.au',]
 ['Muriel', 'Drozdowski', 'Durham Downs', 'QLD', 4454, '07-5686-8088', 'muriel_drozdowski@hotmail.com',]
 ['Juliann', 'Dammeyer', 'Bouvard', 'WA', 6210, '08-3562-8644', 'juliann@gmail.com',]
 ['Reiko', 'Dejarme', 'Bentley Dc', 'WA', 6983, '08-3733-5261', 'rdejarme@dejarme.net.au',]
 ['Verdell', 'Garness', 'Thornton', 'NSW', 2322, '02-6291-7620', 'verdell.garness@yahoo.com',]
 ['Arleen', 'Kane', 'Eagle Farm', 'QLD', 4009, '07-3476-2066', 'arleen.kane@hotmail.com',]
 ['Launa', 'Vanauken', 'Peake', 'SA', 5301, '08-9808-2647', 'launa@gmail.com',]
 ['Casandra', 'Gordis', 'Chippendale', 'NSW', 2008, '02-5808-6388', 'casandra_gordis@gordis.com.au',]
 ['Julio', 'Puccini', 'Gorokan', 'NSW', 2263, '02-5632-9914', 'julio@gmail.com',]
 ['Alica', 'Alerte', 'Grevillia', 'NSW', 2474, '02-6974-7785', 'aalerte@alerte.com.au',]
 ['Karol', 'Sarkissian', 'Chatsworth', 'NSW', 2469, '02-3490-2407', 'ksarkissian@yahoo.com',]
 ['Wava', 'Ochs', 'Bawley Point', 'NSW', 2539, '02-1222-7812', 'wava.ochs@gmail.com',]
 ['Felicitas', 'Gong', 'Weengallon', 'QLD', 4497, '07-8516-6453', 'fgong@gong.com.au',]
 ['Jamie', 'Kushnir', 'Tuggeranong Dc', 'ACT', 2901, '02-4623-8120', 'jamie@kushnir.net.au',]
 ['Fidelia', 'Dampier', 'Dangar Island', 'NSW', 2083, '02-8035-9997', 'fidelia_dampier@gmail.com',]
 ['Kris', 'Medich', 'Shannon', 'TAS', 7030, '03-6589-2556', 'kris.medich@hotmail.com',]
 ['Lashawna', 'Filan', 'Greenhills', 'WA', 6302, '08-6937-4366', 'lashawna.filan@filan.net.au',]
 ['Lachelle', 'Andrzejewski', 'Cherrybrook', 'NSW', 2126, '02-3416-9617', 'lachelle.andrzejewski@andrzejewski.com.au',]
 ['Katy', 'Saltourides', 'Junee', 'NSW', 2663, '02-3003-1369', 'katy_saltourides@yahoo.com',]
 ['Bettyann', 'Fernades', 'Tibradden', 'WA', 6532, '08-2901-3421', 'bettyann@fernades.com.au',]
 ['Valda', 'Levay', 'Tungkillo', 'SA', 5236, '08-2401-5672', 'vlevay@levay.net.au',]
 ['Lynette', 'Beaureguard', 'Tarawera', 'QLD', 4494, '07-6679-3722', 'lynette.beaureguard@hotmail.com',]
 ['Victor', 'Laroia', 'Scotts Head', 'NSW', 2447, '02-8156-6969', 'victor@laroia.net.au',]
 ['Pa', 'Badgero', 'Pakenham Upper', 'VIC', 3810, '03-1861-5074', 'pa_badgero@badgero.com.au',]
 ['Dorathy', 'Miskelly', 'Westerway', 'TAS', 7140, '03-6340-9772', 'dorathy.miskelly@gmail.com',]
 ['Rodrigo', 'Schuh', 'Burrier', 'NSW', 2540, '02-3869-4096', 'rodrigo_schuh@gmail.com',]
 ['Stanford', 'Waganer', 'East Nabawa', 'WA', 6532, '08-3200-1670', 'stanford_waganer@waganer.net.au',]
 ['Michael', 'Orehek', 'Millers Point', 'NSW', 2000, '02-1919-1709', 'michael_orehek@gmail.com',]
 ['Ines', 'Tokich', 'Bunya Mountains', 'QLD', 4405, '07-5017-7337', 'ines_tokich@tokich.net.au',]
 ['Dorinda', 'Markoff', 'Mayfield East', 'NSW', 2304, '02-6529-9317', 'dorinda_markoff@hotmail.com',]
 ['Clarence', 'Gabbert', 'Verges Creek', 'NSW', 2440, '02-4776-1384', 'clarence.gabbert@gmail.com',]
 ['Omer', 'Radel', 'Hill River', 'WA', 6521, '08-9919-9540', 'omer_radel@radel.net.au',]
 ['Winifred', 'Kingshott', 'Marshdale', 'NSW', 2420, '02-5318-1342', 'winifred.kingshott@yahoo.com',]
 ['Theresia', 'Salomone', 'Bundall', 'QLD', 4217, '07-8250-2277', 'theresia_salomone@gmail.com',]
 ['Daisy', 'Kearsey', 'Mount Nasura', 'WA', 6112, '08-2127-5977', 'dkearsey@yahoo.com',]
 ['Aretha', 'Bodle', 'Parndana', 'SA', 5220, '08-7385-2716', 'aretha_bodle@hotmail.com',]
 ['Bettina', 'Diciano', 'Dripstone', 'NSW', 2820, '02-3566-7608', 'bdiciano@diciano.com.au',]
 ['Omega', 'Mangino', 'Gnotuk', 'VIC', 3260, '03-6623-5501', 'omega.mangino@hotmail.com',]
 ['Dana', 'Vock', 'Yarralumla', 'ACT', 2600, '02-6689-1150', 'dana_vock@yahoo.com',]
 ['Naomi', 'Tuamoheloa', 'Muja', 'WA', 6225, '08-6137-1726', 'naomi@yahoo.com',]
 ['Luis', 'Yerry', 'Summerhill', 'TAS', 7250, '03-4492-4927', 'luis@hotmail.com',]
 ['Dominga', 'Barchacky', 'Port Flinders', 'SA', 5495, '08-3087-9658', 'dominga.barchacky@hotmail.com',]
 ['Isreal', 'Calizo', 'Wombeyan Caves', 'NSW', 2580, '02-3494-3282', 'isreal_calizo@gmail.com',]
 ['Myrtie', 'Korba', 'Dartnall', 'WA', 6320, '08-3174-2706', 'mkorba@hotmail.com',]
 ['Jodi', 'Naifeh', 'Dural', 'NSW', 2330, '02-6193-5184', 'jodi@hotmail.com',]
 ['Pearly', 'Hedstrom', 'Wandering', 'WA', 6308, '08-3412-6699', 'pearly@gmail.com',]
 ['Aileen', 'Menez', 'Manjimup', 'WA', 6258, '08-1196-2822', 'aileen_menez@menez.net.au',]
 ['Glory', 'Carlo', 'Grange', 'QLD', 4051, '07-9265-7183', 'glory_carlo@gmail.com',]
 ['Kathrine', 'Francoise', 'Indented Head', 'VIC', 3223, '03-8791-9436', 'kathrine@yahoo.com',]
 ['Domingo', 'Mckale', 'Marla', 'SA', 5724, '08-9919-7850', 'domingo_mckale@mckale.net.au',]
 ['Julian', 'Laprade', 'Mungabunda', 'QLD', 4718, '07-2627-9976', 'jlaprade@laprade.net.au',]
 ['Marylou', 'Lofts', 'Houston', 'VIC', 3128, '03-1765-4584', 'marylou_lofts@lofts.com.au',]
 ['Louis', 'Brueck', 'Larrakeyah', 'NT', 820, '08-5228-3628', 'louis.brueck@brueck.net.au',]
 ['Ellsworth', 'Guenther', 'Docklands', 'VIC', 3008, '03-2749-1381', 'eguenther@hotmail.com',]
 ['Wilburn', 'Lary', 'Gabbadah', 'WA', 6041, '08-1042-4275', 'wlary@lary.net.au',]
 ['Arlie', 'Borra', 'Morundah', 'NSW', 2700, '02-1211-3823', 'arlie.borra@gmail.com',]
 ['Alysa', 'Lehoux', 'Trungley Hall', 'NSW', 2666, '02-1385-3480', 'alysa@hotmail.com',]
 ['Marilynn', 'Herrera', 'Tawonga', 'VIC', 3697, '03-1447-7041', 'marilynn.herrera@herrera.net.au',]
 ['Scot', 'Jarva', 'Kingswood', 'NSW', 2550, '02-9676-4462', 'scot.jarva@jarva.com.au',]
 ['Adelaide', 'Ender', 'Greenslopes', 'QLD', 4120, '07-7538-5504', 'aender@gmail.com',]
 ['Jackie', 'Borchelt', 'Grovedale', 'VIC', 3216, '03-8055-8668', 'jackie_borchelt@hotmail.com',]
 ['Carli', 'Bame', 'Elanora', 'QLD', 4221, '07-5354-7251', 'carli@yahoo.com',]
 ['Coletta', 'Thro', 'North Fremantle', 'WA', 6159, '08-1991-6947', 'coletta.thro@thro.net.au',]
 ['Katheryn', 'Lamers', 'Fyshwick', 'ACT', 2609, '02-4885-1611', 'katheryn_lamers@gmail.com',]
 ['Santos', 'Wisenbaker', 'Allworth', 'NSW', 2425, '02-2957-4812', 'swisenbaker@wisenbaker.net.au',]
 ['Kimberely', 'Weyman', 'Kingsway West', 'NSW', 2208, '02-7091-8948', 'kweyman@weyman.com.au',]
 ['Earlean', 'Suffern', 'Woodford', 'NSW', 2463, '02-9653-2199', 'earlean.suffern@suffern.net.au',]
 ['Dannette', 'Heimbaugh', 'Breakaway', 'QLD', 4825, '07-8738-4205', 'dannette@gmail.com',]
 ['Odelia', 'Hutchin', 'Gorrie', 'WA', 6556, '08-9895-1954', 'odelia.hutchin@hutchin.com.au',]
 ['Lina', 'Schwiebert', 'Koorlong', 'VIC', 3501, '03-3608-5660', 'lina@yahoo.com',]
 ['Fredric', 'Johanningmeie', 'Wardell', 'NSW', 2477, '02-1827-1736', 'fredric@hotmail.com',]
 ['Alfreda', 'Delsoin', 'Bongeen', 'QLD', 4356, '07-7369-8849', 'adelsoin@yahoo.com',]
 ['Bernadine', 'Elamin', 'Waverley', 'NSW', 2024, '02-1815-8700', 'bernadine_elamin@yahoo.com',]
 ['Ming', 'Thaxton', 'Forrest', 'VIC', 3236, '03-4010-1900', 'mthaxton@gmail.com',]
 ['Gracia', 'Pecot', 'Gundaroo', 'NSW', 2620, '02-8081-3883', 'gpecot@hotmail.com',]
 ['Yuette', 'Metevelis', 'North Boyanup', 'WA', 6237, '08-4700-8894', 'yuette.metevelis@metevelis.net.au',]
 ['Yuriko', 'Kazarian', 'Mouroubra', 'WA', 6472, '08-1109-5346', 'yuriko_kazarian@gmail.com',]
 ['Hyman', 'Hegeman', 'Flinders University', 'SA', 5042, '08-9280-9177', 'hyman@hotmail.com',]
 ['Linette', 'Summerfield', 'Crows Nest', 'QLD', 4355, '07-7489-7577', 'linette.summerfield@hotmail.com',]
 ['Jospeh', 'Couzens', 'Panmure', 'VIC', 3265, '03-8451-7537', 'jospeh.couzens@couzens.com.au',]
 ['Anna', 'Ovit', 'Bygalorie', 'NSW', 2669, '02-4649-5341', 'anna.ovit@hotmail.com',]
 ['Shawnta', 'Woodhams', 'Oakhurst', 'NSW', 2761, '02-5770-8546', 'shawnta@woodhams.com.au',]
 ['Ettie', 'Luckenbach', 'Mandurah East', 'WA', 6210, '08-9378-7021', 'ettie@yahoo.com',]
 ['Chara', 'Leveston', 'Daisy Hill', 'VIC', 3465, '03-2574-8915', 'cleveston@gmail.com',]
 ['Lauran', 'Huntsberger', 'Willetton', 'WA', 6155, '08-2704-3706', 'lhuntsberger@huntsberger.net.au',]
 ['Pansy', 'Todesco', 'Tarnagulla', 'VIC', 3551, '03-3233-4255', 'pansy_todesco@gmail.com',]
 ['Georgeanna', 'Silverstone', 'Steels Creek', 'VIC', 3775, '03-7416-6750', 'georgeanna@silverstone.net.au',]
 ['Jesus', 'Liversedge', 'Broken Head', 'NSW', 2481, '02-4418-5927', 'jesus.liversedge@hotmail.com',]
 ['Jamey', 'Tetter', 'Bundaberg West', 'QLD', 4670, '07-6073-5039', 'jamey.tetter@gmail.com',]
 ['Alberta', 'Motter', 'Port Melbourne', 'VIC', 3207, '03-1248-8221', 'alberta_motter@hotmail.com',]
 ['Ronald', 'Grube', 'Happy Valley', 'SA', 5159, '08-3305-5436', 'ronald.grube@yahoo.com',]
 ['Tamala', 'Hickie', 'Benambra', 'VIC', 3900, '03-3695-2399', 'tamala_hickie@yahoo.com',]
 ['Gerry', 'Mohrmann', 'Brockman', 'WA', 6701, '08-1399-2471', 'gerry_mohrmann@mohrmann.net.au',]
 ['Isaiah', 'Kueter', 'Amphitheatre', 'VIC', 3468, '03-3725-6290', 'ikueter@kueter.com.au',]
 ['Magnolia', 'Overbough', 'Penrith', 'NSW', 2750, '02-7947-2980', 'moverbough@overbough.com.au',]
 ['Ngoc', 'Guglielmina', 'Darke Peak', 'SA', 5642, '08-2264-5559', 'ngoc_guglielmina@hotmail.com',]
 ['Julene', 'Lauretta', 'Mole Creek', 'TAS', 7304, '03-1036-9594', 'julene.lauretta@gmail.com',]
 ['Magda', 'Lindbeck', 'Emerald Beach', 'NSW', 2456, '02-3713-3646', 'magda_lindbeck@yahoo.com',]
 ['Shantell', 'Lizama', 'Logan Village', 'QLD', 4207, '07-5346-5917', 'shantell.lizama@gmail.com',]
 ['Audria', 'Piccinich', 'Coober Pedy', 'SA', 5723, '08-9757-2379', 'audria.piccinich@gmail.com',]
 ['Nickole', 'Derenzis', 'Berowra Heights', 'NSW', 2082, '02-5573-6627', 'nderenzis@hotmail.com',]
 ['Grover', 'Reynolds', 'Innaloo', 'WA', 6018, '08-7785-3040', 'grover.reynolds@gmail.com',]
 ['Rocco', 'Bergstrom', 'Leeman', 'WA', 6514, '08-3987-7521', 'rocco@yahoo.com',]
 ['Ethan', 'Quintero', 'East Damboring', 'WA', 6608, '08-8280-9492', 'ethan_quintero@quintero.com.au',]
 ['Glynda', 'Sanzenbacher', 'Kinglake West', 'VIC', 3757, '03-1051-7865', 'glynda@sanzenbacher.com.au',]
 ['Yolande', 'Scrimsher', 'Canning Vale', 'WA', 6155, '08-2136-2433', 'yolande@yahoo.com',]
 ['Twanna', 'Sieber', 'Upper Glastonbury', 'QLD', 4570, '07-5235-7319', 'twanna@yahoo.com',]
 ['Rosenda', 'Petteway', 'Caroline Springs', 'VIC', 3023, '03-9599-4122', 'rosenda@gmail.com',]
 ['Lacey', 'Francis', 'Hunchy', 'QLD', 4555, '07-4119-3981', 'lacey.francis@francis.net.au',]
 ['Cordie', 'Meikle', 'Hamlyn Terrace', 'NSW', 2259, '02-8727-4906', 'cordie.meikle@hotmail.com',]
 ['Annalee', 'Graleski', 'Darbys Falls', 'NSW', 2793, '02-6118-8773', 'annalee.graleski@hotmail.com',]
 ['Dana', 'Ladeau', 'Pinnacle', 'QLD', 4741, '07-3511-9233', 'dana@ladeau.net.au',]
 ['Wai', 'Raddle', 'Carlsruhe', 'VIC', 3442, '03-4811-3832', 'wai.raddle@raddle.com.au',]
 ['Johana', 'Conquest', 'Paulls Valley', 'WA', 6076, '08-6579-7569', 'johana@conquest.net.au',]
 ['Tomas', 'Fults', 'Mirani', 'QLD', 4754, '07-1536-4805', 'tomas_fults@fults.net.au',]
 ['Karon', 'Etzler', 'Buckland', 'TAS', 7190, '03-6698-8416', 'karon@hotmail.com',]
 ['Delbert', 'Houben', 'Mitta Mitta', 'VIC', 3701, '03-1560-6800', 'delbert.houben@hotmail.com',]
 ['Ashleigh', 'Rimmer', 'Boat Harbour Beach', 'TAS', 7321, '03-5354-9557', 'ashleigh.rimmer@hotmail.com',]
 ['Nenita', 'Mckenna', 'Botany', 'NSW', 1455, '02-5059-2649', 'nmckenna@yahoo.com',]
 ['Micah', 'Shear', 'Scaddan', 'WA', 6447, '08-6270-6829', 'mshear@hotmail.com',]
 ['Stefany', 'Figueras', 'Lenswood', 'SA', 5240, '08-2209-8647', 'stefany@figueras.net.au',]
 ['Rene', 'Burnsworth', 'Farrell Flat', 'SA', 5416, '08-8222-3171', 'rene@burnsworth.net.au',]
 ['Cary', 'Orazine', 'Melrose', 'SA', 5483, '08-7718-8495', 'cary.orazine@hotmail.com',]
 ['Micheal', 'Ocken', 'Freemans Waterhole', 'NSW', 2323, '02-9828-4921', 'micheal.ocken@ocken.net.au',]
 ['Frederick', 'Tamburello', 'Simpsons Bay', 'TAS', 7150, '03-4800-7102', 'frederick.tamburello@hotmail.com',]
 ['Burma', 'Noa', 'Ripponlea', 'VIC', 3185, '03-6438-4586', 'burma.noa@gmail.com',]
 ['Cherry', 'Roh', 'North Cascade', 'WA', 6445, '08-5175-3585', 'cherry_roh@yahoo.com',]
 ['Gabriele', 'Frabotta', 'Ensay', 'VIC', 3895, '03-2689-6049', 'gabriele_frabotta@gmail.com',]
 ['Clement', 'Chee', 'Golden Point', 'VIC', 3451, '03-2775-4083', 'clement@hotmail.com',]
 ['Beckie', 'Apodace', 'Middle Cove', 'NSW', 2068, '02-5630-3114', 'bapodace@gmail.com',]
 ['Catrice', 'Fowlkes', 'Waterfront Place', 'QLD', 4001, '07-9032-5149', 'cfowlkes@hotmail.com',]
 ['Richelle', 'Remillard', 'Buraminya', 'WA', 6452, '08-6831-6370', 'richelle.remillard@remillard.net.au',]
 ['Cherri', 'Miccio', 'Balnagowan', 'QLD', 4740, '07-5626-7937', 'cherri_miccio@gmail.com',]
 ['Dorethea', 'Taketa', 'Lower Cressbrook', 'QLD', 4313, '07-2209-2731', 'dtaketa@taketa.net.au',]
 ['Barb', 'Latina', 'Larrakeyah', 'NT', 820, '08-8506-7259', 'blatina@hotmail.com',]
 ['Bettye', 'Meray', 'Middleton', 'TAS', 7163, '03-9424-2956', 'bmeray@yahoo.com',]
 ['Sherrell', 'Sprowl', 'Oak Flats', 'NSW', 2529, '02-4074-4461', 'sherrell_sprowl@hotmail.com',]
 ['Ruth', 'Niglio', 'Orange Hill', 'QLD', 4455, '07-5128-8956', 'ruth.niglio@hotmail.com',]
 ['Alva', 'Shoulders', 'Welshpool', 'WA', 6106, '08-8329-4211', 'alva@gmail.com',]
 ['Carri', 'Palaspas', 'Minnenooka', 'WA', 6532, '08-6069-1579', 'carri_palaspas@palaspas.net.au',]
 ['Onita', 'Milbrandt', 'Wagga Wagga South', 'NSW', 2650, '02-1157-3829', 'onita.milbrandt@milbrandt.com.au',]
 ['Jessenia', 'Sarp', 'Wansbrough', 'WA', 6320, '08-8878-5994', 'jsarp@hotmail.com',]
 ['Tricia', 'Peressini', 'Pintharuka', 'WA', 6623, '08-4326-1560', 'tperessini@yahoo.com',]
 ['Stephaine', 'Manin', 'Eumundi', 'QLD', 4562, '07-2031-6566', 'stephaine_manin@yahoo.com',]
 ['Florinda', 'Gudgel', 'Halton', 'NSW', 2311, '02-2501-8301', 'fgudgel@gudgel.com.au',]
 ['Marsha', 'Farnham', 'Glenmore Park', 'NSW', 2745, '02-5402-8024', 'marsha@farnham.com.au',]
 ['Josefa', 'Oakland', 'Mccutcheon', 'QLD', 4856, '07-5404-6221', 'josefa_oakland@oakland.com.au',]
 ['Deeann', 'Nicklous', 'Pimpimbudgee', 'QLD', 4615, '07-6382-5073', 'deeann_nicklous@gmail.com',]
 ['Jeannetta', 'Vonstaden', 'Ilford', 'NSW', 2850, '02-8222-9319', 'jvonstaden@gmail.com',]
 ['Desmond', 'Amuso', 'Caparra', 'NSW', 2429, '02-1706-8506', 'desmond@hotmail.com',]
 ['Trina', 'Bakey', 'Duaringa', 'QLD', 4712, '07-5922-1983', 'tbakey@bakey.com.au',]
 ['Ramonita', 'Picotte', 'Weston', 'NSW', 2326, '02-4360-8467', 'ramonita_picotte@yahoo.com',]
 ['Temeka', 'Bodine', 'Clunes', 'NSW', 2480, '02-2581-7479', 'temeka.bodine@gmail.com',]
 ['Bea', 'Iida', 'Oakey', 'QLD', 4401, '07-6984-9278', 'bea_iida@iida.net.au',]
 ['Soledad', 'Mockus', 'Barton', 'ACT', 2600, '02-1291-8182', 'soledad_mockus@yahoo.com',]
 ['Margurite', 'Okon', 'Lanena', 'TAS', 7275, '03-9721-7313', 'margurite.okon@hotmail.com',]
 ['Artie', 'Saine', 'Cora Lynn', 'VIC', 3814, '03-3457-2524', 'artie_saine@yahoo.com',]
 ['Major', 'Studwell', 'Allora', 'QLD', 4362, '07-1377-6898', 'major@gmail.com',]
 ['Veronika', 'Buchauer', 'Willow Tree', 'NSW', 2339, '02-4202-5191', 'veronika.buchauer@buchauer.net.au',]
 ['Christene', 'Cisney', 'Keilor Downs', 'VIC', 3038, '03-3630-2467', 'christene@hotmail.com',]
 ['Miles', 'Feldner', 'Barringun', 'QLD', 4490, '07-8561-5894', 'miles@hotmail.com',]
 ['Julio', 'Mikel', 'Pilliga', 'NSW', 2388, '02-6995-9902', 'julio.mikel@mikel.net.au',]
 ['Aide', 'Ghera', 'Rhodes', 'NSW', 2138, '02-3738-7508', 'aide.ghera@ghera.com.au',]
 ['Noelia', 'Brackett', 'Castletown', 'WA', 6450, '08-3773-3770', 'noelia@brackett.net.au',]
 ['Lenora', 'Delacruz', 'Turill', 'NSW', 2850, '02-7862-5151', 'lenora@delacruz.net.au']]

### BIN500 Assignment 3, Nisan Ece Kalem, 2008472

#### Question 1)


data_list1 = data_list[:] ### Before beginning I created a copy of data_list given, and popped the first element, because it's header and does not contain any personal info, thus it's unnecessary
data_list1.pop(0)

### Creating dictionaries for function 1
sameName = {} ## Creating the empty dictionary

for entry in data_list1: ###beginning of the loop to iterate the names in the list
    name = entry[0] 
    surname = entry[1]
    if name in sameName:
        sameName[name].append(name + ' ' + surname) ###if the name is in the dictionary, the persons full name is appended to dictionary's value (value's type is a list) 
        
    else:
        sameName[name] = [name + ' ' + surname] ### else, it generates a list as dictionary's value
            
            
#### Creating dictionary for function 2
keys =  [i[0]+ ' ' +i[1] for i in data_list1[1:]] ### creates keys as person's full name
vals = [x[2:] for x in data_list1[1:]] ### Creates values as list of city, state, phone, email
fihrist = dict(zip(keys, vals)) ### generates dictionary by zipping keys and values


### Creating the dictionary for function 3

cityDict = {} 
for entry in data_list1[1:]: ### creating a dictionary where the city is the key and list of full names are the values
    city = entry[2]
    name = entry[0]
    surname = entry[1]
    FullName = name + ' ' + surname

    if city in cityDict:
        cityDict[city].append(FullName)
    else:
        cityDict[city] = [FullName]


### Function 1


def f1(n):
    global sameName
    print('%i people found whose name is %s as %s' % (len(sameName[n]), n ,', '.join(sameName[n]))) ###prints the number of people found in the same name as length of the values of the key, input, and uses string method join to concatanate the elements of the list 
        

### Function 2


def f2(firstname, lastname):
    global fihrist
    if firstname + ' ' + lastname in fihrist:
        info = fihrist[firstname + ' ' +lastname] ### values of the dictionary
        person = firstname + ' ' + lastname
        print('%s`s city is %s, state is %s, post number is %s, phone is %s and email is %s' % (person, info[0], info[1], info[2], info[3], info[4]) ) ### prints the info of the person 
    else:
        print('The person %s %s that you are looking for is not found on the list' % (firstname, lastname))
    
    

### Function 3


# Here I decided to write a function than requires full name from the user, and prints out the input's personal info and other people that live in the same city.

def f3(firstname, lastname):
    fullname = firstname+ " "+ lastname
    if fullname in fihrist: 
        city = fihrist[fullname][0] ## retrieves the city info of the person from the fihrist
        othercitizens = cityDict[city].copy() ### copies the dictionary's values => not to change the original cityDict
        othercitizens.remove(fullname) ### Removes the input person from the value
        f2(firstname, lastname) ### recalls the function two
        print('Other citizen(s) of this city include: %s' % ", ".join(othercitizens)) ### prints out the other citizen(s) that live in the same city
    else:
        print('Please check your input and try again')
    

### Explanations of the functions for the user and required inputs of the functions

print('Welcome to digital phonebook. Lets get to know you.') 

name = input('Enter your name\t') 
lastname = input('Enter your last name\t')


print('Hello %s %s. This phonebook has several features' % (name, lastname)) ###Informs the user about the capabilities of the phonebook
print('Feature 1 is asks the name of the person and displays how many people has that name in the phonebook')
print('Feature 2 is asks the full name of the person and displays the person`s personal info')
print('Feature 3 is asks the full name of the person and displays the person`s personal info and other people who live in the same city.')

functioninp = int(input('Please enter the number of the feature that you want to use')) ###asks the desired feature that user wants to use

if functioninp == 1: ###uses boolean operator for the function decision and asks the further inputs accordingly
    f1name = str(input('Please enter the name of the person'))
    f1(f1name)
elif functioninp == 2:
    f2name = str(input('Please enter the name of the person'))
    f2lastname = str(input('Please enter the lastname of the person'))
    f2(f2name, f2lastname)
elif functioninp == 3:
    f3name = str(input('Please enter the name of the person'))
    f3lastname = str(input('Please enter the lastname of the person'))
    f3(f3name, f3lastname)
else:
    print("Please choose between numbers: 1, 2, 3")


###2)

alphabetdict = {v:k for v, k in enumerate('abcdefghijklmnopqrstuvwxyz', start = 1)} ##Generates a dictionary of letters in alphabeth; position as keys, letters as values

def decrypter(n):
    global alphabetdict
    words = n.split('  ') ###string method to split strings in a list that has double spaces
    decrypted_words = [] ###empty dictionaries for the decrypted words
    for word in words: ###loop to append integers with single space and append to words
        letters = word.split(' ')
        decrpyted = "".join([alphabetdict[int(x)] for x in letters]) ### for loop to iterate
        decrypted_words.append(decrpyted)
    decrypted_words = " ".join(decrypted_words)
    return(decrypted_words)



n = '9 6  25 15 21  3 15 21 12 4  20 9 13 5  20 18 1 22 5 12  23 8 5 14  23 15 21 12 4  25 15 21  7 15  1 14 19 23 5 18  23 9 20 8  12 5 20 20 5 18 19  23 5  4 15 14 20  8 1 22 5  14 21 13 2 5 18 19'

print(decrypter(n))


###After I deciphered the given message, I wrote a function to cipher my answer. 

def encrypter(m):
    revAlphabetdict = dict(zip(alphabetdict.values(), alphabetdict.keys()))
    words = m.split(' ') ### string method split to split the numbers with single space into a list
    encrypted_words = []
    for word in words: ### loop to append the letters with single space and words with double space
        letters = [i for i in word]
        encrypted = ' '.join([str(revAlphabetdict[x]) for x in letters])
        encrypted_words.append(encrypted)
    encrypted_words = '  '. join(encrypted_words)
    return encrypted_words


m = 'i would go to early seventies'
encrypter(m)

