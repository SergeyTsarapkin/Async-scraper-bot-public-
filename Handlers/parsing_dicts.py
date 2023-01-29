fed_districts_dict = {'ЦФО': '01', 'СЗФО': '02', 'ЮФО': '03', 'ПФО': '04', 'УФО': '05', 'СФО': '06', 'ДФО': '07', 'СКФО': '08', 'Неизвестный ФО': 'NN'}

fed_subj_dict = {'01': ['14000 - БЕЛГОРОДСКАЯ ОБЛАСТЬ', '15000 - БРЯНСКАЯ ОБЛАСТЬ', '17000 - ВЛАДИМИРСКАЯ ОБЛАСТЬ',
                        '20000 - ВОРОНЕЖСКАЯ ОБЛАСТЬ', '24000 - ИВАНОВСКАЯ ОБЛАСТЬ', '28000 - ТВЕРСКАЯ ОБЛАСТЬ',
                        '29000 - КАЛУЖСКАЯ ОБЛАСТЬ', '34000 - КОСТРОМСКАЯ ОБЛАСТЬ', '38000 - КУРСКАЯ ОБЛАСТЬ',
                        '42000 - ЛИПЕЦКАЯ ОБЛАСТЬ', '45000 - ГОРОД МОСКВА СТОЛИЦА РОССИЙСКОЙ ФЕДЕРАЦИИ ГОРОД ФЕДЕРАЛЬНОГО ЗНАЧЕНИЯ',
                        '46000 - МОСКОВСКАЯ ОБЛАСТЬ', '54000 - ОРЛОВСКАЯ ОБЛАСТЬ', '61000 - РЯЗАНСКАЯ ОБЛАСТЬ',
                        '66000 - СМОЛЕНСКАЯ ОБЛАСТЬ', '68000 - ТАМБОВСКАЯ ОБЛАСТЬ', '70000 - ТУЛЬСКАЯ ОБЛАСТЬ', '78000 - ЯРОСЛАВСКАЯ ОБЛАСТЬ'],
                 '02': ['11000 - АРХАНГЕЛЬСКАЯ ОБЛАСТЬ', '11100 - НЕНЕЦКИЙ АВТОНОМНЫЙ ОКРУГ (АРХАНГЕЛЬСКАЯ ОБЛАСТЬ)',
                        '19000 - ВОЛОГОДСКАЯ ОБЛАСТЬ', '27000 - КАЛИНИНГРАДСКАЯ ОБЛАСТЬ',
                        '40000 - ГОРОД САНКТ-ПЕТЕРБУРГ ГОРОД ФЕДЕРАЛЬНОГО ЗНАЧЕНИЯ', '41000 - ЛЕНИНГРАДСКАЯ ОБЛАСТЬ',
                        '47000 - МУРМАНСКАЯ ОБЛАСТЬ', '49000 - НОВГОРОДСКАЯ ОБЛАСТЬ', '58000 - ПСКОВСКАЯ ОБЛАСТЬ',
                        '86000 - РЕСПУБЛИКА КАРЕЛИЯ', '87000 - РЕСПУБЛИКА КОМИ'],
                 '03': ['03000 - КРАСНОДАРСКИЙ КРАЙ', '12000 - АСТРАХАНСКАЯ ОБЛАСТЬ', '18000 - ВОЛГОГРАДСКАЯ ОБЛАСТЬ',
                        '35000 - РЕСПУБЛИКА КРЫМ', '60000 - РОСТОВСКАЯ ОБЛАСТЬ', '67000 - СЕВАСТОПОЛЬ - ГОРОД ФЕДЕРАЛЬНОГО ЗНАЧЕНИЯ',
                        '79000 - РЕСПУБЛИКА АДЫГЕЯ (АДЫГЕЯ)', '85000 - РЕСПУБЛИКА КАЛМЫКИЯ'],
                 '04': ['22000 - НИЖЕГОРОДСКАЯ ОБЛАСТЬ', '33000 - КИРОВСКАЯ ОБЛАСТЬ', '36000 - САМАРСКАЯ ОБЛАСТЬ',
                        '53000 - ОРЕНБУРГСКАЯ ОБЛАСТЬ', '56000 - ПЕНЗЕНСКАЯ ОБЛАСТЬ', '57000 - ПЕРМСКИЙ КРАЙ',
                        '63000 - САРАТОВСКАЯ ОБЛАСТЬ', '73000 - УЛЬЯНОВСКАЯ ОБЛАСТЬ', '80000 - РЕСПУБЛИКА БАШКОРТОСТАН',
                        '88000 - РЕСПУБЛИКА МАРИЙ ЭЛ', '89000 - РЕСПУБЛИКА МОРДОВИЯ', '92000 - РЕСПУБЛИКА ТАТАРСТАН (ТАТАРСТАН)',
                        '94000 - УДМУРТСКАЯ РЕСПУБЛИКА', '97000 - ЧУВАШСКАЯ РЕСПУБЛИКА - ЧУВАШИЯ'],
                 '05': ['37000 - КУРГАНСКАЯ ОБЛАСТЬ', '65000 - СВЕРДЛОВСКАЯ ОБЛАСТЬ', '71000 - ТЮМЕНСКАЯ ОБЛАСТЬ',
                        '71100 - ХАНТЫ-МАНСИЙСКИЙ АВТОНОМНЫЙ ОКРУГ (ТЮМЕНСКАЯ ОБЛАСТЬ)',
                        '71140 - ЯМАЛО-НЕНЕЦКИЙ АВТОНОМНЫЙ ОКРУГ (ТЮМЕНСКАЯ ОБЛАСТЬ)', '75000 - ЧЕЛЯБИНСКАЯ ОБЛАСТЬ'],
                 '06': ['01000 - АЛТАЙСКИЙ КРАЙ', '04000 - КРАСНОЯРСКИЙ КРАЙ', '25000 - ИРКУТСКАЯ ОБЛАСТЬ',
                        '32000 - КЕМЕРОВСКАЯ ОБЛАСТЬ - КУЗБАСС', '50000 - НОВОСИБИРСКАЯ ОБЛАСТЬ', '52000 - ОМСКАЯ ОБЛАСТЬ',
                        '69000 - ТОМСКАЯ ОБЛАСТЬ', '84000 - РЕСПУБЛИКА АЛТАЙ', '93000 - РЕСПУБЛИКА ТЫВА', '95000 - РЕСПУБЛИКА ХАКАСИЯ'],
                 '07': ['05000 - ПРИМОРСКИЙ КРАЙ', '08000 - ХАБАРОВСКИЙ КРАЙ', '10000 - АМУРСКАЯ ОБЛАСТЬ', '30000 - КАМЧАТСКИЙ КРАЙ',
                        '44000 - МАГАДАНСКАЯ ОБЛАСТЬ', '64000 - САХАЛИНСКАЯ ОБЛАСТЬ', '76000 - ЗАБАЙКАЛЬСКИЙ КРАЙ',
                        '77000 - ЧУКОТСКИЙ АВТОНОМНЫЙ ОКРУГ', '81000 - РЕСПУБЛИКА БУРЯТИЯ', '98000 - РЕСПУБЛИКА САХА (ЯКУТИЯ)',
                        '99000 - ЕВРЕЙСКАЯ АВТОНОМНАЯ ОБЛАСТЬ'],
                 '08': ['07000 - СТАВРОПОЛЬСКИЙ КРАЙ', '26000 - РЕСПУБЛИКА ИНГУШЕТИЯ', '82000 - РЕСПУБЛИКА ДАГЕСТАН',
                        '83000 - КАБАРДИНО-БАЛКАРСКАЯ РЕСПУБЛИКА', '90000 - РЕСПУБЛИКА СЕВЕРНАЯ ОСЕТИЯ-АЛАНИЯ',
                        '91000 - КАРАЧАЕВО-ЧЕРКЕССКАЯ РЕСПУБЛИКА', '96000 - ЧЕЧЕНСКАЯ РЕСПУБЛИКА']}


g_20 = ['CN', 'IN', 'US', 'ID', 'BR', 'RU', 'JP', 'MX', 'DE', 'TR', 'FR', 'GB', 'IT', 'ZA', 'KR', 'AR', 'CA', 'SA', 'AU', 'BE', 'BG', 'CZ', 'DK', 'EE', 'IE', 'EL', 'ES', 'HR', 'CY', 'LV', 'LT', 'LU', 'HU', 'MT', 'NL', 'AT', 'PL', 'PT', 'RO', 'SI', 'SK', 'FI', 'SE']

g_8 = ['FR', 'DE', 'IT', 'GB', 'JP', 'US', 'CA', 'RU']

european_union = ['BE', 'BG', 'CZ', 'DK', 'DE', 'EE', 'IE', 'EL', 'ES', 'FR', 'HR', 'IT', 'CY', 'LV', 'LT', 'LU', 'HU', 'MT', 'NL', 'AT', 'PL', 'PT', 'RO', 'SI', 'SK', 'FI', 'SE']

countries_list = {'AB': ['АБХАЗИЯ', 'REPUBLIC ABKHAZIA'], 'AU': ['АВСТРАЛИЯ', 'AUSTRALIA'], 'AT': ['АВСТРИЯ', 'AUSTRIA'],
                  'AZ': ['АЗЕРБАЙДЖАН', 'AZERBAIJAN'], 'AL': ['АЛБАНИЯ', 'ALBANIA'], 'DZ': ['АЛЖИР', 'ALGERIA'],
                  'AS': ['АМЕРИКАНСКОЕ САМОА', 'AMERICAN (EASTERN) SAMOA'], 'Al': ['АНГИЛЬЯ', 'ANGUILLA'],
                  'АО': ['АНГОЛА', 'ANGOLA'], 'AD': ['АНДОРРА', 'ANDORRA'], 'AQ': ['АНТАРКТИДА', 'ANTARCTICA'],
                  'AG': ['АНТИГУА И БАРБУДА', 'ANTIGUA AND BARBUDA'], 'AR': ['АРГЕНТИНА', 'ARGENTINA'], 'AM': ['АРМЕНИЯ', 'ARMENIA'],
                  'AW': ['АРУБА', 'ARUBA'], 'AF': ['АФГАНИСТАН', 'AFGANISTAN'], 'BS': ['БАГАМЫ', 'BAHAMAS'],
                  'BD': ['БАНГЛАДЕШ', 'BANGLADESH'], 'BB': ['БАРБАДОС', 'BARBADOS'], 'BH': ['БАХРЕЙН', 'BAHRAIN'],
                  'BY': ['БЕЛАРУСЬ', 'BELARUS'], 'BZ': ['БЕЛИЗ', 'BELIZE'], 'BE': ['БЕЛЬГИЯ', 'BELGIUM'], 'BJ': ['БЕНИН', 'BENIN'],
                  'BM': ['БЕРМУДЫ', 'BERMUDA'], 'BG': ['БОЛГАРИЯ', 'BULGARIA'], 'ВО': ['БОЛИВИЯ, МНОГОНАЦИОНАЛ. ГОСУДАРСТВО', 'BOLIVIA'],
                  'BQ': ['БОНЕЙР, СИНТ-ЭСТАТИУС И САБА', 'BONAIRE, SAINT EUSTATIUS AND SABA'], 'BA': ['БОСНИЯ И ГЕРЦЕГОВИНА', 'BOSNIA AND HERZEGOWINA'],
                  'BW': ['БОТСВАНА', 'BOTSWANA'], 'BR': ['БРАЗИЛИЯ', 'BRAZIL'], 'IO': ['БРИТАНСКАЯ ТЕРРИТОРИЯ В ИНД. ОКЕАНЕ', 'BRITISH INDIAN OCEAN TERRITORY'],
                  'BN': ['БРУНЕЙ-ДАРУССАЛАМ', 'BRUNEL'], 'BV': ['БУВЕ', 'BOUVET ISLAND'], 'BF': ['БУРКИНА-ФАСО', 'BURKINA FASO'],
                  'Bl': ['БУРУНДИ', 'BURUNDI'], 'BT': ['БУТАН', 'BHUTAN'], 'VU': ['ВАНУАТУ', 'VANUATU'], 'HU': ['ВЕНГРИЯ', 'HUNGARY'],
                  'VE': ['ВЕНЕСУЭЛА, БОЛИВИВА РИАНСКАЯ РЕСПУБЛИКА', 'VENEZUELA'], 'VG': ['ВИРГИНСКИЕ ОСТРОВА, БРИТАНСКИЕ', 'VIRGIN ISLANDS'],
                  'VI': ['ВИРГИНСКИЕ ОСТРОВА, США', 'VIRGIN ISLANDS (U.S.)'], 'VN': ['ВЬЕТНАМ', 'VIETNAM'],
                  'GA': ['ГАБОН', 'GABON'], 'HT': ['ГАИТИ', 'HAITI'], 'GY': ['ГАЙАНА', 'GUYANA'], 'GM': ['ГАМБИЯ', 'GAMBIA'],
                  'GH': ['ГАНА', 'GHANA'], 'GP': ['ГВАДЕЛУПА', 'GUADELOUPE'], 'GT': ['ГВАТЕМАЛА', 'GUATEMALA'], 'GN': ['ГВИНЕЯ', 'GUINEA'],
                  'GW': ['ГВИНЕЯ-БИСАУ', 'GUINEA-BISSAU'], 'DE': ['ГЕРМАНИЯ', 'GERMANY'], 'GG': ['ГЕРНСИ', 'GUERNSEY'],
                  'Gl': ['ГИБРАЛТАР', 'GIBRALTAR'], 'HN': ['ГОНДУРАС', 'HONDURAS'], 'HK': ['ГОНКОНГ', 'HONG KONG'],
                  'GD': ['ГРЕНАДА', 'GRENADA'], 'GL': ['ГРЕНЛАНДИЯ', 'GREENLAND'], 'GR': ['ГРЕЦИЯ', 'GREECE'], 'GE': ['ГРУЗИЯ', 'GEORGIA'],
                  'GU': ['ГУАМ', 'GUAM'], 'DK': ['ДАНИЯ', 'DENMARK'], 'JE': ['ДЖЕРСИ', 'JERSEY'], 'DJ': ['ДЖИБУТИ', 'DJIBOUTI'],
                  'DM': ['ДОМИНИКА', 'DOMINICA'], 'DO': ['ДОМИНИКАНСКАЯ РЕСПУБЛИКА', 'DOMINICAN REPUBLIC'], 'EG': ['ЕГИПЕТ', 'EGYPT'],
                  'ZM': ['ЗАМБИЯ', 'ZAMBIA'], 'EH': ['ЗАПАДНАЯ САХАРА', 'WESTERN SAHARA'], 'ZW': ['ЗИМБАБВЕ', 'ZIMBABWE'],
                  'IL': ['ИЗРАИЛЬ', 'ISRAEL'], 'IN': ['ИНДИЯ', 'INDIA'], 'ID': ['ИНДОНЕЗИЯ', 'INDONESIA'], 'JO': ['ИОРДАНИЯ', 'JORDAN'],
                  'IQ': ['ИРАК', 'IRAQ'], 'IR': ['ИРАН, ИСЛАМСКАЯ РЕСПУБЛИКА', 'IRAN'], 'IE': ['ИРЛАНДИЯ', 'IRELAND'],
                  'IS': ['ИСЛАНДИЯ', 'ICELAND'], 'ES': ['ИСПАНИЯ', 'SPAIN'], 'IT': ['ИТАЛИЯ', 'ITALY'], 'YE': ['ЙЕМЕН', 'YEMEN'],
                  'CV': ['КАБО-ВЕРДЕ', 'CAPE VERDE'], 'KZ': ['КАЗАХСТАН', 'KAZAKHSTAN'], 'KH': ['КАМБОДЖА', 'CAMBODIA'],
                  'CM': ['КАМЕРУН', 'CAMEROON'], 'CA': ['КАНАДА', 'CANADA'], 'QA': ['КАТАР', 'QATAR'], 'KE': ['КЕНИЯ', 'KENYA'],
                  'CY': ['КИПР', 'CYPRUS'], 'KG': ['КЫРГЫЗСТАН', 'KYRGYZSTAN'], 'Kl': ['КИРИБАТИ', 'KIRIBATI'], 'CN': ['КИТАЙ', 'CHINA'],
                  'CC': ['КОКОСОВЫЕ (КИЛИНГ) ОСТРОВА', 'COCOS (KEELING) ISLANDS'], 'CO': ['КОЛУМБИЯ', 'COLOMBIA'], 'KM': ['КОМОРЫ', 'COMOROC'],
                  'CG': ['КОНГО', 'CONGO'], 'CD': ['КОНГО, ДЕМОКРАТИЧЕСКАЯ РЕСПУБЛИКА', 'CONGO, THE DEMOCRATIC REPUBLIC OF THE'],
                  'KP': ['КОРЕЯ, НАРОДНО-ДЕМОКРАТИЧЕСКАЯ РЕСПУБЛИКА', 'KOREA, DEMOCRATIC PEOPLE’S REPUBLIC OF'],
                  'KR': ['КОРЕЯ, РЕСПУБЛИКА', 'KOREA, REPUBLIC OF'], 'CR': ['КОСТА-РИКА', 'COSTA RICA'], 'CI': ['КОТ-Д’ИВУАР', 'COTE D’VOIRE'],
                  'CU': ['КУБА', 'CUBA'], 'KW': ['КУВЕЙТ', 'KUWAIT'], 'CW': ['КЮРАСАО', 'CURACAO'], 'LA': ['ЛАОС', "LAO PEOPLE'S DEMOCRATIC REPUBLIC"],
                  'LV': ['ЛАТВИЯ', 'LATVIA'], 'LS': ['ЛЕСОТО', 'LESOTHO'], 'LR': ['ЛИБЕРИЯ', 'LIBERIA'], 'LB': ['ЛИВАН', 'LIVANON'],
                  'LY': ['ЛИВИЯ', 'LIBYA'], 'LT': ['ЛИТВА', 'LITHUANIA'], 'LI': ['ЛИХТЕНШТЕЙН', 'LIECHTENSTEIN'], 'LU': ['ЛЮКСЕМБУРГ', 'LUXEMBOURG'],
                  'MU': ['МАВРИКИЙ', 'MAURITIUS'], 'MR': ['МАВРИТАНИЯ', 'MAURITANIA'], 'MG': ['МАДАГАСКАР', 'MADAGASCAR'],
                  'YT': ['МАЙОТТА', 'MAYOTTE'], 'MO': ['МАКАО', 'MACAU'], 'MW': ['МАЛАВИ', 'MALAWI'], 'MY': ['МАЛАЙЗИЯ', 'MALAYSIA'],
                  'ML': ['МАЛИ', 'MALI'], 'UM': ['МАЛЫЕ ТИХООКЕАНСКИЕ ОСТРОВА (США)', 'UNITED STATES MINOR OUTLYING ISLANDS'],
                  'MV': ['МАЛЬДИВЫ', 'MALDIVES'], 'MT': ['МАЛЬТА', 'MALTA'], 'MA': ['МАРОККО', 'MOROCCO'], 'MQ': ['МАРТИНИКА', 'MARTINIQUE'],
                  'МН': ['МАРШАЛЛОВЫ ОСТРОВА', 'MARSHALL ISLANDS'], 'MX': ['МЕКСИКА', 'MEXICO'], 'FM': ['МИКРОНЕЗИЯ, ФЕДЕРАТИВНЫЕ ШТАТЫ', 'MICRONESIA'],
                  'MZ': ['МОЗАМБИК', 'MOZAMBIQUE'], 'MD': ['МОЛДОВА, РЕСПУБЛИКА', 'MOLDOVA, REPUBLIC OF'], 'MC': ['МОНАКО', 'MONACO'],
                  'MN': ['МОНГОЛИЯ', 'MONGOLIA'], 'MS': ['МОНТСЕРРАТ', 'MONTSERRAT'], 'MM': ['МЬЯНМА', 'MYANMAR (BURMA)'],
                  'NA': ['НАМИБИЯ', 'NAMIBIA'], 'NR': ['НАУРУ', 'NAURU'], 'NP': ['НЕПАЛ', 'NEPAL'], 'NE': ['НИГЕР', 'NIGER'],
                  'NG': ['НИГЕРИЯ', 'NIGERIA'], 'NL': ['НИДЕРЛАНДЫ', 'NETHERLANDS'], 'Nl': ['НИКАРАГУА', 'NICARAGUA'],
                  'NU': ['НИУЭ', 'NIUE'], 'NZ': ['НОВАЯ ЗЕЛАНДИЯ', 'NEW ZEALAND'], 'NC': ['НОВАЯ КАЛЕДОНИЯ', 'NEW CALEDONIA'],
                  'NO': ['НОРВЕГИЯ', 'NORWAY'], 'AE': ['ОБЪЕДИНЕННЫЕ АРАБСКИЕ ЭМИРАТЫ', 'UNITED ARAB EMIRATES'], 'OM': ['ОМАН', 'OMAN'],
                  'IM': ['ОСТРОВ МЭН', 'ISLE OF MAN'], 'NF': ['ОСТРОВ НОРФОЛК', 'NORFOLK ISLAND'], 'CX': ['ОСТРОВ РОЖДЕСТВА', 'CHRISTMAS ISLAND (AUSTRALIA)'],
                  'HM': ['ОСТРОВА ХЕРД И ОСТРОВА МАКДОНАЛЬД', 'HEARD AND MC DONALD ISLANDS'], 'KY': ['ОСТРОВА КАЙМАН', 'CAYMAN ISLANDS'],
                  'CK': ['ОСТРОВА КУКА', 'COOK ISLANDS'], 'ТС': ['ОСТРОВА ТЕРКС И КАЙКОС', 'TURKS AND CAICOS ISLANDS'],
                  'PK': ['ПАКИСТАН', 'PAKISTAN'], 'PW': ['ПАЛАУ', 'PACIFIC ISLANDS (PALAU)'], 'PS': ['ПАЛЕСТИНА, ГОСУДАРСТВО', 'STATE OF PALESTINE'],
                  'PA': ['ПАНАМА', 'PANAMA'], 'VA': ['ПАПСКИЙ ПРЕСТОЛ (ГОС. ГОРОД ВАТИКАН)', 'VATICAN (HOLY SEE)'],
                  'PG': ['ПАПУА-НОВАЯ ГВИНЕЯ', 'PAPUA NEW GUINEA'], 'PY': ['ПАРАГВАЙ', 'PARAGUAY'], 'PE': ['ПЕРУ', 'PERU'],
                  'PN': ['ПИТКЕРН', 'PITCAIRN'], 'PL': ['ПОЛЬША', 'POLAND'], 'PT': ['ПОРТУГАЛИЯ', 'PORTUGAL'], 'PR': ['ПУЭРТО-РИКО', 'PUERTO RICO'],
                  'MK': ['РЕСПУБЛИКА МАКЕДОНИЯ', 'MACEDONIA'], 'RE': ['РЕЮНЬОН', 'REUNION'], 'RU': ['РОССИЯ', 'RUSSIAN'], 'RW': ['РУАНДА', 'RWANDA'],
                  'RO': ['РУМЫНИЯ', 'ROMANIA'], 'WS': ['САМОА', 'SAMOA'], 'SM': ['САН-МАРИНО', 'SAN MARINO'],
                  'ST': ['САН-ТОМЕ И ПРИНСИПИ', 'SAO TOME AND PRINCIPE'], 'SA': ['САУДОВСКАЯ АРАВИЯ', 'SAUDI ARABIA'],
                  'SZ': ['СВАЗИЛЕНД', 'SWAZILAND '], 'SH': ['СВ.ЕЛЕНА, О.ВОЗНЕСЕНИЯ, ТР.-ДА-КУНЬЯ', 'ST. HELENA, ASCENSION AND TRISTAN DA KUNHA'],
                  'MP': ['СЕВЕРНЫЕ МАРИАНСКИЕ ОСТРОВА', 'NORTHERN MARIANA ISLANDS'], 'SC': ['СЕЙШЕЛЫ', 'SEYCHELLES'],
                  'BL': ['СЕН-БАРТЕЛЕМИ', 'SAINT BARTHELEMY'], 'SN': ['СЕНЕГАЛ', 'SENEGAL'], 'MF': ['СЕН-МАРТЕН', 'SAINT MARTIN'],
                  'SX': ['СЕН-МАРТЕН (НИДЕРЛАНДСКАЯ ЧАСТЬ)', 'SINT MAARTEN'], 'PM': ['СЕН-ПЬЕР И МИКЕЛОН', 'SAINT PIERRE AND MIQUELON'],
                  'VC': ['СЕНТ-ВИНСЕНТ И ГРЕНАДИНЫ', 'SAINT VINCENT AND THE GRENADINES'], 'KN': ['СЕНТ-КИТС И НЕВИС', 'SAINT KITTS AND NEVIS'],
                  'LC': ['СЕНТ-ЛЮСИЯ', 'SAINT LUCIA'], 'RS': ['СЕРБИЯ', 'SERBIA'], 'SG': ['СИНГАПУР', 'SINGAPORE'],
                  'SY': ['СИРИЙСКАЯ АРАБСКАЯ РЕСПУБЛИКА', 'SYRIA'], 'SK': ['СЛОВАКИЯ', 'SLOVAKIA'], 'Sl': ['СЛОВЕНИЯ', 'SLOVENIA'],
                  'GB': ['СОЕДИНЕННОЕ КОРОЛЕВСТВО', 'GREAT BRITAIN'], 'US': ['СОЕДИНЕННЫЕ ШТАТЫ', 'UNITED STATES'],
                  'SB': ['СОЛОМОНОВЫ ОСТРОВА', 'SOLOMON ISLANDS'], 'SO': ['СОМАЛИ', 'SOMALIA'], 'SD': ['СУДАН', 'SUDAN'],
                  'SR': ['СУРИНАМ', 'SURINAME'], 'SL': ['СЬЕРРА-ЛЕОНЕ', 'SIERRA LEONE'], 'TJ': ['ТАДЖИКИСТАН', 'TAJIKISTAN'], 'TH': ['ТАИЛАНД', 'THAILAND'],
                  'TW': ['ТАЙВАНЬ (КИТАЙ)', 'TAIWAN, PROVINCE OF CHINA'], 'TZ': ['ТАНЗАНИЯ, ОБЪЕДИНЕННАЯ РЕСПУБЛИКА', 'TANZANIA'],
                  'TL': ['ТИМОР-ЛЕСТЕ', 'EAST TIMOR'], 'TG': ['ТОГО', 'TOGO'], 'TK': ['ТОКЕЛАУ', 'TOKELAU'], 'TO': ['ТОНГА', 'TONGA'],
                  'TT': ['ТРИНИДАД И ТОБАГО', 'TRINIDAD AND TOBAGO'], 'TV': ['ТУВАЛУ', 'TUVALU'], 'TN': ['ТУНИС', 'TUNISIA'],
                  'TM': ['ТУРКМЕНИЯ', 'TURKMENISTAN'], 'TR': ['ТУРЦИЯ', 'TURKEY'], 'UG': ['УГАНДА', 'UGANDA'], 'UZ': ['УЗБЕКИСТАН', 'UZBEKISTAN'],
                  'UA': ['УКРАИНА', 'UKRAINA'], 'WF': ['УОЛЛИС И ФУТУНА', 'WALLIS AND FUTUNA ISLANDS'], 'UY': ['УРУГВАЙ', 'URUGUAY'],
                  'FO': ['ФАРЕРСКИЕ ОСТРОВА', 'FAROE ISLANDS'], 'FJ': ['ФИДЖИ', 'FIJI'], 'PH': ['ФИЛИППИНЫ', 'PHILIPPINES'],
                  'Fl': ['ФИНЛЯНДИЯ', 'FINLAND'], 'FK': ['ФОЛКЛЕНДСКИЕ ОСТРОВА (МАЛЬВИНСКИЕ)', 'FALKLAND ISLANDS (MALVINAS)'],
                  'FR': ['ФРАНЦИЯ', 'FRANCE'], 'GF': ['ФРАНЦУЗСКАЯ ГВИАНА', 'FRENCH GUIANA'], 'PF': ['ФРАНЦУЗСКАЯ ПОЛИНЕЗИЯ', 'FRENCH POLYNESIA'],
                  'TF': ['ФРАНЦУЗСКИЕ ЮЖНЫЕ ТЕРРИТОРИИ', 'FRENCH SOUTHERN TERRITORIES'], 'HR': ['ХОРВАТИЯ', 'CROATIA'],
                  'CF': ['ЦЕНТРАЛЬНО-АФРИКАНСКАЯ РЕСПУБЛИКА', 'CENTRAL AFRICAN REPUBLIC'], 'TD': ['ЧАД', 'CHAD'], 'ME': ['ЧЕРНОГОРИЯ', 'MONTENEGRO'],
                  'CZ': ['ЧЕХИЯ', 'CZECH REPUBLIC'], 'CL': ['ЧИЛИ', 'CHILE'], 'CH': ['ШВЕЙЦАРИЯ', 'SWITZERLAND'], 'SE': ['ШВЕЦИЯ', 'SWEDEN'],
                  'SJ': ['ШПИЦБЕРГЕН И ЯН-МАЙЕН', 'SVALBARD AND JAN MAYEN ISLANDS'], 'LK': ['ШРИ-ЛАНКА', 'SRI LANKA'],
                  'ЕС': ['ЭКВАДОР', 'ECUADOR'], 'GQ': ['ЭКВАТОРИАЛЬНАЯ ГВИНЕЯ', 'EQUATORIAL GUINEA'], 'АХ': ['ЭЛАНДСКИЕ ОСТРОВА', 'ALAND ISLANDS'],
                  'SV': ['ЭЛЬ-САЛЬВАДОР', 'EL SALVADOR'], 'ER': ['ЭРИТРЕЯ', 'ERITREA'], 'ЕЕ': ['ЭСТОНИЯ', 'ESTONIA'],
                  'ET': ['ЭФИОПИЯ', 'ETHIOPIA'], 'GS': ['ЮЖН. ДЖОРДЖИЯ И ЮЖН. САНДВИЧ. ОСТРОВА', 'S. SANDWICH ISLANDS'],
                  'ZA': ['ЮЖНАЯ АФРИКА', 'SOUTH AFRICA'], 'OS': ['ЮЖНАЯ ОСЕТИЯ', 'SOUTH OSSETIA'], 'SS': ['ЮЖНЫЙ СУДАН', 'SOUTH SUDAN'],
                  'JM': ['ЯМАЙКА', 'JAMAICA'], 'JP': ['ЯПОНИЯ', 'JAPAN']}

