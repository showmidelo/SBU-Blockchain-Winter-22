import rsa
import base64


private = rsa.PrivateKey(
    16316540661868924479143490951683879449467017961563866412866074211553351456863894197852874521485465290608387217977356354466020449772774599823282197909624183622644713810374695242522095713897048312065580436397541055869429749891470120507454131577228682652480193612511693549594351168403770160557142561031833502677443498087934890092402138931663463712850198755729462279557142816082483381467189794556139016764010067812833226469115816749973938754360744797959699086079627237944663024158006677553998472225114255855032515139064588491039439904430640980220472324936542704852515461869749008162430600189511616627005667119755077645043, 
    65537,
    1957128433449068699063841530298716394590234954237355293521830559485800323518120638560224706858678954628263910775897558668498508562549111634814247795406498732893023715814814216419216540380925229735073741711110826558884100033520707650778902426546754876346900254634091017186645628192044756887293169611747315965614383393605710583199024659439543769357706305085370360131996109880879635306979549253177787308875604706346688757237847400815698365374379789687567472103693394887754515576663852251327521739045702088077141426633762426848989406674411679629241868968552234755748319215076055970352241648790328335590198808943241556833,
    2183591836427848633623393207291529897621167150647147518778187489053521397342955966874455513860323912161976401349210202733016697687387163230673881135032697942329228071549859541432081669569108607784261217690275971077040600879058165939267122443808720577486570895662934227244881197429464583149268832520631130152499986386518083979761,
    7472340017794375932334620399396257869875813301246458229748630211805072244493223985828112411916059052023830196412294626047197967937762351040151932460947569197895021713080470537270426195218623522589997304761226057502808137505130191233448079934694871504832692368438844427746380473510085904163)

message = input('enter message to sign\n')

sign = rsa.sign(message.encode(),private,"MD5")

signString = str(base64.b64encode(sign),'utf-8')
print("\n\n")
print(signString)
