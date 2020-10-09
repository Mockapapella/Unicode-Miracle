from pathlib import Path

from fontTools.ttLib.ttFont import TTFont

# some font types require an specified fontNumber parameter
# This list will need to change depending on what fonts you have installed
list_of_fonts = [
    TTFont(
        file=Path("C:\\Users\\Quinten\\AppData\\Local\\Microsoft\\Windows\\Fonts\\gw2696936.ttf")
    ),
    TTFont(
        file=Path("C:\\Users\\Quinten\\AppData\\Local\\Microsoft\\Windows\\Fonts\\gw2695709.ttf")
    ),
    TTFont(
        file=Path(
            "C:\\Users\\Quinten\\AppData\\Local\\Microsoft\\Windows\\Fonts\\Behistun-J8dE.ttf"
        )
    ),
    TTFont(
        file=Path(
            "C:\\Users\\Quinten\\AppData\\Local\\Microsoft\\Windows\\Fonts\\unifont_upper-13.0.03.ttf"
        )
    ),
    TTFont(
        file=Path("C:\\Users\\Quinten\\AppData\\Local\\Microsoft\\Windows\\Fonts\\Everson Mono.ttf")
    ),
    TTFont(
        file=Path(
            "C:\\Users\\Quinten\\AppData\\Local\\Microsoft\\Windows\\Fonts\\Everson Mono Oblique.ttf"
        )
    ),
    TTFont(
        file=Path(
            "C:\\Users\\Quinten\\AppData\\Local\\Microsoft\\Windows\\Fonts\\Everson Mono Bold Oblique.ttf"
        )
    ),
    TTFont(
        file=Path(
            "C:\\Users\\Quinten\\AppData\\Local\\Microsoft\\Windows\\Fonts\\Everson Mono Bold.ttf"
        )
    ),
    TTFont(
        file=Path(
            "C:\\Users\\Quinten\\AppData\\Local\\Microsoft\\Windows\\Fonts\\unifont-13.0.03.ttf"
        )
    ),
    TTFont(file=Path("C:\\Windows\\Fonts\\arial.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\corbelli.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\tahomabd.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\RAGE.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\LATINWD.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\MTCORSVA.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\segmdl2.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\NirmalaS.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\ROCKB.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\CALIFI.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\OUTLOOK.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\ITCBLKAD.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\constanb.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\seguisb.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\GARABD.TTF")),
    TTFont(
        file=Path(
            "C:\\Program Files\\SOLIDWORKS Corp\\SOLIDWORKS Visualize\\Plugins\\sp.x\\resources\\fonts\\OpenType\\DSISO1BI.otf"
        )
    ),
    TTFont(
        file=Path(
            "C:\\Program Files\\SOLIDWORKS Corp\\SOLIDWORKS Visualize\\Plugins\\sp.x\\resources\\fonts\\extrafiles\\TrueType\\Dutch.ttf"
        )
    ),
    TTFont(file=Path("C:\\Windows\\Fonts\\LFAX.TTF")),
    TTFont(
        file=Path(
            "C:\\Program Files\\SOLIDWORKS Corp\\SOLIDWORKS Visualize\\Plugins\\sp.x\\resources\\fonts\\extrafiles\\TrueType\\SwissCL.ttf"
        )
    ),
    TTFont(file=Path("C:\\Windows\\Fonts\\cambriai.ttf")),
    TTFont(
        file=Path(
            "C:\\Program Files\\SOLIDWORKS Corp\\SOLIDWORKS Visualize\\Plugins\\sp.x\\resources\\fonts\\extrafiles\\TrueType\\SymbP.ttf"
        )
    ),
    TTFont(file=Path("C:\\Windows\\Fonts\\GLSNECB.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\palab.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\ROCKEB.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\swmono.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\malgunsl.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\DUBAI-MEDIUM.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\GOTHICI.TTF")),
    TTFont(
        file=Path(
            "C:\\Program Files\\SOLIDWORKS Corp\\SOLIDWORKS Visualize\\Plugins\\sp.x\\resources\\fonts\\extrafiles\\TrueType\\SwissB.ttf"
        )
    ),
    TTFont(file=Path("C:\\Windows\\Fonts\\georgiaz.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\AGENCYB.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\GILB____.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\ANTQUABI.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\segoeprb.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\BOOKOS.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\BELLI.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\BRLNSB.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\Gothic.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\DUBAI-REGULAR.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\PERI____.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\hyswlongfangsong.ttf")),
    TTFont(
        file=Path(
            "C:\\Program Files\\SOLIDWORKS Corp\\SOLIDWORKS\\HoopsPublish\\resource\\Font\\courierstd-oblique.otf"
        )
    ),
    TTFont(file=Path("C:\\Windows\\Fonts\\PERTILI.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\swsimp.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\BRADHITC.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\msyi.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\ELEPHNT.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\Candarai.ttf")),
    TTFont(
        file=Path(
            "C:\\Program Files\\SOLIDWORKS Corp\\SOLIDWORKS Visualize\\Plugins\\sp.x\\resources\\fonts\\extrafiles\\TrueType\\SwissI.ttf"
        )
    ),
    TTFont(file=Path("C:\\Windows\\Fonts\\YuGothB.ttc"), fontNumber=0),
    TTFont(file=Path("C:\\Windows\\Fonts\\LFAXI.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\TCCM____.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\Candara.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\TCMI____.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\trebucit.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\GIGI.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\BOD_B.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\SitkaZ.ttc"), fontNumber=0),
    TTFont(file=Path("C:\\Windows\\Fonts\\arialbd.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\LeelaUIb.ttf")),
    TTFont(
        file=Path(
            "C:\\Program Files\\SOLIDWORKS Corp\\SOLIDWORKS Visualize\\Plugins\\sp.x\\resources\\fonts\\extrafiles\\TrueType\\DutchB.ttf"
        )
    ),
    TTFont(file=Path("C:\\Windows\\Fonts\\trebucbi.ttf")),
    TTFont(
        file=Path(
            "C:\\Program Files\\SOLIDWORKS Corp\\SOLIDWORKS Visualize\\Plugins\\sp.x\\resources\\fonts\\extrafiles\\TrueType\\CoureI.ttf"
        )
    ),
    TTFont(file=Path("C:\\Windows\\Fonts\\LBRITEI.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\swromnd.ttf")),
    TTFont(
        file=Path(
            "C:\\Program Files\\SOLIDWORKS Corp\\SOLIDWORKS Visualize\\Plugins\\sp.x\\resources\\fonts\\extrafiles\\TrueType\\SymbM.ttf"
        )
    ),
    TTFont(file=Path("C:\\Windows\\Fonts\\YuGothL.ttc"), fontNumber=0),
    TTFont(file=Path("C:\\Windows\\Fonts\\FREESCPT.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\LSANSI.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\Sitka.ttc"), fontNumber=0),
    TTFont(file=Path("C:\\Windows\\Fonts\\COLONNA.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\ROCK.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\ONYX.TTF")),
    TTFont(
        file=Path(
            "C:\\Program Files\\SOLIDWORKS Corp\\SOLIDWORKS Visualize\\Plugins\\sp.x\\resources\\fonts\\TrueType\\3ds_fonticon.ttf"
        )
    ),
    TTFont(file=Path("C:\\Windows\\Fonts\\NIAGENG.TTF")),
    TTFont(
        file=Path(
            "C:\\Program Files\\SOLIDWORKS Corp\\SOLIDWORKS Visualize\\Plugins\\sp.x\\resources\\fonts\\TrueType\\3ds Bold.ttf"
        )
    ),
    TTFont(file=Path("C:\\Windows\\Fonts\\mmrtextb.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\MSUIGHUR.TTF")),
    TTFont(
        file=Path(
            "C:\\Program Files\\SOLIDWORKS Corp\\SOLIDWORKS Visualize\\Plugins\\sp.x\\resources\\fonts\\extrafiles\\TrueType\\SwissCLI.ttf"
        )
    ),
    TTFont(file=Path("C:\\Windows\\Fonts\\corbelz.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\swisot3.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\LTYPE.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\LSANS.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\ntailub.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\calibrili.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\PERBI___.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\swtxt.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\LFAXDI.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\COPRGTB.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\INFROMAN.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\NirmalaB.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\corbeli.ttf")),
    TTFont(
        file=Path(
            "C:\\Program Files\\SOLIDWORKS Corp\\SOLIDWORKS\\HoopsPublish\\resource\\Font\\adobemingstd-light.otf"
        )
    ),
    TTFont(file=Path("C:\\Windows\\Fonts\\seguisym.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\msyhl.ttc"), fontNumber=0),
    TTFont(file=Path("C:\\Windows\\Fonts\\palai.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\3ds Light.otf")),
    TTFont(
        file=Path(
            "C:\\Program Files\\SOLIDWORKS Corp\\SOLIDWORKS Visualize\\Plugins\\sp.x\\resources\\fonts\\TrueType\\3ds Italic.ttf"
        )
    ),
    TTFont(file=Path("C:\\Windows\\Fonts\\swromnc.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\TCCEB.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\OLDENGL.TTF")),
    TTFont(
        file=Path(
            "C:\\Program Files\\SOLIDWORKS Corp\\SOLIDWORKS Visualize\\Plugins\\sp.x\\resources\\fonts\\extrafiles\\TrueType\\DutchBI.ttf"
        )
    ),
    TTFont(file=Path("C:\\Windows\\Fonts\\ROCCB___.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\seguibli.ttf")),
    TTFont(
        file=Path(
            "C:\\Program Files\\SOLIDWORKS Corp\\SOLIDWORKS\\HoopsPublish\\resource\\Font\\courierstd.otf"
        )
    ),
    TTFont(file=Path("C:\\Windows\\Fonts\\segoeuisl.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\ITCKRIST.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\ITCEDSCR.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\courbi.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\msyh.ttc"), fontNumber=0),
    TTFont(file=Path("C:\\Windows\\Fonts\\simsun.ttc"), fontNumber=0),
    TTFont(file=Path("C:\\Windows\\Fonts\\REFSPCL.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\TCB_____.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\LeelawUI.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\swromns.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\Nirmala.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\CALISTI.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\Gabriola.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\Candaraz.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\comicz.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\palabi.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\segoeuil.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\timesi.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\sylfaen.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\MISTRAL.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\RAVIE.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\LTYPEBO.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\segoeuii.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\PERB____.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\ARIALNI.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\PRISTINA.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\swastro.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\ARIALNBI.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\phagspab.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\seguibl.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\calibrib.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\cambriaz.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\GIL_____.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\segoeuib.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\msyhbd.ttc"), fontNumber=0),
    TTFont(file=Path("C:\\Windows\\Fonts\\JUICE___.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\VLADIMIR.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\LFAXD.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\swscrps.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\AGENCYR.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\BOD_BI.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\FRADMCN.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\PERTIBD.TTF")),
    TTFont(
        file=Path(
            "C:\\Program Files\\SOLIDWORKS Corp\\SOLIDWORKS\\HoopsPublish\\resource\\Font\\adobepistd.otf"
        )
    ),
    TTFont(file=Path("C:\\Windows\\Fonts\\corbel.ttf")),
    TTFont(
        file=Path(
            "C:\\Program Files\\SOLIDWORKS Corp\\SOLIDWORKS\\HoopsPublish\\resource\\Font\\adobesongstd-light.otf"
        )
    ),
    TTFont(file=Path("C:\\Windows\\Fonts\\BOD_PSTC.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\swisop3.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\LSANSDI.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\BRITANIC.TTF")),
    TTFont(
        file=Path(
            "C:\\Program Files\\SOLIDWORKS Corp\\SOLIDWORKS Visualize\\Plugins\\sp.x\\resources\\fonts\\extrafiles\\TrueType\\Coure.ttf"
        )
    ),
    TTFont(file=Path("C:\\Windows\\Fonts\\comic.ttf")),
    TTFont(
        file=Path(
            "C:\\Program Files\\SOLIDWORKS Corp\\SOLIDWORKS Visualize\\Plugins\\sp.x\\resources\\fonts\\OpenType\\DSISO1I.otf"
        )
    ),
    TTFont(file=Path("C:\\Windows\\Fonts\\calibriz.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\SCHLBKI.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\YuGothR.ttc"), fontNumber=0),
    TTFont(file=Path("C:\\Windows\\Fonts\\swisop2.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\swgrekc.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\ebrima.ttf")),
    TTFont(
        file=Path(
            "C:\\Program Files\\SOLIDWORKS Corp\\SOLIDWORKS Visualize\\Plugins\\sp.x\\resources\\fonts\\extrafiles\\TrueType\\MonosI.ttf"
        )
    ),
    TTFont(file=Path("C:\\Windows\\Fonts\\MAIAN.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\GARA.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\LEELAWAD.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\BOD_CB.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\taile.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\ariali.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\msgothic.ttc"), fontNumber=0),
    TTFont(file=Path("C:\\Windows\\Fonts\\TEMPSITC.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\calibrii.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\BOD_I.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\STENCIL.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\BRLNSDB.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\georgiab.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\GILLUBCD.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\malgun.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\switalt.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\GOTHICBI.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\lucon.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\CALIFR.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\calibri.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\couri.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\GILC____.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\ERASMD.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\BRUSHSCI.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\swromnt.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\MTEXTRA.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\ANTQUAB.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\LBRITED.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\CENSCBK.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\YuGothM.ttc"), fontNumber=0),
    TTFont(
        file=Path(
            "C:\\Program Files\\SOLIDWORKS Corp\\SOLIDWORKS Visualize\\Plugins\\sp.x\\resources\\fonts\\TrueType\\3ds Regular.ttf"
        )
    ),
    TTFont(file=Path("C:\\Windows\\Fonts\\gadugi.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\MAGNETOB.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\swscrpc.ttf")),
    TTFont(
        file=Path(
            "C:\\Program Files\\SOLIDWORKS Corp\\SOLIDWORKS\\HoopsPublish\\resource\\Font\\myriadcad.otf"
        )
    ),
    TTFont(file=Path("C:\\Windows\\Fonts\\ARIALNB.TTF")),
    TTFont(
        file=Path(
            "C:\\Program Files\\SOLIDWORKS Corp\\SOLIDWORKS Visualize\\Plugins\\sp.x\\resources\\fonts\\extrafiles\\TrueType\\CoureBI.ttf"
        )
    ),
    TTFont(file=Path("C:\\Windows\\Fonts\\swgothg.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\FORTE.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\ALGER.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\ROCC____.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\FRABKIT.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\Candarab.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\micross.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\FRADM.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\wingding.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\malgunbd.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\VINERITC.TTF")),
    TTFont(
        file=Path(
            "C:\\Program Files\\SOLIDWORKS Corp\\SOLIDWORKS Visualize\\Plugins\\sp.x\\resources\\fonts\\extrafiles\\TrueType\\Monos.ttf"
        )
    ),
    TTFont(file=Path("C:\\Windows\\Fonts\\HARLOWSI.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\OCRAEXT.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\GOUDOSB.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\seguiemj.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\comicbd.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\Candarali.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\consolaz.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\segoepr.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\BOD_BLAR.TTF")),
    TTFont(
        file=Path(
            "C:\\Program Files\\SOLIDWORKS Corp\\SOLIDWORKS Visualize\\Plugins\\sp.x\\resources\\fonts\\OpenType\\DSISO1B.otf"
        )
    ),
    TTFont(file=Path("C:\\Windows\\Fonts\\COPRGTL.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\framd.ttf")),
    TTFont(
        file=Path(
            "C:\\Program Files\\SOLIDWORKS Corp\\SOLIDWORKS Visualize\\Plugins\\sp.x\\resources\\fonts\\extrafiles\\TrueType\\DutchI.ttf"
        )
    ),
    TTFont(file=Path("C:\\Windows\\Fonts\\SNAP____.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\webdings.ttf")),
    TTFont(
        file=Path(
            "C:\\Program Files\\SOLIDWORKS Corp\\SOLIDWORKS\\HoopsPublish\\resource\\Font\\adobemyungjostd-medium.otf"
        )
    ),
    TTFont(file=Path("C:\\Windows\\Fonts\\FRADMIT.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\pala.ttf")),
    TTFont(
        file=Path(
            "C:\\Program Files\\SOLIDWORKS Corp\\SOLIDWORKS Visualize\\Plugins\\sp.x\\resources\\fonts\\OpenType\\DSISO1.otf"
        )
    ),
    TTFont(file=Path("C:\\Windows\\Fonts\\REFSAN.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\swgothi.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\BAUHS93.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\BOD_BLAI.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\SHOWG.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\CALIST.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\framdit.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\KUNSTLER.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\GILI____.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\consolab.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\bahnschrift.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\msjh.ttc"), fontNumber=0),
    TTFont(file=Path("C:\\Windows\\Fonts\\LBRITE.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\seguisli.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\swmeteo.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\SCRIPTBL.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\ERASDEMI.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\LeelUIsl.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\verdanai.ttf")),
    TTFont(
        file=Path(
            "C:\\Program Files\\SOLIDWORKS Corp\\SOLIDWORKS\\HoopsPublish\\resource\\Font\\adobeheitistd-regular.otf"
        )
    ),
    TTFont(file=Path("C:\\Windows\\Fonts\\swgothe.ttf")),
    TTFont(file=Path("C:\\Users\\Quinten\\AppData\\Local\\Microsoft\\Windows\\Fonts\\Monos.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\ROCKBI.TTF")),
    TTFont(
        file=Path(
            "C:\\Program Files\\SOLIDWORKS Corp\\SOLIDWORKS Visualize\\Plugins\\sp.x\\resources\\fonts\\extrafiles\\TrueType\\SymbC.ttf"
        )
    ),
    TTFont(file=Path("C:\\Windows\\Fonts\\segoeuiz.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\GILBI___.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\GLECB.TTF")),
    TTFont(
        file=Path(
            "C:\\Program Files\\SOLIDWORKS Corp\\SOLIDWORKS\\HoopsPublish\\resource\\Font\\courierstd-boldoblique.otf"
        )
    ),
    TTFont(
        file=Path(
            "C:\\Program Files\\SOLIDWORKS Corp\\SOLIDWORKS Visualize\\Plugins\\sp.x\\resources\\fonts\\extrafiles\\TrueType\\MonosBI.ttf"
        )
    ),
    TTFont(file=Path("C:\\Windows\\Fonts\\mvboli.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\olfsimplesansoc-regular.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\TCM_____.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\FRSCRIPT.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\COOPBL.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\SitkaI.ttc"), fontNumber=0),
    TTFont(file=Path("C:\\Windows\\Fonts\\MATURASC.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\monbaiti.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\ROCKI.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\mmrtext.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\VIVALDII.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\BOOKOSB.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\CENTAUR.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\switalc.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\swlink.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\IMPRISHA.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\ARLRDBD.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\SitkaB.ttc"), fontNumber=0),
    TTFont(
        file=Path(
            "C:\\Program Files\\SOLIDWORKS Corp\\SOLIDWORKS Visualize\\Plugins\\sp.x\\resources\\fonts\\extrafiles\\TrueType\\SwiOuB.ttf"
        )
    ),
    TTFont(file=Path("C:\\Windows\\Fonts\\BKANT.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\ERASLGHT.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\BOD_CR.TTF")),
    TTFont(
        file=Path(
            "C:\\Program Files\\SOLIDWORKS Corp\\SOLIDWORKS Visualize\\Plugins\\sp.x\\resources\\fonts\\extrafiles\\TrueType\\CoureB.ttf"
        )
    ),
    TTFont(file=Path("C:\\Windows\\Fonts\\CALIFB.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\swgreks.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\BOD_R.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\MSUIGHUB.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\ebrimabd.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\phagspa.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\GOTHICB.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\LBRITEDI.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\simsunb.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\ntailu.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\BOOKOSBI.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\GILSANUB.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\BOD_CBI.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\CURLZ___.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\timesbd.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\FRAHVIT.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\corbell.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\ARIALN.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\Candaral.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\CALISTB.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\BSSYM7.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\ENGR.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\msjhl.ttc"), fontNumber=0),
    TTFont(file=Path("C:\\Windows\\Fonts\\comici.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\BELLB.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\courbd.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\TCCB____.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\cour.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\BOD_CI.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\marlett.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\LTYPEO.TTF")),
    TTFont(
        file=Path(
            "C:\\Program Files\\SOLIDWORKS Corp\\SOLIDWORKS Visualize\\Plugins\\sp.x\\resources\\fonts\\extrafiles\\TrueType\\MonosB.ttf"
        )
    ),
    TTFont(file=Path("C:\\Windows\\Fonts\\mingliub.ttc"), fontNumber=0),
    TTFont(file=Path("C:\\Windows\\Fonts\\consolai.ttf")),
    TTFont(
        file=Path(
            "C:\\Program Files\\SOLIDWORKS Corp\\SOLIDWORKS\\HoopsPublish\\resource\\Font\\courierstd-bold.otf"
        )
    ),
    TTFont(file=Path("C:\\Windows\\Fonts\\Inkfree.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\LHANDW.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\CHILLER.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\swisot2.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\swisot1.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\CALISTBI.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\SCHLBKB.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\symbol.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\swisop1.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\GOUDOS.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\ERASBD.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\gadugib.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\teamviewer14.otf")),
    TTFont(
        file=Path(
            "C:\\Program Files\\SOLIDWORKS Corp\\SOLIDWORKS Visualize\\Plugins\\sp.x\\resources\\fonts\\extrafiles\\TrueType\\Mathe.ttf"
        )
    ),
    TTFont(file=Path("C:\\Windows\\Fonts\\solidworks gdt.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\GOUDOSI.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\GOUDYSTO.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\MOD20.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\segoeui.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\times.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\swgdt.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\LEELAWDB.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\seguihis.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\JOKERMAN.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\ariblk.ttf")),
    TTFont(
        file=Path(
            "C:\\Program Files\\SOLIDWORKS Corp\\SOLIDWORKS\\HoopsPublish\\resource\\Font\\kozminpr6n-regular.otf"
        )
    ),
    TTFont(file=Path("C:\\Windows\\Fonts\\cambria.ttc"), fontNumber=0),
    TTFont(file=Path("C:\\Windows\\Fonts\\segoescb.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\POORICH.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\WINGDNG3.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\l_10646.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\NIAGSOL.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\BROADW.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\taileb.ttf")),
    TTFont(
        file=Path(
            "C:\\Program Files\\SOLIDWORKS Corp\\SOLIDWORKS Visualize\\Plugins\\sp.x\\resources\\fonts\\TrueType\\3ds Bold Italic.ttf"
        )
    ),
    TTFont(file=Path("C:\\Windows\\Fonts\\FRAMDCN.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\GARAIT.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\constan.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\PARCHM.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\corbelb.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\calibril.ttf")),
    TTFont(
        file=Path(
            "C:\\Program Files\\SOLIDWORKS Corp\\SOLIDWORKS\\HoopsPublish\\resource\\Font\\kozgopr6n-medium.otf"
        )
    ),
    TTFont(file=Path("C:\\Windows\\Fonts\\georgia.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\PAPYRUS.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\ELEPHNTI.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\LSANSD.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\BASKVILL.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\consola.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\himalaya.ttf")),
    TTFont(
        file=Path(
            "C:\\Program Files\\SOLIDWORKS Corp\\SOLIDWORKS Visualize\\Plugins\\sp.x\\resources\\fonts\\extrafiles\\TrueType\\SwissBI.ttf"
        )
    ),
    TTFont(file=Path("C:\\Windows\\Fonts\\HTOWERTI.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\verdanaz.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\CASTELAR.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\swmap.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\DUBAI-LIGHT.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\PLAYBILL.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\seguili.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\SCHLBKBI.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\WINGDNG2.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\trebucbd.ttf")),
    TTFont(
        file=Path(
            "C:\\Program Files\\SOLIDWORKS Corp\\SOLIDWORKS Visualize\\Plugins\\sp.x\\resources\\fonts\\extrafiles\\TrueType\\Swiss.ttf"
        )
    ),
    TTFont(file=Path("C:\\Windows\\Fonts\\javatext.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\constani.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\LCALLIG.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\swcomp.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\swmath.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\impact.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\FTLTLT.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\BRLNSR.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\FRAHV.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\verdanab.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\FELIXTI.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\BERNHC.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\arialbi.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\swital.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\PALSCRI.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\HTOWERT.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\HATTEN.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\georgiai.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\TCBI____.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\segoesc.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\FRABK.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\cambriab.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\LTYPEB.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\seguisbi.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\tahoma.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\HARNGTON.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\msjhbd.ttc"), fontNumber=0),
    TTFont(file=Path("C:\\Windows\\Fonts\\timesbi.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\PER_____.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\swmusic.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\ANTQUAI.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\DUBAI-BOLD.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\BELL.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\constanz.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\verdana.ttf")),
    TTFont(file=Path("C:\\Windows\\Fonts\\CENTURY.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\BOOKOSI.TTF")),
    TTFont(file=Path("C:\\Windows\\Fonts\\trebuc.ttf")),
    TTFont(
        file=Path("C:\\Users\\Quinten\\AppData\\Local\\Microsoft\\Windows\\Fonts\\LastResort.ttf")
    ),
]
