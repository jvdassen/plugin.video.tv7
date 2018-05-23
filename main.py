# -*- coding: utf-8 -*-
# Module: default
# Author: Jan vdA

import sys
from urllib import urlencode
from urlparse import parse_qsl
import xbmcgui
import xbmcplugin

# Get the plugin url in plugin:// notation.
_url = sys.argv[0]
# Get the plugin handle as an integer number.
_handle = int(sys.argv[1])

# Free sample videos are provided by www.vidsplay.com
# Here we use a fixed set of properties simply for demonstrating purposes
# In a "real life" plugin you will need to get info and links to video files/streams
# from some web-site or online service.
VIDEOS = {'channels':
[{'name': 'SRF1 HD',
'thumb': 'https://upload.wikimedia.org/wikipedia/commons/thumb/2/29/Logo_SRF_1.svg/1200px-Logo_SRF_1.svg.png',
'video': 'udp://@239.77.0.77:5000',
'genre': 'TV'},
{'name': 'SRFzwei HD',
'thumb': 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/48/Logo_SRF_2.svg/1200px-Logo_SRF_2.svg.png',
'video': 'udp://@239.77.0.78:5000',
'genre': 'TV'},
{'name': 'SRF Info HD',
'thumb': 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d9/Logo_SRF_info.svg/1200px-Logo_SRF_info.svg.png',
'video': 'udp://@239.77.0.5:5000',
'genre': 'TV'},
{'name':'3+ HD','video':'udp://@239.77.0.117:5000','thumb':'https://upload.wikimedia.org/wikipedia/de/thumb/a/a0/Logo_3plus.svg/1200px-Logo_3plus.svg.png','genre':'TV'},
{'name':'4+ HD','video':'udp://@239.77.0.118:5000','thumb':'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e2/Logo_4plus.svg/2000px-Logo_4plus.svg.png','genre':'TV'},
{'name':'5+ HD','video':'udp://@239.77.0.179:5000','thumb':'http://www.evard.ch/digitv/logo/5plus_hd.png','genre':'TV'},
{'name':'TV24 HD','video':'udp://@239.77.0.183:5000','thumb':'http://www.persoenlich.com/media/cache/top/sites/default/files/tv24logo_positiv_jpg_web.jpg','genre':'TV'},
{'name':'TV25 HD','video':'udp://@239.77.0.184:5000','thumb':'https://upload.wikimedia.org/wikipedia/commons/3/31/TV25Logo_cmyk.jpg','genre':'TV'},
{'name':'Tele Züri HD','video':'udp://@239.77.0.203:5000','thumb':'https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Logo_TeleZ%C3%BCri.svg/1280px-Logo_TeleZ%C3%BCri.svg.png','genre':'TV'},
{'name':'TELE TOP HD','video':'udp://@239.77.0.206:5000','thumb':'https://upload.wikimedia.org/wikipedia/de/thumb/a/a9/Logo_Tele_Top.svg/1200px-Logo_Tele_Top.svg.png','genre':'TV'},
{'name':'TeleBärn HD','video':'udp://@239.77.0.201:5000','thumb':'https://www.telebaern.tv/images/886075a.png','genre':'TV'},
{'name':'TVO HD','video':'udp://@239.77.0.209:5000','thumb':'https://www.firstonetv.net/images/logos/ch/TVO.png','genre':'TV'},
{'name':'Tele M1 HD','video':'udp://@239.77.0.214:5000','thumb':'https://upload.wikimedia.org/wikipedia/commons/thumb/1/13/Logo_Tele_M1.svg/1200px-Logo_Tele_M1.svg.png','genre':'TV'},
{'name':'TeleBasel HD','video':'udp://@239.77.0.202:5000','thumb':'https://upload.wikimedia.org/wikipedia/commons/thumb/9/93/Logo_TeleBasel.svg/1280px-Logo_TeleBasel.svg.png','genre':'TV'},
{'name':'Tele Z HD','video':'udp://@239.77.0.213:5000','thumb':'http://telez.ch/index_htm_files/14559.jpg','genre':'TV'},
{'name':'Tele1 HD','video':'udp://@239.77.0.204:5000','thumb':'http://raphaelareichlin.ch/wp-content/uploads/2018/01/1.png','genre':'TV'},
{'name':'TV Südostschweiz HD','video':'udp://@239.77.0.222:5000','thumb':'http://klubkran.ch/klubkran/wp-content/uploads/2015/11/Logo_Tele_S%C3%BCdostschweiz.png','genre':'TV'},
{'name':'Tele Bielingue HD','video':'udp://@239.77.1.42:5000','thumb':'https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/TeleBielingue_Logo.svg/1200px-TeleBielingue_Logo.svg.png','genre':'TV'},
{'name':'Star TV HD','video':'udp://@239.77.0.191:5000','thumb':'https://upload.wikimedia.org/wikipedia/commons/7/7d/Star_tv_hd.png','genre':'TV'},
{'name':'Puls 8 HD','video':'udp://@239.77.0.180:5000','thumb':'','genre':'TV'},
{'name':'CHTV HD','video':'udp://@239.77.0.181:5000','thumb':'','genre':'TV'},
{'name':'Schweiz 5','video':'udp://@239.77.0.21:5000','thumb':'','genre':'TV'},
{'name':'TeleD HD','video':'udp://@239.77.0.208:5000','thumb':'http://www.phtg.ch/uploads/tx_news/140612_TeleD_Lehrplan21_1.jpg','genre':'TV'},
{'name':'Alf','video':'udp://@239.77.5.154:5000','thumb':'','genre':'TV'},
{'name':'S1 HD','video':'udp://@239.77.0.217:5000','thumb':'','genre':'TV'},
{'name':'wetter.tv','video':'udp://@239.77.0.224:5000','thumb':'','genre':'TV'},
{'name':'Teleclub Zoom','video':'udp://@239.77.0.4:5000','thumb':'https://www.teleclubzoom.ch/wp-content/uploads/2017/08/TeleclubZoom_Logo.jpg','genre':'TV'},
{'name':'MySports HD D','video':'udp://@239.77.0.12:5000','thumb':'','genre':'TV'},
{'name':'Arte HD','video':'udp://@239.77.0.82:5000','thumb':'','genre':'TV'},
{'name':'3Sat HD','video':'udp://@239.77.0.106:5000','thumb':'','genre':'TV'},
{'name':'ORF1 HD','video':'udp://@239.77.0.109:5000','thumb':'','genre':'TV'},
{'name':'ORF2 HD','video':'udp://@239.77.0.110:5000','thumb':'','genre':'TV'},
{'name':'Servus TV HD','video':'udp://@239.77.0.84:5000','thumb':'','genre':'TV'},
{'name':'Das Erste HD','video':'udp://@239.77.0.80:5000','thumb':'','genre':'TV'},
{'name':'ZDF HD','video':'udp://@239.77.0.79:5000','thumb':'','genre':'TV'},
{'name':'RTL CH','video':'udp://@239.77.0.190:5000','thumb':'','genre':'TV'},
{'name':'RTL 2 (Schweiz)','video':'udp://@239.77.0.14:5000','thumb':'','genre':'TV'},
{'name':'Super RTL (Schweiz)','video':'udp://@239.77.0.29:5000','thumb':'','genre':'TV'},
{'name':'RTL Nitro','video':'udp://@239.77.0.88:5000','thumb':'','genre':'TV'},
{'name':'ProSieben (Schweiz)','video':'udp://@239.77.0.15:5000','thumb':'','genre':'TV'},
{'name':'ProSieben Maxx','video':'udp://@239.77.0.119:5000','thumb':'','genre':'TV'},
{'name':'Sat.1 (Schweiz)','video':'udp://@239.77.0.11:5000','thumb':'','genre':'TV'},
{'name':'Sat1 Gold','video':'udp://@239.77.0.99:5000','thumb':'','genre':'TV'},
{'name':'VOX (Schweiz)','video':'udp://@239.77.0.17:5000','thumb':'','genre':'TV'},
{'name':'SIXX','video':'udp://@239.77.0.69:5000','thumb':'','genre':'TV'},
{'name':'Kabel1 (Schweiz)','video':'udp://@239.77.0.18:5000','thumb':'','genre':'TV'},
{'name':'Kika HD','video':'udp://@239.77.0.108:5000','thumb':'','genre':'TV'},
{'name':'Nickelodeon CH HD','video':'udp://@239.77.0.197:5000','thumb':'','genre':'TV'},
{'name':'Disney Channel','video':'udp://@239.77.0.44:5000','thumb':'','genre':'TV'},
{'name':'VIVA CH HD','video':'udp://@239.77.0.192:5000','thumb':'','genre':'TV'},
{'name':'MTV Schweiz HD','video':'udp://@239.77.0.196:5000','thumb':'','genre':'TV'},
{'name':'Eurosport','video':'udp://@239.77.0.34:5000','thumb':'','genre':'TV'},
{'name':'SPORT1 HD CH','video':'udp://@239.77.0.193:5000','thumb':'','genre':'TV'},
{'name':'DMAX HD','video':'udp://@239.77.0.195:5000','thumb':'','genre':'TV'},
{'name':'TLC','video':'udp://@239.77.0.132:5000','thumb':'https://1.bp.blogspot.com/-BegH_L2Q6fk/VvMY69oH6lI/AAAAAAAAmrc/ajX3HEaK2TsLBNOWLpJDq6-b0XIPpjN6A/s1600/TLCK_Channel%2BLogo_Strawberry_RGB.png','genre':'TV'},
{'name':'Anixe HD','video':'udp://@239.77.0.83:5000','thumb':'','genre':'TV'},
{'name':'one HD','video':'udp://@239.77.0.111:5000','thumb':'','genre':'TV'},
{'name':'ZDF Info HD','video':'udp://@239.77.0.102:5000','thumb':'','genre':'TV'},
{'name':'ZDF Neo HD','video':'udp://@239.77.0.100:5000','thumb':'','genre':'TV'},
{'name':'Welt der Wunder','video':'udp://@239.77.0.46:5000','thumb':'','genre':'TV'},
{'name':'Welt HD','video':'udp://@239.77.0.194:5000','thumb':'','genre':'TV'},
{'name':'ARD Alpha','video':'udp://@239.77.0.51:5000','thumb':'','genre':'TV'},
{'name':'Phoenix HD','video':'udp://@239.77.0.105:5000','thumb':'','genre':'TV'},
{'name':'tagesschau24 HD','video':'udp://@239.77.0.129:5000','thumb':'https://www.senselan.ch/content/images/nextv/thumbs/280.png','genre':'TV'},
{'name':'n-tv','video':'udp://@239.77.0.24:5000','thumb':'','genre':'TV'},
{'name':'EuroNews','video':'udp://@239.77.0.43:5000','thumb':'','genre':'TV'},
{'name':'DW Europe','video':'udp://@239.77.0.66:5000','thumb':'','genre':'TV'},
{'name':'SWR BW HD','video':'udp://@239.77.0.81:5000','thumb':'','genre':'TV'},
{'name':'BR HD','video':'udp://@239.77.0.107:5000','thumb':'','genre':'TV'},
{'name':'WDR HD Köln','video':'udp://@239.77.0.215:5000','thumb':'','genre':'TV'},
{'name':'NDR HD','video':'udp://@239.77.0.103:5000','thumb':'','genre':'TV'},
{'name':'MDR Sachsen HD','video':'udp://@239.77.0.124:5000','thumb':'','genre':'TV'},
{'name':'rbb Berlin HD','video':'udp://@239.77.0.123:5000','thumb':'','genre':'TV'},
{'name':'hr-fernsehen HD','video':'udp://@239.77.0.122:5000','thumb':'','genre':'TV'},
{'name':'Tele 5','video':'udp://@239.77.0.64:5000','thumb':'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d5/Tele_5_2010_Logo_Rot.svg/2000px-Tele_5_2010_Logo_Rot.svg.png','genre':'TV'},
{'name':'Die Neue Zeit TV','video':'udp://@239.77.0.60:5000','thumb':'','genre':'TV'},
{'name':'Bibel TV HD','video':'udp://@239.77.0.127:5000','thumb':'','genre':'TV'},
{'name':'HSE24 ','video':'udp://@239.77.0.63:5000','thumb':'','genre':'TV'},
{'name':'HSE24 TREND','video':'udp://@239.77.0.216:5000','thumb':'','genre':'TV'},
{'name':'Channel 55','video':'udp://@239.77.0.223:5000','thumb':'','genre':'TV'},
{'name':'GoTV','video':'udp://@239.77.0.97:5000','thumb':'','genre':'TV'},
{'name':'Booster TV','video':'udp://@239.77.0.225:5000','thumb':'','genre':'TV'},
{'name':'RTS 1 HD','video':'udp://@239.77.1.28:5000','thumb':'','genre':'TV'},
{'name':'RTS 2 HD','video':'udp://@239.77.1.29:5000','thumb':'','genre':'TV'},
{'name':'la télé HD','video':'udp://@239.77.1.39:5000','thumb':'','genre':'TV'},
{'name':'Canal Alpha JU HD','video':'udp://@239.77.1.53:5000','thumb':'','genre':'TV'},
{'name':'Canal Alpha HD','video':'udp://@239.77.1.37:5000','thumb':'','genre':'TV'},
{'name':'Télé Versoix','video':'udp://@239.77.1.55:5000','thumb':'http://televersoix.ch/wp-content/uploads/2014/07/Grand-logo-TVX3-750x206.jpg','genre':'TV'},
{'name':'MySports HD F','video':'udp://@239.77.1.56:5000','thumb':'','genre':'TV'},
{'name':'TF1 HD','video':'udp://@239.77.1.3:5000','thumb':'https://vignette.wikia.nocookie.net/logopedia/images/d/d4/Tf1_hd.png/revision/latest?cb=20111122132245','genre':'TV'},
{'name':'France 2 HD','video':'udp://@239.77.1.4:5000','thumb':'','genre':'TV'},
{'name':'France 3','video':'udp://@239.77.1.5:5000','thumb':'','genre':'TV'},
{'name':'France 4','video':'udp://@239.77.1.6:5000','thumb':'','genre':'TV'},
{'name':'France 5','video':'udp://@239.77.1.7:5000','thumb':'','genre':'TV'},
{'name':'M6 HD','video':'udp://@239.77.1.10:5000','thumb':'','genre':'TV'},
{'name':'C8 HD CH','video':'udp://@239.77.1.54:5000','thumb':'','genre':'TV'},
{'name':'W9 HD','video':'udp://@239.77.1.13:5000','thumb':'','genre':'TV'},
{'name':'RTL 9 HD','video':'udp://@239.77.1.36:5000','thumb':'','genre':'TV'},
{'name':'NRJ12','video':'udp://@239.77.1.16:5000','thumb':'','genre':'TV'},
{'name':'Arte F HD','video':'udp://@239.77.1.47:5000','thumb':'','genre':'TV'},
{'name':'NT1','video':'udp://@239.77.1.20:5000','thumb':'','genre':'TV'},
{'name':'Gulli','video':'udp://@239.77.1.23:5000','thumb':'','genre':'TV'},
{'name':'TMC','video':'udp://@239.77.1.15:5000','thumb':'https://vignette.wikia.nocookie.net/tvfanon6528/images/b/b7/TMC_Monte_Carlo_%282004-2009%29.png/revision/latest?cb=20170718174949','genre':'TV'},{'name':'BFM TV','video':'udp://@239.77.1.24:5000','thumb':'','genre':'TV'},
{'name':'TVM3','video':'udp://@239.77.1.38:5000','thumb':'https://upload.wikimedia.org/wikipedia/commons/thumb/9/96/Logo_TVM3_2015.png/1200px-Logo_TVM3_2015.png','genre':'TV'},
{'name':'Rouge TV HD','video':'udp://@239.77.1.40:5000','thumb':'','genre':'TV'},
{'name':'6ter','video':'udp://@239.77.1.46:5000','thumb':'','genre':'TV'},
{'name':'2M Maroc','video':'udp://@239.77.1.45:5000','thumb':'','genre':'TV'},
{'name':'Numéro 23','video':'udp://@239.77.1.50:5000','thumb':'','genre':'TV'},
{'name':'LFM TV','video':'udp://@239.77.1.51:5000','thumb':'','genre':'TV'},
{'name':'One TV','video':'udp://@239.77.1.52:5000','thumb':'','genre':'TV'},
{'name':'Euronews F','video':'udp://@239.77.1.41:5000','thumb':'','genre':'TV'},
{'name':'France 24','video':'udp://@239.77.1.43:5000','thumb':'','genre':'TV'},
{'name':'TV5MONDE EUROPE','video':'udp://@239.77.1.49:5000','thumb':'http://directostv.teleame.com/wp-content/uploads/2016/05/TV5-Monde-Europe.png','genre':'TV'},
{'name':'Alsace 20','video':'udp://@239.77.1.25:5000','thumb':'','genre':'TV'},
{'name':'RSI LA 1 HD','video':'udp://@239.77.2.17:5000','thumb':'','genre':'TV'},
{'name':'RSI LA 2 HD','video':'udp://@239.77.2.18:5000','thumb':'','genre':'TV'},
{'name':'Tele Ticino HD','video':'udp://@239.77.2.73:5000','thumb':'https://upload.wikimedia.org/wikipedia/fr/8/83/TeleTicino.png','genre':'TV'},
{'name':'Rai HD','video':'udp://@239.77.2.19:5000','thumb':'','genre':'TV'},
{'name':'Rai Uno','video':'udp://@239.77.2.3:5000','thumb':'','genre':'TV'},
{'name':'Rai Due','video':'udp://@239.77.2.4:5000','thumb':'','genre':'TV'},
{'name':'Rai Tre','video':'udp://@239.77.2.5:5000','thumb':'','genre':'TV'},
{'name':'Rai 4','video':'udp://@239.77.2.6:5000','thumb':'','genre':'TV'},
{'name':'Rete4 HD','video':'udp://@239.77.2.21:5000','thumb':'','genre':'TV'},
{'name':'Canale5 HD','video':'udp://@239.77.2.22:5000','thumb':'','genre':'TV'},
{'name':'Italia 1 HD','video':'udp://@239.77.2.20:5000','thumb':'','genre':'TV'},
{'name':'LA 7','video':'udp://@239.77.2.15:5000','thumb':'','genre':'TV'},
{'name':'LA7d','video':'udp://@239.77.2.12:5000','thumb':'','genre':'TV'},
{'name':'IRIS','video':'udp://@239.77.2.14:5000','thumb':'','genre':'TV'},
{'name':'Boing','video':'udp://@239.77.2.16:5000','thumb':'','genre':'TV'},
{'name':'Rai Sport+ HD','video':'udp://@239.77.2.10:5000','thumb':'','genre':'TV'},
{'name':'Top Calcio 24','video':'udp://@239.77.2.52:5000','thumb':'https://live-tv-channels.net/pt-data/uploads/logo/it-top-calcio-24.jpg','genre':'TV'},
{'name':'Sportitalia','video':'udp://@239.77.2.64:5000','thumb':'','genre':'TV'},
{'name':'Sportitalia 2','video':'udp://@239.77.2.68:5000','thumb':'','genre':'TV'},
{'name':'Sportitalia 24','video':'udp://@239.77.2.65:5000','thumb':'','genre':'TV'},
{'name':'Rai Storia','video':'udp://@239.77.2.31:5000','thumb':'','genre':'TV'},
{'name':'Rai News ','video':'udp://@239.77.2.32:5000','thumb':'','genre':'TV'},
{'name':'Rai Premium','video':'udp://@239.77.2.33:5000','thumb':'','genre':'TV'},
{'name':'Rai Yoyo','video':'udp://@239.77.2.34:5000','thumb':'','genre':'TV'},
{'name':'Rai Movie','video':'udp://@239.77.2.36:5000','thumb':'','genre':'TV'},
{'name':'VH1','video':'udp://@239.77.2.13:5000','thumb':'','genre':'TV'},
{'name':'Real Time','video':'udp://@239.77.2.63:5000','thumb':'','genre':'TV'},
{'name':'ELELOMBARDIA HD','video':'udp://@239.77.2.23:5000','thumb':'','genre':'TV'},
{'name':'ANTENNATRE HD','video':'udp://@239.77.2.24:5000','thumb':'','genre':'TV'},
{'name':'BBC HD','video':'udp://@239.77.3.29:5000','thumb':'','genre':'TV'},
{'name':'BBC One HD','video':'udp://@239.77.3.30:5000','thumb':'','genre':'TV'},
{'name':'BBC Two HD','video':'udp://@239.77.3.29:5000','thumb':'','genre':'TV'},
{'name':'ITV 1 HD','video':'udp://@239.77.3.31:5000','thumb':'','genre':'TV'},
{'name':'Channel 4 HD','video':'udp://@239.77.3.32:5000','thumb':'','genre':'TV'},
{'name':'CBBC HD','video':'udp://@239.77.3.54:5000','thumb':'','genre':'TV'},
{'name':'CBeebies HD','video':'udp://@239.77.3.55:5000','thumb':'','genre':'TV'},
{'name':'CITV','video':'udp://@239.77.3.17:5000','thumb':'','genre':'TV'},
{'name':'ITV 2','video':'udp://@239.77.3.14:5000','thumb':'','genre':'TV'},
{'name':'ITV 3','video':'udp://@239.77.3.15:5000','thumb':'','genre':'TV'},
{'name':'ITV 4','video':'udp://@239.77.3.16:5000','thumb':'','genre':'TV'},
{'name':'E4','video':'udp://@239.77.3.8:5000','thumb':'','genre':'TV'},
{'name':'Film 4','video':'udp://@239.77.3.21:5000','thumb':'','genre':'TV'},
{'name':'BBC World News Europe HD','video':'udp://@239.77.3.53:5000','thumb':'','genre':'TV'},
{'name':'BBC NEWS HD','video':'udp://@239.77.3.52:5000','thumb':'','genre':'TV'},
{'name':'CNN International','video':'udp://@239.77.3.23:5000','thumb':'','genre':'TV'},
{'name':'CNBC Europe','video':'udp://@239.77.3.26:5000','thumb':'','genre':'TV'},
{'name':'Bloomberg','video':'udp://@239.77.3.27:5000','thumb':'','genre':'TV'},
{'name':'Sky News','video':'udp://@239.77.3.25:5000','thumb':'','genre':'TV'},
{'name':'Russia Today','video':'udp://@239.77.5.51:5000','thumb':'','genre':'TV'},
{'name':'Al Jazeera English HD','video':'udp://@239.77.5.153:5000','thumb':'','genre':'TV'},
{'name':'France 24 E','video':'udp://@239.77.1.44:5000','thumb':'','genre':'TV'},
{'name':'5 USA','video':'udp://@239.77.3.59:5000','thumb':'','genre':'TV'},
{'name':'5STAR','video':'udp://@239.77.3.60:5000','thumb':'','genre':'TV'},
{'name':'Travel','video':'udp://@239.77.3.50:5000','thumb':'https://upload.wikimedia.org/wikipedia/commons/e/e2/Travel_Channel_HD_Logo.png','genre':'TV'},
{'name':'More 4','video':'udp://@239.77.3.9:5000','thumb':'','genre':'TV'},
{'name':'Fashion TV','video':'udp://@239.77.3.28:5000','thumb':'','genre':'TV'},
{'name':'TVR International','video':'udp://@239.77.5.112:5000','thumb':'http://www.frocus.net/images/logotv/original/tvri.gif','genre':'TV'},
{'name':'TVE Internacional','video':'udp://@239.77.4.1:5000','thumb':'https://upload.wikimedia.org/wikipedia/commons/8/83/Logo_TVE-Internacional.svg','genre':'TV'},
{'name':'Canal 24 Horas','video':'udp://@239.77.4.2:5000','thumb':'','genre':'TV'},
{'name':'RTP 1','video':'udp://@239.77.4.11:5000','thumb':'','genre':'TV'},
{'name':'RTV Montenegro','video':'udp://@239.77.5.140:5000','thumb':'','genre':'TV'},
{'name':'Svet Plus','video':'udp://@239.77.5.141:5000','thumb':'','genre':'TV'},
{'name':'TVP Polonia','video':'udp://@239.77.5.21:5000','thumb':'https://vignette.wikia.nocookie.net/logopedia/images/d/dc/TV_Polonia_old.png/revision/latest?cb=20101212221322','genre':'TV'},
{'name':'Duna TV','video':'udp://@239.77.5.157:5000','thumb':'','genre':'TV'},
{'name':'Atlas TV','video':'udp://@239.77.5.155:5000','thumb':'','genre':'TV'},
{'name':'BN','video':'udp://@239.77.5.163:5000','thumb':'','genre':'TV'},
{'name':'TV CG','video':'udp://@239.77.5.164:5000','thumb':'http://4.bp.blogspot.com/-7HFlfswld4k/T_vTTCkppNI/AAAAAAAAIMI/1jqSoX4W8fA/s400/RTCG+logo.png','genre':'TV'},
{'name':'4E','video':'udp://@239.77.5.138:5000','thumb':'','genre':'TV'},
{'name':'C1R Europe','video':'udp://@239.77.5.136:5000','thumb':'','genre':'TV'},
{'name':'RTK 1','video':'udp://@239.77.5.38:5000','thumb':'','genre':'TV'},
{'name':'TVSH','video':'udp://@239.77.5.167:5000','thumb':'https://upload.wikimedia.org/wikipedia/commons/thumb/1/17/Radio_Televizioni_Shqiptar.svg/1200px-Radio_Televizioni_Shqiptar.svg.png','genre':'TV'},
{'name':'TV Shqiptar','video':'udp://@239.77.5.142:5000','thumb':'https://upload.wikimedia.org/wikipedia/commons/thumb/1/17/Radio_Televizioni_Shqiptar.svg/1200px-Radio_Televizioni_Shqiptar.svg.png','genre':'TV'},
{'name':'RTRS plus','video':'udp://@239.77.5.148:5000','thumb':'','genre':'TV'},
{'name':'STERK TV','video':'udp://@239.77.5.151:5000','thumb':'','genre':'TV'},
{'name':'BVN TV','video':'udp://@239.77.5.18:5000','thumb':'','genre':'TV'},
{'name':'Arirang World','video':'udp://@239.77.5.70:5000','thumb':'','genre':'TV'},
{'name':'PCNE Chinese','video':'udp://@239.77.5.149:5000','thumb':'','genre':'TV'},
{'name':'Thai Global Network','video':'udp://@239.77.5.69:5000','thumb':'http://www.frocus.net/images/logotv/original/Thai-Global-Network.jpg','genre':'TV'},
{'name':'TRT TURK','video':'udp://@239.77.5.132:5000','thumb':'http://trtkurumsal.trt.net.tr/Uploads/image/png/2015-07-02-16.21.35/1d7e3e40e0a6455eb35e5fa6c3d529a7.png','genre':'TV'},
{'name':'KANAL 7 AVRUPA','video':'udp://@239.77.5.131:5000','thumb':'','genre':'TV'},
{'name':'HABERTURK','video':'udp://@239.77.5.133:5000','thumb':'','genre':'TV'},
{'name':'TRT 3-SPOR','video':'udp://@239.77.5.130:5000','thumb':'https://vignette.wikia.nocookie.net/logopedia/images/7/75/Trt3_spor.png/revision/latest?cb=20121222012706','genre':'TV'},
{'name':'FB TV','video':'udp://@239.77.5.135:5000','thumb':'','genre':'TV'},
{'name':'TTN','video':'udp://@239.77.5.160:5000','thumb':'','genre':'TV'},
{'name':'LBC Europe','video':'udp://@239.77.5.161:5000','thumb':'','genre':'TV'},
{'name':'Al Masriyah','video':'udp://@239.77.5.165:5000','thumb':'','genre':'TV'},
{'name':'Sama Dubai','video':'udp://@239.77.5.168:5000','thumb':'','genre':'TV'},
{'name':'MBC Europe','video':'udp://@239.77.5.169:5000','thumb':'','genre':'TV'},
{'name':'Saudi 1','video':'udp://@239.77.5.171:5000','thumb':'','genre':'TV'},
{'name':'Dubai Sports 3','video':'udp://@239.77.5.172:5000','thumb':'','genre':'TV'},
{'name':'Jordan TV','video':'udp://@239.77.5.173:5000','thumb':'','genre':'TV'},
{'name':'Kuwait TV','video':'udp://@239.77.5.174:5000','thumb':'','genre':'TV'},
{'name':'Oman TV','video':'udp://@239.77.5.175:5000','thumb':'','genre':'TV'},
{'name':'Qatar TV','video':'udp://@239.77.5.176:5000','thumb':'','genre':'TV'},
{'name':'Sharjah TV','video':'udp://@239.77.5.178:5000','thumb':'','genre':'TV'},
{'name':'Dubai TV','video':'udp://@239.77.5.179:5000','thumb':'','genre':'TV'},
{'name':'Abu Dhabi TV','video':'udp://@239.77.5.180:5000','thumb':'','genre':'TV'},
{'name':'Al Sharqiya','video':'udp://@239.77.5.181:5000','thumb':'','genre':'TV'},
{'name':'BBB Teststream','video':'udp://@239.77.0.1:5000','thumb':'','genre':'TV'}]}



def get_url(**kwargs):
    """
    Create a URL for calling the plugin recursively from the given set of keyword arguments.

    :param kwargs: "argument=value" pairs
    :type kwargs: dict
    :return: plugin call URL
    :rtype: str
    """
    return '{0}?{1}'.format(_url, urlencode(kwargs))


def list_videos():
    """
    Create the list of playable videos in the Kodi interface.

    :param category: Category name
    :type category: str
    """
    # Set plugin category. It is displayed in some skins as the name
    # of the current section.
    xbmcplugin.setPluginCategory(_handle, 'video')
    # Set plugin content. It allows Kodi to select appropriate views
    # for this type of content.
    xbmcplugin.setContent(_handle, 'videos')
    # Get the list of videos in the category.
    videos = VIDEOS['channels']
    # Iterate through videos.
    for video in videos:
        # Create a list item with a text label and a thumbnail image.
        list_item = xbmcgui.ListItem(label=video['name'])
        # Set additional info for the list item.
        # 'mediatype' is needed for skin to display info for this ListItem correctly.
        list_item.setInfo('video', {'title': video['name'],
                                    'genre': 'TV',
                                    'mediatype': 'video'})
        # Set graphics (thumbnail, fanart, banner, poster, landscape etc.) for the list item.
        # Here we use the same image for all items for simplicity's sake.
        # In a real-life plugin you need to set each image accordingly.
        list_item.setArt({'thumb': video['thumb'], 'icon': video['thumb'], 'fanart': video['thumb']})
        # Set 'IsPlayable' property to 'true'.
        # This is mandatory for playable items!
        list_item.setProperty('IsPlayable', 'true')
        # Create a URL for a plugin recursive call.
        # Example: plugin://plugin.video.example/?action=play&video=http://www.vidsplay.com/wp-content/uploads/2017/04/crab.mp4
        url = get_url(action='play', video=video['video'])
        # Add the list item to a virtual Kodi folder.
        # is_folder = False means that this item won't open any sub-list.
        is_folder = False
        # Add our item to the Kodi virtual folder listing.
        xbmcplugin.addDirectoryItem(_handle, url, list_item, is_folder)
    # Add a sort method for the virtual folder items (alphabetically, ignore articles)
    xbmcplugin.addSortMethod(_handle, xbmcplugin.SORT_METHOD_LABEL_IGNORE_THE)
    # Finish creating a virtual folder.
    xbmcplugin.endOfDirectory(_handle)


def play_video(path):
    """
    Play a video by the provided path.

    :param path: Fully-qualified video URL
    :type path: str
    """
    # Create a playable item with a path to play.
    play_item = xbmcgui.ListItem(path=path)
    # Pass the item to the Kodi player.
    xbmcplugin.setResolvedUrl(_handle, True, listitem=play_item)


def router(paramstring):
    """
    Router function that calls other functions
    depending on the provided paramstring

    :param paramstring: URL encoded plugin paramstring
    :type paramstring: str
    """
    # Parse a URL-encoded paramstring to the dictionary of
    # {<parameter>: <value>} elements
    params = dict(parse_qsl(paramstring))
    # Check the parameters passed to the plugin
    if params:
        if params['action'] == 'listing':
            # Display the list of videos in a provided category.
            list_videos()
        elif params['action'] == 'play':
            # Play a video from a provided URL.
            play_video(params['video'])
        else:
            # If the provided paramstring does not contain a supported action
            # we raise an exception. This helps to catch coding errors,
            # e.g. typos in action names.
            raise ValueError('Invalid paramstring: {0}!'.format(paramstring))
    else:
        # If the plugin is called from Kodi UI without any parameters,
        # display the list of video categories
        list_videos()


if __name__ == '__main__':
    # Call the router function and pass the plugin call parameters to it.
    # We use string slicing to trim the leading '?' from the plugin call paramstring
    router(sys.argv[2][1:])
