import pytest
import time
import numpy as np
from spotify_confidence.analysis.frequentist.confidence_computers.z_test_computer import sequential_bounds


@pytest.mark.skip(reason="Skipping because this test is very slow")
def test_many_days():
    """
    This input (based on a real experiment) is very long, which can cause slow calculation
    """

    t = [
        0.0016169976338740648,
        0.0057857955498163615,
        0.012200379088315757,
        0.020199591701142824,
        0.02956441064038571,
        0.04047102718841871,
        0.052929825413405296,
        0.06580092295219643,
        0.07878439818310792,
        0.09148496950057272,
        0.1028893343050959,
        0.1128434997940756,
        0.12298934256730025,
        0.13280979910049193,
        0.14267997977787195,
        0.15281963941289514,
        0.16293176212095561,
        0.17198778455162406,
        0.17996747917082068,
        0.18786110540725684,
        0.1955669737257397,
        0.20335013690301407,
        0.21277055903588274,
        0.22148328777708232,
        0.2295912740670489,
        0.23640586948077766,
        0.2431234831038822,
        0.24987292468428604,
        0.2568336065927525,
        0.2649271880853427,
        0.27282722271091664,
        0.2799894816822785,
        0.2862801096305317,
        0.2925685639072496,
        0.2988294699944579,
        0.3051314956400879,
        0.3118994077972684,
        0.31887303037202536,
        0.32523581745772245,
        0.3307398353487736,
        0.33616198578702633,
        0.34151324975562525,
        0.3478405485563082,
        0.3546238566149848,
        0.36130761502236336,
        0.36751189302418574,
        0.3730571543616735,
        0.37865278180851814,
        0.38428987795273567,
        0.3900127609160433,
        0.3964718089893684,
        0.40306122104207753,
        0.40914555292031984,
        0.41449831480764515,
        0.4198849769608837,
        0.4256404199470336,
        0.4315384355133149,
        0.43801594290086987,
        0.4444516211895538,
        0.45034373518130405,
        0.4556807858158224,
        0.4610488197166289,
        0.46633036852044285,
        0.4717294082126311,
        0.47769497653470894,
        0.48369759863580825,
        0.4892945325380834,
        0.49431792124380325,
        0.49935417177798586,
        0.5043009639028166,
        0.5093262559789482,
        0.5149098888134348,
        0.5205835093969735,
        0.5261172491490695,
        0.5310141031413226,
        0.5359027242118537,
        0.540068909216935,
        0.5451620919252675,
        0.5506752550043325,
        0.5562355968920056,
        0.5614758121490083,
        0.5660462437469214,
        0.5706616804819072,
        0.5750453002157994,
        0.5795939049979849,
        0.5861802311128667,
        0.5913273051077091,
        0.5958976691303413,
        0.6001503392324151,
        0.6042404457337608,
        0.6082963816680697,
        0.6124734913435614,
        0.6174918231657613,
        0.6223867287374153,
        0.6268875352709179,
        0.6308341907134806,
        0.6348490070893678,
        0.6388763812049537,
        0.6430405276890614,
        0.6476616520101889,
        0.6525750168960728,
        0.6570689758011117,
        0.6610427627189518,
        0.6649727383296814,
        0.6689671694958335,
        0.673019050913289,
        0.6776959248411508,
        0.6825336054124376,
        0.6869984168463193,
        0.6908780826604262,
        0.6949984065748767,
        0.6991746490342636,
        0.7033415661048878,
        0.7082721626873987,
        0.7131064081819068,
        0.7176506656210218,
        0.7216193168175142,
        0.7256178250256133,
        0.7296113326629264,
        0.733677461202103,
        0.7383860054116087,
        0.7431864069529378,
        0.7475115177561259,
        0.7513220765829758,
        0.7551652404828552,
        0.7591154774153049,
        0.7635879699061145,
        0.76888963361854,
        0.7740750002725536,
        0.7788235152607059,
        0.7829338267710377,
        0.7870690059847372,
        0.7912444713283939,
        0.7954864645360872,
        0.8002680350991415,
        0.8051864906561857,
        0.8097254772233912,
        0.8137210008565843,
        0.8175460095309978,
        0.8214444612731922,
        0.8256005212486867,
        0.8302889054993935,
        0.8351108860804202,
        0.839542135124793,
        0.8433705788759852,
        0.8472835029908369,
        0.8513248314019267,
        0.8556693700983707,
        0.8606610209471658,
        0.865499591259651,
        0.8699232042972833,
        0.8737653545679493,
        0.8776996212090155,
        0.8816179062961511,
        0.8856027192473231,
        0.8900849425785808,
        0.8947120585746139,
        0.8993599427069738,
        0.9035026227768521,
        0.9075820073336299,
        0.9115699850604569,
        0.9158137239629064,
        0.9207252417911126,
        0.925749689176233,
        0.9303560370359392,
        0.9343408161994707,
        0.9384800274049299,
        0.9426168396879175,
        0.9475247422385961,
        0.9523909621035122,
        0.9573336433987555,
        0.9618665256655873,
        0.9657568345864344,
        0.9697355995499667,
        0.973736889607129,
        0.9778353641807583,
        0.9828378833872299,
        0.987703190985854,
        0.9921586319807856,
        0.9960384779956415,
        1.0,
    ]

    start_time = time.time()
    results = sequential_bounds(np.array(t), alpha=0.003333333, sides=2)
    my_bounds = results.bounds

    expected = np.array(
        [
            5.75400023,
            8.0,
            5.14701605,
            4.91478643,
            4.80691346,
            4.69004328,
            4.57921075,
            4.49683943,
            4.44452939,
            4.38899083,
            4.35683792,
            4.33289847,
            4.301461,
            4.27383028,
            4.24513591,
            4.21444005,
            4.18809224,
            4.17037988,
            4.15702106,
            4.13796352,
            4.12345883,
            4.10808648,
            4.07898394,
            4.06169498,
            4.04985422,
            4.04453139,
            4.03288177,
            4.02205301,
            4.00664024,
            3.98770613,
            3.97358123,
            3.96589571,
            3.95946059,
            3.94995533,
            3.94128534,
            3.93114789,
            3.91870273,
            3.90749163,
            3.90064315,
            3.8958719,
            3.88847126,
            3.88184277,
            3.86841705,
            3.85642932,
            3.84721152,
            3.84099201,
            3.83689676,
            3.8295672,
            3.82234648,
            3.81501541,
            3.80286989,
            3.79370807,
            3.78728177,
            3.78449351,
            3.77865864,
            3.76988501,
            3.76230126,
            3.75251025,
            3.74474277,
            3.73953663,
            3.73534961,
            3.72974059,
            3.72466752,
            3.71785112,
            3.70903202,
            3.70176221,
            3.6976847,
            3.6944938,
            3.68996741,
            3.68449851,
            3.67888767,
            3.67142884,
            3.66522708,
            3.65968721,
            3.65649679,
            3.65207508,
            3.65156885,
            3.643952,
            3.63644572,
            3.63029181,
            3.62665696,
            3.62527741,
            3.62117738,
            3.61789837,
            3.6128686,
            3.59904477,
            3.5976517,
            3.59678297,
            3.59434356,
            3.59116304,
            3.58814574,
            3.5835558,
            3.57659985,
            3.5726481,
            3.56990393,
            3.56879169,
            3.56501955,
            3.56127173,
            3.55720436,
            3.55194666,
            3.54597713,
            3.5436994,
            3.54287161,
            3.53974477,
            3.53649679,
            3.53314876,
            3.52700997,
            3.52175088,
            3.51873367,
            3.51846468,
            3.51401711,
            3.5106822,
            3.50742162,
            3.50113309,
            3.49658758,
            3.49376264,
            3.49238249,
            3.48979047,
            3.48725107,
            3.48341163,
            3.47810608,
            3.47381485,
            3.47184685,
            3.47110719,
            3.46801712,
            3.46472076,
            3.45913659,
            3.45209404,
            3.4484684,
            3.44587153,
            3.44472549,
            3.44242755,
            3.43895355,
            3.43549018,
            3.43080058,
            3.42621252,
            3.42437516,
            3.42371762,
            3.42122891,
            3.41861765,
            3.41451447,
            3.40936002,
            3.4051931,
            3.40307035,
            3.40295986,
            3.40052495,
            3.39688763,
            3.39279348,
            3.38725208,
            3.38421998,
            3.38214471,
            3.38133324,
            3.37908335,
            3.37689107,
            3.37364203,
            3.36937673,
            3.36593888,
            3.36250238,
            3.36109704,
            3.35878324,
            3.35666501,
            3.35305866,
            3.34754255,
            3.34364255,
            3.34157534,
            3.34085629,
            3.33864193,
            3.33563376,
            3.33016843,
            3.32687574,
            3.32338656,
            3.32166421,
            3.32107266,
            3.31861916,
            3.31615129,
            3.31334059,
            3.30792367,
            3.30479742,
            3.30339238,
            3.30296421,
            3.30041534,
        ]
    )

    assert np.allclose(my_bounds, expected)
    # if the calculation with max_nints takes longer than 10 seconds, something is most likely broken
    assert (time.time() - start_time) < 15

    # Run a second time but with initial state from last run.
    start_time = time.time()
    results = sequential_bounds(np.array(t), alpha=0.003333333, sides=2, state=results.state)
    my_bounds = results.bounds
    assert np.allclose(my_bounds, expected)
    # if the calculation with max_nints takes longer than 10 seconds, something is most likely broken
    print(f"Time passed second round: {time.time() - start_time}")
    assert (time.time() - start_time) < 0.01


@pytest.mark.skip(reason="Skipping because this test is very slow")
def test_many_days_fast_and_no_crash():
    """
    This is based on experiment 1735 on 26.11.2020. The calculation of the corresponding bounds takes many minutes
    without performance tweak. Therefore, this test only checks for absence of crashs and time constraints, but
    does not compare against the baseline without performance tweak. There is a Jupyter notebook making that comparison.
    """

    t = [
        0.011404679673257933,
        0.02292450819418779,
        0.0356455988484443,
        0.04835740420885424,
        0.05971666577058213,
        0.06976017458481187,
        0.07984165086754545,
        0.09002459314412276,
        0.10026356929804565,
        0.11129746744100509,
        0.1222487922920801,
        0.13250332796555583,
        0.1418309168157694,
        0.15072692856918676,
        0.15940425274581055,
        0.16819162796171988,
        0.17766544268380677,
        0.18725283769713902,
        0.19600162922594835,
        0.20386600701959812,
        0.21159934032678884,
        0.21916233120704773,
        0.22688560894714668,
        0.23509036348536208,
        0.24366994698965522,
        0.2515994198750076,
        0.25875219123481424,
        0.2659624389836802,
        0.2731790169781248,
        0.28051081384508175,
        0.28822790138928306,
        0.2962915558739476,
        0.3037246366701631,
        0.31063411372423433,
        0.31767205835063517,
        0.32464032826076655,
        0.3318100596369355,
        0.3397812253123048,
        0.3476375502493003,
        0.3550356746451523,
        0.3616457394863339,
        0.3683042335071859,
        0.375005792804928,
        0.38175551518794676,
        0.3891222824602354,
        0.39652683513644266,
        0.40347332732118724,
        0.4098512458112366,
        0.4163205187081655,
        0.42263992444151655,
        0.42899148558161226,
        0.43464157988476515,
        0.43858871208254674,
        0.44192382717460427,
        0.44482627278235426,
        0.4474605932759375,
        0.44957511937869815,
        0.4509048070694502,
        0.45222422911858906,
        0.45333747002744257,
        0.45426598540713137,
        0.4551955091445229,
        0.45605329943533507,
        0.456895460181754,
        0.4578387508027823,
        0.45881449093488524,
        0.45965707183034693,
        0.4603621239391219,
        0.4610501740166303,
        0.46173166976907054,
        0.4624475477181825,
        0.4632872155802805,
        0.4641010162663083,
        0.46481571779810027,
        0.4654194019478082,
        0.4660207332628762,
        0.4666458170038323,
        0.4672646265190821,
        0.46791675385342846,
        0.4685898046101078,
        0.46918687841487516,
        0.46969451649339183,
        0.47019581032136176,
        0.4706811945055765,
        0.47116992587716583,
        0.47170379526092326,
        0.47227291514937425,
        0.4727852448922026,
        0.47322669549150526,
        0.4736554715946826,
        0.47408022827201673,
        0.47450655350577753,
        0.4749737592414058,
        0.47545756086422586,
        0.4759381553493523,
        0.47630259262910407,
        0.4766609657576709,
        0.47699441004302984,
        0.4773518028238301,
        0.477775327063972,
        0.4781977729215707,
        0.47856485714029223,
        0.47888037506649034,
        0.47919262983512245,
        0.47949520717080135,
        0.47980748994936967,
        0.4801789017032324,
        0.4805627078538587,
        0.48090167009664675,
        0.4811904245288165,
        0.48149113920373887,
        0.4817901452725537,
        0.4820966860142033,
        0.48243977972257923,
        0.4827841618880198,
        0.48309197708176604,
        0.4833586316742829,
        0.4836129058750043,
        0.4838654994795544,
        0.4841171547512422,
        0.48439948090305657,
        0.48470691796266424,
        0.4849764575786085,
        0.4852081697757299,
        0.48545255646897667,
        0.4856974893559792,
        0.48595208567096676,
        0.48624575584693763,
        0.4865416528128355,
        0.4867930840050338,
        0.4870117575768593,
        0.4872274340855126,
        0.4874240218226533,
        0.4876215198827202,
        0.4878617751103791,
        0.488108108494191,
        0.48831807097586183,
        0.4884937072807334,
        0.48866595438332605,
        0.488852192449045,
        0.48903411698459087,
        0.4892522303576926,
        0.4894829201921431,
        0.4896802221826566,
        0.4898457609055321,
        0.49001188783706756,
        0.4901847091433521,
        0.4903469286887892,
        0.4905345812562857,
        0.49073597269748276,
        0.49091467609036693,
        0.4910691508884479,
        0.4912115954189357,
        0.49135658885361677,
        0.49150574176382184,
        0.49167835299558493,
        0.49186735004001847,
        0.49203167033066975,
        0.49216849886895175,
        0.4923075682021289,
        0.4924506289512129,
        0.49259525825672346,
        0.49276396210238826,
        0.49294465420074185,
        0.4931019580023778,
        0.49330306934421303,
        0.4935200763248353,
        0.49373208353184794,
        0.4939721566949216,
        0.4942334053697541,
        0.4944958444668745,
        0.4947262121870588,
        0.49492469059489225,
        0.4951192336066912,
        0.495294323717807,
        0.4954780829041733,
        0.4956838158854796,
        0.49592192835302007,
        0.49614550366367866,
        0.49633301618149417,
        0.49652995404283723,
        0.4967104500716375,
        0.4969174855149766,
        0.49712443692850716,
        0.4973541744251272,
        0.49756258235533957,
        0.49772464784612763,
        0.4978989396740621,
        0.4980669292663541,
        0.4982378038820735,
        0.49843929335804726,
        0.4986487236509305,
        0.49883442952786183,
        0.49899118713574214,
        0.49915640374435144,
        0.49932506557511197,
    ]

    alpha = 0.0033333333333333335
    sides = 2

    start_time = time.time()
    my_bounds = sequential_bounds(np.array(t), alpha=alpha, sides=sides).bounds

    expected = np.array(
        [
            5.0536015,
            4.819334,
            4.70702194,
            4.60970036,
            4.55329219,
            4.5118919,
            4.465161,
            4.42168832,
            4.37932413,
            4.33343066,
            4.29780246,
            4.26550766,
            4.2476601,
            4.22343408,
            4.20455427,
            4.1834642,
            4.15580542,
            4.13352266,
            4.1170148,
            4.10326736,
            4.08845795,
            4.07496919,
            4.05959646,
            4.0417501,
            4.02262887,
            4.01056674,
            4.00192679,
            3.98996708,
            3.97709149,
            3.96442225,
            3.95010566,
            3.93456306,
            3.92603865,
            3.91801377,
            3.90630556,
            3.8975012,
            3.88641115,
            3.87143326,
            3.85966246,
            3.85112482,
            3.84569926,
            3.83714224,
            3.82719647,
            3.81910741,
            3.80682977,
            3.79652758,
            3.78889289,
            3.78428912,
            3.77646938,
            3.76966463,
            3.76150223,
            3.75820905,
            3.76088934,
            3.76171382,
            3.76141619,
            3.76079216,
            3.76237742,
            3.76725034,
            3.76769877,
            3.7690107,
            3.7710916,
            3.77168583,
            3.76813708,
            3.7705804,
            3.76669411,
            3.76711572,
            3.76808636,
            3.76962133,
            3.76680748,
            3.76844159,
            3.76552364,
            3.76210975,
            3.76321355,
            3.76471956,
            3.76227721,
            3.76424368,
            3.76172169,
            3.75923,
            3.76099518,
            3.75829319,
            3.76028082,
            3.75824824,
            3.7562443,
            3.76013739,
            3.75818674,
            3.7560594,
            3.75379557,
            3.75757852,
            3.75582548,
            3.75412511,
            3.75244297,
            3.75075688,
            3.74891172,
            3.75280489,
            3.75090966,
            3.7494744,
            3.74806463,
            3.75254602,
            3.75114099,
            3.74947802,
            3.74782149,
            3.74638383,
            3.75092969,
            3.74970739,
            3.7485241,
            3.74730404,
            3.74585452,
            3.74435839,
            3.74303855,
            3.74191532,
            3.74074663,
            3.73958567,
            3.74415751,
            3.74282592,
            3.74149075,
            3.74029857,
            3.73926672,
            3.73828357,
            3.73730769,
            3.7363362,
            3.7352472,
            3.73406243,
            3.74020438,
            3.7393112,
            3.73836986,
            3.73742713,
            3.73644796,
            3.73531947,
            3.73418345,
            3.73321896,
            3.73238074,
            3.73155456,
            3.73080198,
            3.73004637,
            3.7291278,
            3.72818669,
            3.7273851,
            3.72671496,
            3.72605809,
            3.72534827,
            3.72465527,
            3.72382494,
            3.72294733,
            3.73077145,
            3.73014101,
            3.72950865,
            3.72885115,
            3.7282343,
            3.72752112,
            3.72675617,
            3.7260778,
            3.7254917,
            3.72495149,
            3.72440186,
            3.72383671,
            3.723183,
            3.72246763,
            3.72184599,
            3.7213286,
            3.72080295,
            3.72026245,
            3.71971626,
            3.71907946,
            3.71839777,
            3.71780463,
            3.71704671,
            3.7162294,
            3.71543144,
            3.71452847,
            3.72065881,
            3.71967136,
            3.71880523,
            3.71805949,
            3.71732896,
            3.71667185,
            3.71598258,
            3.71521135,
            3.71431933,
            3.71348235,
            3.71278081,
            3.71204444,
            3.71136994,
            3.7105967,
            3.70982427,
            3.70896735,
            3.71527887,
            3.71467395,
            3.71402372,
            3.71339733,
            3.71276051,
            3.71201001,
            3.71123041,
            3.71053954,
            3.70995666,
            3.70934263,
            3.70871611,
        ]
    )

    assert np.allclose(my_bounds, expected)
    # if the calculation with max_nints takes longer than 30 seconds, something is most likely broken
    assert (time.time() - start_time) < 30