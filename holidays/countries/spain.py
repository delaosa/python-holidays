#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

from datetime import date

from dateutil.easter import easter
from dateutil.relativedelta import relativedelta as rd

from holidays.constants import JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP
from holidays.constants import OCT, NOV, DEC, SUN
from holidays.holiday_base import HolidayBase
from holidays.utils import _islamic_to_gre


class Spain(HolidayBase):
    country = "ES"
    subdivisions = [
        "AN",
        "AR",
        "AS",
        "CB",
        "CE",
        "CL",
        "CM",
        "CN",
        "CT",
        "EX",
        "GA",
        "IB",
        "MC",
        "MD",
        "ML",
        "NC",
        "PV",
        "RI",
        "VC",
    ]

    def _is_observed(self, date_holiday, name_holiday):
        if self.observed and date_holiday.weekday() == SUN:
            self[date_holiday + rd(days=+1)] = name_holiday + " (Trasladado)"
        else:
            self[date_holiday] = name_holiday

    def _populate(self, year):
        super()._populate(year)

        self._is_observed(date(year, JAN, 1), "Año nuevo")
        self._is_observed(date(year, JAN, 6), "Epifanía del Señor")

        easter_date = easter(year)

        if (
            year < 2015
            and self.subdiv
            and self.subdiv
            in {
                "AR",
                "CL",
                "CM",
                "EX",
                "GA",
                "MC",
                "MD",
                "ML",
                "NC",
                "PV",
                "VC",
            }
        ):
            self._is_observed(date(year, MAR, 19), "San José")
        elif (
            year == 2015
            and self.subdiv
            and self.subdiv in {"CM", "MC", "MD", "ML", "NC", "PV", "VC"}
        ):
            self._is_observed(date(year, MAR, 19), "San José")
        elif (
            year == 2016
            and self.subdiv
            and self.subdiv in {"MC", "ML", "PV", "VC"}
        ):
            self._is_observed(date(year, MAR, 19), "San José")
        elif year == 2017 and self.subdiv in {"PV"}:
            self._is_observed(date(year, MAR, 19), "San José")
        elif (
            2018 <= year <= 2019
            and self.subdiv
            and self.subdiv in {"GA", "MC", "NC", "PV", "VC"}
        ):
            self._is_observed(date(year, MAR, 19), "San José")
        elif (
            2020 <= year <= 2021
            and self.subdiv
            and self.subdiv in {"CM", "GA", "MC", "NC", "PV", "VC"}
        ):
            self._is_observed(date(year, MAR, 19), "San José")
        elif year == 2022 and self.subdiv and self.subdiv == "VC":
            self._is_observed(date(year, MAR, 19), "San José")
        elif year == 2023 and self.subdiv and self.subdiv == "MD":
            self._is_observed(date(year, MAR, 19), "San José")
        if year <= 2022 and self.subdiv not in {"CT", "VC"}:
            self[easter_date + rd(days=-3)] = "Jueves Santo"
        elif year == 2022 and self.subdiv and self.subdiv not in {"CT"}:
            self[easter_date + rd(days=-3)] = "Jueves Santo"
        elif year >= 2023:
            self[easter_date + rd(days=-3)] = "Jueves Santo"
        self[easter_date + rd(days=-2)] = "Viernes Santo"
        if year < 2022 and self.subdiv in {
            "CM",
            "CT",
            "IB",
            "NC",
            "PV",
            "VC",
        }:
            self[easter(year) + rd(days=+1)] = "Lunes de Pascua"
        elif year >= 2022 and self.subdiv in {
            "RI",
            "CT",
            "IB",
            "NC",
            "PV",
            "VC",
        }:
            self[easter(year) + rd(days=+1)] = "Lunes de Pascua"
        if year == 2022 and self.subdiv in {
            "AN",
            "AR",
            "AS",
            "CL",
            "EX",
            "MC",
        }:
            self._is_observed(date(year, MAY, 1), "Día del Trabajador")
        if year != 2022:
            self._is_observed(date(year, MAY, 1), "Día del Trabajador")
        if year == 2023 and self.subdiv in {"CT", "VC"}:
            self._is_observed(date(year, JUN, 24), "San Juan")
        if year != 2023 and self.subdiv in {"CT", "GA", "VC"}:
            self._is_observed(date(year, JUN, 24), "San Juan")
        self._is_observed(date(year, AUG, 15), "Asunción de la Virgen")
        self._is_observed(date(year, OCT, 12), "Día de la Hispanidad")
        self._is_observed(date(year, NOV, 1), "Todos los Santos")
        self._is_observed(
            date(year, DEC, 6), "Día de la Constitución Española"
        )
        self._is_observed(date(year, DEC, 8), "La Inmaculada Concepción")
        if year == 2022 and self.subdiv not in {"CE", "GA", "PV", "VC"}:
            self._is_observed(date(year, DEC, 25), "Navidad")
        elif year != 2022:
            self._is_observed(date(year, DEC, 25), "Navidad")

        # Provinces festive day
        if self.subdiv == "AN":
            self._is_observed(date(year, FEB, 28), "Día de Andalucia")
        elif self.subdiv == "AR":
            self._is_observed(date(year, APR, 23), "Día de San Jorge")
        elif self.subdiv == "AS":
            self._is_observed(date(year, SEP, 8), "Día de Asturias")
        elif self.subdiv == "CB":
            self._is_observed(
                date(year, JUL, 28),
                "Día de las Instituciones de Cantabria",
            )
            self._is_observed(date(year, SEP, 15), "Día de la Bien Aparecida")
        elif self.subdiv == "CE":
            self._is_observed(date(year, AUG, 5), "Nuestra Señora de África")
            self._is_observed(
                date(year, SEP, 2), "Día de la Ciudad Autónoma de Ceuta"
            )
            if year == 2022:
                self._is_observed(
                    _islamic_to_gre(year, 12, 10)[0], "Eid al-Adha"
                )
            elif year == 2023:
                self._is_observed(
                    _islamic_to_gre(year, 12, 10)[0] + rd(days=+1),
                    "Eid al-Adha",
                )
        elif self.subdiv == "CM":
            if year == 2022:
                self._is_observed(date(year, JUN, 16), "Corpus Christi")
            elif year == 2023:
                self._is_observed(date(year, JUN, 8), "Corpus Christi")
            self._is_observed(date(year, MAY, 31), "Día de Castilla La Mancha")
        elif self.subdiv == "CN":
            self._is_observed(date(year, MAY, 30), "Día de Canarias")
        elif self.subdiv == "CL":
            self._is_observed(date(year, APR, 23), "Día de Castilla y Leon")
            if year == 2023:
                self._is_observed(
                    date(year, JUL, 25), "Día de Santiago Apóstol"
                )
        elif self.subdiv == "CT":
            if year == 2022:
                self._is_observed(
                    date(year, JUN, 6), "Día de la Pascua Granada"
                )
            self._is_observed(date(year, SEP, 11), "Día Nacional de Catalunya")
            self._is_observed(date(year, DEC, 26), "San Esteban")
        elif self.subdiv == "EX":
            self._is_observed(date(year, SEP, 8), "Día de Extremadura")
        elif self.subdiv == "GA":
            if year >= 2022:
                self._is_observed(
                    date(year, MAY, 17), "Día de las letras Gallegas"
                )
            self._is_observed(date(year, JUL, 25), "Día Nacional de Galicia")
        elif self.subdiv == "IB":
            self._is_observed(date(year, MAR, 1), "Día de las Islas Baleares")
            if year <= 2020:
                self._is_observed(date(year, DEC, 26), "San Esteban")
        elif self.subdiv == "MD":
            self._is_observed(date(year, MAY, 2), "Día de Comunidad de Madrid")
            if year >= 2022:
                self._is_observed(
                    date(year, JUL, 25), "Día de Santiago Apóstol"
                )
        elif self.subdiv == "MC":
            self._is_observed(date(year, JUN, 9), "Día de la Región de Murcia")
        elif self.subdiv == "ML":
            self._is_observed(date(year, SEP, 8), "Vírgen de la victoria")
            self._is_observed(date(year, SEP, 17), "Día de Melilla")
            if year == 2022:
                self._is_observed(
                    _islamic_to_gre(year, 10, 1)[0] + rd(days=+1), "Eid Fitr"
                )
                self._is_observed(
                    _islamic_to_gre(year, 12, 10)[0] + rd(days=+2),
                    "Eid al-Adha",
                )
            elif year == 2023:
                self._is_observed(_islamic_to_gre(year, 10, 1)[0], "Eid Fitr")
                self._is_observed(
                    _islamic_to_gre(year, 12, 10)[0] + rd(days=+1),
                    "Eid al-Adha",
                )
        elif self.subdiv == "NC":
            if year >= 2022:
                self._is_observed(
                    date(year, JUL, 25), "Día de Santiago Apóstol"
                )
            self._is_observed(date(year, SEP, 27), "Día de Navarra")
        elif self.subdiv == "PV":
            if year >= 2022:
                self._is_observed(
                    date(year, JUL, 25), "Día de Santiago Apóstol"
                )
            if year < 2023:
                self._is_observed(date(year, SEP, 6), "Día de Elcano")
            if 2011 <= year <= 2013:
                self._is_observed(date(year, OCT, 25), "Día del País Vasco")
        elif self.subdiv == "RI":
            self._is_observed(date(year, JUN, 9), "Día de La Rioja")
        elif self.subdiv == "VC":
            if year <= 2021:
                self._is_observed(
                    date(year, OCT, 9), "Día de la Comunidad Valenciana"
                )


class ES(Spain):
    pass


class ESP(Spain):
    pass
